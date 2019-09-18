import requests
from requests.exceptions import HTTPError
import click
import urllib.request

def _download_gitignore_file(language):
    language = language.capitalize() # first letter must be upper case

    try:
        response = requests.get("https://api.github.com/repos/github/gitignore/contents").json()

        # get a list with all files that are named <language>.gitignore in the repo
        language_gitignore_object = [obj for obj in response if obj["name"] == language + ".gitignore"]
        # if this list is not empty, download the file
        if len(language_gitignore_object) != 0:
            language_gitignore_object = language_gitignore_object[0]
            url = language_gitignore_object["download_url"]
            click.echo(f"Downloading {language} .gitignore from {url}")
            urllib.request.urlretrieve(url, ".gitignore") # download file
        # else, the user typed the language wrong
        else:
            click.echo(f".gitignore not found for {language}")
                
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}') 

@click.group()
def download_gitignore():
    pass


@download_gitignore.command()
@click.argument("language")  
def download(language):
    _download_gitignore_file(language)
    

# download alias
@download_gitignore.command()
@click.argument("language")
def get(language):
    _download_gitignore_file(language)
 

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