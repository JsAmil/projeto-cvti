from ast import Break
from time import sleep
import sys
import os
def clrscr():
    _ = os.system("cls")

print('''⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⢀⣤⣤⣤⣠⣤⣤⡀⠄⠄⢀⣤⣤⡤⣄⣤⣤⣤⣤⣴⣶⣶⡆⠄⠄⠄
⠄⠄⠄⣼⣿⡿⠿⠿⠿⠾⢿⣿⡆⢠⣿⣿⠯⠾⠿⢿⣿⡿⠿⢟⣛⣛⠃⠄⠄⠄
⠄⠄⢸⣿⣿⠄⠄⠄⠄⠄⠘⣿⣿⣼⣿⠇⠄⠄⠄⢸⣿⡇⠄⢸⣿⣿⠄⠄⠄⠄
⠄⠄⠄⢿⣿⣷⣤⣤⡄⠄⠄⢹⣿⣿⡿⠄⠄⠄⠄⢸⣿⡇⠄⢸⣿⣿⠄⠄⠄⠄
⠄⠄⠄⠄⠉⠛⠛⠛⠃⠄⠄⠈⠛⠛⠁⠄⠄⠄⠄⠘⠛⠃⠄⠘⠛⠛⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
''')


def intro():
    dte='''23 Março 1962.
Nova Iguaçu, RJ \n \n'''
    for char in dte:
        sleep(0.20)
        sys.stdout.write(char)
        sys.stdout.flush()

    dte1 = '''Em 1962, na cidade de Nova Iguaçu, viveu-se um episódio marcante que envolveu uma fazenda e um personagem chamado João, 
    um jovem ambicioso que sonhava em deixar a vida rural para trás e se aventurar na cidade grande.'''
    for char in dte1:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    sleep(2)
    print("\nJoão trabalhava na fazenda há anos, cuidando dos animais e das plantações, mas nunca se sentiu realizado com essa vida.")
    sleep(2)
    print("Ele sempre quis mais, queria uma vida de aventuras e luxos, algo que parecia impossível dentro dos limites da fazenda.....")
    sleep(2)
    sleep(2)
    print('''
Então
João decide sair da vida rural
Ele precisa de um plano
    ''')
    sleep(5)
intro()
clrscr()  

def tools():
    dte = '''Antes de começar, João decide pegar suas ferramentas \n \n'''
    for char in dte:
        sleep(0.20)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("1)Procure suas ferramentas: \n")
    while(1):    
        ans=input("Selecione sua escolha: ")
        if(ans=='1'):
            print("\n Onde procurar mais ferramentas?")
            print('''
1)Cozinha
2)Porão
3)Celeiro \n''')
            ans1=input("Selecione sua escolha:")
            while(1):
                if(ans1=='1'):
                    print("Viva... Você encontrou um alicate aqui \n")
                    
                    print('''Onde procurar mais ferramentas? 
2)Porão
3)Celeiro \n''')
                    ans2=input("Selecione sua escolha:")
                    if(ans2=='2'):
                        print(" Ao vasculhar o porão, você encontrou um machado escondido atrás de uma caixa \n ")
                        print('''Onde procurar mais ferramentas? 
                    
3)Celeiro\n''')
                    ans3=input("Selecione sua escolha:")
                    if(ans3=='3'):
                        print("Pronto... Você viu uma pá velha cheia de pó guardado no fundo do feno. Pode ter estado lá por meses. \n ")
                        break
                    elif(ans2=='3'):
                        print("Pronto... Você viu uma pá velha cheia de pó guardado no fundo do feno. Pode ter estado lá por meses. ")
                        print('''\n Onde procurar mais ferramentas?
2)Porão \n''')
                    ans3=input("Selecione sua escolha:")
                    if(ans3=='2'):
                        print(" Ao vasculhar o porão, você encontrou um machado escondido atrás de uma caixa \n ")
                    break
                    
                elif(ans1=='2'):
                    print(" Ao vasculhar o porão, você encontrou um machado escondido atrás de uma caixa ")
                    
                    print('''Onde procurar mais ferramentas?
1)Cozinha
3)Celeiro \n''')
                    ans2=input("Selecione sua escolha:")
                    if(ans2=='1'):
                        print("Viva... Você encontrou um alicate aqui \n")
                        print('''Onde procurar mais ferramentas?
3)Celeiro \n''')
                        ans3=input("Selecione sua escolha:")
                        if(ans3=='3'):
                            print("Pronto... Você viu uma pá velha cheia de pó guardado no fundo do feno. Pode ter estado lá por meses. ")        
                        break
                    elif(ans2=='3'):
                        print("Pronto... Você viu uma pá velha cheia de pó guardado no fundo do feno. Pode ter estado lá por meses.")
                        print('''Onde procurar mais ferramentas? 
2)Porão \n''')
                        ans3=input("Selecione sua escolha:")
                        if(ans3=='2'):
                            print("Ao vasculhar o porão, você encontrou um machado escondido atrás de uma caixa")    
                        break

                elif(ans1=='2'):
                    print("Pronto... Você viu uma pá velha cheia de pó guardado no fundo do feno. Pode ter estado lá por meses.")
                    
                    print('''Onde procurar mais ferramentas?
1)Cozinha
2)Porão \n''')
                    ans2=input("Selecione sua escolha:")
                    if(ans2=='1'):
                        print("Viva... Você encontrou um alicate aqui\n")
                        print('''Onde procuar mais ferramentas?
2)Porão \n''')
                        ans3=input("Selecione sua escolha:")
                        if(ans3=='2'):
                           print("Ao vasculhar o porão, você encontrou um machado escondido atrás de uma caixa")    
                        break
                    elif(ans2=='2'):
                        print("Ao vasculhar o porão, você encontrou um machado escondido atrás de uma caixa")    
                        print('''Onde procurar mais ferramentas?
1)Cozinha \n''')
                        ans3=input("Selecione sua escolha:")
                        if(ans3=='1'):
                            print("Viva... Você encontrou um alicate aqui\n")
                        break
            break
        else:
                    print("\n Digite a escolha correta")

def seebehind():
    dte = '''O que você irá fazer? \n \n'''
    for char in dte:
        sleep(0.20)
        sys.stdout.write(char)
        sys.stdout.flush()
    print('''
1) Lutar 
2) Ignorar
3) Explicar o plano\n''')
   
    while(1):
            ans= input("Digite sua escolha: ")
            if(ans == '1'):
                print('''\nVOCÊ MORRE. VOCÊ NÃO LUTA COM COMPANHEIROS (BROCODE) ''')
                print("TENTE NOVAMENTE")
            elif(ans == '2'):
                print('''Ele relata você ao CHEFE e você é pego. ''')
                print("TENTE NOVAMENTE")
            elif(ans == '3'):
                print('''Você pensa na idéia de que não pode fazer nada sozinho, então explica para ele e o mesmo parece interessado.''')
                print('''Mas ele quer incluir uma outra pessoa no plano ''')
                break
            else:
                print("Escolha correta")
    
    dte = '''O que você irá fazer? \n \n'''
    for char in dte:
        sleep(0.20)
        sys.stdout.write(char)
        sys.stdout.flush()
    print('''
1)Incluir a outra pessoa no plano
2)Recusar \n''')
    
    while(1):
            ans= input("Digite sua escolha: ")
            if(ans == '1'):
               print('''Agora que estão todos juntos, você começa a planejar como será sua vida fora do campo''') 
               break 
            elif(ans == '2'):
                print('''Você se recusa a incluir a outra pessoa, então os outros dois delataram você para os guardas e seguiram seu plano.''')
                print("TENTE NOVAMENTE")
            else:
                print("Digite a escolha correta:")
    
def plan1():
    dte = '''O que você irá fazer? \n \n'''
    for char in dte:
        sleep(0.20)
        sys.stdout.write(char)
        sys.stdout.flush()
    print('''
1) Pergunte aos outros moradores da fazenda
2) Pense no seu próprio plano
3) Explorar a Fazenda\n''')
    while(1):
            ans= input("Digite o número da sua escolha: ")
            if(ans == '1'):
                print('''\nOs outros moradores discordam, depois de ver o número de tentativas fracassadas, pois morar na cidade e ser bem sucedido é quase impossível.''')
                print("Tente novamente")
            elif(ans == '2'):
                print('''Você pensa em seu próprio plano de sair do campo.''')
                break
            elif(ans == '3'):
                print('''Você começa a explorar a fazenda em busca de algo que possa ajudá-lo a sair da vida difícil de ser um fazendeiro''')
                break
            else:
                print("Escolha correta.")
    
    sleep(4)
    clrscr()
    dte = '''o que você irá fazer?\n \n'''
    for char in dte:
        sleep(0.20)
        sys.stdout.write(char)
        sys.stdout.flush()
        
    print('''1) Sair da fazenda
2) Procure outro plano \n ''')
    while (1):
            ans1=input("Digite sua escolha :")
            if(ans1=='1'):
                print("\n Para sair da fazenda, você precisa das suas ferramentas.\n")
                tools()
                return
            elif(ans1=='2'):
                print("\n Você pensa em quebrar o cadeado do portão da frente, mas requer ferramentas.\n")
                tools()
                return
            else:
                print("Escolha correta \n")

def plan2():
    print("\n Ao sair da fazenda com todas as ferramentas que você tinha, alguém o interrompe. \n")
    dte = '''o que você irá fazer? \n \n'''
    for char in dte:
        sleep(0.20)
        sys.stdout.write(char)
        sys.stdout.flush()
    
    print('''\n 
    1) Correr
    2) Olhar para trás''')
    while(1):
            ans= input("Digite sua escolha:")
            if(ans == '1'):
                print('''\nVocê começou a correr e foi pego pelos donos. Todas as suas ferramentas se foram e agora você foi trancado dentro de sua instalação. Portanto FUGIR NÃO É UMA OPÇÃO.
                TENTE NOVAMENTE''')
            elif(ans == '2'):
                print('''Você verifica atrás e vê que há algum fazendeiro de quem você roubou o machado, ele parece familiar para você ''')
                seebehind()
                break
            else:
                print("Escolha correta \n")

def plan3():
    print('''Conforme você considera as alternativas, a saída na parte de trás da fazenda chama sua atenção.
Você começa a cortar as cercas da fazenda usando o machado descartado encontrado no terreno da porão,
alicate da cozinha e a pá improvisada achada no celeiro.''')
    print('''uh, mas estas cercas quebradas são visíveis e se o guarda vier para sua verificação de rotina, eles podem perceber e todos irão vir atrás da gente.''')
    
    dte = '''O que você irá fazer \n \n'''
    for char in dte:
        sleep(0.20)
        sys.stdout.write(char)
        sys.stdout.flush()
    print('''
    1) Remendar as cercas
    2) Deixar
    3) Subornar o guarda''')
    while(1):
        ans= input("Digite sua escolha:")
        if(ans == '1'):
            print('''\nVocê remendou as cercas com o que encontrou, como um silvertape ou um pedaço de madeira, etc.''')
            dte = '''Após as cercas estarem remendadas, o que você faz? \n \n'''
            for char in dte:
                sleep(0.20)
                sys.stdout.write(char)
                sys.stdout.flush()
            print("1)Ir embora \n")
            while(1):    
                ans=input("Digite sua escolha:")
                if(ans=='1'):
                    print('''Ao ir embora, você encontra um rio em seu caminho.''')
                    print('''Vocês três seguem até à margem do rio.
A fazenda é cercada pelas águas frias e agitadas do rio. Então você precisará de algo para chegar ao outro lado.
''')        
                    dte = '''O que você irá fazer?'''
                    for char in dte:
                        sleep(0.20)
                        sys.stdout.write(char)
                        sys.stdout.flush()
                    print('''\n 
            1) Construir uma mini passagem
            2) Tentar nadar''')
                    while(1):    
                        ans12= input("Digite sua escolha: ")
                        if(ans12 == '1'):
                            print('''Você constrói uma mini passagem com madeiras...''')
                            print('''Opa! Você se esqueceu completamente dos guardas! Eles podem notar sua ausência enquanto você está trabalhando em sua mini passagem.''')
                            dte = '''O que você irá fazer? \n \n'''
                            for char in dte:
                                sleep(0.20)
                                sys.stdout.write(char)
                                sys.stdout.flush()
                            print('''\n 1) Atravessar correndo
2) Subornar o guarda
3) Se esconder do guarda''')
                            while(1):
                                ans= input("Digite sua escolha: ")
                                if(ans == '1'):
                                    print('''Você consegue atravessar a mini passagem''')
                                    break
                                elif(ans == '2'):
                                    print('''\nVocê suborna o guarda com dinheiro e álcool que roubou e guardou para mais tarde. Mas ele ainda informa seus oficiais sobre você, e você é enviado de volta para a fazenda.
                TENTE NOVAMENTE''')
                                elif(ans == '3'):
                                    print('''Você se esconde mas o guarda o encontra.
                TENTE NOVAMENTE''')
                                else:
                                    print("Escolha correta \n")
                        
                            break
                        
                        elif(ans12=='2'):
                            print('''você pulou na água e tentou nadar até o outro lado, mas desistiu rapidamente, você se afogou no rio e seu corpo foi arrastado para o fundo pela forte correnteza do rio. ''')
                            print('''TENTE NOVAMENTE''')
                    
                        else:
                            print("Escolha correta \n")
                        
                    break

                else:
                    print("Digite a escolha correta \n")

            break

        elif(ans == '2'):
            print('''\n Os guardas descobrem que alguem passou por ali, acabam encontrando João e ele tem que retornar a fazenda.
                TENTE NOVAMENTE''')
            
        elif(ans == '3'):
            print('''\nVocê suborna o guarda com dinheiro e álcool que roubou e guardou para mais tarde. Mas ele ainda informa seus oficiais sobre você, e você é enviado de volta para a fazenda.
                TENTE NOVAMENTE''')

        else:
            print("Digite a escolha correta \n")

def plan4():
    clrscr()
    dte='''30 de Março 1962 '''
    for char in dte:
        sleep(0.20)
        sys.stdout.write(char)
        sys.stdout.flush()
    print(''' \n \n O plano deu certo\n''')
    print(''' Você conseguiu chegar ao centro de Nova Iguaçu. \n \n''')
    dte='''Após se erguer financeiramente, João decidiu entrar para política e se tornou um dos primeiros prefeitos da cidade de Nova Iguaçu !!! \n'''
    for char in dte:
        sleep(0.20)
        sys.stdout.write(char)
        sys.stdout.flush()
plan1()
plan2()
plan3()
plan4()
