build:
	./build.sh

render-start:
	gunicorn task_manager.wsgi

dev:
	uv run python3 manage.py runserver

install:
	uv sync

collectstatic:
	python manage.py collectstatic --no-input

migrate:
	make migrations && uv run python3 manage.py migrate

migrations:
	uv run python3 manage.py makemigrations

test:
	uv run python manage.py test

lint:
	ruff check --fix
	ruff format