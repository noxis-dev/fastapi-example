import json

import cv2

from ..config import settings


def get_azure_vision_headers(content_type: str) -> dict[str, str]:
    """Get the headers for the Azure Vision API."""
    return {
        "Content-Type": content_type,
        "Ocp-Apim-Subscription-Key": settings.AZURE_VISION_KEY,
    }


def get_azure_vision_url() -> str:
    """Get the endpoint for the Azure Vision API."""
    return settings.AZURE_VISION_ENDPOINT + settings.AZURE_VISION_API_ENDPOINT


def convert_image_to_bytes(image) -> bytes:
    """Convert the image to bytes."""
    retval, buffer = cv2.imencode(".jpg", image)
    img_bytes = buffer.tobytes()
    return img_bytes


def convert_to_json(data_string: str) -> dict:
    """Convert the string received from AI messege to JSON."""
    start_index = data_string.find("{")
    end_index = data_string.rfind("}") + 1
    valid_json_string = data_string[start_index:end_index]
    json_data = json.loads(valid_json_string)
    return json_data
