import requests
from requests.exceptions import HTTPError
import click
import urllib.request

def _get_list_of_gitignore_files():
    response = requests.get("https://api.github.com/repos/github/gitignore/contents").json()
    list_of_gitignore_files = [obj for obj in response 
        if obj["type"] == "file" and ".gitignore" in obj["name"]]
    return list_of_gitignore_files

def _download_gitignore_file(language):
    language = language.capitalize() # first letter must be upper case

    try:
        list_of_gitignore_files = _get_list_of_gitignore_files()

        # get a list with all (the only) files that are named <language>.gitignore in the repo
        language_gitignore_object = [obj for obj in list_of_gitignore_files 
            if obj["name"] == language + ".gitignore"]
        # if this list is not empty, download the file
        if len(language_gitignore_object) != 0:
            language_gitignore_object = language_gitignore_object[0]
            url = language_gitignore_object["download_url"]
            click.echo(f"Downloading {language} .gitignore from {url}")
            urllib.request.urlretrieve(url, ".gitignore") # download file
        # else, the user typed the language wrong
        else:
            click.echo(f""".gitignore not found for {language}. Use download-gitignore list to list all the available files.""")
                
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}') 
        click.echo("\nYou may want to check your internet connection.")


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(context_settings=CONTEXT_SETTINGS)
def download_gitignore():
    """Tool to download .gitignore files from command line"""


@download_gitignore.command("download", short_help="Download .gitignore file for LANGUAGE")
@click.argument("language")  
def download(language):
    _download_gitignore_file(language)
    

# download alias
@download_gitignore.command("get", short_help="Download .gitignore file for LANGUAGE")
@click.argument("language")
def get(language):
    _download_gitignore_file(language)


@download_gitignore.command("list", short_help="List all .gitignore files available to download")
def list():
    click.echo("Getting list of .gitignore files...")
    list_of_gitignore_files = _get_list_of_gitignore_files()
    click.echo("List of all .gitignore files available to download:\n")
    for f in list_of_gitignore_files:
        click.echo(f["name"])

def main():
    pass
    
    
if __name__ == '__main__':
    main()