.DEFAULT_GOAL := deploy

.PHONY: deploy
deploy:
	gcloud functions deploy segment-violations-bugsnag \
        --entry-point main --runtime python37 --trigger-http \
        --set-env-vars=BUGSNAG_API_KEY=$(BUGSNAG_API_KEY),AUTH_TOKEN=$(AUTH_TOKEN),STAGE=production
