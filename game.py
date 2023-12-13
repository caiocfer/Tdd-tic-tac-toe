class Game:
    def initialize_field(self):
        self.field = []
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
        self.field[row][column] = "X"

    def player2_play(self, row, column):
        self.field[row][column] = "O"
    
    def check_empty_field(self,row, column):
        print("Row: ", row)
        print("Column: ", column)
        print("Field: ", self.field)
        if self.field[row][column] == ' ':
            print("True")
            return True
        else:
            print("This is not empty, please choose another row/column")
            return False

        
    def start_game(self):
        field = self.initialize_field()
        return field
    
    def check_winning_conditions(self):
        for i in range(3):
            #Check Columns
            if self.field[i][0] == self.field[i][1] == self.field[i][2] != ' ':
                return True
            
            #Check Rows
            if self.field[0][i] == self.field[1][i] == self.field[2][i] != ' ':
                return True
        
        #Check diagonals
        if self.field[0][0] == self.field[1][1] == self.field[2][2] != ' ':
            return True
        
        if self.field[0][2] == self.field[1][1] == self.field[2][0] != ' ':
            return True
    
        return False