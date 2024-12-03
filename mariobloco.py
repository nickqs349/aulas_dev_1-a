def bloco() :
    quant = int(input("diga uma quantidade para formar um bloco:"))
    alt = quant
    while quant > 0: 
        print("°" * alt)
        quant -= 1 
bloco()