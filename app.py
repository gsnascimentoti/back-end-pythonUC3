from doctest import debug

from flask import Flask, render_template, request
import mensagens
app = Flask(__name__)

# Verbos
# get - verbo(metodo) http responsavel por chamadas simples, urls
# post - verbo(metodo) http responsável por chamadas complexas, salvamento de dados e etc

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Obtém o nome do formulário
        nome = request.form.get("nome")# atributo name do formulário

        # Gera mensagem
        mensagem = f"Olá {nome}!\nMensagem: {mensagens.obter_mensagens_aleatoria()}"

        # Renderiza a página com a mensagem
        return render_template("index.html", texto=mensagem)

    # Renderiza a página inicial com o formulário
    return render_template("index.html")

# @app.route("/backend_com_python", methods=["GET", "POST"])
# def backend_com_python():
#     return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)
