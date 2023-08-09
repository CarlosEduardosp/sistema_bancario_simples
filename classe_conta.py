class Conta:
    """ classe conta do cliente """

    saldo = float(0)
    __extrato = []
    agencia = '0001'

    def __init__(self, conta: int):
        self.conta = conta

    def depositar(self, valor: float):
        self.saldo = self.saldo + valor
        self.__extrato.append(f'Deposito no valor de {valor:.2f}')
        print(f"Você depositou R$: {valor:.2f}")

    def extrato(self):
        for i in self.__extrato:
            print(f"{i}")
        print(f'Saldo Atual: R$ {self.saldo:.2f}')

    def sacar(self, valor: float):
        self.saldo = self.saldo - valor
        self.__extrato.append(f'Saque no valor de {valor}')
        print(f"Você sacou R$: {valor:.2f}")

