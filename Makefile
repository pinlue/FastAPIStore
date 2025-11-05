.PHONY: install run seed docker-up

install:
	pip install -r requirements.txt

run:
	uvicorn app.main:app --reload

seed:
	python seed_data.py

docker-up:
	docker compose up --build
