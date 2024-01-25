Alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

Alfabeto = [letras for i, letras in enumerate(Alfabeto) if (i+1) % 3 != 0]

print(Alfabeto)