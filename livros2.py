livros = [
        {"nome" : "amores,trens e outra coisas que saem dos trilhos", "páginas" : "304" , "preço" : "R$25,90" , "autor" : "jennifer e. smith" , "editora" : "galera"},
        {"nome" : "coisas obvias sobre o amor", "páginas" : "644" , "preço" : "R$66,88" , "autor" : "Elayne baeta" , "editora" : "galera"},
        {"nome" : "axíoma", "páginas" : "304" , "preço" : "R$45,87" , "autor" : "cora menetrelli" , "editora" : "planeta"},
        {"nome" : "vou te rceitar um gato", "páginas" : "224" , "preço" : "R$36,14" , "autor" : "ishida syou" , "editora" : "intrínseca"},
        {"nome" : "noiva", "páginas" : "368" , "preço" : "R$39,45" , "autor" : "ali hazelwood" , "editora" : "arqueiro"},
        {"nome" : "se você pudesse ver o sol", "páginas" : "328" , "preço" : "R$40,89" , "autor" : "ann liang" , "editora" : "alt"},
        {"nome" : "era uma vez no século xxi", "páginas" : "256" , "preço" : "R$53,12" , "autor" : "ara fidélis" , "editora" : "naci"},
        {"nome" : "melhor que nos filmes", "páginas" : "352" , "preço" : "R$39,45" , "autor" : "lynn painter" , "editora" : "intrínseca"},
        {"nome" : "não é como nos filmes", "páginas" : "416" , "preço" : "R$53,46" , "autor" : "lynn painter" , "editora" : "intríneca"},
        {"nome" : "fahrenheit 451", "páginas" : "216" , "preço" : "R$42,60" , "autor" : "ray brandbury" , "editora" : "biblioteca azul"}
        ]

def exibir_livro(livro):
    livro = livro.strip().lower()
    for nome in livros:
        if livro in nome["nome"]:
            print("aqui está:", nome["nome"])
            print("páginas: ", nome["páginas"])
            print("valor: ", nome["preço"])
            print("autor: ", nome["autor"])
            print("editora: ", nome["editora"]) 

def loop():
    while True:
        pergunta = input('quer ver outro livro? ')          
        if pergunta in ['sim', 'ss', 's']:
            p2 = input('qual livro? ').strip()
            exibir_livro(p2)
        elif pergunta in ['nao', 'não', 'n']:
            print('ta bom')
            break
        else:
            print('responda com sim ou não')

def main():
    p1 = input("qual livro quer olhar? ")
    exibir_livro(p1)
    loop()

main()