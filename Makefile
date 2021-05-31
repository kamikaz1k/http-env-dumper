run-local:
	docker run --rm -p 9090:80 http-env-dumper

build:
	docker build --tag=http-env-dumper .
