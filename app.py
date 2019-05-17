from flask import Flask, render_template, request, redirect, url_for
from tweet_connection import TweetConnection

app = Flask(__name__)

conexao = TweetConnection()

@app.route("/")
def hello():
    return render_template("pesquisa.html")

@app.route("/key")
def pesquisa():
        return render_template("pesquisa.html")

@app.route("/keyword", methods=["POST"])
def pegando_palavra():
        palavra_chave = request.form["keyword"]
        idioma = request.form["language"]
        return redirect(url_for("mostrando_resultados", keyword=palavra_chave, language=idioma))

@app.route("/resultados")
def mostrando_resultados():
        palavra_chave = request.args.get("keyword")
        idioma = request.args.get("language")
        tweetss = pegando_tweets(palavra_chave, idioma)
        return render_template("resultado_pesquisa.html", tweets=tweetss)


def pegando_tweets(chave, idioma):
        return conexao.procurando_tweets(chave, idioma)


app.run(debug=True)