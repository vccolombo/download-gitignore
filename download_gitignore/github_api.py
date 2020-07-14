import requests
import urllib.request
from requests.exceptions import HTTPError
import click

class github_api:
    def get_list_of_gitignore_files(self):
        response = requests.get("https://api.github.com/repos/github/gitignore/contents").json()
        list_of_gitignore_files = [obj for obj in response 
            if obj["type"] == "file" and ".gitignore" in obj["name"]]
        return list_of_gitignore_files

    def download_gitignore_file(self, languages):
        click.echo("Trying to download .gitignore file...\n")

        try:
            list_of_gitignore_files = self.get_list_of_gitignore_files()
            github_gitignore_names = [ obj["name"].lower() for obj in list_of_gitignore_files ]
            user_gitignore_names = [ '{}.gitignore'.format(lang.lower()) for lang in languages ]

            # check if there is a .gitignore for all languages
            for lang in languages:
                if '{}.gitignore'.format(lang.lower()) not in github_gitignore_names:
                    click.echo('.gitignore not found for {}. Use download-gitignore list to list all the available files'.format(lang))
                    return

            # get a list with all files to download
            language_gitignore_objects = [obj for obj in list_of_gitignore_files
                if obj["name"].lower() in user_gitignore_names]
            # if this list is not empty, download the files
            if len(language_gitignore_objects) != 0:
                with open('.gitignore', 'w') as f:
                    for obj in language_gitignore_objects:
                        url = obj["download_url"]
                        click.echo("Downloading {} from {}".format(obj["name"], url))
                        with urllib.request.urlopen(url) as res:
                            f.write(res.read().decode('utf-8') + "\n\n")
                    
                click.echo("Download successful")
                    
        except HTTPError as http_err:
            click.echo("HTTP error occurred: " + http_err)
        except Exception as err:
            click.echo("Other error occurred: " + err) 
            click.echo("\nYou may want to check your internet connection.")