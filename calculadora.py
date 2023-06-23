from flask import Flask, render_template, request
import datetime

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
            data = request.form[f'data_{i}']
            cheques.append((valor_cheque, data))

    total_cheques = len(cheques)
    total_valor_cheques = sum(cheque[0] for cheque in cheques)

    desconto_total = 0
    for cheque in cheques:
        taxa_juros = float(request.form['taxa_juros'])
        valor_cheque = cheque[0]
        data = cheque[1]

        # Convertendo a taxa de juros para decimal
        taxa_decimal = taxa_juros / 100

        # Calculando o desconto
        desconto = taxa_decimal * valor_cheque
        desconto_total += desconto

    valor_total_descontado = total_valor_cheques - desconto_total

    return render_template('resultado.html', total_cheques=total_cheques, total_valor_cheques=total_valor_cheques,
                           desconto_total=desconto_total, valor_total_descontado=valor_total_descontado)

if __name__ == '__main__':
    app.run(debug=True)
