
def leer():
    nom={}


    while True:
        nombre=input("Ingrese su nombre:")
        cedula=int(input("Ingrese su cedula:"))
        continuar=int(input("desea continuar? Si:1, No:0"))
        nom.update({nombre:cedula})
        if(continuar==0):
            break
        
    return nom


def main():
    nomb=leer()
    print(nomb)

main()
    
