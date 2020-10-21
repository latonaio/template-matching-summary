docker-build:
	bash deployment/docker-build-template-matching-summary.sh
	bash deployment/docker-build-template-matching-summary-server.sh

docker-push:
	bash deployment/docker-build-template-matching-summary.sh push
	bash deployment/docker-build-template-matching-summary-server.sh push

python-proto:
	python3 -m grpc_tools.protoc -I. --python_out=./ --grpc_python_out=./ ./proto/*.proto
	cp proto/*.py server/proto/
	cp proto/*.py client/proto/
	rm -rf proto/*.py

apply:
	-kubectl apply -f deployment/k8s/template-matching-summary.yml
	-kubectl apply -f deployment/k8s/template-matching-summary-server.yml

delete:
	-kubectl delete -f deployment/k8s/template-matching-summary.yml
	-kubectl delete -f deployment/k8s/template-matching-summary-server.yml

run-template-matching-summary:
	# client run, not server
	bash deployment/run.sh template-matching-summary server
