#parte 7
palavra = input('Digite uma palavra: ')
vogais = 0
for letra in palavra:
    print(letra.upper())
    if letra.lower() in 'aeiou':
        vogais += 1
print('Vogais:', vogais)
print('a' in palavra.lower())
