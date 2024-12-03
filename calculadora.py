def calculadora():
    expressao = input("Digite sua expressão: ").strip().split()  #ele ta perguntando a expresão e recortando ela pra se transforma em uma lita, para isso é só digitar algo assim = "5 + 5"

    op1 = None  #aqui ele ta definido os 2 operadores e a operação como vazio
    op2 = None
    operacao = None

    for exp in expressao: #ele ta percorrendo a lista e ta procurando se tem uma operação, se tiver, ele define a operação como a operação q esta na lista
        match exp:
            case "+" | "-" | "" | "/":
                operacao = exp # definindo a operação
            case _:
                if op1 == None: # caso o de cima não esteja sendo cumprida, ele vai verificar se o op1 esta vazio e vai botar o op1 como primeiro operando
                    op1 = float(exp)
                else:
                    op2 = float(exp) # a mesma coisa que o de cima so que comm o op2

    match operacao: #realiza a operação
        case "+":
            print(op1 + op2)
        case "-":
            print(op1 - op2)
        case "":
            print(op1 * op2)
        case "/":
            print(op1 / op2)

while True: #deixa em loop
    calculadora()