import textwrap

def menu():
    menu = """

    ============Menu=========
    [d]\tDepositar
    [s]\tSacar
    [e]\t Extrato
    [nc]\tNova Conta
    [lc]\tListar contas
    [nu]\t Novo usuário
    [q]\t Sair
    
 ====> """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato,/):
    if valor > 0:
        saldo += valor
        extrato += f"Desposito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! o valor informado é inválido! @@@")
        
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques
    
    if excedeu_saldo:
        print("@@@ Operação falhou, saldo insuficiente!@@@")

    elif excedeu_limite:
        print("@@@ O peração valhou,  o valor do saque excedeu o limite! @@@")
    
    elif excedeu_saques:
        print("@@@@ Operação falhou, numero de saques excedeu o limite! @@@")

    elif valor  > 0:
         saldo -= valor
         extrato += f"Saque:\t\tR$ {valor:.2f}\n"
         numero_saques += 1
         print("===  Saque realizado com sucesso  ===")

    else:
        print("\n@@@@ Operação falhou, o valor informado é inválido! @@@")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):

    print("\n=============== Extrato ==============")
    print("Não foram realizada movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    cpf = input("Informa o cpf: (Somente numero!): ")
    usuario = filtrar_usuario( cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse cpf! @@@")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aa): ")
    endereco = input("Informe o endereço (logradouro, numero - bairro - cidade/estado sigla): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereço": endereco})

    print("===== Usuário criado com sucesso ====")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuario):
    cpf = input("Infrome o cpf do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("=== Conta criada com sucesso ===")

        return {"agência": agencia, "numero_da_conta": numero_conta, "usuario": usuario}
    print("\n@@@  Usuário não encontrado, fluxo de de criação de conta encerrado! @@@")


def listar_conta(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
    """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITES_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuario = []
    contas = []


    while True:

        opc = menu()

        if opc == "d":
            valor = float(input("Informa o valor de depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opc == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo= saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITES_SAQUES,
            )
        
        elif opc == "e":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opc == "nu":
            criar_usuario(usuarios)
        
        elif opc == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta: 
                contas.append(conta)
        
        elif opc == "lc":
            listar_conta(contas)
        
        elif opc == "q":
            break
        
        else:
            print("Operação inválida, por favor, selecione novamente a opção desejada!")
        
    
main()