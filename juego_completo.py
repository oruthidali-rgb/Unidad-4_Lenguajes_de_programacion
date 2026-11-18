#juego_completo
#este 
#idali
#07 de octubre de 2026
import json
import sqlite3
import random
class Jugador:
    def __init__(self, nombre):
            self.nombre = nombre
            self.puntaje = 0
class Ranking:
    def __init__(self):
         self.ranking= []
    def guardar(self,nombre,puntaje):
        self.ranking.append((nombre,puntaje))
        self.ranking.sort(key=lambda x: x[1], reverse=True)
        self.ranking=self.ranking[:5]
    def obtener_top5(self):
        return self.ranking
class ElementoJuego:
    def mostrar(self):
        print("mostrando elemento")
    def esta_correcto(self,respuesta):
        return False
    def calcular_puntaje(self,tiempo):
        pass
class PreguntaMultiple(ElementoJuego):
    def __init__(self,texto,opciones, indice_correcto):
        self.texto=texto
        self.opciones=opciones
        self.indice_correcto=indice_correcto
        self.ultima_respuesta=False
    def mostrar(self):
        print(self.texto)
        for i, opcion in enumerate(self.opciones, start=1):
            print(f"{i}.{opcion}")
    def esta_correcto(self, respuesta_usuario):
        opcion_correcta=self.opciones[self.indice_correcto]
        if respuesta_usuario==str(self.indice_correcto+1):
            self.ultima_respuesta=True
            return True
        if respuesta_usuario==opcion_correcta:
            self.ultima_respuesta=True
            return True
        self.ultima_respuesta=False
        return False
    def calcular_puntaje(self, tiempo):
        if self.ultima_respuesta:
            return 10
        return 0
class PreguntaVF(ElementoJuego):
    def __init__(self,texto,correcta):
        self.texto=texto
        self.correcta=correcta
        self.ultima_respuesta= False
    def mostrar(self):
        print(f"Pregunta: {self.texto} (V/F)")
    def esta_correcto(self, respuesta):
        primera_letra= respuesta[0].upper()
        if primera_letra=="v":
            respuesta_usuario=True
        elif primera_letra=="F":
            respuesta_usuario=False
        else:
            self.ultima_respuesta= False
            return False
        self.ultima_respuesta=(respuesta_usuario==self.correcta)
        return self.ultima_respuesta
    def calcular_puntaje(self, tiempo):
        if self.ultima_respuesta:
            return 5
        return -2
def cargar_preguntas(archivo):
    preguntas=[]
    try:
        with open("C:\\Users\\ASUS\\Documents\\202623206\\202623206,poo\\preguntas.json", "r", encoding="utf-8") as archivo:
            datos=json.load(archivo)
    except FileNotFoundError:
        print("archivo no encontrando, creando lista de preguntas vacias.")
        return []
    except json.JSONDecodeError:
        print("error de formato, revisa el archivo JSON.")
        return []
    for item in datos:
        if item ["tipo"]=="multiple":
            pregunta=PreguntaMultiple(
                item ["texto"],
                item["opciones"],
                item["correcta"]
                
            )
            preguntas.append(pregunta)
        elif item["tipo"]=="vf":
            pregunta=PreguntaVF(
                item["texto"],
                item["correcta"]
                
            )
            preguntas.append(pregunta)
    return preguntas
import random
class Juego:
    jugador = None
    preguntas = []
    ranking = Ranking()
    while True:
        print("\n--- QUIZ GAME ---")
        print("1. Registrar jugador")
        print("2. Cargar preguntas (desde JSON)")
        print("3. Jugar ronda (3 preguntas aleatorias)")
        print("4. Ver ranking")
        print("5. Salir")
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Error: Debe ingresar un número.")
            continue
        # OPCION 1
        if opcion == 1:
            nombre = input("Ingrese el nombre del jugador: ")
            jugador = Jugador(nombre)
            print("Jugador registrado correctamente.")
        # OPCION 2
        elif opcion == 2:
            preguntas = cargar_preguntas("preguntas.json")
            print(f"Se cargaron {len(preguntas)} preguntas.")
        # OPCION 3
        elif opcion == 3:
            if jugador is None:
                print("Error: Primero debe registrar un jugador.")
                continue
            if len(preguntas) == 0:
                print("Error: Primero debe cargar preguntas.")
                continue
            puntaje_ronda = 0
            for pregunta in preguntas[:3]:
                pregunta.mostrar()
                respuesta = input("Respuesta: ")
                pregunta.esta_correcto(respuesta)
                puntaje = pregunta.calcular_puntaje(0)
                puntaje_ronda += puntaje
            jugador.puntaje += puntaje_ronda
            ranking.guardar(
                jugador.nombre,
                jugador.puntaje
            )
            print(f"Puntaje obtenido en la ronda: {puntaje_ronda}")
            print(f"Puntaje acumulado: {jugador.puntaje}")
        # OPCION 4
        elif opcion == 4:
            top5 = ranking.obtener_top5()
            print("\n--- RANKING ---")
            for nombre, puntaje in top5:
                print(f"{nombre}: {puntaje}")
        # OPCION 5
        elif opcion == 5:
            print("Gracias por jugar.")
            break
        else:
            print("Opción inválida.")
if __name__ == "__main__":
    juego = Juego()
