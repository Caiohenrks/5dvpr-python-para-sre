from datetime import datetime
from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route("/")
def hello():
    return f"<h1>Hello World<br>{str(datetime.now())}</h1>"

@app.route("/api/soma", methods=["POST"])
def api_soma():
    data = request.get_json()
    if not data or "var1" not in data or "var2" not in data:
        return jsonify({"error": "É necessário enviar os campos 'var1' e 'var2' no body"}), 400

    try:
        var1 = float(data["var1"])
        var2 = float(data["var2"])
        result = var1 + var2
        return jsonify({"soma": result})
    except ValueError:
        return jsonify({"error": "Os valores devem ser números válidos"}), 400
    
@app.route("/api/subtracao", methods=["POST"])
def api_sub():
    data = request.get_json()
    if not data or "var1" not in data or "var2" not in data:
        return jsonify({"error": "É necessário enviar os campos 'var1' e 'var2' no body"}), 400

    try:
        var1 = float(data["var1"])
        var2 = float(data["var2"])
        result = var1 - var2
        return jsonify({"subtração": result})
    except ValueError:
        return jsonify({"error": "Os valores devem ser números válidos"}), 400

@app.route("/api/divisao", methods=["POST"])
def api_div():
    data = request.get_json()
    if not data or "var1" not in data or "var2" not in data:
        return jsonify({"error": "É necessário enviar os campos 'var1' e 'var2' no body"}), 400

    try:
        var1 = float(data["var1"])
        var2 = float(data["var2"])
        result = var1 / var2
        return jsonify({"divisão": result})
    except ValueError:
        return jsonify({"error": "Os valores devem ser números válidos"}), 400

@app.route("/api/multiplicacao", methods=["POST"])
def api_mult():
    data = request.get_json()
    if not data or "var1" not in data or "var2" not in data:
        return jsonify({"error": "É necessário enviar os campos 'var1' e 'var2' no body"}), 400

    try:
        var1 = float(data["var1"])
        var2 = float(data["var2"])
        result = var1 * var2
        return jsonify({"multiplicação": result})
    except ValueError:
        return jsonify({"error": "Os valores devem ser números válidos"}), 400
    
    
    
motivacao = [
    "O único limite para o nosso sucesso é a nossa mente.",
    "Acredite em si mesmo e tudo será possível.",
    "Não tenha medo de começar pequeno, grandes coisas vêm de passos simples.",
    "Cada desafio é uma oportunidade de crescimento.",
    "O fracasso é apenas um degrau no caminho para o sucesso.",
    "Persistência é a chave para transformar sonhos em realidade.",
    "Você é mais forte do que pensa, mais corajoso do que imagina.",
    "O esforço de hoje é o sucesso de amanhã.",
    "Tudo parece impossível até que seja feito.",
    "Grandes jornadas começam com o primeiro passo.",
    "Aprenda com os erros, eles são professores disfarçados.",
    "Nunca subestime o poder da determinação.",
    "Seja a mudança que você deseja ver no mundo.",
    "A coragem não é a ausência de medo, é agir apesar dele.",
    "Cada dia é uma nova chance de recomeçar.",
    "Mantenha o foco no objetivo, não nos obstáculos.",
    "Você é o autor da sua própria história.",
    "Acredite no processo, o sucesso virá com o tempo.",
    "Grandes sonhos exigem grandes esforços.",
    "Os limites existem apenas se você permitir.",
    "Não espere pelo momento perfeito, faça o momento perfeito acontecer.",
    "A ação é a chave para transformar planos em realidade.",
    "O sucesso é construído um passo de cada vez.",
    "Confie no caminho que está trilhando.",
    "A disciplina é o que transforma boas intenções em realizações.",
    "Pequenos progressos diários levam a grandes conquistas.",
    "Você nunca é velho demais para definir outro objetivo ou sonhar um novo sonho.",
    "Seja grato pelo que você tem enquanto trabalha pelo que deseja.",
    "A chave para o sucesso está em nunca desistir.",
    "Cada novo amanhecer traz uma nova oportunidade."
]
    
@app.route("/expiracao")
def frase():
    escolha = random.choice(motivacao)
    return f"""
    <html>
        <head>
            <style>
                body {{
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    font-family: 'Arial', sans-serif;
                    background-color: #f5f5f5;
                }}
                h1 {{
                    text-align: center;
                    font-size: 2em;
                    color: #333;
                }}
            </style>
        </head>
        <body>
            <h1>{escolha}</h1>
        </body>
    </html>
    """

    
    
    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
