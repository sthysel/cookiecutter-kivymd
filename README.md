# Cookiecutter KivyMD template (Version 0.0.1)

![cookiecutter](docs/pics/cookiecutter.jpg)

This is a [cookiecutter](https://github.com/cookiecutter/cookiecutter)
[KivyMD](https://github.com/kivymd/KivyMD) template to automate the creation of
a new [Kivy](https://kivy.org) project. 

It also provides a containerized android build environment to build and deploy
the application to an attached android device.

# Why even ?

[KivyMD](https://github.com/kivymd/KivyMD) is a collection of Material Design
compliant widgets for use with [Kivy](https://kivy.org) which is framework for
building cross-platform, touch-enabled graphical applications in Python. 

This cookiecutter recipe will create the basic scaffolding for a KivyMD
application as well as a [buildozer](https://github.com/kivy/buildozer) spec
file to manage the android build and deploy process. It also provides a
buildozer container to do the actual build and deploy work, which is often the
most tricky bit of getting your app on the phone.


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
