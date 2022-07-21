import phonenumbers
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("verif.html")

@app.route("/ver", methods = ['POST',])
def ver():
    # Formatação do valor recebido.
    telefone = request.form['telefone']
    numero = telefone
    numero_cliente = phonenumbers.parse(numero, "BR")
    numero_formatado = phonenumbers.format_number(numero_cliente, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    numero = numero_formatado
    return render_template("verifi.html", resposta = numero)


app.run(debug=True)
