#enunciado
#faça um calculador de pontuação de um torneio,o programa principal irá receber o nome do jogador, e as  3 pontuações, ele deve  chamar a função para fazer a media das 3,
# se a media for menor que 40 ele será nivel bronze
#se for maior ou igual a 40 será prata, se for maior ou igual a 60 ele é ouro, se for maior ou igual a 75 é diamante, se for igual ou maior que 90 é campeão.
#ao final deve-se mostrar o nome do jogador, as 3 pontuações, a media entre elas e sua classificação final
def classificar_jogador(p1, p2, p3):
    media = (p1 + p2 + p3) / 3

    if media >= 90:
        classificacao = "Campeão "
    elif media >= 75:
        classificacao = "Diamante "
    elif media >= 60:
        classificacao = "Ouro "
    elif media >= 40:
        classificacao = "Prata "
    else:
        classificacao = "Bronze "

    return media, classificacao


# Função principal (main)
print("TORNEIO DE GAMES")
nome = input("Nome do jogador: ")
p1 = float(input("Pontuação da partida 1 (0 a 100): "))
p2 = float(input("Pontuação da partida 2 (0 a 100): "))
p3 = float(input("Pontuação da partida 3 (0 a 100): "))

media, classificacao = classificar_jogador(p1, p2, p3)

print("\nRESULTADO DO TORNEIO")
print(f"Jogador:        {nome}")
print(f"Partida 1:      {p1:.1f} pts")
print(f"Partida 2:      {p2:.1f} pts")
print(f"Partida 3:      {p3:.1f} pts")
print(f"Média:          {media:.1f} pts")
print(f"Classificação:  {classificacao}")