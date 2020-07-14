from setuptools import setup
import setuptools

setup(
    name="download-gitignore",
    version="2.0.1",
    description="A Python CLI program to download .gitignore files from Github's repository",
    url="https://github.com/vccolombo/download-gitignore",
    author="Víctor Cora Colombo",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[
        "click==7.0",
        "requests==2.22.0",
    ],
    entry_points={
        "console_scripts": ["dgi=download_gitignore.download_gitignore:download_gitignore",
            "download-gitignore=download_gitignore.download_gitignore:download_gitignore"],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Version Control :: Git'
    ],
    python_requires='>=3.5'
)
