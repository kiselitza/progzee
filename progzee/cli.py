import click
from .progzee import Progzee

@click.group()
def cli():
    """Progzee: A Python tool for making HTTP requests with proxy rotation."""
    pass

@cli.command()
@click.option("--url", required=True, help="The URL to fetch.")
@click.option("--config", default="config.ini", help="Path to the config file.")
def fetch(url: str, config: str):
    """Fetch data from a URL using Progzee."""
    pz = Progzee(config_file=config)
    response = pz.get(url)
    click.echo(response.text)

@cli.command()
@click.option("--url", required=True, help="The URL to send the POST request to.")
@click.option("--data", help="Data to send in the request body (JSON format).")
@click.option("--config", default="config.ini", help="Path to the config file.")
def post(url: str, data: str, config: str):
    """Send a POST request using Progzee."""
    pz = Progzee(config_file=config)
    response = pz.post(url, data=json.loads(data) if data else pz.post(url))
    click.echo(response.text)

@cli.command()
@click.option("--url", required=True, help="The URL to send the PUT request to.")
@click.option("--data", help="Data to send in the request body (JSON format).")
@click.option("--config", default="config.ini", help="Path to the config file.")
def put(url: str, data: str, config: str):
    """Send a PUT request using Progzee."""
    pz = Progzee(config_file=config)
    response = pz.put(url, data=json.loads(data) if data else pz.put(url))
    click.echo(response.text)

@cli.command()
@click.option("--url", required=True, help="The URL to send the DELETE request to.")
@click.option("--config", default="config.ini", help="Path to the config file.")
def delete(url: str, config: str):
    """Send a DELETE request using Progzee."""
    pz = Progzee(config_file=config)
    response = pz.delete(url)
    click.echo(response.text)

@cli.command()
@click.option("--config", default="config.ini", help="Path to the config file.")
def update_proxies(config: str):
    """Update the proxy list from a config file."""
    pz = Progzee(config_file=config)
    click.echo(f"Loaded {len(pz.proxies)} proxies from {config}.")

if __name__ == "__main__":
    cli()