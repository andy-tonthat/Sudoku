#---[ Global Imports ]---------------------------------------------------------
import sys
import random
from   string import digits

##--[ Global Imports ]---------------------------------------------------------


#---[ CLI Arguments Handler Class ]--------------------------------------------
class ArgvHandler:
    def __init__(self) -> None:
        self._EXPECTED_ARG_COUNT = 6
        self._argv = sys.argv

        return

    def getArgsTup(self) -> tuple[str, int, int, int, int]:
        self.validateArgs()
        return (
            self._argv[1],
            int(self._argv[2]),
            int(self._argv[3]),
            int(self._argv[4]),
            int(self._argv[5]),
        )

    def validateArgs(self) -> None:
        invalidArgCount = len(self._argv) != self._EXPECTED_ARG_COUNT

        if invalidArgCount:
            self.printUsageMessage()
            raise SystemExit
        
        # validate numBoards, rows, cols, & numHints are ints
        invalidTypes = False
        for arg in self._argv[2:]:
            if not arg.isnumeric():
                invalidTypes = True
                break
        
        if invalidTypes:
            self.printUsageMessage()
            raise SystemExit

    def printUsageMessage(self) -> None:
        print("Usage:")
        print(f"$ boardMaker fileName numBoards rows cols numHints\n")
        print(f"{'':2s}{'fileName ':<15s}Base file name for collection of game boards storage")
        print(f"{'':2s}{'numBoards':<15s}Number of files to create storing each board")
        print(f"{'':2s}{'rows     ':<15s}Row count for each cell")
        print(f"{'':2s}{'cols     ':<15s}Column count for each cell")
        print(f"{'':2s}{'numHints ':<15s}Total number of revealed values at the start of the game")

        return

##--[ CLI Arguments Handler Class ]--------------------------------------------

#---[ Board Generator Class ]--------------------------------------------------
class BoardGenerator:
    def __init__(self, argTup: tuple[str, int, int, int, int]) -> None:
        self.baseFileName = argTup[0]
        self.numFiles     = argTup[1]
        self.rows         = argTup[2]
        self.cols         = argTup[3]
        self.numHints     = argTup[4]

        return
    
    def createBoard(self) -> list[list[str]]:
        
        return

##--[ Board Generator Class ]--------------------------------------------------
    

#---[ Main Function ]----------------------------------------------------------
def main() -> None:
    argvHandler = ArgvHandler()
    argvCorrect = argvHandler.getArgsTup()

    generator = BoardGenerator()
    
    return

##--[ Main Function ]----------------------------------------------------------


#---[ Entry ]------------------------------------------------------------------
if __name__ == "__main__":
    main()

##--[ Entry ]------------------------------------------------------------------
