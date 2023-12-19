import os

restaurantes = [
    {'nome': 'BK', 'categoria': 'Fast Food', 'ativo': False},
    {'nome': 'MC', 'categoria': 'Fast Food', 'ativo': True},
    {'nome': 'KFC', 'categoria': 'Fast Food', 'ativo': True},
]

def exibir_nome_programa():

    print("""
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
  ─██████████████─██████████████─██████████████───██████████████─████████████████──────██████████████─████████──████████─██████████████─████████████████───██████████████─██████████████─██████████████─
  ─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░░░██──────██░░░░░░░░░░██─██░░░░██──██░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
  ─██░░██████████─██░░██████░░██─██░░██████░░██───██░░██████░░██─██░░████████░░██──────██░░██████████─████░░██──██░░████─██░░██████░░██─██░░████████░░██───██░░██████████─██░░██████████─██░░██████████─
  ─██░░██─────────██░░██──██░░██─██░░██──██░░██───██░░██──██░░██─██░░██────██░░██──────██░░██───────────██░░░░██░░░░██───██░░██──██░░██─██░░██────██░░██───██░░██─────────██░░██─────────██░░██─────────
  ─██░░██████████─██░░██████░░██─██░░██████░░████─██░░██──██░░██─██░░████████░░██──────██░░██████████───████░░░░░░████───██░░██████░░██─██░░████████░░██───██░░██████████─██░░██████████─██░░██████████─
  ─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░░░██──────██░░░░░░░░░░██─────██░░░░░░██─────██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
  ─██████████░░██─██░░██████░░██─██░░████████░░██─██░░██──██░░██─██░░██████░░████──────██░░██████████───████░░░░░░████───██░░██████████─██░░██████░░████───██░░██████████─██████████░░██─██████████░░██─
  ─────────██░░██─██░░██──██░░██─██░░██────██░░██─██░░██──██░░██─██░░██──██░░██────────██░░██───────────██░░░░██░░░░██───██░░██─────────██░░██──██░░██─────██░░██─────────────────██░░██─────────██░░██─
  ─██████████░░██─██░░██──██░░██─██░░████████░░██─██░░██████░░██─██░░██──██░░██████────██░░██████████─████░░██──██░░████─██░░██─────────██░░██──██░░██████─██░░██████████─██████████░░██─██████████░░██─
  ─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██░░░░░░██────██░░░░░░░░░░██─██░░░░██──██░░░░██─██░░██─────────██░░██──██░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
  ─██████████████─██████──██████─████████████████─██████████████─██████──██████████────██████████████─████████──████████─██████─────────██████──██████████─██████████████─██████████████─██████████████─
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
          """)

def voltar_menu():
    input('\nDê ENTER para voltar ao menu principal ')
    main()

def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar/Desativar Restaurante')
    print('4. Sair\n')

def finalizar_app():
    os.system('cls')
    print('Aplicativo finalizado')

def cadastrar_restaurantes():
    os.system('cls')
    print("""

▒█▀▀█ ░█▀▀█ ▒█▀▀▄ ░█▀▀█ ▒█▀▀▀█ ▀▀█▀▀ ▒█▀▀█ ░█▀▀█ ▒█▀▀█ 　 ▒█▄░▒█ ▒█▀▀▀█ ▒█░░▒█ ▒█▀▀▀█ 　 ▒█▀▀█ ▒█▀▀▀ ▒█▀▀▀█ ▀▀█▀▀ ░█▀▀█ ▒█░▒█ ▒█▀▀█ ░█▀▀█ ▒█▄░▒█ ▀▀█▀▀ ▒█▀▀▀ 
▒█░░░ ▒█▄▄█ ▒█░▒█ ▒█▄▄█ ░▀▀▀▄▄ ░▒█░░ ▒█▄▄▀ ▒█▄▄█ ▒█▄▄▀ 　 ▒█▒█▒█ ▒█░░▒█ ░▒█▒█░ ▒█░░▒█ 　 ▒█▄▄▀ ▒█▀▀▀ ░▀▀▀▄▄ ░▒█░░ ▒█▄▄█ ▒█░▒█ ▒█▄▄▀ ▒█▄▄█ ▒█▒█▒█ ░▒█░░ ▒█▀▀▀ 
▒█▄▄█ ▒█░▒█ ▒█▄▄▀ ▒█░▒█ ▒█▄▄▄█ ░▒█░░ ▒█░▒█ ▒█░▒█ ▒█░▒█ 　 ▒█░░▀█ ▒█▄▄▄█ ░░▀▄▀░ ▒█▄▄▄█ 　 ▒█░▒█ ▒█▄▄▄ ▒█▄▄▄█ ░▒█░░ ▒█░▒█ ░▀▄▄▀ ▒█░▒█ ▒█░▒█ ▒█░░▀█ ░▒█░░ ▒█▄▄▄
    """)
    nome_restaurante = input("Insira o nome do restaurante que deseja cadastrar: ")
    categoria_restaurante = input(f'Insira a categoria do restaurante {nome_restaurante}: ')
    dados_restaurante = {'nome': nome_restaurante, 'categoria': categoria_restaurante, 'ativo': False}
    restaurantes.append(dados_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')
    voltar_menu()

def opcao_invalida():
    print('Opção inválida')
    voltar_menu()

def listar_restaurantes():
    os.system('cls')
    print('''
▒█▀▀█ ▒█▀▀▀ ▒█▀▀▀█ ▀▀█▀▀ ░█▀▀█ ▒█░▒█ ▒█▀▀█ ░█▀▀█ ▒█▄░▒█ ▀▀█▀▀ ▒█▀▀▀ ▒█▀▀▀█ 
▒█▄▄▀ ▒█▀▀▀ ░▀▀▀▄▄ ░▒█░░ ▒█▄▄█ ▒█░▒█ ▒█▄▄▀ ▒█▄▄█ ▒█▒█▒█ ░▒█░░ ▒█▀▀▀ ░▀▀▀▄▄ 
▒█░▒█ ▒█▄▄▄ ▒█▄▄▄█ ░▒█░░ ▒█░▒█ ░▀▄▄▀ ▒█░▒█ ▒█░▒█ ▒█░░▀█ ░▒█░░ ▒█▄▄▄ ▒█▄▄▄█
        \n''')
    titulo = f'{"Nome do Restaurante".ljust(23)} | {"Categoria".ljust(20)} | Status'
    print(titulo)
    print('─'*(len(titulo)+2))
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        status = 'Ativo' if restaurante['ativo'] else 'Inativo'

        print(f'-> {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {status}')

def alternar_status():
    os.system('cls')
    print('''
▒█▀▀▀█ ▀▀█▀▀ ░█▀▀█ ▀▀█▀▀ ▒█░▒█ ▒█▀▀▀█ 
░▀▀▀▄▄ ░▒█░░ ▒█▄▄█ ░▒█░░ ▒█░▒█ ░▀▀▀▄▄ 
▒█▄▄▄█ ░▒█░░ ▒█░▒█ ░▒█░░ ░▀▄▄▀ ▒█▄▄▄█''')
    listar_restaurantes()
    nome_restaurante = input('\nDigite o nome do restaurante que deseja alterar o status (Ativo|Inativo): ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'\nO restaurante {nome_restaurante} foi ativado com sucesso. ✅' if restaurante['ativo'] else f'\nO restaurante {nome_restaurante} foi desativado com sucesso. ✘'
            print(mensagem)

    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} não foi encontrado.')
    
    voltar_menu()

def escolher_opcao():
    opcao_escolhida = input('Escolha uma opção: ')
    match opcao_escolhida:
        case '1':
            cadastrar_restaurantes()
        case '2':
            listar_restaurantes()
            print()
            voltar_menu()
        case '3':
            alternar_status()
        case '4':
            finalizar_app()
        case _:
            opcao_invalida()


def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()