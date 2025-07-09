# Definición de una función que saluda con un nombre
def saludar(nombre):
    mensaje = f"Hola, {nombre}"
    return mensaje

# Llamar a la función y mostrar el resultado
resultado = saludar("Carlos")
print(resultado)

def saludar(nombre="invitado"):
    return f"Hola, {nombre}"

print(saludar())
print(saludar("Bastián"))

def sumar(*numeros):
    return sum(numeros)

print(sumar(1, 2, 3))
print(sumar(10, 20, 30, 40))

def mostrar_info(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Ana", edad=30, ciudad="Santiago")

def saludar(nombre):
    print(f"Hola, {nombre}")

saludar("Elena")

def multiplicar(a, b):
    return a * b

resultado = multiplicar(3, 4)
print(resultado)

def procesar(accion, *args, **kwargs):
    print(f"Acción: {accion}")
    print("Argumentos:", args)
    print("Opciones:", kwargs)

procesar("guardar", 10, 20, 30, usuario="admin", modo="rápido")

from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola desde Django!")

from fastapi import FastAPI

app = FastAPI()

@app.get("/saludo")
def saludar(nombre: str = "Invitado"):
    return {"mensaje": f"Hola, {nombre}"}
