# {{cookiecutter.app_name}} (Version 0.0.1)

# make commands
- `make deploy`
    - build your app with [buildozer](https://buildozer.readthedocs.io/) and deploy it to your conencted android device
- `make tests`
    - run tests with [Pytests](https://docs.pytest.org/en/stable/) in tests folder
- `make quality`
    - run [Black](https://black.readthedocs.io/en/stable/), [isort](https://pycqa.github.io/isort/) and [Flake8](https://flake8.pycqa.org/en/latest/) on your code
- `make clean`
    - Clean your current repository
- `make poetry $args`
    - Execute [Poetry](https://python-poetry.org/) CLI on your project with "$args" parameters
- `make run-ide`
    - run [VS code in the browser](https://hub.docker.com/r/codercom/code-server) with ms-python.python and VisualStudioExptTeam.vscodeintellicode plugins on your project
