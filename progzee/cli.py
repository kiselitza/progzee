import click
from .progzee import Progzee
import requests
import json

@click.group()
def cli():
    """Progzee: A Python tool for making HTTP requests with proxy rotation."""
    pass

@cli.command()
@click.option("--url", required=True, help="The URL to fetch.")
@click.option("--proxies", help="Comma-separated list of proxies (e.g., 'http://proxy1:port,http://proxy2:port').")
@click.option("--config", default="config.ini", help="Path to the config file.")
def fetch(url: str, proxies: str, config: str):
    """Fetch data from a URL using Progzee."""
    try:
        if proxies:
            pz = Progzee(proxies=proxies.split(","))
        else:
            pz = Progzee(config_file=config)
        response = pz.get(url)
        click.echo(response.text)
    except requests.exceptions.RequestException as e:
        click.echo(f"Request failed: {e}", err=True)
        raise click.Abort()

@cli.command()
@click.option("--url", required=True, help="The URL to send the POST request to.")
@click.option("--proxies", help="Comma-separated list of proxies (e.g., 'http://proxy1:port,http://proxy2:port').")
@click.option("--data", help="Data to send in the request body (JSON format).")
@click.option("--config", default="config.ini", help="Path to the config file.")
def post(url: str, proxies: str, data: str, config: str):
    """Send a POST request using Progzee."""
    try:
        if proxies:
            pz = Progzee(proxies=proxies.split(","))
        else:
            pz = Progzee(config_file=config)
        response = pz.post(url, data=json.loads(data) if data else pz.post(url))
        click.echo(response.text)
    except requests.exceptions.RequestException as e:
        click.echo(f"Request failed: {e}", err=True)
        raise click.Abort()

@cli.command()
@click.option("--url", required=True, help="The URL to send the PUT request to.")
@click.option("--proxies", help="Comma-separated list of proxies (e.g., 'http://proxy1:port,http://proxy2:port').")
@click.option("--data", help="Data to send in the request body (JSON format).")
@click.option("--config", default="config.ini", help="Path to the config file.")
def put(url: str, proxies: str, data: str, config: str):
    """Send a PUT request using Progzee."""
    try:
        if proxies:
            pz = Progzee(proxies=proxies.split(","))
        else:
            pz = Progzee(config_file=config)
        response = pz.put(url, data=json.loads(data) if data else pz.put(url))
        click.echo(response.text)
    except requests.exceptions.RequestException as e:
        click.echo(f"Request failed: {e}", err=True)
        raise click.Abort()

@cli.command()
@click.option("--url", required=True, help="The URL to send the DELETE request to.")
@click.option("--proxies", help="Comma-separated list of proxies (e.g., 'http://proxy1:port,http://proxy2:port').")
@click.option("--config", default="config.ini", help="Path to the config file.")
def delete(url: str, proxies: str, config: str):
    """Send a DELETE request using Progzee."""
    try:
        if proxies:
            pz = Progzee(proxies=proxies.split(","))
        else:
            pz = Progzee(config_file=config)
        response = pz.delete(url)
        click.echo(response.text)
    except requests.exceptions.RequestException as e:
        click.echo(f"Request failed: {e}", err=True)
        raise click.Abort()

@cli.command()
@click.option("--config", default="config.ini", help="Path to the config file.")
def update_proxies(config: str):
    """Update the proxy list from a config file."""
    try:
        pz = Progzee(config_file=config)
        click.echo(f"Loaded {len(pz.proxies)} proxies from {config}.")
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        raise click.Abort()

if __name__ == "__main__":
    cli()