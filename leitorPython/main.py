with open('entrada.txt', 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()

linhas_formatadas = []



for linha in linhas:
    linhas_formatadas.append(linha.rstrip('\n'))

index = 0
for linha in linhas_formatadas:
    if(linha[0].islower()):
        linhas_formatadas[index-1] += " " + linha
        del linhas_formatadas[index]
    index += 1

index = 0
aux = ""
for linha in linhas_formatadas:
    if(linha.isupper()):
        linhas_formatadas[index] = "<strong>" + linha + "</strong>"
    index += 1

index = 0
for linha in linhas_formatadas:
    linhas_formatadas[index] = "<p>" + linha + "</p>"
    index += 1

texto_formatado = []
for linha in linhas_formatadas:
    texto_formatado.append(linha)
    texto_formatado.append("<p></p>")

for linha in texto_formatado:
    print(linha)

 # if (linha.isupper() and index == 0):
    #     linhas_formatadas.append("<p><strong>{}</strong></p>".format(linha.rstrip('\n')))
    # else:
    #     linhas_formatadas.append('<p>{}</p>'.format(linha.rstrip('\n')))
    # index += 1
    # # linhas_formatadas.append('<p></p>')