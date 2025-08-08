print("Sistema de Recomendação de Equipamentos de TI ")
print("Departamentos disponíveis:")
print("1 - Desenvolvimento de Software")
print("2 - Marketing")
print("3 - Recursos Humanos")
print("4 - Pesquisa e Desenvolvimento")

departamento = input("Digite o nome do departamento: ")

if departamento.lower() == "desenvolvimento de software":
    print("Recomendamos: Laptop de alto desempenho.")
elif departamento.lower() == "marketing":
    print("Recomendamos: Tablet para mobilidade e apresentações.")
elif departamento.lower() == "recursos humanos":
    print("Recomendamos: Computador desktop pela estabilidade e custo-benefício.")
elif departamento.lower() == "pesquisa e desenvolvimento":
    print("Recomendamos: Equipamento de última geração.")
else:
    print("Departamento não encontrado.")