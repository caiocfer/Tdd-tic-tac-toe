class Game:
    def initialize_field(self):
        self.field = []
        self.winning_player = ""

        for i in range(3):
            row = []
            for j in range(3):
                row.append(' ')
            self.field.append(row)
        return self.field    

    def instatiate_players(self):
        self.player1 = "X"
        self.player2 = "O"
        return self.player1, self.player2
    
    def player1_play(self, row, column):
        self.field[row][column] = self.player1

    def player2_play(self, row, column):
        self.field[row][column] = self.player2

    
    def check_empty_field(self,row, column):
        if self.field[row][column] == ' ':
            return True
        else:
            print("This is not empty, please choose another row/column")
            return False

    def check_winning_conditions(self):
        for i in range(3):
            #Check Columns
            if self.field[i][0] == self.field[i][1] == self.field[i][2] != ' ':
                self.winning_player = self.field[i][0]
                return True
            
            #Check Rows
            if self.field[0][i] == self.field[1][i] == self.field[2][i] != ' ':
                self.winning_player = self.field[0][i]
                return True
        
        #Check diagonals
        if self.field[0][0] == self.field[1][1] == self.field[2][2] != ' ':
            self.winning_player = self.field[0][0]
            return True
        
        if self.field[0][2] == self.field[1][1] == self.field[2][0] != ' ':
            self.winning_player = self.field[0][2]
            return True

        return False
    
    def start_game(self):
        self.instatiate_players()
        self.field = self.initialize_field()
    
    def player1_turn(self):
        print("Player 1 - Plays\n")
        row = int(input("Player 1 - Choose Row: "))
        column = int(input("Player 1 - Choose Column: "))
        if self.check_empty_field(row, column):
            self.player1_play(row, column)
        else:
            self.player1_turn()

    def player2_turn(self):
        print("Player 2 - Plays\n")
        row = int(input("Player 2 - Choose Row: "))
        column = int(input("Player 2 - Choose Column: "))
        if self.check_empty_field(row, column):
            self.player2_play(row, column)
        else:
            self.player2_turn()
    
    def print_field(self):
        for i in range(3):
            print(self.field[i])

    def play_game(self):
        self.start_game()
        while self.winning_player == "":
            if not self.check_winning_conditions():
                self.player1_turn()
                self.print_field()
            if not self.check_winning_conditions():                
                self.player2_turn()
                self.print_field()
        winner = ""
        if self.winning_player == self.player1:
            winner = "Player 1"
        else:
            winner = "Player 2"
        print("The winner is ", winner)

            

    