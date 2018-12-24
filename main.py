from flask import Flask, render_template, request
from vigenere import encrypt
import jinja2
import os

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)



app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    template = jinja_env.get_template('form1.html')
    return template.render()

@app.route("/encrypt",methods=['POST'])

def encrypt_txt():
    key = request.form['key']
    text = request.form['text']
    template = jinja_env.get_template('form2.html')
    encipher = encrypt(text,key)
    return template.render(enciphered=encipher)

app.run()