# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

from flask import Flask, request, jsonify 
import openai 
import os # Import the os module

app = Flask(__name__)

openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/gpt', methods=['POST']) 
def gpt_response(): 
    data = request.json 
    try: 
        text = data['text'] 
        response = openai.Completion.create(engine="ft:gpt-3.5-turbo-1106:personal:pocketdoc:99jRcUpe", prompt=text) # Ensure to use the 'text' variable from the request ) 
        return jsonify({'response': response.choices[0].text.strip()}) 
    except Exception as e: 
        return jsonify({'error': str(e)})

if __name__ == 'main': 
    app.run(debug=True)