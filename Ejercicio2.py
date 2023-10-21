from pyfiglet import Figlet
import random


fuentes_disponibles = Figlet().getFonts()


fuente = input("Ingrese el nombre de la fuente (o presione Enter para una fuente aleatoria): ")
if not fuente:
    fuente = random.choice(fuentes_disponibles)


texto = input("Ingrese el texto que desea imprimir: ")


figlet = Figlet(font=fuente)


print(figlet.renderText(texto))

