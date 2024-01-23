#!/usr/bin/env python3

from flask import Flask

# Ensure to run pip install --upgrade flask werkzeug in the pipenv terminal

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/<string:sentence>')
def print_string(sentence):
    return f"<h1>Displaying sentence {sentence}</h1>"

@app.route('/count/<int:number>')
def count(number):
    numbers = '\n'.join(str(i) for i in range(1, number+1))
    return f"<h1>Counting numbers up to {number}</h1><pre>{numbers}</pre>"

@app.route('/math/<float:num1><string:operation><float:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    
    return f"<h1>Math Operation: {num1} {operation} {num2} = {result}</h1>"

if __name__ == '__main__':
    app.run(port=5555, debug=True)
