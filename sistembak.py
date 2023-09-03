###############################################Depósito#####################################
numero_deposito = int(input("Quantas vezes vai depositar?\n"))
contagem = 0

while contagem < numero_deposito:

    deposito = int(input("Digite o valor a depositar:\n"))
    extrato = deposito
    if(extrato < 1):
        print("Não pode depoistar esse valor {}".format(extrato))
    
    else:
        print("Seu depósito é de {}".format(extrato))
        print("Depósito realizado com sucesso!")
        break

#####################################Saque##################################################
    
def sistema_bancario(saqueDiario):
    files_save = open("ExtratoBancario", "a")
    files_save.writelines(saqueDiario)
    files_save.close()


saque_diario = 3
limite_saque = 500

for c in saque_diario:
    saque = int(input("Faz o saque {}\n".format(c)))
    if((saque >= limite_saque) and (saque >= extrato)):
        print("A operação não pode ser realizada!")

    elif((saque <= limite_saque) and (saque >= extrato)):
        print("O Seu saldo não é suficiente!")

    elif((saque >= limite_saque) and (saque <= extrato)):
        print("Só pode fazer trê saques diários!!")

    else:
        sacou = extrato - saque
        print("sacou {} kz".format(sacou))
        print("Gaurdando registo....")
        sistema_bancario(sacou)