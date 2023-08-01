
def validar_positivos(valor: float):
    """ função para validar se o valor é positivo. """

    if valor > 0:
        return True
    else:
        return False


def limite_saque(limite: int):
    """ controla a quantidade de saque diário """

    limite = limite + 1
    return limite


def valor_saque(valor: float):
    """ valida se o valor do saque está abaixo de 500,00 """

    if valor <= 500:
        return True
    else:
        return False


def verifica_saldo(saldo: float, valor: float):
    """ verifica se existe saldo em conta para realização do saque. """

    if valor <= saldo:
        return True
    else:
        return False
