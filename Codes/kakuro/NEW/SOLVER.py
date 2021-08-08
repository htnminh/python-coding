# from typing import ClassVar

#==========================================================================================

class Tile00():
    '''
    x
    '''
    def __init__(self) -> None:
        # self.address = None # a tuple
        pass

    def __str__(self) -> str:
        '''
        |-----
        |#####
        |#####
        |#####
        '''
        return '\
|-----\n\
|#####\n\
|#####\n\
|#####'

#==========================================================================================

class Tile10():
    '''
    39-x
    '''
    def __init__(self, sum_below_block) -> None:
        self.sum_below_block = sum_below_block
        # self.address = None # a tuple
        # self.below_block = None # a list of tuples
                
    
    def __str__(self) -> str:
        '''
        |-----
        | \   
        |  \  
        |39 \ 
        
        |-----
        | \   
        |  \  
        |9  \ 
        '''
        return '\
|-----\n\
| \\   \n\
|  \\  \n\
|%s%s\\ ' % (self.sum_below_block, ' ' * (3 - len(str(self.sum_below_block))))

#==========================================================================================

class Tile01():
    '''
    x-32
    '''
    def __init__(self, sum_right_block) -> None:
        self.sum_right_block = sum_right_block
        # self.address = None # a tuple
        # self.right_block = None # a list of tuples
    
    
    def __str__(self) -> str:
        '''
        |-----
        | \ 32
        |  \  
        |   \ 
        
        |-----
        | \  2
        |  \  
        |   \ 
        '''
        return '\
|-----\n\
| \\ %2s\n\
|  \\  \n\
|   \\ ' % self.sum_right_block

#==========================================================================================

class Tile11(Tile10, Tile01):
    '''
    5-16
    '''
    def __init__(self, sum_below_block, sum_right_block) -> None:
        Tile10.__init__(self, sum_below_block)
        Tile01.__init__(self, sum_right_block)


    def __str__(self) -> str:
        '''
        |-----
        | \ 32
        |  \  
        |9  \ 
        '''
        return '\
|-----\n\
| \\ %2s\n\
|  \\  \n\
|%s%s\\ ' % (self.sum_right_block, 
                     self.sum_below_block, ' ' * (3 - len(str(self.sum_below_block))))
    
#==========================================================================================

class TileBlank():
    '''
    0
    '''
    def __init__(self) -> None:
        pass
    
    
    def __str__(self) -> str:
        return '\
|-----\n\
|     \n\
|     \n\
|     '

#==========================================================================================

class Block():
    pass

#==========================================================================================

class Board():
    def __init__(self, input_path) -> None:
        self.board = self.read_input(input_path)
    
    
    def read_input(self, input_path) -> list:
        #----------------------------
        def input_to_tile_instance(ele): # -> instance of following Tile-classes 
            if ele == 'x':
                return Tile00()
            if ele == '0':
                return TileBlank()
            else: 
                # 39-x, x-32, 5-16
                ele0, ele1 = ele.split('-')
                if ele1 == 'x': # 39-x
                    return Tile10(int(ele0))
                if ele0 == 'x': # x-32
                    return Tile01(int(ele1))
                return Tile11(ele0, ele1)
        #----------------------------
        self.input_path = input_path
        
        with open(input_path, 'r') as input_file:
            first_line = input_file.readline().strip()
            self.num_col = len(first_line.split())
            
            input_file.seek(0)
            
            self.num_row = 0
            board = list()
            for line in input_file:
                self.num_row += 1
                board.append([input_to_tile_instance(ele) for ele in line.split()])
                
        return board

    
    def assign_address_and_blocks(self):
        pass
    
    
    def __str__(self) -> str:
        res = str()
        for row in range(self.num_row):
            line = [str() for i in range(4)]
            for col in range(self.num_col):
                for i in range(4):
                    line[i] += str(self.board[row][col]).split('\n')[i]
            for i in range(4):
                line[i] += '|'

            res += '%s\n%s\n%s\n%s\n' % (line[0], line[1], line[2], line[3])
        res += '|-----' * self.num_col + '|'
        return res
            
#==========================================================================================
    
table = Board('input.txt')
print(table)