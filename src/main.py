
from add_to_GINI import add_one
import requests
import matplotlib.pyplot as plt
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ---------------------------- Constantes ------------------------------- #

ENDPOINT = 'https://api.worldbank.org/v2/en/country/all/indicator/SI.POV.GINI?format=json&date=2011:2020&per_page=32500&page=1&country=%22Argentina%22'

# ---------------------------- Función que obtiene el indice GINI de la API y lo grafica ------------------------------- #

def consult_and_graphic():
    
    country_requested = user_input.get() # obtencion de input de usuario
    
    response = requests.get(ENDPOINT)
    response.raise_for_status()
    response = response.json() # consulta a la API
        
    country_selected = []

    for gini in response[1]:
        if gini["country"]["value"].lower() == country_requested.lower() and gini["value"] != None:
            country_selected.insert(0, {"country": gini["country"]["value"],
                                    "value": float(gini["value"]),
                                    "date": gini["date"]}) # filtrado de respuesta de la API para obtener pais que pidio el usuario
            
    
    # creación y dibujado del gráfico de indice GINI e indice GINI+1
    x = [item["date"] for item in country_selected]  
    y = [item["value"] for item in country_selected]

    x1 = [item["date"] for item in country_selected]  
    y1 = [add_one(item["value"]) for item in country_selected]
    
    fig = plt.figure(figsize=(8, 6))
    plt.plot(x, y, marker='o', linestyle='-')
    plt.plot(x1, y1, marker='o', linestyle=':')
    
    for i, (xi, yi) in enumerate(zip(x, y)):
        plt.annotate(f'({xi}, {yi})', (xi, yi), textcoords="offset points", xytext=(0, 10), ha='center')
    
    plt.title('GINI INDEX')
    plt.xlabel('Year')
    plt.ylabel('GINI value')
    
    plt.grid(True)
    
    graph = FigureCanvasTkAgg(plt.gcf(), window)
    graph.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True) # se agrega a la ventada de tkinter para mostrar al usuario

# ---------------------------- GUI ------------------------------- #

window = Tk()
window.title("Graficador de índice GINI")
window.config(padx=100, pady=50)

text_label = Label(window, text="Escriba el nombre del pais del cual desea obtener el indice GINI: ")
text_label.pack()

user_input = Entry(window)
user_input.pack()

confirm_button = Button(window, text = "Consultar GINI", highlightthickness=0, command=consult_and_graphic)
confirm_button.pack()

window.mainloop()
