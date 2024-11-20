# Ada-Lovelace

def resumo():
    mensagem = "Ada Lovelace, a matemática e escritora inglesa que previu a inteligência artificial e criou o primeiro algoritmo de computador."
    return mensagem


def doutorado():
    mensagem = "Não tem."
    return mensagem


def contribuicoes():
    mensagem = "Ada desenvolveu o primeiro algoritmo projetado para uma máquina, e colaborou na análise da máquina Analítica."
    return mensagem


def artigos():
    mensagem = "Sem artigos de autoria própria."
    return mensagem


def citacoes():
    mensagem = "A ciência matemática mostra o que é. É a linguagem das relações invisíveis entre as coisas.\n\n A imaginação é a faculdade descobridora, por excelência. É o que penetra nos mundos invisíveis ao nosso redor, os mundos da ciência.\n\n O cérebro é algo mais do que meramente mortal; como o tempo mostrará."
    return mensagem


def sair():
    mensagem = "\nObrigado pela leitura!"
    return mensagem


def erro():
    mensagem = "\nOpção inválida!"
    return mensagem


print("\nBoa noite! Você está aprendendo sobre Ada Lovelace.")

continuar = True
while continuar == True:

    opcao = int(
        input(
            "\nDigite o número correspondente ao menu que você deseja acessar: \n\n" +
            
            "1 - Resumo\n" +
            "2 - Doutorado\n" +
            "3 - Contribuições\n" +
            "4 - Principais Artigos\n" +
            "5 - Citações\n" +
            "6 - Sair\n\n"
        )
    )

    if opcao == 1:
        print("1 - Resumo")
        mensagem = resumo()

    elif opcao == 2:
        print("2 - Doutorado")
        mensagem = doutorado()

    elif opcao == 3:
        print("3 - Contribuições")
        mensagem = contribuicoes()

    elif opcao == 4:
        print("4 - Principais Artigos")
        mensagem = artigos()

    elif opcao == 5:
        print("5 - Citações")
        mensagem = citacoes()

    elif opcao == 6:
        mensagem = sair()
        continuar = False

    else:
        mensagem = erro()

    print(mensagem)
