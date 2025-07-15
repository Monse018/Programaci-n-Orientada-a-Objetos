#Protege datos internos usando métodos públicos.
#Ejemplo Clase Cuenta Bancaria
class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial 

    def depositar(self, monto):
        self.__saldo += monto

    def get_saldo(self):
        return self.__saldo

# Uso
cuenta = CuentaBancaria(1500)
cuenta.depositar(900)
print(cuenta.get_saldo())  