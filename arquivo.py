texto_entrada = list(input(''))
posicao_cursor = 0
tamanho_texto = len(texto_entrada)
texto_entrada.insert(posicao_cursor, "|")
while True:
    comando = input('')
    match comando:
        case "F":
            break
        case "x":
            pass
        case "X":
            pass
        case _:
            comando = comando.split(" ")
            match comando[0]:
                case "E":
                    pass
                case "D":
                    pass
                case "I":
                    pass
                case "i":
                    pass
texto_entrada.pop(posicao_cursor)
conversao_lista_para_texto = ""
for i in texto_entrada:
    conversao_lista_para_texto = conversao_lista_para_texto + i
print(conversao_lista_para_texto)
