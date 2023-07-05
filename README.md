# ImagineBooks AI

ImagineBooks AI is a Python program that uses the Dezgo API to generate images based on user prompts and extract text from PDF files. The program provides a graphical user interface (GUI) for easy interaction.

## Features

- Generate Images: Users can enter a prompt in the text box and click the "Generate Image" button to generate an image based on the provided prompt. The generated image will be displayed in the GUI.

- Upload PDF Files: Users can upload a PDF file by clicking the "Upload PDF" button. The program will extract the text content from the uploaded PDF file and display it in a scrollable text box.

## Requirements

- Python 3.x
- tkinter (Python GUI library)
- PIL (Python Imaging Library)
- requests (HTTP library)
- PyMuPDF (Python library for PDF handling)

# Installation

1. Clone the repository:

git clone https://github.com/your-username/imaginebooks-ai.git

2. Install the required dependencies using pip:

pip install -r requirements.txt

3. Sign up and obtain an API key from Dezgo:

   - Visit [Dezgo website](https://www.dezgo.com/) and sign up for an account.
   - Obtain your API key from your account settings.

4. Update the API key in the ```api.py``` script:


#### Set up the base URL for the Dezgo API:

```base_url = "https://api.dezgo.com"```

#### Sign up and obtain your API key from Dezgo:

```api_key = "YOUR_API_KEY_HERE"```

# Usage
Run the main.py script to start the program:

```python main.py```

1. Enter a prompt in the text box.
2. Click the "Generate Image" button to generate an image based on the prompt.
3. Click the "Upload PDF" button to upload a PDF file and extract its text content.
   
# Video Representation
:movie_camera: [![Video File #1](https://drive.google.com/uc?export=download&id=12f3CKPQYTe1meZsCTgZJfD5YRKCzXqOz)](https://drive.google.com/file/d/12f3CKPQYTe1meZsCTgZJfD5YRKCzXqOz/view?usp=drive_link)


If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
