
## Libraries Importation
import random

## Global variables
# Titulo do jogo
str_title = ">>>>>>>>>>>>>>HANGMAN<<<<<<<<<<<<<<<"

# Armazenar o tabuleiro em uma lista
lst_board = [ ["---------   "],
              ["|       |   "],
              ["|       |   "],
              ["|       |   "],
              ["|           "],
              ["|           "],
              ["|           "],
              ["|           "],
              ["|           "],
              ["|           "]]

## Classes
class Hangman:

    def __init__(self, word):
        """
            Description:
                    --

            Keyword arguments:
                    --

            Return:
                    --

            Exception:
                    --
        """
        self.word = word.upper()
        self.correct_letters = []
        self.wrong_letters = []

    def guess(self, p_letter):
        """
            Description:
                Método para adivinhar a letra

            Keyword arguments:
                p_letter -- STRING: Letra a ser pesquisada

            Return:
                --

            Exception:
                --
        """
        if p_letter.upper() in self.word:
            self.correct_letters.append(p_letter)
            return True

        self.wrong_letters.append(p_letter.upper())
        return False

    def hangman_over(self):
        """
            Description:
                Método para verificar se o jogo terminou
            Keyword arguments:
                None
            Return

            Exception

        """
        # Se tiver informado 6 letras incorretas, game over
        if len(self.wrong_letters) == 6:
            return True

        # Se todas as letras não foram adivinhadas
        for letter in self.word:
            if letter not in self.correct_letters:
                return False
        return True

    def hangman_won(self):
        """
            Description:
                Método para verificar se o jogador venceu

            Keyword arguments:

            Return

            Exception
        """
        # Se todas as letras não foram adivinhadas
        for letter in self.word:
            if letter not in self.correct_letters:
                return False
        return True

    def hide_word(self):
        """
            Description:
                Método para não mostrar a letra no board

            Keyword arguments

            Return

            Exception
        """
        word = []

        for letter in self.word:
            if letter.upper() in self.correct_letters:
                word.append(letter)
            else:
                word.append("_")

        print("Palavra: ", word)

    def print_game_status(self):
        """
            Description:
                Método para checar o status do game e imprimir o board na tela

            Keyword arguments

            Return

            Exception

        """
        ## Exibir a forca
        self.print_board_hangman()

        ## Montando o objeto com a palavra que será exibida
        self.hide_word()

        ## Exibir a palavra
        print("\n\nPalavras Acertadas: ", self.correct_letters)
        print("\nPalavras Erradas: ", self.wrong_letters)

    def print_board_hangman(self):
        """
            Description:
                Método imprimi a forca na tela

            Keyword arguments

            Return

            Exception

        """

        ## Para cada letra errada alterar o objeto referente a forca
        if len(self.wrong_letters) == 1:
            lst_board[4] = ["|       O   "]
        elif len(self.wrong_letters) == 2:
            lst_board[5] = ["|       |   "]
        elif len(self.wrong_letters) == 3:
            lst_board[5] = ["|      /|   "]
        elif len(self.wrong_letters) == 4:
            lst_board[5] = ["|      /|\  "]
        elif len(self.wrong_letters) == 5:
            lst_board[6] = ["|      /    "]
        elif len(self.wrong_letters) == 6:
            lst_board[6] = ["|      / \  "]

        ## Para cada item da lista realizar a impressão
        for x in lst_board:
            print(x)

def rand_word():
    """
        Description:
            Função para ler uma palavra de forma aleatória do banco de palavras

        Keyword arguments

        Return

        Exception
    """
    with open("data/words.txt", "rt") as t:
        bank = t.readlines()

    return bank[random.randint(0, len(bank))].strip().upper()

def main():

    # Objeto que referencia a classe Hangman
    game = Hangman(rand_word())

    # Comntador referente a primeira partida
    counter = 0

    while not game.hangman_over():

        # Limpar o console
        print("\n" * 130)

        # Exibir o titulo
        print(str_title)

        # Exibir a forca se for a primeira partida
        game.print_game_status() if counter == 0 else None

        # Solicitar uma letra
        print('Informe uma letra: ')
        letter = str(input()).upper()

        # Submeter a letra ao metodo que verifica se esta correta
        game.guess(letter)

        # Exibir o status atual
        game.print_game_status()


    if game.hangman_won():
        print("Parabéns! Você venceu o jogo")
    else:
        print("\nGame Over! você perdeu.")
        print("\nA palavra era: " + game.word)



if __name__ == "__main__":
    main()

