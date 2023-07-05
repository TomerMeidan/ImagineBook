from tkinter import Tk, Label, Button, filedialog, Text, Frame, Scrollbar, INSERT, END, constants
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk
import os
from api import generate_image_from_prompt
from pdf import get_pdf_text, get_pdf_file_name


# Sign up and obtain your API key from dezgo.com
api_key = "YOUR-API-KEY-HERE"

# Set up the base URL for the dezgo.com API
base_url = "https://api.dezgo.com"

# Prepare the request payload with the desired text prompt
data = {
    "prompt": "",
    "model": "absolute_reality_1",
    "negative_prompt": "ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, "
                       "extra limbs, disfigured, deformed, body out of frame, blurry, bad anatomy, blurred, watermark, "
                       "grainy, signature, cut off, draft",
}

# Create the GUI window
window = Tk()
window.title("ImagineBooks AI")
window.geometry("1600x800")

# Create a label and text box for the prompt
prompt_label = Label(window, text="Enter a prompt:")
prompt_label.pack()

prompt_text = Text(window, height=6, width=50)
prompt_text.pack()

# Create buttons for generating an image and uploading a PDF
generate_button = Button(window, text="Generate Image", width=15, height=2)
generate_button.pack(pady=10)

upload_button = Button(window, text="Upload PDF", width=15, height=2)
upload_button.pack(pady=10)

# Create a frame for the PDF display
pdf_frame = Frame(window)
pdf_frame.pack(side="left", fill=constants.BOTH, expand=True)

# Create a label for displaying the PDF file name above the text box
pdf_file_label = Label(pdf_frame, text="No PDF file uploaded", font=("Arial", 15), padx=100)
pdf_file_label.pack(pady=10)

# Create a scrollable text box to display the PDF content
text_box = Text(pdf_frame, wrap="word")
text_box.pack(side="left", fill=constants.BOTH, expand=True)

# Create a scrollbar for the text box
scrollbar = Scrollbar(pdf_frame)
scrollbar.pack(side="right", fill=constants.Y)

# Configure the scrollbar to scroll the text box
scrollbar.config(command=text_box.yview)
text_box.config(yscrollcommand=scrollbar.set)

# Create a frame for the generated image
image_frame = Frame(window)
image_frame.pack(side="right", fill=constants.BOTH, expand=True)

# Create a label for displaying the generated image
image_label = Label(image_frame)
image_label.pack(pady=10)

# Define global variables
file_path = None
photo = None
file_name = ""


# Function to display the selected PDF file
def display_pdf():
    global file_path
    global file_name

    # Open a file dialog to select a PDF file
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])

    # Display the PDF file name without extension on the labels
    file_name = get_pdf_file_name(file_path)
    pdf_file_label.config(text=file_name)

    # Get the text content of the PDF file
    pdf_text = get_pdf_text(file_path)

    # Clear the text box
    text_box.delete(1.0, END)

    # Insert the extracted text into the text box
    text_box.insert(INSERT, pdf_text)


# Function to generate an image from the prompt
def generate_image():
    # Get the prompt text entered by the user
    prompt = prompt_text.get("1.0", "end-1c")  # Get all the text in the text box

    # Update the request payload with the user's prompt
    data["prompt"] = prompt

    # Generate the image from the prompt
    image_buffer = generate_image_from_prompt(base_url, api_key, data)

    # Create a PIL image from the image buffer
    image = Image.open(image_buffer)

    # Display the image on the GUI
    image.thumbnail((400, 400))  # Resize the image to fit the label
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.image = photo  # Keep a reference to prevent garbage collection


# Bind the display_pdf function to the upload_button
upload_button.config(command=display_pdf)

# Bind the generate_image function to the generate_button
generate_button.config(command=generate_image)

# Run the GUI main loop
window.mainloop()
