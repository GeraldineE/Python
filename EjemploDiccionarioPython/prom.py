def promedio(diccionarioNotas):
  suma = 0
  for nom in diccionarioNotas:
     suma +=diccionarioNotas[nom]
  return suma / len(diccionarioNotas)

def ingresarDatos():
  dicnotas = {}
  while True:
    nombre = input("nombre: ")
    nota = float (input("nota: "))
    dicnotas[nombre] = nota
    terminar = input ("Termina?(S, N):")
    if terminar == "S":
        break
  return dicnotas


def main():
  data = ingresarDatos()
  if len(data)>0:
    prom = promedio(data)
    print('el promedio de nota es ', prom)

main()
