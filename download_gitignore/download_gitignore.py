import requests
from requests.exceptions import HTTPError
import click

@click.group()
def download_gitignore():
    pass

@download_gitignore.command()
@click.argument("language")
def get(language):
    click.echo(f"Downloading {language} gitignore")
    

def main():
    try:
        response = requests.get("https://api.github.com/repos/github/gitignore/contents")

        print(response.text)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}') 
    
    
if __name__ == '__main__':
    main()