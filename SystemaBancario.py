
""" 
Desenvolvido por Daniel dos Santos Maia Reis

Texto Base:
Deve ser possiel depositar valores positivos para a conta bancaria
nao precisa especificar usuario
Todos os depositos devem ser armazenados em uma variavel e exibidos na operacao de extrato
O sistema deve permitir realizar 3 saques diarios com limite maximo de R$500, por saque
Caso o usuario nao tenha saldo na conta, o sistema deve exibir uma mensagem informando que nao é possivel sacar o dinheiro por falta de saldo
Todos os saques devem ser armazenados em uma variavel e exibidos na operacao de extraro:
    Esta operacao deve listar todos os depositos e saques realizados na conta, por fim deve ser exibido o salto atual da conta
    Os valores devem ser exibidos utilizando o formato: R$ xxx,xx




"""
menu = """

Escolha uma das opções abaixo:

[D] para Depositar
[S] para Sacar
[E] para Extrato
[Q] para Sair

"""
saldo = 0.00
strsaldo = ""
limite = 500.00
extrato = ""
numero_saque = 0
limite_saque = 3

def printe_saldo(strsaldo):
    
    strsaldo = str(f'R${saldo:_.2f}')
    strsaldo = strsaldo.replace('.',',').replace('_','.')
    return(strsaldo)

while True:
    opcao = input(menu)
    
    if opcao == "d":
        depositar = float(input("digite o valor a ser depositado: "))
        depositar = round(depositar,2)
        if depositar > 0:
            saldo += depositar            
            strsaldo = printe_saldo(strsaldo)
            strdepositar = str(f'R${depositar:_.2f}, ')
            strdepositar = strdepositar.replace('.',',').replace('_','.')

            extrato += " Deposito - "+ strdepositar
        else:
            print("valor invalido!")
        print(f'seu saldo atual é de: {strsaldo}')

    elif opcao == "s":
        sacar = float(input("digite o valor a ser sacado: "))
        if saldo >= sacar:
            if numero_saque < limite_saque:
                numero_saque += 1                
                if sacar <= limite: 
                    saldo -= sacar   
                    strsaldo = printe_saldo(strsaldo)                                    
                    strsaque = str(f'R${sacar:_.2f}')
                    strsaque = strsaque.replace('.',',').replace('_','.')
                    extrato += " Saque - " + strsaque
                    print("Saque permitido, aguarde a contagem das celulas")
                    
            else:
                print("limite de saque diario ja atingido")
        else:
            print("Saldo insuficiente")

    elif opcao == "e":
        print("Este é seu extrato bancario:")
        print(extrato)
        print(f'seu saldo atual é de: {strsaldo}')
        
    elif opcao == "q":
        break

    else:
        print("Opção invalida, selecione uma opção válida!")

