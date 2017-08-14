################## JOGO DO NIM ############################
def computador_escolhe_jogada(n,m):

    y = m
    if n<=m:
        return n
    else:
        while ((n-y)%(m+1)) != 0:
            y = y-1
    if y == 0:
        return m
    else:
        return y 

###########################################################
def usuario_escolhe_jogada(n,m):

    x = int(input("Quantas peças você vai tirar?"))
    while x>m or x == 0:
        print ("Oops! Jogada inválida! Tente de novo.")
        x = int(input("Quantas peças você vai tirar?"))
    return x
            
###########################################################    
def partida():
    pc = 0
    vc = 0
    pc_turn = True
    
    n = int(input("Quantas peças?"))
    
    while n<=1:
        print("Número de peças deve ser maior que 1!")
        n = int(input("Quantas peças?"))
        
    m = int(input("Limite de peças por jogada?\n"))

    while n<m:
        print("Limite de peças deve ser menor que o número de peças total!")
        m = int(input("Limite de peças por jogada? "))

    if n%(m+1) == 0:        
        print("Você começa!\n")
        pc_turn = False
        jogada = usuario_escolhe_jogada(n,m)
        print ("Você tirou",jogada, "peça(s).")
        n = n - jogada
        print ("Agora resta(m) apenas",n, "peça(s) no tabuleiro.\n")

    else:
        print("Computador começa!")
        pc_turn = True
        jogada = computador_escolhe_jogada(n,m)
        print ("O computador tirou",jogada, "peça(s).")
        n = n - jogada
        if n == 0:
            print("Fim do jogo! O computador ganhou!\n")
        else:
            print ("Agora resta(m) apenas",n, "peça(s) no tabuleiro.\n")

    while n>0:
        if pc_turn == False:
            jogada = computador_escolhe_jogada(n,m)
            print ("O computador tirou",jogada, "peça(s).")
            n = n - jogada
            if n == 0:
                print("Fim do jogo! O computador ganhou!\n")
            else:
                print ("Agora resta(m) apenas",n, "peça(s) no tabuleiro.\n")
            pc_turn = True

        else:
            jogada = usuario_escolhe_jogada(n,m)
            print ("Você tirou",jogada, "peça(s).")
            n = n- jogada
            if n == 0:
                print("Fim do jogo! Você ganhou!\n")
            else:
                print ("Agora resta(m) apenas",n, "peça(s) no tabuleiro.\n")
            pc_turn = False

    if pc_turn == True:
        return 1      




###########################################################
def campeonato():
    pc = 0
    user = 0
    rnd = 1

    while user <3 and pc <3:
        print ("**** Rodada" ,rnd, "****")
        placar = partida()
        rnd = rnd + 1
        if placar == 1:
            pc = pc + 1
            
        else:
            user = user + 1

    print ("**** Final do campeonato! ****")
    print ("Placar: Você",user, "X", pc, "Computador")

###########################################################       

print( "Bem-vindo ao jogo do NIM! Escolha:")
print( "1 - para jogar uma partida isolada")
print( "2 - para jogar um campeonato")
escolha = int(input())

if escolha == 1:
    print ("Voce escolheu uma partida isolada!\n")
    partida()
else:
    print ("Voce escolheu um campeonato!\n")
    campeonato()


