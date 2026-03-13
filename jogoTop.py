print('Jogo Top\n')

print('Menu\n'
      '1 - New Game\n' \
      '2 - Load Game\n' \
      '3 - Exit\n'
      )

escolha =  int(input('Escolha um número referente a sua opção: '))

if escolha == 1:
    print('Iniciando novo jogo...')
    print('Você escuta o som do vento passando pelas árvores… folhas se movendo… e algo distante, como um sino antigo.')
    print('Lentamente, seus olhos se abrem.')
    print('Você está deitado na grama úmida, olhando para um céu desconhecido, iluminado por duas luas prateadas.')
    print('Sua cabeça dói.')
    print('Você tenta se lembrar de algo… qualquer coisa… Mas sua memória está completamente vazia.')
    print('Uma voz suave ecoa na sua mente:')
    print('Estranho: "Viajante… você finalmente despertou."')
    print('Você se levanta devagar. Ao redor, existe apenas uma enorme floresta envolta em névoa.')
    print('A voz continua:')
    print('"Antes de seguir seu destino… diga-me… quem é você?"')
    nome = str(input('Qual é o seu nome?  '))

    print('\nInimigo: ? | Level: ? | HP: ?')

    print('1 - Atacar\n'
          '2 - Defender\n'
          '3 - Fugir\n')
    
    suaVida = 100
    seuDano = 20
    inimigoVida = 80
    inimigoDano = 15





    escolha = int(input('Escolha sua ação: '))
    if escolha ==  1:
        print('Você ataca o inimigo com um golpe poderoso!')
        suaVida -= inimigoDano
    elif escolha == 2:
        print('Você se prepara para defender o próximo ataque do inimigo.')
    elif escolha == 3:
        print('Você nao pode fugir')


elif escolha == 2:
    print('Carregando jogo...')
elif escolha == 3:
    print('Obrigado por jogar!')
    exit()

