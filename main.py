import bugsnag
import os

stage = os.getenv("STAGE", "development")

bugsnag.configure(
    api_key=os.getenv("BUGSNAG_API_KEY"), release_stage=stage, send_code=False
)


def main(request):
    data = request.get_json()

    properties = data["properties"]

    violation_type = properties["violationType"].replace(" ", "")
    custom_exception = type(violation_type, (Exception,), {})

    context = properties["violationField"] + " - " + properties["sourceSlug"]
    description = (
        properties["violationField"] + " - " + properties["violationDescription"]
    )

    bugsnag.notify(
        custom_exception(description),
        context=context,
        meta_data=properties,
        grouping_hash=context,
        severity="error",
    )

    return "OK"
