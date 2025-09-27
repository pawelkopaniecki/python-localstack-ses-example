run:
	uvicorn src.main:app --port 8080 --reload

docker-run:
	docker compose -f ./docker/compose.yaml up -d --build 

add-permissions:
	chmod +x ./resources/init.sh

format:
	ruff format

lint-check:
	ruff check

lint-fix:
	ruff check --fix
