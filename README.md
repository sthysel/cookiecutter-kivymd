# Cookiecutter KivyMD template (Version 0.0.1)

![cookiecutter](docs/pics/cookiecutter.jpg)

This is a [cookiecutter](https://github.com/cookiecutter/cookiecutter) KivyMD
template to automate the creation of a new [Kivy](https://kivy.org) project. It
provides a containerized android build environment to build and deploy the
application to an attached android device.


# Usage

## Quick start for existing cookiecutter users

```bash
$ cookiecutter gh:sthysel/cookiecutter-kivymd
$ make deploy
```
## Install cookiecutter 

Install cookiecutter where its convenient

```bash
$ python -m venv ~/.venvs/ccutter
$ . ~/.venvs/ccutter/bin/activate
$ python -m pip install cookiecutter
$ cookiecutter gh:sthysel/cookiecutter-kivymd
$ make deploy
```

# Notes

To install the android app using `adb` 

```
$ adb install -r bin/theapp.apt
```
