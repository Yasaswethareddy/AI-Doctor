🍎 Nutrition App Using Gemini Pro: Your Comprehensive Guide to Healthy Eating

This project is a Streamlit web application that leverages Google’s Gemini Pro AI model to analyze food images, estimate calorie intake, and provide a nutritional breakdown.

Upload an image of food, and the app will:

Detect food items in the image.

Estimate calories per item.

Provide a total calorie count.

Give a nutritional ratio breakdown (carbohydrates, fats, fibers, sugar, etc.).

Suggest whether the food is healthy or not.

🚀 Features

📷 Upload food images (.jpg, .jpeg, .png).

⚡ Powered by Google Gemini Pro (1.5 Flash) for image + text understanding.

🧮 Provides detailed calorie analysis for each food item.

🥗 Offers dietary insights for healthier choices.

🌐 Interactive and user-friendly Streamlit UI.

📂 Project Structure
nutrition-app/
│── app.py              # Main Streamlit application
│── requirements.txt    # Required dependencies
│── .env                # Store your Google API Key (not pushed to GitHub)
│── README.md           # Project documentation

🛠️ Installation & Setup

Clone the repository

git clone https://github.com/your-username/nutrition-app.git
cd nutrition-app


Create and activate a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate   # For macOS/Linux
venv\Scripts\activate      # For Windows


Install dependencies

pip install -r requirements.txt


Set up environment variables

Create a .env file in the root directory.

Add your Google API Key:

GOOGLE_API_KEY=your_api_key_here


Run the app

streamlit run app.py

📦 Requirements

Python 3.8+

Streamlit

Google Generative AI SDK (google-generativeai)

Pillow (PIL)

python-dotenv

Install with:

pip install streamlit google-generativeai pillow python-dotenv

🧑‍⚕️ Example Output

Input: Uploaded image of rice, curry, and salad.

Output:

1. Rice - 206 calories
2. Curry - 180 calories
3. Salad - 90 calories

Total Calories: 476

Carbohydrates: 55%
Fats: 20%
Fibers: 15%
Sugar: 5%
Other: 5%

✅ This meal is considered healthy.

🔒 Environment Variables

This project requires:

GOOGLE_API_KEY → Google Gemini Pro API key.

🤝 Contributing

Contributions are welcome! If you’d like to improve the calorie estimation or UI, feel free to fork the repo and create a pull request.

📜 License

This project is licensed under the MIT License.

🙌 Acknowledgments

Streamlit
 for rapid app development.

Google Generative AI
 for the Gemini Pro API.

Pillow
 for image handling.
