import clase,crearcuenta
import csv
def tester():
    archivo = open('correo.csv')
    reader = csv.reader(archivo,delimiter=',')
    listaEmail= [] 
    crearcuenta.carga(listaEmail)
    correo=input("Ingrese su email para convertirlo convertirlo:")
    clase.cmail(listaEmail,correo)
    for i in range(len(listaEmail)):
        listaEmail[i].retornaEmail()
    clase.cambiar(listaEmail)
    for i in range(len(listaEmail)):
        listaEmail[i].retornaEmail()
    clase.MismoDominio(listaEmail)
    clase.mensaje(listaEmail)