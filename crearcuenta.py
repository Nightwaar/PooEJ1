from clase import Email

def crear():
    print('Ingrese los siguientes datos:')
    idcuenta = input('Id de la cuenta:')
    dominio = input('Dominio:')
    tipodominio = input('Tipo del dominio:')
    contraseña = input('Contraseña:')
    email=Email(idcuenta,dominio,tipodominio,contraseña)
    return email
def carga(listaemail):
    for i in range(2):
        p = crear()
        print(p)
        listaemail.append(p)
    return