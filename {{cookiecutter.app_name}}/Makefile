.PHONY: tests clean quality

tests: build-devbox
	$(call execute_cmd) run pytest -c pyproject.toml -s --log-cli-level=10  --junitxml=./junit_report.xml

quality: build-devbox
	$(call execute_cmd) run black -l 200 --target-version py37 {{cookiecutter.app_name}}
	$(call execute_cmd) run isort --recursive ./{{cookiecutter.app_name}} -vvv
	$(call execute_cmd) run flake8 {{cookiecutter.app_name}} --ignore=E501

clean:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
	rm -f junit_report.xml
	rm -Rf .coverage
	rm -Rf dist
	rm -Rf *.egg-info
	rm -Rf .pytest_cache

# if the first argument is "poetry"...
ifeq (poetry,$(firstword $(MAKECMDGOALS)))
  # use the rest as arguments for "poetry"
  POETRY_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  # ...and turn them into do-nothing targets
  $(eval $(POETRY_ARGS):dummy;@:)
endif

build-devbox:
	docker build -t {{cookiecutter.app_name | lower}}-devbox -f Dockerfile.dev .

poetry: build-devbox
	$(call execute_cmd) $(POETRY_ARGS)

distclean: build-buildozer
	docker run --interactive --tty --rm -v buildozer_home:/home/user/.buildozer  --volume ${CURDIR}:/home/user/hostcwd {{cookiecutter.app_name | lower}}-buildozer distclean

build-buildozer:
	docker build -t {{cookiecutter.app_name | lower}}-buildozer -f Dockerfile .

deploy: build-buildozer
	docker run -it \
	  --privileged \
	  --volume /dev/bus/usb:/dev/bus/usb \
	  --volume buildozer_home:/root/.buildozer \
	  --volume gradle_cache:/root/.gradle \
	  --volume ${CURDIR}:/home/user/hostcwd \
	  {{cookiecutter.app_name | lower}}-buildozer android debug deploy run logcat

build-ide:
	docker build -t {{cookiecutter.app_name | lower}}-ide -f Dockerfile.ide .

run-ide:
	docker run -it -p 127.0.0.1:8080:8080 -v "${CURDIR}:/home/coder/project" {{cookiecutter.app_name | lower}}-ide --auth none &
	xdg-open "http://localhost:8080/?folder=vscode-remote%3A%2F%2Flocalhost%3A8080%2Fhome%2Fcoder%2Fproject" &


define execute_cmd
	docker run -i -v ${CURDIR}:/opt/{{cookiecutter.app_name}} --env-file .env {{cookiecutter.app_name | lower}}-devbox $(1)
endef
