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