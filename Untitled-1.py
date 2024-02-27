def perguntas():
    print("Perguntas")
    while True:
        try:
            gay = (input("Você é gay?: "))
            if gay.lower() == 'sim':
                print("gay")
            elif gay.lower() == 'nao':
                print("hetero")
            else:
                print("digite valores validos")
                continue
        except ValueError:
            print("Por favor, digite números válidos.")
        while True:            
            try:
                viado = (input("Você é viado?: "))
                if viado.lower() == 'sim':
                    print("viado")
                elif viado.lower() == 'nao':
                    print("hetero")
                else:
                    print("digite valores validos")
                    continue
            except ValueError:
                print("Por favor, digite valores válidos para a segunda pergunta.")
            while True:
                try:
                    hetero =(input("Você é hetero?: "))
                    if hetero.lower() == 'sim':
                        print("hetero")
                    elif hetero.lower() == 'nao':
                        print("viadogay")
                    else:
                        print("digite valores validos")
                        continue
                    break
                except ValueError:
                    print("Por favor, digite valores válidos para a segunda pergunta.")
    
            break
        break
perguntas()
