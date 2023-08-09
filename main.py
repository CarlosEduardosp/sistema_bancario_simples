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
                if senha == 's':
                    break

        elif resposta == 'c':

            nome_cliente = input('Digite o seu nome: ')
            data_nasc = input('Digite sua data de nascimento: ')
            cpf = input('Digite seu cpf: ')

            for j in clientes:
                while True:
                    if cpf == j['cliente'].cpf:
                        print('CPF já existe !!')
                        cpf = input('Digite seu cpf: ')
                    else:
                        break

            logradouro = input('Digite o logradouro: ')
            bairro = input('Digite seu bairro: ')
            cidade = input('Digite a cidade: ')
            estado = input('Digite o Estado: ')
            senha_cliente = input('Digite uma senha: ')

            endereco = 'Endereço: ' + logradouro + ' - ' + bairro + ' - ' + cidade + ' - ' + estado

            pessoa = Conta(len(clientes) + 1)

            conta = pessoa.conta + 1
            cliente = Cliente(nome=nome_cliente, senha=senha_cliente, conta=conta, data_nasc=data_nasc, cpf=cpf, endereco=endereco)
            clientes.append({"cliente": cliente, "conta": pessoa})

            print(f'{nome_cliente.title()}, Sua agencia é {pessoa.agencia} e esse é o numero de sua conta: {pessoa.conta}')
            print(endereco)

        elif resposta == 's':

            break


def menu_conta(conta):

    for i in clientes:
        if conta == i['conta'].conta:
            pessoa = i

    while True:
        response = menu()

        if response == 'd':
            valor = int(input('Digite o valor para deposito: '))
            pessoa['conta'].depositar(valor)

        elif response == 's':
            valor = int(input('Digite o valor para saque: '))
            pessoa['conta'].sacar(valor)

        elif response == 'e':
            pessoa['conta'].extrato()

        elif response == 'q':
            break


main()
