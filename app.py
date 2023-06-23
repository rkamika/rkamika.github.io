from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['GET', 'POST'])
def calcular():
    if request.method == 'POST' or request.method == 'GET':
        cheques = []
        for i in range(1, 6):  # Considerando até 5 cheques, você pode ajustar esse valor conforme necessário
            if f'valor_cheque_{i}' in request.form:
                valor_cheque = float(request.form[f'valor_cheque_{i}'])
                data = request.form[f'data_{i}']
                desconto = calcular_desconto(valor_cheque)
                valor_liquido = valor_cheque - desconto
                cheques.append({'valor': valor_cheque, 'data': data, 'desconto': desconto, 'valor_liquido': valor_liquido})
        
        valor_total_cheques = sum(cheque['valor'] for cheque in cheques)
        total_desconto = sum(cheque['desconto'] for cheque in cheques)
        total_descontado = sum(cheque['valor_liquido'] for cheque in cheques)
        
        return render_template('resultado.html', cheques=cheques, valor_total_cheques=valor_total_cheques, total_desconto=total_desconto, total_descontado=total_descontado)
    else:
        return render_template('index.html')

def calcular_desconto(valor_cheque):
    taxa_juros = float(request.form['taxa_juros'])
    desconto = valor_cheque * (taxa_juros / 100)
    return desconto

if __name__ == '__main__':
    app.run(debug=True)
