#---[ Global Imports ]---------------------------------------------------------
from   random  import randint
from   pathlib import Path
from   string  import ascii_uppercase, digits

#---[ Global Imports ]---------------------------------------------------------


#---[ Board Generator Class ]--------------------------------------------------
class BoardGenerator:
    def __init__(self, numRows: int, numCols: int, numHints: int, numFiles: int=1) -> None:
        self.numRows  = numRows
        self.numCols  = numCols
        self.numHints = numHints
        
        self.blockSize = self.numRows * self.numCols

        self.numFiles = numFiles
        self.fileName = input("Enter the file name the boards are stored under: ")

        self.currBoard = []

        # create directory to dump board files
        if not Path("./boards").exists(): Path("./boards").mkdir()
        self.dumpDir = Path(f"./boards/{self.fileName}")
        if not self.dumpDir.exists(): self.dumpDir.mkdir()

        return

    def makeBoards(self) -> None:
        for worldNum in range(self.numFiles):
            print(f"Generating Board #{worldNum}")
            self._createBoard(worldNum)

    def _createBoard(self, worldNum: int) -> None:
        self.currBoard = [
            [0 for _ in range(self.blockSize)]
            for _ in range(self.blockSize)
        ]
        hintsCount = self.numHints

        while hintsCount > 0:
            row, col = randint(0, self.blockSize - 1), randint(0, self.blockSize - 1)
            valToAssign = randint(0, self.blockSize)

            cellIsEmpty   = self.currBoard[row][col] == 0
            assignIsValid = self._isValidValue(valToAssign, row, col)
            if cellIsEmpty and assignIsValid:
                self.currBoard[row][col] = valToAssign
                hintsCount -= 1
        
        filePath = self.dumpDir / f"{self.fileName}-{worldNum}.txt"
        with filePath.open('w') as outFile:
            outFile.write(f"{self.numRows} {self.numCols}\n")

            for i in range(self.blockSize):
                for j in range(self.blockSize):
                    base36Str = self._intToBase36Str(self.currBoard[i][j])
                    outFile.write(f"{base36Str} ")
                outFile.write("\n")

        return
    

    # Utility Methods
    def _isValidValue(self, 
        val: int,
        row: int,
        col: int
    ) -> bool:
        return (
            self._isValidRow(val, row) and
            self._isValidCol(val, col) and
            self._isValidBlock(val, row, col)
        )
    
    def _isValidRow(self, val: int, row: int) -> bool:
        for col in range(self.blockSize):
            if val == self.currBoard[row][col]: return False
        
        return True
    
    def _isValidCol(self, val: int, col: int) -> bool:
        for row in range(self.blockSize):
            if val == self.currBoard[row][col]: return False
        
        return True
    
    def _isValidBlock(self, val: int, row: int, col: int) -> bool:
        rowDiv, colDiv = row // self.numRows, col // self.numCols
        rowLow, rowHigh = rowDiv * self.numRows, (rowDiv + 1) * self.numRows
        colLow, colHigh = colDiv * self.numCols, (colDiv + 1) * self.numCols

        for i in range(rowLow, rowHigh):
            for j in range(colLow, colHigh):
                if self.currBoard[i][j] == val: return False

        return True

    def _intToBase36Str(self, num: int) -> str:
        res = ""
        digitArr = digits + ascii_uppercase

        while num != 0:
            num, remainder = divmod(num, len(digitArr))
            res = digitArr[remainder] + res

        return res if res != "" else '0'

#---[ Board Generator Class ]--------------------------------------------------


#---[ Main Function ]----------------------------------------------------------
def main() -> None:
    numRows   = int(input("Enter the number of rows in a block: "))
    numCols   = int(input("Enter the number of cols in a block: "))
    numHints  = int(input("Enter the number of hints: "))
    numBoards = int(input("Enter the number of boards to make: "))

    generator = BoardGenerator(numRows, numCols, numHints, numBoards)
    generator.makeBoards()

    return

#---[ Main Function ]----------------------------------------------------------


#---[ Entry ]------------------------------------------------------------------
if __name__ == "__main__":
    main()
#---[ Entry ]------------------------------------------------------------------
