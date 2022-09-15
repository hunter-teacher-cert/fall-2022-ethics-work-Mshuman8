#make a cell class
class Cell:
    def __init__(self, value = " "):
        # the self's value is equal to the integer version of the arugement value if that arguemnt is not a space otherwise it is a None
        #The question mark is a ternary >> and is a test then a value if true and a value if false
        self.value = None if value == " " else int(value)
        # Assign this IF condition else assign that.
        self.row_num = ""
        self.col_num = ""
        self.cage_num = ""
        self.possible_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#make a row class
class Row:
    def __init__(self):
        # self.board = board
        self.cells = []
        self.row_num = []
        self.no_repeat_row = []
    
    def check_row(self):
        for a_cell in self.cells:
            if a_cell.value not in self.no_repeat_row:
                self.no_repeat_row.append(a_cell.value)
                print(self.no_repeat_row)
            else:
                print(("You have a repeat in your row"))
                return False
        # print("Your row looks great!")
        return True

    def update_possibilities(self):
        possibles = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
        # for each_cell in self.cells:
        #     if each_cell.value != None:
        #         row_values.append(each_cell.value)
        for each_cell in self.cells:
            if each_cell.value != None:
                for the_cell in self.cells:
                    if each_cell.value in the_cell.possible_values:
                        the_cell.possible_values.remove(each_cell.value)
        return True
          

#make a column class
class Column:
    def __init__(self):
        self.cells = []
        self.no_repeat_column = []

    def check_column(self):
        for a_cell in self.cells:
            if a_cell.value not in self.no_repeat_column:
                self.no_repeat_column.append(a_cell)
            else:
                # print(("You have a repeat in your column"))
                return False
        # print("Your column looks great!")
        return True
    
    def update_possibilities(self):
        possibles = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
        # for each_cell in self.cells:
        #     if each_cell.value != None:
        #         row_values.append(each_cell.value)
        for each_cell in self.cells:
            if each_cell.value != None:
                for the_cell in self.cells:
                    if each_cell.value in the_cell.possible_values:
                        the_cell.possible_values.remove(each_cell.value)
        return True


#make a cage class
class Cage: 
    def __init__(self):
        self.cells = []
        self.no_repeat_cage = []

    def check_cage(self):
        for a_cell in self.cells:
            if a_cell.value not in self.no_repeat_cage:
                self.no_repeat_cage.append(a_cell.value)
            else:
                print(("You have a repeat in your cage"))
                return False
        # print("Your cage looks great!")
        return True

    def update_possibilities(self):
        possibles = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
        # for each_cell in self.cells:
        #     if each_cell.value != None:
        #         row_values.append(each_cell.value)
        for each_cell in self.cells:
            if each_cell.value != None:
                for the_cell in self.cells:
                    if each_cell.value in the_cell.possible_values:
                        the_cell.possible_values.remove(each_cell.value)
        return True
  


#make a Board class
class Board: 
    def __init__(self, string_values):
        self.string_values = string_values
        self.cells = []
        self.rows = []
        self.columns = []
        self.cages = []

    def make_cells(self):
        for char in self.string_values:
            self.cells.append(Cell(char))
        # print(self.cells)
    
    def determine_placement(self):
        for cell in self.cells:
            index_num = self.cells.index(cell)
            #calculate row
            if index_num <= 8:
                cell.row_num = 0
            elif index_num <= 17:
                cell.row_num = 1
            elif index_num <= 26:
                cell.row_num = 2
            elif index_num <= 35:
                cell.row_num = 3
            elif index_num <= 44:
                cell.row_num = 4
            elif index_num <= 53:
                cell.row_num = 5
            elif index_num <= 62:
                cell.row_num = 6
            elif index_num <= 71:
                cell.row_num = 7
            else: 
                cell.row_num = 8
            #calculate column
            if index_num % 9 == 0:
                cell.col_num = 0
            elif index_num % 9 == 1:
                cell.col_num = 1
            elif index_num % 9 == 2:
                cell.col_num = 2
            elif index_num % 9 == 3:
                cell.col_num = 3
            elif index_num % 9 == 4:
                cell.col_num = 4
            elif index_num % 9 == 5:
                cell.col_num = 5
            elif index_num % 9 == 6:
                cell.col_num = 6
            elif index_num % 9 == 7:
                cell.col_num = 7
            elif index_num % 9 == 8:
                cell.col_num = 8 

            #calculate cage
            if index_num in [0, 1, 2, 9, 10, 11, 18, 19, 20]:
                cell.cage_num = 0
            elif index_num in [3, 4, 5, 12, 13, 14, 21, 22, 23]:
                cell.cage_num = 1
            elif index_num in [6, 7, 8, 15, 16, 17, 24, 25, 26]:
                cell.cage_num = 2
            elif index_num in [27, 28, 29, 36, 37, 38, 45, 46, 47]:
                cell.cage_num = 3
            elif index_num in [30, 31, 32, 39, 40, 41, 48, 49, 50]:
                cell.cage_num = 4
            elif index_num in [33, 34, 35, 42, 43, 44, 51, 52, 53]:
                cell.cage_num = 5
            elif index_num in [54, 55, 56, 63, 64, 65, 72, 73, 74]:
                cell.cage_num = 6
            elif index_num in [57, 58, 59, 66, 67, 68, 75, 76, 77]:
                cell.cage_num = 7
            else:
                cell.cage_num = 8

    def make_rows(self):
        for x in range(9):
            self.rows.append(Row())
    
    def add_cell_to_row(self):
        for a_cell in self.cells:
            self.rows[a_cell.row_num].cells.append(a_cell)

    def make_columns(self):
        for x in range(9):
            self.columns.append(Column())
        
    def add_cell_to_col(self):
        for a_cell in self.cells:
            # print(a_cell.col_num)
            self.columns[a_cell.col_num].cells.append(a_cell)

    def make_cages(self):
        for x in range(9):
            self.cages.append(Cage())
    
    def add_cell_to_cage(self):
        for a_cell in self.cells:
            self.cages[a_cell.cage_num].cells.append(a_cell)

    def make_board(self):
        self.make_cells()
        self.determine_placement()
        self.make_rows()
        self.add_cell_to_row()
        self.make_columns()
        self.add_cell_to_col()
        self.make_cages()
        self.add_cell_to_cage()

    # def check_board(self):
    #     for a_row in self.rows:
    #         a_row.check_row()
    #     for a_col in self.columns:
    #         a_col.check_column()
    #     for a_cage in self.cages:
    #         a_cage.check_cage()

    def print_board(self):
        num = 0
        for x in range(len(self.rows)):
            row_sent = ""
            for a_cell in self.rows[x].cells:
                if a_cell.value == None:
                    poss_sent = ""
                    for a_value in a_cell.possible_values:
                        poss_sent += str(a_value)
                    row_sent += "{" + poss_sent + "}"
                else: 
                    row_sent += str(a_cell.value)
                if a_cell.col_num == 2 or a_cell.col_num == 5:
                    row_sent += "|"
            num += 1
            if x % 3 == 0: 
                print("___________")
            print(row_sent)

    def assign_values(self):
        for a_cell in self.cells:
            if a_cell.value == None:
                if len(a_cell.possible_values) == 1:
                    a_cell.value = a_cell.possible_values[0]
                    
    def determine_possible_cell_values(self):
        for a_row in self.rows:
            a_row.update_possibilities()
        for a_column in self.columns: 
            a_column.update_possibilities()
        for a_cage in self.cages:
            a_cage.update_possibilities()

    def solve(self):
        for a_cell in self.cells:
            while a_cell.value == None:
                self.determine_possible_cell_values()
                self.assign_values()

    def make_solve_print(self):
        self.make_board()
        self.solve()
        self.print_board()
    
    def check_board(self):
        for a_row in self.rows:
            checker = a_row.check_row()
            print("running1")
            if checker == False:
                print("running2")
                return False
        for a_col in self.columns: 
            checker = a_col.check_column()
            print("running3")
            if checker == False:
                print("running4")
                return False
        for a_cage in self.cages:
            checker = a_cage.check_cage()
            print("running5")
            if checker == False:
                print("running6")
                return False
        else:
          print("running7")
          return True



##Asking for input
print("Welcome to Sudoku Solver. This works best for easy and medium puzzles.\n")
row1 = input("Please enter all the values of the first (top) row. For a blank, enter a space.\n")
row2 = input("Please enter all the values of the second (from top) row. For a blank, enter a space.\n")
row3 = input("Please enter all the values of the third (from top) row. For a blank, enter a space.\n")
row4 = input("Please enter all the values of the fourth (from top) row. For a blank, enter a space.\n")
row5 = input("Please enter all the values of the fifth (from top) row. For a blank, enter a space.\n")
row6 = input("Please enter all the values of the sixth (from top) row. For a blank, enter a space.\n")
row7 = input("Please enter all the values of the seventh (from top) row. For a blank, enter a space.\n")
row8 = input("Please enter all the values of the eighth (from top) row. For a blank, enter a space.\n")
row9 = input("Please enter all the values of the ninth (from top) row. For a blank, enter a space.\n")

sudoku_string = row1 + row2 + row3 + row4 + row5 + row6 + row7 + row8 + row9

board5 = Board(sudoku_string)
board5.make_solve_print()