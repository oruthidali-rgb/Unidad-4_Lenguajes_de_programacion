#
# Clase (molde)
class Pregunta:
    def __init__(self, texto, respuesta_correcta):
        self.texto = texto
        self.respuesta_correcta = respuesta_correcta
    def verificar(self, respuesta_usuario):
        return respuesta_usuario.strip().lower() == self.respuesta_correcta.strip().lower()
    
pregunta = Pregunta("¿Cuál es la capital de Francia?", "Paris")
print(pregunta.texto)
respuesta_usuario = input("Dame tu respuesta: ")
if pregunta.verificar(respuesta_usuario):
    print("Correcto")
else:
    print("Incorrecto")