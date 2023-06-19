from flask import Flask, render_template
import json

app = Flask(__name__)

file_name = "countries.json" # Nombre del archivo JSON

with open(file_name, "r", encoding="utf8") as json_file: # Abrir el archivo JSON, EL COLMO
    json_data = json.load(json_file)# Cargar el contenido del archivo JSON

urls_main_img = []      #lista donde se guardaran las URL de las imagenes main
urls_landscape_img = [] #lista donde se guardaran las URL de las imagenes landscape

for country in json_data:                                 
    urls_landscape_img.append(country['landscape_img'])
    urls_main_img.append(country['main_img'])                  # se recorre cada elemento del json y se guardan las url's en listas paralelas

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')

@app.route('/')
def index():
    return render_template('index.html', countries=json_data, imagenes=urls_landscape_img) #le paso como parametro la data del json
 
@app.route('/programs') 
def programs(): 
    return render_template('programs.html', countries=json_data, imagenes=urls_main_img) #le paso como parametro la data del json
 
@app.route('/inscriptions')  
def inscriptions(): 
    return render_template('inscriptions.html', countries=json_data, imagenes=urls_main_img) #le paso como parametro la data del json

 
if __name__ == '__main__':
    app.run()