build:
	./build.sh

render-start:
	gunicorn task_manager.wsgi

dev:
	uv run python3 manage.py runserver

install:
	uv sync

collectstatic:
	uv run python3 manage.py collectstatic --no-input

migrate:
	uv run python3 manage.py migrate

migrations:
	uv run python3 manage.py makemigrations

test:
	python3 manage.py test

lint:
	ruff check --fix
	ruff format