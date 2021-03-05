# FUNÇÕES DO JOGO
def linhas():
    print("=" * 180)

def apresentacao_jogo():
    linhas()
    linhas()

    print('''
     ╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗╔╗  ╔╗╔══╗╔═══╗      ╔╗ ╔═══╗
     ║╔═╗║║╔═╗║║╔═╗║║╔═╗║║╔═╗║║╚╗╔╝║╚╣─╝╚╗╔╗║     ╔╝║ ║╔═╗║
     ║║ ║║║╚═╝║║║ ║║║║ ╚╝║║ ║║╚╗║║╔╝ ║║  ║║║║     ╚╗║ ║╚═╝║
     ║╚═╝║║╔══╝║║ ║║║║ ╔╗║╚═╝║ ║╚╝║  ║║  ║║║║      ║║ ╚══╗║
     ║╔═╗║║║   ║╚═╝║║╚═╝║║╔═╗║ ╚╗╔╝ ╔╣─╗╔╝╚╝║     ╔╝╚╗╔══╝║
     ╚╝ ╚╝╚╝   ╚═══╝╚═══╝╚╝ ╚╝  ╚╝  ╚══╝╚═══╝     ╚══╝╚═══╝
    ''')

    linhas()
    linhas()

def escolha_jogador():
    print('''
    Você está pronto para jogar?
    Escolha um jogador:
    < 1 > Jacarezinho
    < 2 > Zé Gotinha
    < 3 > Mutantinho
    ''')
    linhas()
    resposta_usuario = int(input("Digite o número do seu jogador: "))
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
    linhas()

    print(f'''
    Você está em uma sala pequena e mal iluminada, poucos segundos depois, uma pessoa estranha se aproxima.
    "Agora que você chegou até aqui, preciso te explicar porque você está aqui." - Disse uma mulher de cabelos escuros.
    "Tudo começou em 2020, quando o mundo foi alastrado por um vírus chinês. As pessoas acharam que era só uma "gripezinha"
    e pouco ligaram, e bom, se você está jogando esse jogo, coisas boas não aconteceram, né?
    Uma pequena parte da população teve acesso às vacinas, os ricos, claro! Eles foram levados para a Nova Terra, um planeta
    um pouco longe daqui, e deixaram nós para perecer." - Disse a mulher com uma voz fraca.
    "Você, {jogador}, é o único capaz de salvar a humanidade dessa catastrofe. O nosso estoque de vacinas estava escasso e 
    você recebeu a última dose, você é a nossa única esperança, estamos muito fracos para conseguir jogar o 'APOCAVID'.
    Por favor, nos ajude a salvar nosso planeta." - Clamou a mulher.
        ''')
    linhas()

def expressao_usuario(jogador):
    linhas()

    print('''
    IMAGINO QUE VOCÊ ESTEJA MUITO CONFUSO, QUAL A SUA EXPRESSÃO NESSE MOMENTO? VOU TE DAR ALGUMAS SUGESTÕES: 
        > HÃ?
        > CUMEQUIÉ?
        > CARAI CENOURINHA
    ''')
    linhas()

    expressao = input("Digite sua expressão aqui: ")

    linhas()

    print(f'''
    Depois de gritar "{expressao.upper()}" inúmeras vezes sem entender onde havia se metido. {jogador} se acalmou e a mulher continuou explicando
    o que estava acontecendo...
    "Antes de partirem, os ricos deixaram um estoque de vacinas aqui que é capaz de salvar a todos, mas para termos acesso a elas, precisamos
    jogar o 'APOCAVID'. Porém, só se pode jogar uma vez, se você perder, todo o estoque de vacinas explode e todos morremos."
    "Nós estavamos há dias buscando alguém com as características ideiais para jogar o 'APOCAVID' e encontramos você."
    "Para começar a jogar, você precisa ir até o Porto Tapajós e entregar o passe do jogo, a partir daí, o jogo começa e não há mais como voltar.
        ''')

def regras_jogo():
    linhas()
    print("REGRAS DO JOGO")
    linhas()

    print('''
    'APOCAVID' é um jogo de perguntas e respostas, onde cada sala tem uma pergunta.
    O jogo só tem duas regras: 
        > Você não pode errar a primeira pergunta. 
        > Depois de acertar a primeira pergunta, você só pode errar duas vezes. 
        ''')

def local(jogador):
    linhas()
    print('INICIO DE JOGO')
    linhas()

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

def pergunta1(jogador):
    linhas()
    print("SALA 1")
    linhas()
    print(
        f"DENTRO DA SALA 1, TINHA UMA GELADEIRA, {jogador} AO ABRIR O FREEZER SE DEPAROU COM UM POTE AZUL DE SORVETE.")
    linhas()

    print('''
    [ PERGUNTA 1 ] DENTRO DESSE POTE DE SORVETE TEM: 
        A. SORVETE
        B. FEIJÃO
        C. NADA
        ''')
    linhas()

    resposta_p1 = input("DIGITE A ALTERNATIVA CORRETA: ").strip().upper()
    linhas()

    return resposta_p1

def pergunta2():
    linhas()
    print("SALA 2")
    linhas()

    print('''
    [ PERGUNTA 2 ] QUAL É O ÚNICO MAMÍFERO QUE VOA? 
        A. MORCEGO
        B. PÁSSARO
        C. ABELHA
        ''')

    resposta_p2 = input("DIGITE A ALTERNATIVA CORRETA: ").strip().upper()
    linhas()

    return resposta_p2

def pergunta3():
    linhas()
    print("SALA 3")
    linhas()

    print('''
    [ PERGUNTA 3 ] QUAL É O MAIOR RIO DO BRASIL? 
        A. RIO PARANÁ
        B. RIO AMAZONAS
        C. RIO SÃO FRANCISCO
    ''')

    resposta_p3 = input("DIGITE A ALTERNATIVA CORRETA: ").strip().upper()
    linhas()

    return resposta_p3

def pergunta4():
    linhas()
    print("SALA 4")
    linhas()

    print('''
    [ PERGUNTA 4 ] SE, DURANTE UMA CORRIDA DE CARROS, VOCÊ DEIXA O SEGUNDO COLOCADO PARA TRÁS, QUAL É A SUA COLOCAÇÃO APÓS A ULTRAPASSAGEM? 
        A. PRIMEIRO
        B. TERCEIRO
        C. SEGUNDO
    ''')

    resposta_p4 = input("DIGITE A ALTERNATIVA CORRETA: ").strip().upper()
    linhas()

    return resposta_p4

def pergunta_sala_alternativa(jogador):
    linhas()
    print(f"APÓS SAIR DA SALA 4, {jogador} ENTROU EM UM CORREDOR QUE TINHAM 3 PORTAS.")

    resposta_porta = int(input("QUAL DELAS VOCÊ QUER ENTRAR? PORTA 1, 2 OU 3? "))
    linhas()

    return resposta_porta

def pergunta5():
    linhas()
    print("SALA 5")
    linhas()

    print('''
    [ PERGUNTA 5 ] QUAL É O MAIOR ÓRGÃO DO CORPO HUMANO? 
        A. PELE
        B. INTESTINOS
        C. CÉREBRO        
            ''')

    resposta_p5 = input("DIGITE A ALTERNATIVA CORRETA: ").strip().upper()
    linhas()

    return resposta_p5

def pergunta5_alternativa():
    linhas()
    print("QUE SORTE! VOCÊ ACHOU UM ATALHO! SE PREPARE, A PRÓXIMA PERGUNTA É A MAIS DIFICIL DO JOGO.")
    print("SE VOCÊ ACERTAR, VOCÊ GANHA O JOGO, SE ERRAR, GAME OVER")
    linhas()

    print('''
    [ PERGUNTA 5 ] QUAL É A LINGUA MAIS FALADA NO MUNDO?
        A. HINDI
        B. INGLES
        C. MANDARIM
            ''')

    resposta_atalho = input("DIGITE A ALTERNATIVA CORRETA: ").strip().upper()
    linhas()

    return resposta_atalho

def pergunta6():
    linhas()
    print("SALA 6")
    linhas()

    print('''
    [ PERGUNTA 6 ] QUAL É O MAIOR PLANETA DO SISTEMA SOLAR?
        A. SATURNO
        B. JUPITER
        C. MERCURIO
    ''')

    resposta_p6 = input("DIGITE A ALTERNATIVA CORRETA: ").strip().upper()
    linhas()

    return resposta_p6

def pergunta7():
    linhas()
    print("SALA 7")
    linhas()

    print('''
    [ PERGUNTA 7 ] QUAL É O MAIOR ANIMAL TERRESTRE DO MUNDO?
        A. HIPOPOTAMO-PIGMEU DA AFRICA OCIDENTAL
        B. ELEFANTE DA SAVANA AFRICANA
        C. BALEIA-AZUL DA ILHA GEÓRGIA DO SUL
    ''')

    resposta_p7 = input("DIGITE A ALTERNATIVA CORRETA: ").strip().upper()
    linhas()

    return resposta_p7

def repetir():
    pergunta_jogar_novamente = input("Jogar novamente? [S/N] ").strip().upper()
    if pergunta_jogar_novamente == 'N':
        return False
    else:
        return True

# ______________________________________________________ INICIO DO JOGO _________________________________________________________________________

gabarito = ['B', 'A', 'B', 'C', 'A', 'B', 'B', 'B']

while (True):
    erros = 0

    apresentacao_jogo()

    jogador = escolha_jogador()

    enredo(jogador)

    expressao_usuario(jogador)

    linhas()
    print(f"    Depois de horas tentando encontrar onde era o suposto 'Porto' para iniciar o jogo, {jogador} entregou seu passe e puff... apagou.")

    regras_jogo()

    local(jogador)

    if pergunta1(jogador) != gabarito[0]:
        print('A regra é clara! Se errar a primeira questão, já era! Você perdeu! 💀')
        if not repetir():
            break
        else:
            continue

    if pergunta2() != gabarito[1]:
        erros += 1

    if pergunta3() != gabarito[2]:
        erros += 1
        if erros == 2:
            print('A regra é clara! Se errar mais de uma pergunta, já era! Você perdeu! 💀')
            if not repetir():
                break
            else:
                continue

    if pergunta4() != gabarito[3]:
        erros += 1
        if erros == 2:
            print('A regra é clara! Se errar mais de uma pergunta, já era! Você perdeu! 💀')
            if not repetir():
                break
            else:
                continue

    print(f"Após sair da SALA 4, {jogador} entrou em um corredor que tinham 3 portas.")
    resposta = int(input("Em qual porta você quer entrar? Digite 1, 2 ou 3? "))

    if resposta == 1:
        linhas()
        print('Ih... Porta errada! Sentimos muito, seu jogo termina por aqui. Você perdeu! 💀')
        linhas()
        if not repetir():
            break
        else:
            continue

    elif resposta == 2:
        if pergunta5_alternativa() != gabarito[5]:
            print(
                "Você errou a resposta! Já esperávamos, afinal, essa era a pergunta mais difícil do jogo. Você perdeu! 💀")
            if not repetir():
                break
            else:
                continue

        else:
            linhas()
            print("   Você acertou a pergunta! Parabéns! Mas calma, agora temos mais uma pergunta para você.")
            print('''
            Você foi convidado para viver em Terra Nova (o planeta dos ricos). Porém, para aceitar o convite,
            você irá se salvar e todo o resto da humanidade irá perecer. 

            Se você salvar a humanidade, você perde a sua chance única de se juntar aos Terra Novers e continuará no seu planeta. 
            E aí, qual vai ser? Agora você vai ter que escolher! 

            ''')

            linhas()

            dilema = int(input('Digite [1] Salvar a humanidade ou [2] Para se salvar e ir para Terra Nova: '))

            if dilema == 1:
                print('Que alegria! Você salvou a humanidade do APOCAVID! Parabéns, você venceu! 🏆')
                if not repetir():
                    break
                else:
                    continue
            else:
                print(
                    'Terra Nova pensou melhor e voltou atrás no convite. Sentimos muito, mas você irá perecer com o resto da humanidade. Você perdeu! 💀')
                if not repetir():
                    break
                else:
                    continue
    else:
        if pergunta5() != gabarito[4]:
            erros += 1
            if erros == 2:
                print('A regra é clara! Se errar mais de uma pergunta, já era! Você perdeu! 💀')
                if not repetir():
                    break
                else:
                    continue

    if pergunta6() != gabarito[6]:
        erros += 1
        if erros == 2:
            print('A regra é clara! Se errar mais de uma pergunta, já era! Você perdeu! 💀')
            if not repetir():
                break
            else:
                continue

    if pergunta7() != gabarito[7]:
        erros += 1
        if erros == 2:
            print('A regra é clara! Se errar mais de uma pergunta, já era! Você perdeu! 💀')
            if not repetir():
                break
            else:
                continue

    linhas()
    print("Que alegria! Você salvou a humanidade do APOCAVID! Parabéns, você venceu! 🏆")
    linhas()

    if not repetir():
        break
    else:
        continue