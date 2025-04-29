#!/usr/bin/env python3
import click
import requests
import geocoder

def get_location_from_zip(zipcode):
    response = requests.get(f'https://api.zippopotam.us/us/{zipcode}')
    if response.status_code == 200:
        data = response.json()
        place = data['places'][0]
        return {
            'city': place['place name'],
            'state': place['state'],
            'zipcode': zipcode
        }
    return None

#Create a function to get the wind conditions, which woudl complement the existing weather functionallity
def get_wind_conditions(location):
    # Using the wttr.in API which is free and requires no registration
    response = requests.get(f'https://wttr.in/{location["zipcode"]}?format=%w')
    if response.status_code == 200:
        wind = response.text.strip()
        return {
            'wind_conditions': wind.strip()
        }
    return None

def get_current_location():
    g = geocoder.ip('me')
    if g.ok:
        return {
            'city': g.city,
            'state': g.state,
            'zipcode': g.postal
        }
    return None

def get_weather(location):
    # Using the wttr.in API which is free and requires no registration
    response = requests.get(f'https://wttr.in/{location["zipcode"]}?format=%t|%C')
    if response.status_code == 200:
        temp, condition = response.text.strip().split('|')
        return {
            'temperature': temp.strip(),
            'condition': condition.strip()
        }
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

#Generate a new command to get the wind conditions
@cli.command()
@click.option('--zipcode', help='ZIP code to look up wind conditions for')
def wind(zipcode):
    """Show current wind conditions"""
    if zipcode:
        location = get_location_from_zip(zipcode)
    else:
        location = get_current_location()
    
    if location:
        wind_conditions = get_wind_conditions(location)
        if wind_conditions:
            click.echo(f"The wind conditions are: {wind_conditions['wind_conditions']} in {location['city']}, {location['state']}.")
        else:
            click.echo("Unable to fetch wind data.")
    else:
        click.echo("Unable to determine location.")


if __name__ == '__main__':
    cli()