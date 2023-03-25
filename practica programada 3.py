print ('Bienvenido a el Banco El Cinquito')
print ('\n')
def datosCuenta(numCuenta, cedula, saldo):
    print('Número de cuenta:', numCuenta)
    print('Identificación del cliente:', cedula)
    print('Saldo actual:', saldo)

def depositar(saldo, monto):
    return saldo + monto

def validarRetiro(saldo, monto):
    if saldo >= monto:
        return True
    else:
        return False

def retirar(saldo, monto):
    return saldo - monto

numCuenta = input('Ingrese el número de cuenta:')
cedula = input('Ingrese la identificación del cliente:')
saldoActual = float(input('Ingrese el saldo actual:'))

if numCuenta == '' or cedula == '':
    print('El número de cuenta e identificación son campos obligatorios.')
else:
    opcion = 0
    while opcion != 5:
        print('\n-- MENÚ --')
        print('1 para consultar información de la cuenta')
        print('2 para hacer depósito')
        print('3 para hacer retiro de dinero')
        print('4 para cambiar de cuenta')
        print('5 para salir')

        opcion = int(input('Seleccione una opción:'))

        if opcion == 1:
            datosCuenta(numCuenta, cedula, saldoActual)
        elif opcion == 2:
            montoDeposito = float(input('Ingrese el monto a depositar:'))
            saldoActual = depositar(saldoActual, montoDeposito)
            print('Depósito realizado con éxito. Su saldo actual:', saldoActual)
        elif opcion == 3:
            montoRetiro = float(input('Ingrese el monto a retirar:'))
            if validarRetiro(saldoActual, montoRetiro):
                saldoActual = retirar(saldoActual, montoRetiro)
                print('Retiro realizado con éxito. Su saldo actual es de:', saldoActual)
            else:
                print('Saldo insuficiente para realizar el retiro.')
        elif opcion == 4:
            numCuenta = input('Ingrese su número de cuenta:')
            cedula = input('Ingrese su identificación:')
            saldoActual = float(input('Ingrese el saldo actual:'))
        elif opcion == 5:
            print('Gracias por utilizar nuestros servicios.')
        else:
            print('Opción inválida.')
            print('Por favor seleccione una opción válida.')
