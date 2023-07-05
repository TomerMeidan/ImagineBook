import requests
from io import BytesIO
import json.decoder


def generate_image_from_prompt(base_url, api_key, data):
    # Set up the API key header
    headers = {
        "X-Dezgo-Key": api_key,
        "Content-Type": "application/json"
    }

    try:
        # Make the API request
        response = requests.post(base_url + "/text2image", json=data, headers=headers, stream=True)
        response.raise_for_status()  # Raise an exception if the request was unsuccessful

        # Get the total length of the response content (in bytes)
        total_length = int(response.headers.get("content-length", 0))

        # Create a buffer to store the image data
        buffer = BytesIO()
        downloaded_length = 0

        # Iterate over the response content and update the buffer
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                buffer.write(chunk)
                downloaded_length += len(chunk)

        # Return the image data from the buffer
        buffer.seek(0)
        return buffer

    except requests.exceptions.RequestException as e:
        # Handle any errors that occurred during the API request
        print("Error:", e)

    except json.decoder.JSONDecodeError as e:
        # Handle JSONDecodeError if the response cannot be parsed as JSON
        print("JSONDecodeError:", e)
