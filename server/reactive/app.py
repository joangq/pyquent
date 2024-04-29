from flask import Flask, request, jsonify, render_template, send_from_directory
from pyquent import Pyquent

"""
TODO: This only works for single lines, which means that it does parse Sequent Calculus correctly,
but cannot handle natural deduction trees.
"""

pyquent = Pyquent()
app = Flask(__name__, static_folder='static')

def process_input(input):
    return '' if not input else pyquent.transform(input).to_latex()

@app.route('/')
def home():
    return send_from_directory('static', 'index.html')

@app.route('/process', methods=['POST'])
def process():
    text = request.json.get('text', '')
    error_message = ""
    modified_text = ""

    try:
        modified_text = process_input(text)
    except Exception as e:
        error_message = str(e)
    
    return jsonify({'response': modified_text, 'errors': error_message})

if __name__ == '__main__':
    from waitress import serve
    serve(app, host='localhost', port=8080)