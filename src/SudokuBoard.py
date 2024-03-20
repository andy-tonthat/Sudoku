#---[ Global Imports ]---------------------------------------------------------
import random
from   string import digits, ascii_uppercase

##--[ Global Imports ]---------------------------------------------------------


#---[ Sudoku Board Class ]-----------------------------------------------------
class SudokuBoard:
    '''
        - Represents the game board.
        - Intended for conversion into Constraint Network for BacktrackSolver to
          solve as a Constraint Satisfaction Problem.
    '''

    #---[ Data Model Methods ]-------------------------------------------------
    def __init__(self) -> None:
        self.numRows = 0
        self.numCols = 0

        self.cellSize = self.numRows * self.numCols

    def __str__(self) -> str:
        pass

    ##--[ Data Model Methods ]-------------------------------------------------


    #---[ Accessors ]----------------------------------------------------------
    
    ##--[ Accessors ]----------------------------------------------------------


    #---[ Mutators ]-----------------------------------------------------------
    
    ##--[ Mutators ]-----------------------------------------------------------


    #---[ Utility Methods ]----------------------------------------------------
    def _convertDecimalToBase36(self, val: int) -> str:
        res = ''
        base36Digits = digits + ascii_uppercase

        while num != 0:
            num, index = divmod(num, len(base36Digits))
            res = base36Digits[index] + res

        if res == '':
            res = '0'

        return res

    def _convertBase36ToDecimal(self, char: str) -> int:
        resInt = 0
        
        try:
            resInt = int(char, base=36)
        except ValueError:
            pass

        return resInt
    
    ##--[ Utility Methods ]----------------------------------------------------

##--[ Sudoku Board Class ]-----------------------------------------------------
