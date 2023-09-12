def main():
    print("Pense em um número entre 1 e n.")
    n = int(input("Digite o valor de n: "))
    
    inicio, fim = 1, n
    tentativas = 0
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        print(f"O número que você pensou é maior que {meio}?")
        resposta = input("Digite 'sim' ou 'nao': ").lower()

        tentativas += 1

        if resposta == 'sim':
            inicio = meio + 1
        elif resposta == 'nao':
            print(f"Então o número que você pensou é menor que {meio}?")
            resposta_menor = input("Digite 'sim' ou 'nao': ").lower()

            if resposta_menor == 'sim':
                fim = meio - 1
            elif resposta_menor == 'nao':
                print(f"Adivinhei! O número que você pensou é {meio}!")
                print(f"Eu adivinhei em {tentativas} tentativas.")
                return
            else:
                print("Resposta inválida. Encerrando o jogo.")
                return
        else:
            print("Resposta inválida. Encerrando o jogo.")
            return

    print("Hmm, algo deu errado. Não consegui adivinhar seu número!")

if __name__ == "__main__":
    main()
