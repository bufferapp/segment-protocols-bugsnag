IMAGE_NAME := bufferapp/segment-violations-bugsnag:0.1.0

.DEFAULT_GOAL := run

.PHONY: run
run: build
	docker run --env-file .env --rm $(IMAGE_NAME)

.PHONY: build
build:
	 docker build . -t $(IMAGE_NAME)

.PHONY: push
push: build
	 docker push $(IMAGE_NAME)

.PHONY: dev
dev: build
	docker run -p 5000:5000 -it --env-file .env --rm -v $(PWD):/app $(IMAGE_NAME)  /bin/bash

.PHONY: deploy
deploy:
	@ gcloud functions deploy segment-violations-bugsnag \
        --entry-point main --runtime python37 --trigger-http \
        --set-env-vars=BUGSNAG_API_KEY=$(BUGSNAG_API_KEY),STAGE=production
