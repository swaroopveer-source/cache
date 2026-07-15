import runpod

from app.version import VERSION
from modules.helper import get_message


def handler(event):
    input_data = event.get("input", {})

    return {
        "success": True,
        "version": VERSION,
        "message": get_message(),
        "input": input_data
    }


runpod.serverless.start({"handler": handler})
