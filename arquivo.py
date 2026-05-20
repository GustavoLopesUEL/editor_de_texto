# Entradas 123
texto_entrada = list(input(''))
posicao_cursor = 0
tamanho_texto = len(texto_entrada)
texto_entrada.insert(posicao_cursor, "|")
#Casos
while True:
    comando = input('')
    match comando:
        case "F":
            break
        case "x":
            if posicao_cursor < tamanho_texto:
                texto_entrada.pop(posicao_cursor + 1)
            else: 
                pass
        case "X":
            pass
       case _:
            comando = comando.split(" ")
            match comando[0]:
                case "E":
                    nova_posicao = posicao_cursor - int(comando[1])
                    texto_entrada.pop(posicao_cursor)

                    if (nova_posicao > 0):
                        texto_entrada.insert(nova_posicao, "|")
                        posicao_cursor = nova_posicao
                    else:
                        texto_entrada.insert(0, "|")
                        posicao_cursor = 0
                case "D":
                    nova_posicao = posicao_cursor + int(comando[1])
                    texto_entrada.pop(posicao_cursor)

                    if (nova_posicao < tamanho_texto):
                        texto_entrada.insert(nova_posicao, "|")
                        posicao_cursor = nova_posicao
                    else:
                        texto_entrada.append("|")
                        print(texto_entrada)
                        posicao_cursor = tamanho_texto
                case "I":
                    pass
                case "i":
                    caracter = comando[1]
                    texto_entrada.insert(posicao_cursor, caracter)
                    tamanho_texto += 1
                    posicao_cursor += 1
texto_entrada.pop(posicao_cursor)
conversao_lista_para_texto = ""
for i in texto_entrada:
    conversao_lista_para_texto = conversao_lista_para_texto + i
print(conversao_lista_para_texto)
