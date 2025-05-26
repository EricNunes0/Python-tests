proceed = True
while proceed == True:
    act = None
    while act == None:
        try:
            act = int(input("1 - Adicionar linha\n2 - Ler linhas\n3 - Encerrar programa\n\nInforme sua próxima ação: "))
        except:
            act = None
    if act == 1:
        f = open("arquivo.txt", "w")
        i = int(input("Quantas linhas deseja inserir? "))
        for i in range(0, i):
            q = str(input(f"{i + 1}º linha: "))
            f.writelines(f"{q}\n")
        f.close()
    elif act == 2:
        re = open("arquivo.txt", "r")
        lines = len(re.readlines())
        r = open("arquivo.txt", "r")
        for i in range(0, lines):
            conteudo = r.readline()
            print(conteudo)
    elif act == 3:
        proceed = False
        print("⚫️ Programa finalizado!")
    else:
        print("❌ Ação inválida!")
