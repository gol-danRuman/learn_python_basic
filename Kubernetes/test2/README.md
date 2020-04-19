#Test2 kubernetes folder
	

- 	using deployment yaml file and service yaml file
-	using my dockerhubtest image

#Steps used:
	-	minikube start --cpus 2 --memory 4096
	-	kubectl apply -f demo-deployment.yml
	-	kubectl get all
	-	kubectl apply -f demo-service.yml
	-	minikube service python-helloworld-service --url


