def termo():
    termo=input("aceita os termos mesmo sem ter lido?")
    match termo:
        case "sim" | "s" | "aham" | "yes" | "aceito" | "ta joia" | "e apois" :
            print("pode entrar parcerokkk")
        case "nao" | "não" | "nao aceito" | "não aceito" | "no" | "n" :
            print("sai pra laa")
        case _ :
            print("ue")
termo()
