# Segment Protocols to Bugsnag

Serverless function that send Segment Protocols Violations to Bugsnag.

## Quickstart

1. Enable [Protocols Audit Source in Segment](https://segment.com/docs/protocols/anomaly_detection/).
2. Create a [Google Cloud Function destination also in Segment](https://segment.com/docs/destinations/google-cloud-function/).
3. Grab the `BUGSNAG_API_KEY` from yourr Bugsnag Project.
4. Add `BUGSNAG_API_KEY` and `AUTH_TOKEN` (from the [Google Cloud Segment Destination](https://segment.com/docs/destinations/google-cloud-function/#configure-google-cloud-function-destination)) to your environment.
5. Run `make`
