import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from PIL import Image

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_text, prompt, image_data):
    """
    Generate a response using the Gemini model.
    """
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input_text, image_data[0], prompt])
    return response.text

def input_image_setup(uploaded_file):
    """
    Prepare the uploaded image file for processing.
    """
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Initialize Streamlit app
st.set_page_config(page_title="Nutrition App Using Gemini Pro: Your Comprehensive Guide to Healthy")

st.header("Nutrition App Using Gemini Pro: Your Comprehensive Guide to Healthy")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "JPG", "Jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Tell me about the Total Calories")

input_prompt = """
You are an expert nutritionist who needs to analyze the food items from the image
and calculate the total calories. Provide the details of every food item with calorie intake
in the following format:

1. item 1 - number of calories
2. Item 2 - number of calories
...
...
Finally, mention whether the food is healthy or not and provide the percentage split of the ratio of carbohydrates,
fats, fibers, sugar, and other dietary components.
"""

if submit:
    image_data = input_image_setup(uploaded_file)
    response = get_gemini_response("", input_prompt, image_data)
    st.header("The Response is")
    st.write(response)