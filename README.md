# Download-gitignore

A Python CLI program to download .gitignore files from [Github's repository](https://github.com/github/gitignore) easily.

***

# How to Download

**download-gitignore requires** that you have installed in your machine:

* Python >= 3.5
* Pip3

Run the following command to **install download-gitignore**:

```console
pip3 install download-gitignore
```

***

# How to use

### Download .gitignore file

Use the command `download-gitignore download` with the language you want to download the .gitignore file. 

Example:

```console
download-gitignore download python
```

You can also use `dgi`as an alias for `download-gitignore`:

```console
dgi download c++
```

**New in 2.0.0**: Now you can download more than one gitignore file at the same time:

```console
download-gitignore download c c++
```

### List all available .gitignore files

Use the command `download-gitignore list` to list all available .gitignore files to download:

```console
download-gitignore list
```
