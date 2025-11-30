from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/adivinar', methods=['POST'])
def adivinar():
    respuestas = ["Sí", "No", "Tal vez", "Definitivamente", "Pregunta de nuevo más tarde"]
    respuesta = random.choice(respuestas)
    return respuesta

if __name__ == '__main__':
    app.run(debug=True)