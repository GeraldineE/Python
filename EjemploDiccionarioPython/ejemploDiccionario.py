nom={}
print(nom)
for i in range(5):
    nombre=input("Ingrese su nombre:")
    cedula=int(input("Ingrese su cedula:"))
    nom.update({nombre:cedula})
print(nom)

