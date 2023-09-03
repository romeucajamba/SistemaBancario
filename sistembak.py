menu = """

[d] Depositar
[e] Extrato
[s] Sacar
[q] Sair

"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITES_SAQUES = 3


while True:
   
    opcao =input(menu)
    
    if opcao == "d":
       
        valor = float(input("Informe o depósito:"))
        
        if valor > 0:
           
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou, valor inválido!")
            
    elif opcao == "s":
        
        saque = float(input("Informe o valor do saque:\n"))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques >= LIMITES_SAQUES
        
        if excedeu_saldo: 
        
            print("Operação falhou, você não tem saldo suficiente!")
        
        elif excedeu_limite:
            
            print("Operação falhou, o valor do saque excedeu o limite!")
        
        if excedeu_saque:

            print("Operação falhou, excedeu o número de saques")
        
        elif valor > 0:
            
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1

        else:
            
            print("Operação falhou, o valor é inválido!")
    
    elif opcao == "e":
        print("\n################Extrato###############")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("########################################")
    
    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a opção desejada!")
