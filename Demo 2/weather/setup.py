from setuptools import setup, find_packages

setup(
    name="weather-or-not",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "click>=8.0.0",
        "requests>=2.31.0",
        "geocoder>=1.38.1",
    ],
    entry_points={
        'console_scripts': [
            'weather=weather:cli',
        ],
    },
    author="caiocqueiroz",
    description="A simple command-line weather application",
    long_description=open("../../README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/caiocqueiroz/weather-or-not",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)