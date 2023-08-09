from classe_conta import Conta
from classe_cliente import Cliente
from validacoes import *
import textwrap


clientes = []


def menu_cliente():
    menucliente = """
    ================ Menu Inicial ==========
    
    [l]\tLogin
    [c]\tCadastrar Cliente
    [s]\tsair    
    => """
    return input(textwrap.dedent(menucliente))


def menu():
    menu = """\n
    ================ Conta ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato   
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def main():

    while True:
        resposta = menu_cliente()

        if resposta == 'l':
            nome = input('Digite seu nome: ')

            x = 1
            while x == 1:
                senha = input('Digite sua senha: ')
                for i in clientes:
                    if senha == i['cliente'].senha:
                        print(f'Seja Bem vindo, {nome.title()}')
                        menu_conta(i['conta'].conta)
                        x = 2

        elif resposta == 'c':

            nome_cliente = input('Digite o seu nome: ')
            senha_cliente = input('Digite uma senha: ')

            pessoa = Conta(len(clientes) + 1)

            conta = pessoa.conta + 1
            cliente = Cliente(nome=nome_cliente, senha=senha_cliente, conta=conta)
            clientes.append({"cliente": cliente, "conta": pessoa})

            print(f'{nome_cliente.title()}, Sua agencia é {pessoa.agencia} e esse é o numero de sua conta: {pessoa.conta}')

        elif resposta == 's':

            break


def menu_conta(conta):

    for i in clientes:
        if conta == i['conta'].conta:
            pessoa = i


main()
for i in clientes:
    print(i['cliente'].nome, i['conta'].conta)
