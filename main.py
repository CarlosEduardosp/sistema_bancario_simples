from classe_cliente import Cliente
from validacoes import *
import textwrap


def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato   
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def main():
    pessoa = Cliente()
    limite = int(0)

    while True:
        response = menu()

        if response == 'd':
            valor = float(input('Digite o Valor para deposito: '))
            response = validar_positivos(valor)
            if response:
                pessoa.depositar(valor)
            else:
                print('Valor não pode ser um numero negativo ou Zero')

        elif response == 'e':
            pessoa.extrato()

        elif response == 's':

            if limite < 3:
                valor = float(input('Digite o Valor para Saque: '))
                resp = valor_saque(valor)
                resp_saldo = verifica_saldo(pessoa.saldo, valor)
                if resp:
                    if resp_saldo:
                        pessoa.sacar(valor)
                        limite = limite_saque(limite)
                    else:
                        print(f'Saldo insuficiente.Saldo Atual: R$ {pessoa.saldo}')
                else:
                    print('Valor para saque não pode ultrapassar R$ 500,00.')

            else:
                print('Você atingiu seu limite de 3 saques diários.')

        elif response == 'q':
            print('Sistema Finalizado com Sucesso!!')
            break


main()
