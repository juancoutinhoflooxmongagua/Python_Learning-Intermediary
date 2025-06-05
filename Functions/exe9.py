pokemons = {
    'Charmander': {
        'nome': 'Charmander',
        'tipo': 'Fogo',
        'poder': 'Incinerar',
        'atk': 52,
        'hp': 39,
        'def': 43
    },
    'Bulbasauro': {
        'nome': 'Bulbasauro',
        'tipo': 'Grama',
        'poder': 'Vinhas',
        'atk': 49,
        'hp': 45,
        'def': 49
    }
}


print(pokemons.keys())
print(list(pokemons.keys()))

for name in pokemons:
    print(name)

my = pokemons['Charmander']
enemie = pokemons['Bulbasauro']

vermelho = '\033[31m'
verde = '\033[32m'
reset = '\033[0m'

while enemie['hp'] > 0:
    if my['poder'] == 'Incinerar':
        input('Pressione ENTER para atacar')
        print(vermelho, "ATAQUE", my['nome'], my['atk'], reset)
        print("HP inimigo", enemie['hp'])
        my['atk_reduzido'] = my['atk'] - enemie['def']
        print("Pokemon defendeu e o ataque foi reduzido para:", my['atk_reduzido'])
        print("HP após ataque", enemie['hp'] - my['atk_reduzido'])

    if enemie['poder'] == 'Vinhas':
        print('UPGRADE', enemie['atk'])
        enemie['hp'] = enemie['hp'] + 0.5
        enemie['atk_reduzido'] = enemie['atk'] - my['def']
        print("Ataque reduzido para:", enemie['atk_reduzido'])
        my['hp'] = my['hp'] - enemie['atk_reduzido']
        print(enemie['nome'], "ATACOU E TIROU A VIDA PARA", my['hp'])
        print("HP após upgrade", enemie['hp'])

    print(verde + "Como estou:", "HP", my['hp'], "ATAQUE", my['atk'], "DEFESA", my['def'], reset)
    input('Pressione ENTER pra continuar a batalha....')

    if my['hp'] <= 0:
        print('VC perdeu')
        break
