#contadores
excelente = 0
ruim = 0

TOTAL_ENTREVISTADOS = 50

for i in range(TOTAL_ENTREVISTADOS):
    print(f"\nEntrevistado {i + 1}")
    
    #dados
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    
    #opções
    print("Opinião sobre o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")
    opiniao = int(input("Digite sua opção (1, 2 ou 3): "))
    
    # Estrutura de decisão para contabilizar
    if opiniao == 1:
        excelente += 1
    elif opiniao == 3:
        ruim += 1
    elif opiniao == 2:
        pass
    else:
        print("Opção inválida! Esta resposta não será contabilizada.")

#resultados finais
print("\n RESULTADO DA PESQUISA ")
print(f"Total de intrevistados: {TOTAL_ENTREVISTADOS}")
print(f"Total de respostas EXCELENTE: {excelente}")
print(f"Total de respostas RUIM: {ruim}")