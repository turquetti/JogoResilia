# FUNÇÕES PARA FORMATAÇÃO DO JOGO
def linhas():
    print("=" * 180)


def escolha_jogador():
    linhas()
    print('''
Você está pronto para jogar?

Escolha um jogador:

< 1 > Jacarezinho
< 2 > Zé Gotinha
< 3 > Mutantinho
    ''')
    linhas()
    resposta_usuario = int(input("DIGITE O NÚMERO DO SEU JOGADOR: "))
    linhas()

    if resposta_usuario == 1:
        jogador = 'JACAREZINHO'

        print('''
Você escolheu o 'JACAREZINHO'
        ▄▄▄▄▄ ▄ ▄ ▄ ▄
    ▄▄▄▄██▄████▀█▀█▀█▀██▄
    ▀▄▀▄▀▄████▄█▄█▄█▄█████
     ▀▀▀▀▀▀▀▀██▀▀▀▀██▀ ▄██
           ▀▀    ▀▀▄▄██▀ 
     ''')
    elif resposta_usuario == 2:
        jogador = 'ZE GOTINHA'
        print('''
Você escolheu o 'ZÉ GOTINHA'
               ▓▓
             ▓▓   ▓▓
           ▓         ▓
         ▓            ▓
        ▓   █     █    ▓
        ▓              ▓
        ▓   █      █   ▓
          ▓  ▀▀▀▀▀▀   ▓
            ▓  ▓▓▓  ▓
     ''')
    else:
        jogador = 'MUTANTINHO'
        print('''
Você escolheu o 'MUTANTINHO'
          ▄▄▀▀▀▀▀▀▀▀▀▄▄
        █             █
        █          ▄▄▄  █
        █  ▄▄▄  ▄  ███  █
        ▄█ ▄   ▀▀▀   ▄ █▄
        █  ▀█▀█▀█▀█▀█▀  █
        ▄██▄▄▀▀▀▀▀▀▀▄▄██▄
      ▄█ █▀▀█▀▀▀█▀▀▀█▀▀█ █▄
        ''')

    return jogador

def enredo(jogador):
    print(f'''
VOCÊ ESTÁ EM UMA SALA MAL ILUMINADA E COM ODORES FORTES, E POUCOS SEGUNDOS DEPOIS, UMA PESSOA ESTRANHA SE APROXIMA.
"AGORA QUE VOCÊ CHEGOU ATÉ AQUI, PRECISO TE EXPLICAR MELHOR A HISTÓRIA. AFINAL, ATÉ AGORA VOCÊ NÃO SABE MUITO BEM
POR ONDE ENTROU E PORQUE ESTÁ AQUI." - Disse uma mulher de cabelos escuros.
"TUDO COMEÇOU EM 2020, QUANDO O MUNDO FOI ALASTRADO POR UM VÍRUS VINDO DA CHINA. AS PESSOAS ACHARAM QUE ERA SÓ UMA
"GRIPEZINHA" E NÃO LIGARAM, E BOM, SE VOCÊ ESTÁ JOGANDO ESSE JOGO, VOCÊ IMAGINA QUE COISAS BOAS NÃO ACONTECERAM, CERTO?
UMA PEQUENA PARTE DA POPULAÇÃO TEVE O ACESSO ÀS VACINAS, OS RICOS, CLARO! E ELES FORAM LEVADOS PARA A NOVA TERRA, UM
PLANETA LOCALIZADO A 1 ANO-LUZ DAQUI, E DEIXARAM NÓS, CIENTISTAS E POPULAÇÃO CARENTE PARA PERECER.
VOCÊ, {jogador}, É O ÚNICO CAPAZ DE SALVAR A HUMANIDADE DESSA CATASTROFE. O NOSSO ESTOQUE DE VACINAS ESTAVA ESCASSO E 
E VOCÊ RECEBEU A ÚLTIMA DOSE, VOCÊ É A NOSSA ÚNICA ESPERANÇA, ESTAMOS MUITO FRACOS PARA CONSEGUIR JOGAR O 'APOCAVID'.
POR FAVOR, NOS AJUDE A SALVAR A TERRA!" - Clamou a mulher.
    ''')


def expressao_usuario(jogador):
    print('''
IMAGINO QUE VOCÊ ESTEJA MUITO CONFUSO, QUAL A SUA EXPRESSÃO NESSE MOMENTO? VOU TE DAR ALGUMAS SUGESTÕES: 
    > HÃ?
    > CUMEQUIÉ?
    > CARAI CENOURINHA
''')

    expressao = input("Digite sua expressão aqui: ")

    print(f'''
DEPOIS DE GRITAR "{expressao.upper()}" INÚMERAS VEZES SEM ENTENDER ONDE HAVIA SE METIDO. {jogador} SE ACALMOU E A CIENTISTA CONTINUOU
EXPLICANDO O QUE ESTAVA ACONTECENDO...
"ANTES DE PARTIREM, OS RICOS DEIXARAM UM ESTOQUE DE VACINAS NA TERRA CAPAZ DE SALVAR A TODOS, MAS PARA TERMOS ACESSO A ELAS, É
PRECISO JOGAR O 'APOCAVID'. PORÉM, SÓ SE PODE JOGAR UMA VEZ, CASO CONTRÁRIO, TODO O ESTOQUE DE VACINAS EXPLODE E TODOS MORREMOS.
"NÓS ESTAMOS BUSCANDO HÁ DIAS ALGUÉM COM AS CARACTERÍSTICAS IDEAIS PARA JOGAR O 'APOCAVID' E ENCONTRAMOS VOCÊ." - Disse a cientista.
"PARA COMEÇAR A JOGAR, VOCÊ PRECISA IR ATÉ O PORTO TAPAJÓS E ENTREGAR O PASSE DO JOGO, A PARTIR DAÍ, O JOGO COMEÇA E NÃO HÁ MAIS COMO VOLTAR.
BOA SORTE." - Disse a cientista que se retirou do cômodo.
    ''')


def regras_jogo():
    print('''
VOCÊ ACORDOU UM POUCO TONTO E LOGO PERCEBEU QUE JUNTO A VOCÊ, TINHA UM MAPA QUE INDICAVA EXATAMENTE ONDE VOCÊ DEVERIA IR. 
QUE OS JOGOS COMECEM! 
REGRAS DO JOGO:
'APOCAVID' É UM JOGO DE PERGUNTAS E RESPOSTAS, CADA SALA TEM UMA PERGUNTA, E SÓ TEMOS DUAS REGRAS: 
    > VOCÊ NÃO PODE ERRAR A PRIMEIRA PERGUNTA.
    > DEPOIS DE ACERTAR A PRIMEIRA PERGUNTA, VOCÊ SÓ PODE ERRAR DUAS VEZES.
    ''')


def local(jogador):
    print('''
    ++++++++++++++++
     INICIO DE JOGO 
    ++++++++++++++++
    ''')
    if jogador == 'JACAREZINHO':
        print('''
     __________________________________
    |                                  |
    | BEM VINDO AO PORTO DE FORDLANDIA |
    |__________________________________|
    ''')
    elif jogador == 'ZE GOTINHA':
        print('''
     ___________________________________________
    |                                           |
    | BEM VINDO AO POSTO DE SAUDE DE FORDLANDIA |
    |___________________________________________|
''')
    else:
        print('''
     _______________________________________________
    |                                               |
    | BEM VINDO AO ESCRITORIO CENTRAL DE FORDLANDIA |
    |_______________________________________________|
    ''')

def pergunta1():
    print("SALA 1")
    print("DENTRO DA SALA 1, TINHA UMA GELADEIRA, {jogador} AO ABRIR O FREEZER SE DEPAROU COM UM POTE AZUL DE SORVETE.")
    print('''
    [ PERGUNTA 1 ] DENTRO DESSE POTE DE SORVETE TEM: 
        A. SORVETE
        B. FEIJÃO
        C. NADA
        ''')
    resposta_p1 = input("DIGITE A ALTERNATIVA CORRETA: ")
    return resposta_p1


def pergunta2():
    print("SALA 2")
    linhas()
    print('''
    [ PERGUNTA 2 ] QUAL É O ÚNICO MAMÍFERO QUE VOA? 
        A. MORCEGO
        B. PÁSSARO
        C. ABELHA
        ''')
    resposta_p2 = input("DIGITE A ALTERNATIVA CORRETA: ")
    return resposta_p2


def pergunta3():
    print("SALA 3")
    linhas()
    print('''
    [ PERGUNTA 3 ] QUAL É O MAIOR RIO DO BRASIL? 
        A. RIO PARANÁ
        B. RIO AMAZONAS
        C. RIO SÃO FRANCISCO
    ''')
    resposta_p3 = input("DIGITE A ALTERNATIVA CORRETA: ")
    return resposta_p3


def pergunta4():
    print("SALA 4")
    linhas()
    print('''
    [ PERGUNTA 4 ] SE, DURANTE UMA CORRIDA DE CARROS, VOCÊ DEIXA O SEGUNDO COLOCADO PARA TRÁS, QUAL É A SUA COLOCAÇÃO APÓS A ULTRAPASSAGEM? 
        A. PRIMEIRO
        B. TERCEIRO
        C. SEGUNDO
    ''')
    resposta_p4 = input("DIGITE A ALTERNATIVA CORRETA: ")
    return resposta_p4


def pergunta_sala_alternativa(jogador):
    print(f"APÓS SAIR DA SALA 4, {jogador} ENTROU EM UM CORREDOR QUE TINHAM 3 PORTAS.")

    resposta_porta = int(input("QUAL DELAS VOCÊ QUER ENTRAR? PORTA 1, 2 OU 3? "))
    return resposta_porta


def pergunta5():
    print("SALA 5")
    linhas()
    print('''
            [ PERGUNTA 5 ] QUAL É O MAIOR ÓRGÃO DO CORPO HUMANO? 
                A. PELE
                B. INTESTINOS
                C. CÉREBRO
            ''')
    resposta_p5 = input("DIGITE A ALTERNATIVA CORRETA: ")
    return resposta_p5


def pergunta5_alternativa():
    print("ATALHO")
    print("QUE SORTE! VOCÊ ACHOU UM ATALHO! SE PREPARE, A PRÓXIMA PERGUNTA É A MAIS DIFICIL DO JOGO.")
    print("SE VOCÊ ACERTAR, VOCÊ GANHA O JOGO, SE ERRAR, GAME OVER")

    print('''
            [ PERGUNTA 5 ] QUAL É A LINGUA MAIS FALADA NO MUNDO?
                A. HINDI
                B. INGLES
                C. MANDARIM
            ''')
    resposta_atalho = input("DIGITE A ALTERNATIVA CORRETA: ")
    return resposta_atalho


def pergunta6():
    print("SALA 6")
    linhas()
    print('''
    [ PERGUNTA 6 ] QUAL É O MAIOR PLANETA DO SISTEMA SOLAR?
        A. SATURNO
        B. JUPITER
        C. MERCURIO
    ''')
    resposta_p6 = input("DIGITE A ALTERNATIVA CORRETA: ")
    return resposta_p6


def pergunta7():
    print("SALA 7")
    linhas()
    print('''
    [ PERGUNTA 7 ] QUAL É O MAIOR ANIMAL TERRESTRE DO MUNDO?
        A. HIPOPOTAMO-PIGMEU DA AFRICA OCIDENTAL
        B. ELEFANTE DA SAVANA AFRICANA
        C. BALEIA-AZUL DA ILHA GEÓRGIA DO SUL
    ''')
    resposta_p7 = input("DIGITE A ALTERNATIVA CORRETA: ")
    return resposta_p7


#perguntas = [pergunta1(jogador), ...]

####### INICIO DO JOGO
# contador_resposta = 0
# pergunta1 = 0
#
# while pergunta1 != 1 and contador_resposta != 1:
#     linhas()
#     linhas()
#     print('''
#     ╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗╔╗  ╔╗╔══╗╔═══╗      ╔╗ ╔═══╗
#     ║╔═╗║║╔═╗║║╔═╗║║╔═╗║║╔═╗║║╚╗╔╝║╚╣─╝╚╗╔╗║     ╔╝║ ║╔═╗║
#     ║║ ║║║╚═╝║║║ ║║║║ ╚╝║║ ║║╚╗║║╔╝ ║║  ║║║║     ╚╗║ ║╚═╝║
#     ║╚═╝║║╔══╝║║ ║║║║ ╔╗║╚═╝║ ║╚╝║  ║║  ║║║║      ║║ ╚══╗║
#     ║╔═╗║║║   ║╚═╝║║╚═╝║║╔═╗║ ╚╗╔╝ ╔╣─╗╔╝╚╝║     ╔╝╚╗╔══╝║
#     ╚╝ ╚╝╚╝   ╚═══╝╚═══╝╚╝ ╚╝  ╚╝  ╚══╝╚═══╝     ╚══╝╚═══╝
#     ''')
#     linhas()
#     linhas()
#
#     jogador = escolha_jogador()
#
#     enredo(jogador)
#
#     expressao_usuario(jogador)
#
#     print(
#         f"DEPOIS DE HORAS TENTANDO ENCONTRAR ONDE ERA O SUPOSTO 'PORTO' PARA DAR INICIO AO JOGO, {jogador} ENTREGOU SEU PASSE E PUFF... APAGOU.")
#
#     regras_jogo()
#
#     local(jogador)
#
#     perguntas(jogador)
#
#     resposta = input("QUER JOGAR NOVAMENTE? S/N")
#     if resposta == 'N':
#         break

gabarito = ['B', 'A', 'B', 'C', 'A', 'B', 'B', 'A']


erros = 0

while True:
    jogador = escolha_jogador()

    if pergunta1() != gabarito[0]:
        print('GAME OVER')
        print(erros)
        break

    if pergunta2() != gabarito[1]:
        erros += 1
        print(erros)

    if pergunta3() != gabarito[2]:
        erros += 1
        if erros <= 2:
            break

    if pergunta4() != gabarito[3]:
        erros += 1
        if erros <= 2:
            break

    print(f"APÓS SAIR DA SALA 4, {jogador} ENTROU EM UM CORREDOR QUE TINHAM 3 PORTAS.")
    resposta = int(input("QUAL DELAS VOCÊ QUER ENTRAR? PORTA 1, 2 OU 3? "))

    if resposta == 1:
        print('GAME OVER')
        break
    elif resposta == 2:
        if pergunta5_alternativa() != gabarito[5]:
            print("GAME OVER")
            break
        else:
            dilema = int(input('[1] DESEJA SALVAR A HUMANIDADE OU [2] SE SALVAR? '))
            if dilema == 1:
                print('GANHOU')
                break
            else:
                print('GAME OVER')
                break
    else:
        if pergunta5() != gabarito[4]:
            erros += 1
            if erros <= 2:
                break
            pass

    if pergunta6() != gabarito[6]:
        erros += 1
        if erros <= 2:
            break

    if pergunta7() != gabarito[7]:
        erros += 1
        if erros <= 2:
            break


