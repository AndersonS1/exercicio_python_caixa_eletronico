print("Bem Vindo ao Banco")
print('='* 20)
print('Digite a operação desejada')
menu = """"

[0] Depositar Dinheiro
[1] Sacar Dinheiro
[2] Extrato da Conta
[3] Sair

=> """

saldo = 0
limite = 1000
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 4

while True:
    escolha = input(menu)

    if escolha == "0":
        valor = float(input("Informe o valor do depósito que será realizado: "))


        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
            print(f"\nsaldo atual: R$ {saldo:.2f}")
        else:
            print("Operação falhou ! O valor informado é invalido.")


    
    elif escolha == "1":

      valor = float(input("Informe o valor do saque: "))
      excedeu_saldo = valor > saldo

      excedeu_limite = valor > limite

      excedeu_saques = numero_saques >= LIMITE_SAQUES

      if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

      elif excedeu_limite:
        print("Operação falhou! O valor do saque excedeu o limite.")

      elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
      
      elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R${valor:.2f}\n"
        numero_saques +=1
        print(f"\nsaldo atual: R$ {saldo:.2f}")
      else:
        print("Operação falhou! O valor informado é invalido.")
      
    elif escolha == "2":
        print('='* 5)
        print("\nEXTRATO=")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"\nsaldo: R$ {saldo:.2f}")
        print("==========================")

    elif escolha == "3":
        print("Volte Sempre ! ")
        break


    else:
       print("Operação inválida, por favor selecione novamente a operação desejada.")