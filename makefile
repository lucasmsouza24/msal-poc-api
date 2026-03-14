push:
	git push origin main
	git push azure main

docker up:
	make docker down
	docker run --name msal-poc-api --env-file .env -p 8000:8000 -it -d msal-poc-api
	docker logs msal-poc-api -f

docker down:
	docker stop msal-poc-api || true
	docker rm msal-poc-api || true
