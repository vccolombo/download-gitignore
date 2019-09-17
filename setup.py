from setuptools import setup

setup(
    name="download-gitignore",
    version="0.1",
    description="A Python CLI program to download .gitignore files from Github's repository",
    url="https://github.com/vccolombo/download-gitignore",
    author="Víctor Cora Colombo",
    author_email="victorcora98@gmail.com",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=[
        "click==7.0",
        "requests",
    ],
    entry_points={
        "console_scripts": ["dgi=download_gitignore.download_gitignore:download_gitignore"],
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
)
