from flask import Flask, render_template,  request
from entidades.number import Number

app = Flask(__name__)


#request -> petición
#response -> respuesta
#client -> cliente

@app.route('/')
def index():
    return render_template('welcome.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/par')
def par():
   return render_template ('par.html', resultado=None)

@app.route('/es_par', methods= ['POST'])
def es_par():
    try:
        num1 = int(request.form.get('value'))

        number = Number(num1)
        resultado = number.es_par() 
        return render_template('par.html', resultado = resultado)
    except (ValueError):
        return render_template('par.html', resultado = "Error: Ingrese un número válido")
    

if __name__ == "__main__":
    app.run(debug=True)