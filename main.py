import crearcuenta,test,clase
from clase import Email
import csv
if __name__ == '__main__' :
    #test.tester()
    archivo = open('C:\\Users\\Marcos\\Desktop\\Poo\\Ej 1\\poo\\Ej1\\mails.csv')
    reader = csv.reader(archivo,delimiter=',')
    listaEmail= [] 
    crearcuenta.carga(listaEmail)
    Email.cmail(listaEmail)
    for i in range(len(listaEmail)):
        listaEmail[i].retornaEmail()
    for fila in reader:
        separador = fila[0].split("@")
        sepdominio = separador[1].split(".")
        idcuenta= separador[0]
        dominio=sepdominio[0]
        tipodominio=sepdominio[1]
        correo = Email(idcuenta,dominio,tipodominio,fila[1])
        listaEmail.append(correo)
    for i in range(len(listaEmail)):
        listaEmail[i].retornaEmail()
    Email.cambiar(listaEmail)
    for i in range(len(listaEmail)):
        listaEmail[i].retornaEmail()
    Email.MismoDominio(listaEmail)
    Email.mensaje(listaEmail)