from pyfiglet import Figlet
import random

# Obtener la lista de fuentes disponibles
fuentes_disponibles = Figlet().getFonts()

# Solicitar al usuario el nombre de la fuente
fuente = input("Ingrese el nombre de la fuente (o presione Enter para una fuente aleatoria): ")
if not fuente:
    fuente = random.choice(fuentes_disponibles)

# Solicitar al usuario el texto a imprimir
texto = input("Ingrese el texto que desea imprimir: ")

# Configurar la fuente seleccionada
figlet = Figlet(font=fuente)

# Imprimir el texto con la fuente seleccionada
print(figlet.renderText(texto))

