#!/usr/bin/env python3
import click
import requests
import geocoder
import re

def validate_zipcode(zipcode):
    """Validate US ZIP code format"""
    return bool(re.match(r'^\d{5}(-\d{4})?$', zipcode))

def get_location_from_zip(zipcode):
    if not validate_zipcode(zipcode):
        return None
    try:
        response = requests.get(f'https://api.zippopotam.us/us/{zipcode}', timeout=10)
        response.raise_for_status()
        data = response.json()
        place = data['places'][0]
        return {
            'city': place['place name'],
            'state': place['state'],
            'zipcode': zipcode
        }
    except (requests.RequestException, KeyError, IndexError):
        return None

def get_current_location():
    try:
        g = geocoder.ip('me', timeout=10)
        if g.ok:
            return {
                'city': g.city,
                'state': g.state,
                'zipcode': g.postal
            }
    except Exception:
        return None
    return None

def get_weather(location):
    try:
        response = requests.get(f'https://wttr.in/{location["zipcode"]}?format=%t|%C', timeout=10)
        response.raise_for_status()
        temp, condition = response.text.strip().split('|')
        return {
            'temperature': temp.strip(),
            'condition': condition.strip()
        }
    except (requests.RequestException, ValueError):
        return None

@click.group()
def cli():
    """Weather CLI application"""
    pass

@cli.command()
@click.option('--zipcode', help='ZIP code to look up')
def where_is(zipcode):
    """Show the city and state for a location"""
    if zipcode:
        location = get_location_from_zip(zipcode)
    else:
        location = get_current_location()
    
    if location:
        click.echo(f"{location['zipcode']} is in {location['city']}, {location['state']}.")
    else:
        click.echo("Unable to determine location.")

@cli.command()
@click.option('--zipcode', help='ZIP code to look up weather for')
def current(zipcode):
    """Show current temperature and weather conditions"""
    if zipcode:
        location = get_location_from_zip(zipcode)
    else:
        location = get_current_location()
    
    if location:
        weather = get_weather(location)
        if weather:
            click.echo(f"It is currently {weather['temperature']}, and {weather['condition']} in {location['city']}, {location['state']}.")
        else:
            click.echo("Unable to fetch weather data.")
    else:
        click.echo("Unable to determine location.")

if __name__ == '__main__':
    cli()