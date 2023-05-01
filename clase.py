class Email:
    __idCuenta=''
    __Dominio=''
    __tipodominio= ''
    __contraseña= ''
    def __init__(self,idCuenta,Dominio,tipodominio,contraseña):
        self.__idCuenta = idCuenta
        self.__Dominio = Dominio
        self.__tipodominio = tipodominio
        self.__contraseña= contraseña
    def retornaEmail(self):
        print('idCuenta: {},dominio: {}, tipodominio: {},contraseña: {} Resultado devuelto por Retornaemail: {}@{}.{}'.format(self.__idCuenta,self.__Dominio,self.__tipodominio,self.__contraseña,self.__idCuenta,self.__Dominio,self.__tipodominio))
    def getDominio(self):
        return 'El dominio es: '.format(self.__Dominio)
    def CrearCuenta(self):
        print('Ingrese un email para crear la cuenta')
    def cambiarcontra(self,contraseñanueva):
        self.__contraseña = contraseñanueva
    def verif(self, contraseñanueva):
        if self.__contraseña == contraseñanueva:
            return True
    def Mensaje():
        print('Ingrese nombre y email para enviar un mensaje:')
        nombre = input ('Ingrese nombre:')
        email = input ('Ingrese email:')
        print('Estimado {} te enviaremos tus mensajes a la dirección {}.'.format(nombre,email))
        return 
    def cmail(listaemail):
        mail = input("Ingrese su email para convertirlo")
        separador = mail.split("@")
        sepdominio = mail.split(".")
        idcuenta= separador[0]
        dominio=sepdominio[0]
        tipodominio=sepdominio[1]
        contraseña = input("Ingrese su contraseña:")
        correo = Email(idcuenta,dominio,tipodominio,contraseña)
        listaemail.append(correo)
        return 
    def cambiar(listaemail):
        print("Escriba la contraseña para buscar:")
        contra = input("Contraseña:")
        for i in range(len(listaemail)):
            if listaemail[i].verif(contra) == True:
                print("Ingrese una nueva contraseña:")
                contranueva = input("Contraseña nueva:")
                listaemail[i].cambiarcontra(contranueva)
    def VerifDom(self,dominio):
        if self.__Dominio == dominio:
            return True
    def MismoDominio(lista):
        c=0
        dom = input("Ingrese dominio para buscar: ")
        for i in range(len(lista)):
            if lista[i].verif(lista.dom) == True:
                c=c+1
        return "La cantidad dominios iguales a {} es {}".format(dom,c)