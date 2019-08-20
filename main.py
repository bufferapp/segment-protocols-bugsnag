import bugsnag
import os
import base64

stage = os.getenv("STAGE", "development")

bugsnag.configure(
    api_key=os.getenv("BUGSNAG_API_KEY"), release_stage=stage, send_code=False
)


def main(request):
    data = request.get_json()

    # Authentication
    token = request.headers.get("Authorization").split()[1]
    decoded_token = base64.b64decode(token)[:-1].decode()
    if str(decoded_token) != str(os.getenv("AUTH_TOKEN")):
        return "Unauthorized", 401

    # Get information about the violations
    properties = data["properties"]
    violation_type = properties["violationType"].replace(" ", "")
    custom_exception = type(violation_type, (Exception,), {})
    context = properties["violationField"] + " - " + properties["sourceSlug"]
    description = (
        properties["violationField"] + " - " + properties["violationDescription"]
    )

    # Notify Bugsnag
    bugsnag.notify(
        custom_exception(description),
        context=context,
        meta_data=properties,
        grouping_hash=context,
        severity="error",
    )

    return "OK", 200
