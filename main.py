import random


class Colors:
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    BLACK = '\033[30m'
    RESET = '\033[0m'


class Ship:

    def __init__(self):
        print(f'{Colors.BLUE}\t\t\tWelcome to my little Ship Battle game!')
        print(f"This is a free-sized ships' battle{Colors.RESET}")

        self.user_board = []
        self.size = 0
        self.ships = 0
        self.board = []
        self.row = 0
        self.col = 0
        self.hits = 0
        self.attempts = 0

    def add_ship(self):
        self.size += 1

    def generate_board(self):
        self.board = [[random.choices([0, 1]) for _ in range(self.size)] for _ in range(self.size)]
        return self.board

    def decide(self):
        print(f'{Colors.BLUE}1) Play again')
        print(f'2) Exit{Colors.RESET}')
        option = input(f'{Colors.CYAN}Enter your choice:{Colors.PURPLE} {Colors.RESET}')
        if option == '1':
            self.reset_game()
            self.play()
        elif option == '2':
            exit()
        else:
            print(f'{Colors.RED}Invalid option{Colors.RESET}')
            self.decide()

    def reset_game(self):
        self.ships = 0
        self.user_board.clear()
        self.hits = 0
        self.attempts = 3


    def show_user_board(self):
        for row in self.user_board:
            print(' '.join(map(str, row)))

    def generate_user_board(self):
        self.user_board = [['*' for _ in range(self.size)] for _ in range(self.size)]
        return self.user_board

    def count_ships(self):
        return sum(row.count(1) for row in self.board)

    def play(self):
        self.size = int(input(f'{Colors.CYAN}Enter the size of the board:{Colors.PURPLE} {Colors.RESET}'))
        if self.size <= 1:
            print(f'{Colors.YELLOW}Cannot create such board{Colors.RESET}')
            self.play()
        self.attempts = self.size
        print(f'{Colors.BLUE}Attempts you will be given:{Colors.PURPLE}', self.attempts, Colors.RESET)
        self.generate_board()
        self.generate_user_board()
        self.ships = self.count_ships()
        print(f'{Colors.BLUE}\t<--- This is your chosen board! --->{Colors.RESET}')
        self.show_user_board()

        def loop():
            try:
                self.row = int(input(f'{Colors.CYAN}Enter the row:{Colors.PURPLE} {Colors.RESET} '))
                self.col = int(input(f'{Colors.CYAN}Enter the column:{Colors.PURPLE} {Colors.RESET} '))

                if self.row < 1 or self.row > self.size or self.col < 1 or self.col > self.size:
                    print(f'{Colors.YELLOW}Please enter numbers between 1 and {self.size}.')
                    loop()

            except ValueError:
                print(f'{Colors.YELLOW}You have chosen wrong input!{Colors.RESET}')
                loop()
            if self.board[self.row - 1][self.col - 1] != 1:
                print(f'{Colors.RED}Not here!{Colors.RESET}')
                self.attempts -= 1
                print(Colors.PURPLE, self.attempts, f'{Colors.BLUE}attempts left{Colors.RESET}')
                self.user_board[self.row - 1][self.col - 1] = 0
                self.show_user_board()
                if self.attempts == 0:
                    print(f'{Colors.RED}You have no attempts left, you lost!{Colors.RESET}')
                    self.decide()
                else:
                    loop()
            if self.board[self.row - 1][self.col - 1] == 1:
                print(f'{Colors.GREEN}You hit the target!{Colors.RESET}')
                self.user_board[self.row - 1][self.col - 1] = 1
                self.hits += 1
                if self.hits == self.ships:
                    print(f'{Colors.GREEN}You win!{Colors.RESET}')
                    self.decide()
                self.show_user_board()
                print(f'{Colors.BLUE}You have {Colors.PURPLE}{self.ships - self.hits}{Colors.BLUE} ships left!{Colors.RESET}')
                loop()

        loop()

game = Ship()
game.play()
