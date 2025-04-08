build:
	./buil
render-start:
	gunicorn task_manager.wsgi
dev:
	uv run manage.py runserver