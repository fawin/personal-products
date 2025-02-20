run:
	uv run manage.py runserver

migrate:
	uv run manage.py migrate

migrations: 
	uv run manage.py makemigrations

createapp:
	uv run manage.py startapp $(app)

check:
	uv run manage.py check

.PHONY:
	createapp migrate migrations run check