#---[ Global Imports ]---------------------------------------------------------
import sys
from   random import randint
from   string import digits, ascii_uppercase
from   pathlib import Path

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
        # checks for exactly 6 arguments
        invalidArgCount = len(self._argv) != self._EXPECTED_ARG_COUNT

        if invalidArgCount:
            self.printUsageMessage()
            raise SystemExit
        
        # check numBoards, rows, cols, & numHints are ints & not negative
        for arg in self._argv[2:]:
            if not arg.isnumeric() or int(arg) < 0:
                self.printUsageMessage()
                print("Error: Please enter non-negative integers only.\n")
                raise SystemExit

        # check last value is at least 1
        if int(self._argv[5]) < 1:
            self.printUsageMessage()
            print("Error: Please enter at least 1 for numHints.\n")
            raise SystemExit

        return

    def printUsageMessage(self) -> None:
        print("Usage:")
        print(f"$ boardMaker fileName numBoards rows cols numHints\n")
        print(f"{'':2s}{'fileName ':<15s}Base file name for collection of game boards storage")
        print(f"{'':2s}{'numBoards':<15s}Number of files to create storing each board")
        print(f"{'':2s}{'rows     ':<15s}Row count for each cell")
        print(f"{'':2s}{'cols     ':<15s}Column count for each cell")
        print(f"{'':2s}{'numHints ':<15s}Total number of revealed values at the start of the game\n")

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

        self.cellSize = self.rows * self.cols
        self.resourcePath = Path(__file__).parent.resolve() / "rsrc"
        if not self.resourcePath.exists():
            self.resourcePath.mkdir()

        return
    
    def createGameFiles(self) -> None:
        for boardNum in range(self.numFiles):
            board = self.createBoard()
            self.saveBoardtoFile(board, boardNum)
        
        return
    
    def createBoard(self) -> list[list[str]]:
        # initalize blank board
        board = self.makeZeroedBoard()

        # assign hint values
        numHintsAssigned = 0
        while numHintsAssigned < self.numHints:
            rowPicked = randint(0, self.cellSize - 1)
            colPicked = randint(0, self.cellSize - 1)
            valToAssign = randint(1, self.cellSize)

            valUnassigned = board[rowPicked][colPicked] == 0
            assignmentIsValid = self.isValidValue(valToAssign, board, rowPicked, colPicked)
            if valUnassigned and assignmentIsValid:
                board[rowPicked][colPicked] = valToAssign
                numHintsAssigned += 1

        return board

    def makeZeroedBoard(self) -> list[list[str]]:
        blankBoard = [
            [0 for col in range(self.cellSize)] for row in range(self.cellSize)
        ]

        return blankBoard

    def isValidValue(self,
        value: int,
        board: list[list[int]],
        rowToCheck: int,
        colToCheck: int,
    ) -> bool:
        rowValid, colValid = True, True

        # check col is valid
        for row in range(self.cellSize):
            if value == board[row][colToCheck]:
                colValid = False
                break

        # check row is valid
        for col in range(self.cellSize):
            if value == board[rowToCheck][col]:
                rowValid = False
                break

        return rowValid and colValid

    def numToBase36(self, num: int) -> str:
        res = ''
        base36Digits = digits + ascii_uppercase

        while num != 0:
            num, index = divmod(num, len(base36Digits))
            res = base36Digits[index] + res

        if res == '':
            res = '0'

        return res

    def saveBoardtoFile(self, board: list[list[str]], boardNum: int) -> None:
        fileName = self.resourcePath / f"{self.baseFileName}_{boardNum}.txt"
        
        with fileName.open('w') as outFile:
            # write board dimensions
            outFile.write(f"{self.rows} {self.cols}\n")

            # write board
            for row in range(self.cellSize):
                for col in range(self.cellSize):
                    outFile.write(self.numToBase36(board[row][col]) + " ")
                outFile.write("\n")

        return

##--[ Board Generator Class ]--------------------------------------------------
    

#---[ Main Function ]----------------------------------------------------------
def main() -> None:
    argvHandler = ArgvHandler()
    argTup = argvHandler.getArgsTup()

    generator = BoardGenerator(argTup)
    generator.createGameFiles()

    return

##--[ Main Function ]----------------------------------------------------------


#---[ Entry ]------------------------------------------------------------------
if __name__ == "__main__":
    main()

##--[ Entry ]------------------------------------------------------------------
