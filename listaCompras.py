# Lista de Compras

import os
import time

lista = [] # Cria um lista vazia

while True:
    print('LISTA DE COMPRAS')
    print('[1] - Inserir\n[2] - Excluir\n[3] - Listar\n[0] - Sair') # Menu
    escolha = input('Escolha uma opção: ') # Vai receber a opção do menu que o usuário digitar
    numeros_validos = None # Variavel que vai verificar se foi digitado número no input

    if escolha == '1':
        os.system('cls') # Limpa a Tela
        print('INSERIR')
        lista.append(input('Digite o item que deseja inserir na lista: ')) # Vai inserir um item na lista
        os.system('cls') # Limpa a Tela
        continue # Voltará para o início do código
    elif escolha == '2':
        os.system('cls') # Limpa a Tela
        print('EXCLUIR')
        indice = input('Qual o índice que deseja excluir: ') # Vai excluir o item que está no índice informado
        try:
            indiceInt = int(indice) # Transformar a String em Int
            numeros_validos = True # Vai validar a variavel que verifica se foi digitado números
        except:
            numeros_validos = None # Ela ficará None caso não seja digitado um número

        if numeros_validos is None:
            print('Número digitado inválido!')
            time.sleep(2)
            os.system('cls') # Limpa a Tela
            continue # Voltará para o início do código
        
        try:
            del lista[indiceInt]
            os.system('cls') # Limpa a Tela
            continue # Voltará para o início do código
        except:
            print('Não foi possível deletar esse índice!')
            time.sleep(2) # Realiza uma pausa de 2seg
            os.system('cls') # Limpa a Tela
            continue # Voltará para o início do código
    elif escolha == '3':
        os.system('cls') # Limpa a Tela
        print('LISTA')
        for item in enumerate(lista):
            print(item) # Vai mostrar os itens da lista com seu respectivo índiceS
        time.sleep(5) # Realiza uma pausa de 5seg
        continue # Voltará para o início do código
    elif escolha == '0':
        print('SAIR')
        break # Encerra o código
    else:
        os.system('cls') # Limpa a Tela
        print('Opção Inválida!')
        time.sleep(2) # Realiza uma pausa de 2seg
        continue # Voltará para o início do código