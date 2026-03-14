.PHONY: push docker-up docker-down k8s-api-up k8s-api-down

# push to remote repositories
push:
	git push origin main
	git push azure main

# local api docker container build
docker-up: docker-down
	docker build -t msal-poc-api .
	docker run --name msal-poc-api --env-file .env -p 8000:8000 -it -d msal-poc-api
	docker logs msal-poc-api -f

docker-down:
	docker stop msal-poc-api || true
	docker rm msal-poc-api || true

# local api minikube k8s build

k8s-api-up: k8s-api-down
	minikube image build -t msal-poc-api .
	kubectl apply -f .k8s/service.yaml
	kubectl apply -f .k8s/deployment.yaml
	sleep 3
	kubectl logs service/msal-api-service -f

k8s-api-down:
	kubectl delete deployment msal-api-deployment || true
	kubectl delete service msal-api-service || true
