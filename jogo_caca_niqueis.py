import random

def exibir_menu(saldo):
    print('\n=== CAÇA NÍQUEIS ===')
    print(f'Saldo atual: R${saldo:.2f}')
    print('1. Girar os rolos (R$ 5)')
    print('2. Sair')


def girar_rolo():
    simbolos = ["🍒", "🍋", "🍊", "🍉", "⭐"]
    return [random.choice(simbolos) for _ in range(3)]


def verificar_combinacao(rolo):
    if rolo[0] == rolo[1] == rolo[2]:
        # Venceu
        return True
    else:
        # Perdeu
        return False


def main():
    while True:
        # Resolvendo erro de não digitar números inteiros
        try:
            print('==== Área de Depósitos ====')
            saldo = int(input('Coloque dinheiro: '))
            print('=' * 27)

            # Valor Armazenado
            valor_armazenado = saldo
            aposta = 5

            while True:
                exibir_menu(saldo)
                opcao = str(input('Escolha uma opção: '))

                # Opção 1 para girar
                if opcao == '1':
                    if saldo < aposta:
                        print('\033[31mSaldo insuficiente! Você não pode girar.\033[0m')
                        continue

                    saldo -= aposta
                    rolo = girar_rolo()
                    print(f'\n 🎰 {rolo[0]} | {rolo[1]} | {rolo[2]} 🎰')

                    if verificar_combinacao(rolo):
                        print('\033[32mVocê ganhou! Todas as colunas são iguais!\033[0m')
                        saldo += 50
                    else:
                        print('\033[31mQue pena, você perdeu!\033[0m')

                # Parando o jogo
                elif opcao == '2':
                    print('=' * 25)
                    # Mostrando o saldo anterior e o saldo atual
                    print(f'> Saldo Anterior: {valor_armazenado}')
                    print(f'> Saldo Atual: {saldo}')
                    break
                else:
                    print('Opção Inválida!')
        except:
            print('DIGITE UM VALOR VÁLIDO!')

        else:
            print('Obrigado por jogar! Até mais!')
            break

if __name__ == '__main__':
    main()