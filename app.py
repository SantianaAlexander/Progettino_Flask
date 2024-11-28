from flask import Flask, render_template, request, redirect, url_for

#inizializza l'app Flask
app = Flask(__name__)

listaSpesa = []

#rotta principale
@app.route('/')
def home():
    return render_template('index.html', listaSpesa = listaSpesa)

@app.route('/aggiungi', methods=['POST']) 
def aggiungi_prodotto():
    elemento = request.form['elemento']
    if elemento:
        listaSpesa.append(elemento)
    return redirect(url_for('home'))

@app.route('/rimuovi/<int:indice>', methods=['POST']) #Fatto grazie a suggerimento del file
def rimuovi_prodotto(indice):
    if 0 <= indice < len(listaSpesa):
        listaSpesa.pop(indice)
    return redirect(url_for('home'))
    

#avvio dell'app Flask - Sempre mettere alla fine
if __name__ == '__main__':
    app.run(debug=True)
