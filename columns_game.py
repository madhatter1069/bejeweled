#Jared Clark 76551956

import pygame
import columns

FRAME_RATE=50

class ColumnsGame:
    def __init__(self):
        self._running=True
        self._game_over=True
        self._board=Board()
        self._column=columns.Column_game()

    def run(self):
        '''initializes the game and runs the game until the player loses and closes the window when the player quits'''
        pygame.init()

        try:
            clock=pygame.time.Clock()

            self._create_surface((600,600))

            self._column.board_maker()
            

            while self._running:
                while self._game_over:
                    self._column.falling_jewel_block()
                    try:
                        a=0
                        while self._column._bottom==self._column._row and self._running or self._column._board[self._column._col_num][self._column._bottom+1]==columns.NONE and self._running:
                            a+=clock.tick(FRAME_RATE)
                            self._handle_events()
                            self._draw_frame()
                            if a>=1000*(self._column._bottom+1):
                                self._column.faller_down()
                                self._draw_frame()
                                    
                            if self._column._bottom==self._column._row-1 or self._column._board[self._column._col_num][self._column._bottom+1]!=columns.NONE:
                                self._handle_events()
                                self._column.land_block()
                                self._handle_events()
                                self._draw_frame()
                                
                            self._draw_frame()
                            end=self._column.end_game()
                            if end==-1:
                                self._game_over=False
                    except:
                        pass
                    finally:
                        self._column.frozen_block()
##                        self._column.match_check()
                        self._draw_frame()
            self._handle_events()
            self.game_over()

        finally:
            pygame.quit()

    def _create_surface(self, size:(int,int)):
        ''' creates a resizable surface for the window'''
        self._surface=pygame.display.set_mode(size,pygame.RESIZABLE)

    def _handle_events(self):
        '''gets all events that occur during the game'''
        for event in pygame.event.get():
            self._handle_event(event)

    def _handle_event(self, event):
        '''handles each individual event that happens in the game'''
        if event.type==pygame.QUIT:
            self._stop_running()
            self._game_over=False
        elif event.type==pygame.VIDEORESIZE:
            self._create_surface(event.size)
            
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                self._column.rotate_faller()
            if event.key==pygame.K_RIGHT:
                self._column.side_shift_right()
            elif event.key==pygame.K_LEFT:
                self._column.side_shift_left()
        pygame.display.update()

    def _draw_frame(self):
        '''draws the window with color and te jewels on the board'''
        self._surface.fill(pygame.Color(235, 168, 23))
        self._draw_board()
        self.faller_rect()
         
        if self._column._bottom==self._column._row-1 or self._column._board[self._column._col_num][self._column._bottom+1]!=columns.NONE:
            self._handle_events()
            if self._column.back_to_falling()==1:
                self._column.back_to_falling
                pygame.display.flip()
                return
            else:
                self.landed_faller()
                pygame.time.delay(FRAME_RATE*6)

        pygame.display.flip()

    def _draw_board(self):
        '''creates the rect the jewels will display over'''
        tl_frac_x, tl_frac_y=self._board.top_left()
        
        game_rect=(
            self._frac_x_to_pixel_x(tl_frac_x),
            self._frac_y_to_pixel_y(tl_frac_y),
            self._frac_x_to_pixel_x(.42),
            self._frac_y_to_pixel_y(.91))
        
        pygame.draw.rect(
            self._surface,
            pygame.Color(0,0,0),
            game_rect)
        
    def faller_rect(self):
        '''displays each jewel in the proper location with its proper color'''
        tl_x,tl_y=self._board.top_left()
        block_size=self._board.block_size()
        
        for col in range(self._column._col):
            for row in range(self._column._row):
                a,b,c=self._board._jewel_color(self._column._board[col][row])
                                               
                spot_rect=(
                    self._frac_x_to_pixel_x(tl_x+(block_size*col)),
                    self._frac_y_to_pixel_y(tl_y+(block_size*row)),
                    self._frac_x_to_pixel_x(block_size),
                    self._frac_y_to_pixel_y(block_size))
                    
                pygame.draw.rect(self._surface,
                                 pygame.Color(a,b,c),
                                 spot_rect)

    def landed_faller(self):
        '''flashes the faller white when it lands'''
        tl_x,tl_y=self._board.top_left()
        block_size=self._board.block_size()
        
        bottom_rect=(
            self._frac_x_to_pixel_x(tl_x+(block_size*self._column._col_num)),
            self._frac_y_to_pixel_y(tl_y+(block_size*self._column._bottom)),
            self._frac_x_to_pixel_x(block_size),
            self._frac_y_to_pixel_y(block_size))
        
        middle_rect=(
            self._frac_x_to_pixel_x(tl_x+(block_size*self._column._col_num)),
            self._frac_y_to_pixel_y(tl_y+(block_size*self._column._middle)),
            self._frac_x_to_pixel_x(block_size),
            self._frac_y_to_pixel_y(block_size))
        
        top_rect=(
            self._frac_x_to_pixel_x(tl_x+(block_size*self._column._col_num)),
            self._frac_y_to_pixel_y(tl_y+(block_size*self._column._top)),
            self._frac_x_to_pixel_x(block_size),
            self._frac_y_to_pixel_y(block_size))
        
        landed_spots=[bottom_rect,middle_rect,top_rect]
        
        for spot in landed_spots:
            pygame.draw.rect(self._surface,
                             pygame.Color(255,255,255),
                             spot)

    def game_over(self):
        '''prints a big L on the game window when the player loses'''
        L=[(self._frac_x_to_pixel_x(.24),self._frac_y_to_pixel_y(.053)),
           (self._frac_x_to_pixel_x(.27),self._frac_y_to_pixel_y(.053)),
           (self._frac_x_to_pixel_x(.27),self._frac_y_to_pixel_y(.89)),
           (self._frac_x_to_pixel_x(.55),self._frac_y_to_pixel_y(.89)),
           (self._frac_x_to_pixel_x(.55),self._frac_y_to_pixel_y(.92)),
           (self._frac_x_to_pixel_x(.24),self._frac_y_to_pixel_y(.92))
            ]
        
        self._surface.fill(pygame.Color(235, 168, 23))
        self._draw_board()
        self.faller_rect()
        
        pygame.draw.polygon(self._surface,
                            pygame.Color(57,192,237),
                            L)

        
        pygame.display.flip()
                            
                      
           
                
    def _frac_x_to_pixel_x(self, frac_x:float):
        '''changes the fractional values of x to amounts o pixels in x direction'''
        return self._frac_to_pixel(frac_x,self._surface.get_width())
    
    def _frac_y_to_pixel_y(self, frac_y:float):
        '''changes the fractional values of y to amounts y pixels in y direction'''
        return self._frac_to_pixel(frac_y,self._surface.get_height())

    def _frac_to_pixel(self, frac:float, max_pixel:int):
        '''multiplies the fractional value times the amount of pixels and returns an int for it'''
        return int(frac*max_pixel)

    def _stop_running(self):
        '''stops the loop from running the game'''
        self._running=False


class Board:
    def __init__(self):
        self._state=columns.Column_game()

    def top_left(self):
        '''is the top left point of the game board'''
        return (.17, .045)

    def block_size(self):
        '''returns the size the block in fractional value'''
        return .07
        
    def _jewel_color(self, jewel:str):
        '''returns the color of each jewel'''
        if "S" in jewel:
            return (25,213,227)
        elif "T" in jewel:
            return (255,0,0)
        elif "V" in jewel:
            return (250,37,207)
        elif "W" in jewel:
            return (107,5,232)
        elif "X" in jewel:
            return (12,232,37)
        elif "Y" in jewel:
            return (250,250,0)
        elif "Z" in jewel:
            return (0,38,255)
        elif jewel=="   ":
            return (0,0,0)
                    
       

        
        





if __name__=='__main__':
    ColumnsGame().run()
    
