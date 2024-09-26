
alunos = {}
carga_horaria = 60

def edit_alunos():
    nome = input('Digite o nome do aluno que deseja editar as informações: ')
    if nome in alunos:
        print('Informe qual informação você deseja editar \n'
              '1 - Alterar nome do aluno \n 2 - Adicionar nota \n 3 - Alterar nota \n 4 - Alterar frequência \n 5 - Voltar para o menu')
        opc = int(input('Digite sua opção: '))
        if opc == 1:
            print('Você escolheu alterar o nome do aluno')
            novo_nome = input('Digite o novo nome do aluno: ')
            alunos[novo_nome] = alunos.pop(nome)
            print(f'Nome alterado para {novo_nome}')
        elif opc == 2:
            print('Você escolheu a opção para adicionar nota')
            nota = float(input('Digite a nota para adicionar: '))
            alunos[nome]['nota'].append(nota)
            alunos[nome]['media'] = calculo_media(alunos[nome]['nota'])
            print(f'Nota {nota} adicionada para {nome}, média: {alunos[nome]["media"]}')
        elif opc == 3:
            print('Você escolheu a opção para alterar nota')
            indice_nota = int(input(f'Qual nota deseja alterar (1 a {len(alunos[nome]["nota"])}): ')) - 1
            nova_nota = float(input('Digite a nova nota: '))
            alunos[nome]['nota'][indice_nota] = nova_nota
            print(f'Nota alterada para {nova_nota}.')
        elif opc == 4:
            nova_frequencia = int(input('Digite a nova frequência: '))
            alunos[nome]['frequencia'] = nova_frequencia
            print(f'Frequência alterada para {nova_frequencia}%.')
        elif opc == 5:
            print('Voltando para o menu...\n')

def nome_aluno():
    return input('Insira o nome do aluno: ')

def inicio():
    print('O sistema acadêmico foi iniciado, informe a seguir o nome, nota e frequência do aluno para continuarmos: \n')
    carga_horaria = 60
    while True:
        nome = nome_aluno()
        notas = []
        for c in range(4):
            nota = float(input(f'Insira a {c + 1}ª nota do aluno {nome}: '))
            notas.append(nota)
        print(f'As notas foram {notas}')
        frequencia = int(input(f'Insira a frequência do aluno {nome}: '))
        media = calculo_media(notas)
        alunos[nome] = {'nota': notas, 'frequencia': frequencia, 'media': media}
        print(f'Média do aluno {nome}: {media:.2f}')
        entrada = input('Você deseja inserir mais um aluno? [sim/nao]: ').strip().lower()
        if entrada == 'sim':
            continue
        elif entrada == 'nao':
            menu()
            break

def menu():
    while True:
        try:
            print('Selecione uma das opções abaixo para continuar: \n '
                  '1 - Adicionar alunos no sistema \n 2 - Editar informações dos alunos existentes \n 3 - Remover alunos do sistema \n 4 - Relatório geral da situação dos alunos '
                  '\n 5 - Relatório dos alunos por filtros (notas, faltas, frequência) \n 6 - Encerrar o programa')
            opc = int(input('Digite a opção: '))
            if opc == 1:
                print('Você selecionou a opção de adicionar alunos ao sistema')
                inicio()
            elif opc == 2:
                print('Você selecionou para editar as informações dos alunos existentes')
                edit_alunos()
            elif opc == 3:
                print('Você selecionou para remover alunos do sistema')
                remove()
            elif opc == 4:
                print('Você selecionou para ver o relatório geral dos alunos \n')
                relatorio_geral()
            elif opc == 5:
                print('\nVocê selecionou para verificar a relação dos alunos por filtros\n')
                filtro = input(' Se você deseja filtrar por alunos aprovados digite: "aprovado"; \n'
                               ' Se deseja filtrar para saber os alunos reprovados por falta digite: "falta"; \n'
                               ' Se deseja filtrar para saber os alunos reprovados por nota digite: "nota"; \n'
                               'Digite aqui: ').strip().lower()
                mostrar_filtros(filtro)
            elif opc == 6:
                print('O programa está se encerrando \n \n')
                break
        except ValueError:
            print('Entrada inválida')

def remove():
    nome = input('Digite o nome que deseja remover: ')
    if nome in alunos:
        del alunos[nome]
        print(alunos)
        print(f'{nome} foi removido do sistema')
    else:
        print('O nome não foi encontrado, digite novamente')
        remove()

def calculo_media(notas):
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

def calc_situacao_aluno(aluno):
    if aluno['frequencia'] < (carga_horaria * 0.75):
        return 'Reprovado por Falta'
    elif aluno['media'] < 7.0:
        return 'Reprovado por Nota'
    else:
        return 'Aprovado'

def relatorio_geral():
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    print("Relatório Geral dos Alunos:\n")
    for c, (nome, info) in enumerate(alunos.items(), 1):
        situacao = calc_situacao_aluno(info)
        print(f'{c}. {nome} - média: {info["media"]:.1f} / frequência: {info["frequencia"]} aulas - ({situacao})')

def mostrar_filtros(filtro):
    situacoes = {'aprovado': 'Aprovado', 'falta': 'Reprovado por Falta', 'nota': 'Reprovado por Nota'}

    if filtro not in situacoes:
        print("Situação inválida. Escolha: 'aprovado', 'falta' ou 'nota'.")
        return

    situacao_filtrada = situacoes[filtro]

    print(f"Relatório de alunos {situacao_filtrada}:\n")
    encontrou = False
    for c, (nome, info) in enumerate(alunos.items(), 1):
        situacao = calc_situacao_aluno(info)
        if situacao == situacao_filtrada:
            encontrou = True
            print(f'{c}. {nome} - média: {info["media"]:.1f} / frequência: {info["frequencia"]} aulas - ({situacao})')

    if not encontrou:
        print(f"Nenhum aluno encontrado com a situação: {situacao_filtrada}.")

print("Ricardo gostoso(?)")
inicio()
menu()
