#########################
#
# Nome: Arlenson Lorran
#
# Data: 24/09/2024
#
#########################

# IMPORTAR BIBLIOTECAS

import time as t

# FUNÇÕES

def adicionar_funcionarios(funcionarios):
    nomes = input('Digite o nome do funcionário: ')
    idades = int(input('Digite a idade do funcionário: '))
    cargos = input('Digite o cargo do funcionário: ').lower()
    funcionarios.append({'nome': nomes, 'idade': idades, 'cargo': cargos})
    print('Funcionario adicionado com sucesso!')

def listar_funcionarios(funcionarios):
    for fun in funcionarios:
         print(f"{fun['nome']}: {fun['idade']} anos. Cargo: {fun['cargo']}")

def buscar_por_cargo(funcionarios, cargo_busca):
    funcionarios_encontrados =[]
    cargo_busca = input('Digite o cargo que deseja buscar: ').lower()
    for f in funcionarios:
        if f['cargo'] == cargo_busca:
            funcionarios_encontrados.append(f)
        if not funcionarios_encontrados:
            print(f'Não há funcionarios com o cargo {cargo_busca}.')
        else:
            print(f'Funcionarios com o cargo {cargo_busca:}')
            for f in funcionarios_encontrados:
                print(f"Nome: {f['nome']} - Idade: {f['idade']}.")
    return funcionarios_encontrados

# OPERANDOS

nomes = ''
idades = 0
cargos = ''
funcionarios = []
cargo_busca = ''

# ENTRADA

while True:
    print('======= SISTEMA DE CADASTRO DE FUNCIONÁRIOS =======\n')
    print('Escolha uma opção:')
    print('1 - Cadrastar funcionario.')
    print('2 - Listar funcionarios.')
    print('3 - Buscar funcionarios por cargo.')
    print('4 - Sair.\n')
    opcao = input('Opção: ')

# PROCESSAMENTO

    if opcao == '1':
        adicionar_funcionarios(funcionarios)
    elif opcao == '2':
        listar_funcionarios(funcionarios)
    elif opcao == '3':
        buscar_por_cargo(funcionarios, cargo_busca)
    elif opcao == '4':
        break
    else:
        print('Digite uma opção valida!')
        


# SAIDA

print('Fim do programa!')
