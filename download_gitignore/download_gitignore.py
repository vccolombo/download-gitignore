import click
from .github_api import github_api

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(context_settings=CONTEXT_SETTINGS)
def download_gitignore():
    """Tool to download .gitignore files from command line"""


@download_gitignore.command("download", short_help="Download .gitignore file for LANGUAGES")
@click.argument("languages",nargs=-1)  
def download(languages):
    github_api().download_gitignore_file(languages)
    

# download alias
@download_gitignore.command("get", short_help="Download .gitignore file for LANGUAGES")
@click.argument("languages",nargs=-1)
def get(languages):
    github_api().download_gitignore_file(languages)


@download_gitignore.command("list", short_help="List all .gitignore files available to download")
def list():
    click.echo("Getting list of .gitignore files...")
    list_of_gitignore_files = github_api().get_list_of_gitignore_files()
    click.echo("List of all .gitignore files available to download:\n")
    for f in list_of_gitignore_files:
        click.echo(f["name"])

def main():
    pass
    
    
if __name__ == '__main__':
    main()