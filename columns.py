#Jared Clark 76551956


import random
NONE = '   '
jewels = ['S', 'T', 'V', 'W', 'X', 'Y', 'Z']

class Invalid_Row_number(Exception):
    pass


class Invalid_Col_number(Exception):
    pass


class Column_game:

    def __init__(self):
        self._col = 6
        self._row = 13
        self._board = []
        self._col_num = 0
        self._block = []
        self._top = -1
        self._middle = -1
        self._bottom = -1
        self._stop = 3
        self._content_list = []
        self._fill_list = []
        self._spots = []
        self._spoot = []
        self._count = []

    def board_maker(self):
        '''creates a list of list that works as the game board'''
        for col in range(self._col):
            self._board.append([])
            for row in range(self._row):
                self._board[-1].append(NONE)

    def print_board(self):
        '''prints the board to the shell in correct format with the end border and bottome border'''
        for row in range(self._row):
            print('|', end='')
            for column in range(self._col):
                print(self._board[column][row], end='')

            print('|')

        print('', self._col * '---', '')

    def column_num(self):
        '''randomly generates a column number for the jewel block to appear in'''
        self._col_num = random.randint(0, self._col - 1)
        
    def falling_jewel_block(self):
        '''randomly generates a jewel block to fall'''
        self.column_num()
        self._stop = 3
        self._bottom = -1
        self._middle = -1
        self._top = -1
        block = []
        for a in range(3):
            block.append(self._falling_jewel(random.choice(jewels)))
        self._block = block

    def _block_in_board(self):
        '''incremently puts the block in the board one by one until it is all the way in'''
        i = 0
        a = -1
        if self._bottom==-1 and self._middle==-1 and self._top==-1:
            self._bottom += 1
            self._board[self._col_num][self._bottom] = self._block[a]
            
        elif self._middle==-1 and self._top==-1 and self._board[self._col_num][self._bottom+1] == NONE:
            self._bottom += 1
            self._middle += 1
            self._board[self._col_num][self._bottom] = self._block[a]
            self._board[self._col_num][self._middle] = self._block[a - 1]
            
            
        elif self._top==-1 and self._board[self._col_num][self._bottom+1]==NONE:
            self._bottom += 1
            self._middle += 1
            self._top += 1
            self._board[self._col_num][self._bottom] = self._block[a]
            self._board[self._col_num][self._middle] = self._block[a - 1]
            self._board[self._col_num][self._top] = self._block[a - 2]
            
    def faller_down(self):
        '''puts the block in the board until all the way in and then drops it down until it gets to the bottom'''
        while self._stop > 0:
            self._block_in_board()
            self._stop-=1
            return

        try:
            if self._board[self._col_num][self._bottom + 1] == NONE:
                self._board[self._col_num][self._bottom + 1] = self._board[self._col_num][self._bottom]
                self._board[self._col_num][self._middle + 1] = self._board[self._col_num][self._middle]
                self._board[self._col_num][self._top + 1] = self._board[self._col_num][self._top]
                self._board[self._col_num][self._top] = NONE
                self._bottom = self._bottom + 1
                self._middle = self._middle + 1
                self._top = self._top + 1
        except IndexError:
            pass

    def side_shift_right(self):
        '''moves the faller to the right when called and changes the col number to the new column the faller is in'''
        if self._board[self._col_num][self._bottom].startswith(' '):
            return
        if self._col_num==self._col-1:
            return 
        try:
            if self._bottom==-1 and self._middle==-1 and self._top==-1:
                self._col_num+=1

            elif self._bottom!=-1 and self._middle==-1 and self._top==-1 and self._board[self._col_num+1][self._bottom]==NONE:
                self._board[self._col_num+1][self._bottom]=self._block[-1]
                self._board[self._col_num][self._bottom]=NONE
                self._col_num+=1

            elif self._bottom!=-1 and self._middle!=-1 and self._top==-1 and self._board[self._col_num+1][self._bottom]==NONE and self._board[self._col_num+1][self._middle]==NONE:
                self._board[self._col_num+1][self._bottom]=self._block[-1]
                self._board[self._col_num+1][self._middle]=self._block[-2]
                self._board[self._col_num][self._bottom]=NONE
                self._board[self._col_num][self._middle]=NONE
                self._col_num+=1

            elif self._bottom!=-1 and self._middle!=-1 and self._top!=-1 and self._board[self._col_num+1][self._top]==NONE and self._board[self._col_num+1][self._bottom]==NONE and self._board[self._col_num+1][self._middle]==NONE:
                self._col_num += 1
                self._board[self._col_num][self._bottom] = self._board[self._col_num - 1][self._bottom]
                self._board[self._col_num][self._middle] = self._board[self._col_num - 1][self._middle]
                self._board[self._col_num][self._top] = self._board[self._col_num - 1][self._top]
                self._board[self._col_num - 1][self._bottom] = NONE
                self._board[self._col_num - 1][self._middle] = NONE
                self._board[self._col_num - 1][self._top] = NONE
        except IndexError:
            pass

    def side_shift_left(self):
        '''moves the faller to the left when called and changes the col number to the new column the faller is in'''

        if self._board[self._col_num][self._bottom].startswith(' '):
            return
        if self._col_num==0:
            return
        try:
            if self._bottom==-1 and self._middle==-1 and self._top==-1:
                self._col_num-=1

            elif self._bottom!=-1 and self._middle==-1 and self._top==-1 and self._board[self._col_num-1][self._bottom]==NONE:
                self._board[self._col_num-1][self._bottom]=self._block[-1]
                self._board[self._col_num][self._bottom]=NONE
                self._col_num-=1

            elif self._bottom!=-1 and self._middle!=-1 and self._top==-1 and self._board[self._col_num-1][self._bottom]==NONE and self._board[self._col_num-1][self._middle]==NONE:
                self._board[self._col_num-1][self._bottom]=self._block[-1]
                self._board[self._col_num-1][self._middle]=self._block[-2]
                self._board[self._col_num][self._bottom]=NONE
                self._board[self._col_num][self._middle]=NONE
                self._col_num-=1

            elif self._bottom!=-1 and self._middle!=-1 and self._top!=-1 and self._board[self._col_num-1][self._top]==NONE and self._board[self._col_num-1][self._bottom]==NONE and self._board[self._col_num-1][self._middle]==NONE:
                self._col_num -= 1
                self._board[self._col_num][self._bottom] = self._board[self._col_num + 1][self._bottom]
                self._board[self._col_num][self._middle] = self._board[self._col_num + 1][self._middle]
                self._board[self._col_num][self._top] = self._board[self._col_num + 1][self._top]
                self._board[self._col_num + 1][self._bottom] = NONE
                self._board[self._col_num + 1][self._middle] = NONE
                self._board[self._col_num + 1][self._top] = NONE
        except IndexError:
            pass

    def rotate_faller(self):
        '''rearranges the order of the faller by shifting the space down one of each and the bottom becomes the top'''
        if self._board[self._col_num][self._bottom].startswith(' '):
            return
        if self._bottom == -1 and self._middle == -1 and self._top == -1:
            a, b, c = self._block
            self._block = [c, a, b]
            
        elif self._bottom == 0 and self._middle == -1 and self._top == -1:
                    a, b, c = self._block
                    self._block = [c, a, b]
                    self._board[self._col_num][self._bottom] = self._block[-1]
        elif self._bottom == 1 and self._middle == 0 and self._top == -1:
            a, b, c = self._block
            self._block = [c, a, b]
            self._board[self._col_num][self._bottom] = self._block[-1]
            self._board[self._col_num][self._middle] = self._block[-2]
            
        elif self._bottom != -1 and self._middle != -1 and self._top != -1:
            a, b, c = self._block
            self._block = [c, a, b]
            self._board[self._col_num][self._bottom] = self._block[-1]
            self._board[self._col_num][self._middle] = self._block[-2]
            self._board[self._col_num][self._top] = self._block[-3]

    def land_block(self):
        '''when the block hits the bottom of the board or cannot move down more because of another jewel
it will change the brackets to straight bars'''
        if self._bottom == self._row - 1:
            self._board[self._col_num][self._bottom] = self._landing_jewel(self._board[self._col_num][self._bottom])
            self._board[self._col_num][self._middle] = self._landing_jewel(self._board[self._col_num][self._middle])
            self._board[self._col_num][self._top] = self._landing_jewel(self._board[self._col_num][self._top])
            return True
        try:
            if self._board[self._col_num][self._bottom + 1] != NONE and self._middle == -1 and self._top == -1:
                self._board[self._col_num][self._bottom] = self._landing_jewel(self._board[self._col_num][self._bottom])
                return True
                
            elif self._board[self._col_num][self._bottom + 1] != NONE and self._middle != -1 and self._top == -1:
                self._board[self._col_num][self._bottom] = self._landing_jewel(self._board[self._col_num][self._bottom])
                self._board[self._col_num][self._middle] = self._landing_jewel(self._board[self._col_num][self._middle])
                return True
                        
            elif self._board[self._col_num][self._bottom + 1] != NONE and self._middle != -1 and self._top != -1:
                self._board[self._col_num][self._bottom] = self._landing_jewel(self._board[self._col_num][self._bottom])
                self._board[self._col_num][self._middle] = self._landing_jewel(self._board[self._col_num][self._middle])
                self._board[self._col_num][self._top] = self._landing_jewel(self._board[self._col_num][self._top])
                return True
        except IndexError:
            pass
        else:
            return False

    def frozen_block(self):
        '''changes the straight bars around the faller to blank space'''
        if self._board[self._col_num][self._bottom].startswith('|'):
            self._board[self._col_num][self._bottom] = self._frozen_jewel(self._board[self._col_num][self._bottom])
            self._board[self._col_num][self._middle] = self._frozen_jewel(self._board[self._col_num][self._middle])
            self._board[self._col_num][self._top] = self._frozen_jewel(self._board[self._col_num][self._top])
            return -1

    def back_to_falling(self):
        '''returns one and takes faller out of landing if the block landed and then moved to allow it to move down more'''
        try:
            if self._board[self._col_num][self._bottom+1]==None:
                self._board[self._col_num][self._bottom]=self._falling_jewel(self._board[self._col_num][self._bottom])
                self._board[self._col_num][self._middle]=self._falling_jewel(self._board[self._col_num][self._middle])
                self._board[self._col_num][self._top]=self._falling_jewel(self._board[self._col_num][self._top])
                return 1
            else:
                pass
        except:
            pass

    def end_game(self):
        '''determines if the new faller can no longer move down signaling an end game'''
        if self._bottom == -1 and self._middle == -1 and self._top == -1 and self._board[self._col_num][0]!=NONE:
            return -1
        
        elif self._middle == -1 and self._top == -1 and self._board[self._col_num][self._bottom+1]!=NONE:
            return -1
        
        elif self._middle!=-1 and self._top == -1 and self._board[self._col_num][self._bottom+1]!=NONE:
            return -1

        elif self._bottom==self._row-1:
            pass

    def match_check(self):
        for row in range(self._row-1, -1,-1):
            for col in range(self._col-1,-1,-1):
                if self._board[col][row]==NONE:
                    pass
                else:
                    self.vertical_match(col,row)
                    self.horizontal_match(col,row)
                    self.diagonal_match_up_right(col, row)
                    self.diagonal_match_down_right(col,row)


##    def diagonal_match_up_right(self,col,row):
##
##    def diagonal_match_down_right(self,col,row):
##
##    def horizontal_match(self, col, row,):
##     
##    def vertical_match(self, col, row):

    def _all_down(self):
        '''drops all the jewels down in the board until everything has moved down as far as possible'''
        for row in range(self._row-1,-1,-1):
            for col in range(self._col-1,-1,-1):
                down=0
                spot=1
                if row==self._row-1 or self._board[col][row]==NONE:
                    pass
                while row+down<self._row-1 and self._board[col][row+spot]==NONE:
                        down+=1
                        spot+=1
                if down!=0:
                    self._board[col][row+down]=self._board[col][row]
                    self._board[col][row]=NONE

    def delete_matches(self, wanted_jewels:list):
        for c,r in wanted_jewels:
            self._board[c][r]=NONE
        self._all_down()

    def _falling_jewel(self, jewel):
        '''returns a jewel with brackets to represent a faller when printing the board
so the game knows it is the current faller'''
        return '[' + jewel + ']'

    def _just_letter(self, jewel):
        '''return the jewel without spaces, brackets, or bars'''
        return jewel[1]

    def _landing_jewel(self, jewel):
        '''return a jewel with bars to represent landing'''
        return '|' + jewel[1] + '|'

    def _frozen_jewel(self, jewel):
        '''returns the jewel with empty space around it to represent it has frozen'''
        return ' ' + jewel[1] + ' '
    
    def _match_jewel(self, jewel):
        '''returns the jewel with empty space around it to represent it has frozen'''
        return '*' + jewel[1] + '*'


