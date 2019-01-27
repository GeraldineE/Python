import datetime
import os

dicarriendo = {}
dicusuario = {}
dicpelis = {}

def menu():
    os.system('clear')
    print("-------------------------------")
    print("Seleccione la opcion que desee")
    print("-------------------------------")
    print("1.Registrar usuarios")
    print("2.Registrar peliculas")
    print("3.Busqueda Usuario/Pelicula")
    print("4.Eliminar Usuario/Pelicula")
    print("5.Arrendar Pelicula")
    print("6.Ver Arrendamientos")
    print("7.Administrar Peliculas")
    print("8. Listar Usuarios Registrados")
    print("9. Listar Películas Registradas")
    print("0. salir","\n")
    print("-------------------------------")

def submenu():

    print("-------------------------------")
    print("Seleccione una de las 3 opciones que desee")
    print("1.Busqueda de Usuario")
    print("2.Busqueda de Pelicula")
    print("3. Atras")
    print("--------------------------------")
    while True:
      opsubmenu=input("Ingrese una opcion")
      if(opsubmenu=="1"):
        print("")
        buscarUsuario()
      elif(opsubmenu=="2"):
        print ("")
        buscarPelicula()
      elif opsubmenu=="3":
        break
      else:
        print ("")
        input("No has pulsado ninguna opción correcta")
def submenuDos():

    print("-------------------------------")
    print("Seleccione una de las 3 opciones que desee")
    print("1.Eliminar Usuario")
    print("2.Eliminar Pelicula")
    print("3. Atras")
    print("--------------------------------")
    while True:
      opsubmenu=input("Ingrese una opcion")
      if(opsubmenu=="1"):
        print("")
        eliminarUsuario()
      elif(opsubmenu=="2"):
        print ("")
        eliminarPelicula()
      elif opsubmenu=="3":
        break
      else:
        print ("")
        input("No has pulsado ninguna opción correcta")

def arrendarPelicula():
    print("Arrendar Película","\n")
    if len(dicpelis) == 0:
       print("no hay películas registradas")
       return
    if len(dicusuario) == 0:
       print("no hay usuarios registrados")
       return
    codpel= input("código película: ")
    if codpel in dicpelis:
      nombrepel= dicpelis[codpel][1]
      if codpel in dicarriendo:
         print("La película",nombrepel,"ya se encuentra arrendada" , "\n")
         return
      print("La película",nombrepel, "esta disponible","\n")
      iduser= input("Ingrese id usuario: ")
      if iduser in dicusuario:
          now = datetime.datetime.now()
          dicarriendo[codpel] = [iduser, now ]
          print("La película",nombrepel, "fue arrendada con exito!. ")
          print("\n")
      else:
          print("Usuario no existe","\n")
    else:
        print("Película no existe","\n")

def listarArriendos():
    os.system('clear')
    print("++++++++++++++++++++")
    print("Listado de arriendos: ","\n")
    for codpel in dicarriendo:
      nombrepel= dicpelis[codpel][1]
      coduser = dicarriendo[codpel][0]
      nombreusr= dicusuario[coduser][1]
      fecha = dicpelis[codpel][1]
      print(nombrepel, ">>", coduser+"-"+nombreusr, ":", str(fecha))
    print("------------------")

def registrarUsuario():
    print("+++++++++++++++++++")
    print("Registro de usuario","\n")
    while True:
       ident= input("Ingrese id: ")
       name= input("Ingrese nombre: ")
       lastname= input("Ingrese apellido: ")
       dicusuario[ident]=[ident,name,lastname]
       terminar = input ("Termina? (S, N) :")
       if terminar == "S" :
          break

def registrarPelicula():
    print("+++++++++++++++++++++")
    print("Registro de peliculas","\n")
    while True:
      code= input("Ingrese el codigo de la pelicula: ")
      title= input("Ingrese el titulo de la pelicula: ")
      dicpelis[code]=[code,title]
      terminar = input ("Termina? (S, N) :")
      if terminar == "S" :
          break

def modificarPelicula():
    print("Modificar Película","\n")
    if len(dicpelis) == 0:
       print("no hay películas registradas")
       return
    codpel= input("código película: ")
    if codpel in dicpelis:
      if codpel in dicarriendo:
         print("Película arrendada. No puede ser modificada","\n")
         return
      else:
        cod = dicpelis[codpel][0]
        tit = dicpelis[codpel][1]
        print ("Código =", cod, "\n")
        print ("Título =", tit, "\n")
        codenew= input("Ingrese el codigo de la pelicula: ")
        titlenew= input("Ingrese el título de la pelicula: ")
        dicpelis[codenew]=[codenew,titlenew]
        if cod != codenew:
           #borrar vieja entrada dic si código si cambío
           del dicpelis[cod]
    else:
        print("Película no existe","\n")


def listarUsuario():
    os.system('clear')
    print("+++++++++++++++++++")
    print("Listado de usuarios: ","\n")
    for id in dicusuario:
      print(dicusuario[id][0], ":", dicusuario[id][1], " , ", dicusuario[id][2])
    print("------------------")

def listarPelicula():
    os.system('clear')
    print("++++++++++++++++++++")
    print("Listado de peliculas: ","\n")
    for cod in dicpelis:
      print(dicpelis[cod][0], ":", dicpelis[cod][1])
    print("------------------")

def buscarUsuario():
    print("Búsqueda de usuario")
    busqueda = input("Ingrese el nombre o apellido a buscar: ")
    for codusr in dicusuario:
        nom = dicusuario[codusr][1]
        ape = dicusuario[codusr][2]
        if  nom == busqueda or ape == busqueda:
            print("------------------")
            print("Su dato ha sido encontrado con exito!")
            print("--> ",nom, ":", ape)
            print("------------------")

def buscarPelicula():
    print("Búsqueda de Pelicula")
    busquedapeli = input("Ingrese el titulo de la pelicula a buscar: ")
    for codpeli in dicpelis:
        cod = dicpelis[codpeli][0]
        tit = dicpelis[codpeli][1]
        if(cod == busquedapeli or tit == busquedapeli):
            print("------------------")
            print("Su dato ha sido encontrado con exito!")
            print("--> ",cod, ":", tit)
            print("------------------")
def eliminarPelicula():
    print("Eliminar Película","\n")
    if len(dicpelis) == 0:
       print("no hay películas registrados")
       return
    codpel= input("ingrese el codigo de la película: ")
    #IMPORTANTE: validar que la película no tenga un arriendo
    if codpel in dicarriendo:
        print("PRECAUCIÓN!!!!: La película está arrendada. ")
        print("No se puede eliminar. ")
        print("===================")
        return
def eliminarUsuario():
    print("Eliminar Usuario","\n")
    if len(dicusuario) == 0:
       print("no hay usuarios registrados")
       return
    iduser= input("Ingrese el id usuario: ")
    #IMPORTANTE: validar que e usuario no tenga una película arrendana
    for codpel in dicarriendo:
      coduser = dicarriendo[codpel][0]
      if coduser == iduser:
        print("PRECAUCIÓN!!!!: Usuario tiene arriendos. ")
        print("No se puede eliminar. ")
        print("===================")
        return

    if iduser in dicusuario:
        del dicusuario[iduser]
        print("Usuario eliminado. ")



def salir():
  dicarriendo.clear()
  dicusuario.clear()
  dicpelis.clear()

while True:
    menu()
    opmenu=input("Ingrese una opcion")

    if opmenu=="1":
        print ("")
        registrarUsuario()

    elif opmenu=="2":
        print ("")
        registrarPelicula()
    elif opmenu=="3":
        print ("")
        submenu()
        listarPelicula()
    elif opmenu=="4":
        print ("")
        submenuDos()

    elif opmenu=="5":
        print("")
        arrendarPelicula()
    elif opmenu=="6":
        print ("")
        listarArriendos()
    elif opmenu=="7":
        print ("")
        modificarPelicula()
    elif opmenu=="8":
        print ("")
        listarUsuario()
    elif opmenu=="9":
        print ("")
        listarPelicula()
    elif opmenu=="0":
        salir()

        break
    else:
        print ("")
        input("No has pulsado ninguna opción correcta")
