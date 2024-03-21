class Domain:
    def __init__(self, valueList: list[int]) -> None:
        self.values   = valueList
        self.modified = False
        
        return

    #---[ Accessors ]----------------------------------------------------------
    def containsValue(self, value: int) -> bool:
        return value in self.valueList
    
    def getSize(self) -> int:
        return len(self.values)

    def isEmpty(self) -> bool:
        return not self.valueList
    
    def isModified(self) -> bool:
        return self.modified
    
    ##--[ Accessors ]----------------------------------------------------------


    #---[ Mutators ]-----------------------------------------------------------
    def addValue(self, value: int) -> None:
        if value not in self.values:
            self.values.append(value)
        
        return
    
    def removeValue(self, value: int) -> bool:
        removedVal = False

        if value in self.values:
            self.values.remove(value)
            self.modified = True
        
        return removedVal
    
    def setModified(self, newModified: bool) -> None:
        self.modified = newModified
        return

    ##--[ Mutators ]-----------------------------------------------------------

class Variable:
    '''
        - represents a variable in CSP
    '''
    def __init__(self) -> None:

        return

class Constraint:
    pass

class Trail:
    '''
        - Represents a stack holding problem changes.
          - stacks fascilitate backtracking
    '''
    
    def __init__(self) -> None:
        self.stack  = []
        self.marker = []

        self.pushCount   = 0
        self.rewindCount = 0

    #---[ Accessors ]----------------------------------------------------------
    def getSize(self) -> int:
        return len(self.stack)

    def getPushCount(self) -> int:
        return self.pushCount
    
    def getRewindCount(self) -> int:
        return self.rewindCount
    ##--[ Accessors ]----------------------------------------------------------


    def placeTrailMarker(self) -> None:
        self.marker.append(self.getSize())
        return

    def pushVariable(self, variable: Variable) -> None:
        currDomain = Domain()
        

        self.pushCount += 1

class ConstraintNetwork:
    pass