import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import openai

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)

# Load OpenAI API key from environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')
print(f"OpenAI API Key: {os.getenv('OPENAI_API_KEY')}")

@app.route('/')
def home():
    return 'Welcome to Dishly!'

@app.route('/generate-recipe', methods=['POST'])
def generate_recipe():
    data = request.json
    ingredients = data.get('ingredients', '')
    prompt = f"Create a recipe with the following ingredients: {ingredients}\n"

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        recipe = response.choices[0].text.strip()
        return jsonify({'recipe': recipe})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)