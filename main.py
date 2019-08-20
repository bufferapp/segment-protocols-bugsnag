import bugsnag
import os

stage = os.getenv("STAGE", "development")

bugsnag.configure(
    api_key=os.getenv("BUGSNAG_API_KEY"), release_stage=stage, send_code=False
)


class InvalidType(Exception):
    pass


class Required(Exception):
    pass


violations_map = {"Invalid Type": InvalidType, "Required": Required}


def main(request):
    data = request.get_json()

    properties = data["properties"]
    violation = violations_map.get(properties["violationType"])
    context = properties["violationField"] + " - " + properties["sourceSlug"]
    description = (
        properties["violationField"] + " - " + properties["violationDescription"]
    )

    bugsnag.notify(violation(description), context=context, meta_data=properties)

    return "OK"
