from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    cheques = []
    for i in range(1, 6):  # Considerando até 5 cheques, você pode ajustar esse valor conforme necessário
        if f'valor_cheque_{i}' in request.form:
            valor_cheque = float(request.form[f'valor_cheque_{i}'])
            data = request.form[f'data_{
