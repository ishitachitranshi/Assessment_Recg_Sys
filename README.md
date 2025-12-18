📊 Assessment Recognition & Recommendation System
A simple web‑based Assessment Recognition and Recommendation System built with Python and Flask.
It reads assessment data from Excel files, generates recommendations using a custom recommender logic, and serves the results through a web interface.

🚀 Features
Loads and processes assessment datasets

Generates recommendations using a recommendation module

Flask‑based web application with simple UI

Static assets (CSS/JS) and HTML templates for front‑end

🧠 About
This project uses dataset files (Gen_AI Dataset.xlsx, gen_ai_data.xlsx) and the Python script recommender.py to produce assessment recommendations. The app.py Flask application serves web pages and handles routing to display recommendations.

🛠️ Tech Stack
Python – Backend logic

Flask – Web application framework

HTML / CSS / JavaScript – Front‑end UI

pandas – Data processing

Additional Python libraries listed in requirements.txt

📦 Installation
Clone the repository:

bash
Copy code
git clone https://github.com/ishitachitranshi/Assessment_Recg_Sys.git
cd Assessment_Recg_Sys
Install dependencies:

bash
Copy code
pip install -r requirements.txt
▶️ Usage
Run the Flask application:

bash
Copy code
python app.py
Open your browser and go to:

arduino
Copy code
http://localhost:5000
Interact with the web application to view and get recommendations.

📁 Project Structure
plaintext
Copy code
Assessment_Recg_Sys/
├── static/               # CSS & JavaScript assets
├── templates/            # HTML files (Flask views)
├── app.py                # Main Flask server
├── recommender.py        # Recommendation logic
├── Gen_AI Dataset.xlsx   # Dataset used for generating recommendations
├── gen_ai_data.xlsx      # Additional dataset file
├── requirements.txt      # Python dependencies
├── README.md             # This README
🌐 Live Demo
Check out the hosted version of the application:
👉 https://shl-generative-ai.onrender.com 
github.com

✍️ Author
Ishita Chitranshi 
github.com
