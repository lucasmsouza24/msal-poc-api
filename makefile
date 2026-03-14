.PHONY: push docker-up docker-down

push:
	git push origin main
	git push azure main

docker-up: docker-down
	docker build -t msal-poc-api .
	docker run --name msal-poc-api --env-file .env -p 8000:8000 -it -d msal-poc-api
	docker logs msal-poc-api -f

docker-down:
	docker stop msal-poc-api || true
	docker rm msal-poc-api || true
