import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import openai

# Load environment variables from .env file
load_dotenv()

# Access the OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
CORS(app)

# List to store ingredients
ingredients_list = []

@app.route('/')
def home():
    return 'Welcome to Dishly!'

@app.route('/generate-recipe', methods=['POST'])
def generate_recipe():
    data = request.json
    ingredients = data.get('ingredients', '')
    # Store the ingredients in the list
    ingredients_list.append(ingredients)

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": f"Create a recipe with the following ingredients: {ingredients}\n",
                }
            ],
            max_tokens=150
        )

        print(f"OpenAI response: {response}")  # Log the raw response from OpenAI

        # Correctly access the content of the response
        recipe = response.choices[0].message['content'].strip()
        print(f"Generated recipe: {recipe}")  # Log the generated recipe

        return jsonify({'recipe': recipe})
    except Exception as e:
        print(f"Error: {str(e)}")  # Print the error for debugging
        return jsonify({'error': str(e)}), 500

@app.route('/ingredients', methods=['GET'])
def get_ingredients():
    return jsonify({'ingredients': ingredients_list})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')