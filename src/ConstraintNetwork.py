#---[ Domain Class ]-----------------------------------------------------------
class Domain:
    def __init__(self, valueList: list[int]) -> None:
        self.values   = valueList
        self.modified = False
        
        return

    #---[ Accessors ]----------------------------------------------------------
    def getValues(self) -> list[int]:
        return self.values

    def isModified(self) -> bool:
        return self.modified
    
    def containsValue(self, value: int) -> bool:
        return value in self.valueList
    
    def getSize(self) -> int:
        return len(self.values)

    def isEmpty(self) -> bool:
        return not self.valueList
    
    def getFront(self) -> int:
        if self.getSize() < 1:
            return 0
        
        return self.values[0]
    
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

##--[ Domain Class ]-----------------------------------------------------------


#---[ Variable Class ]---------------------------------------------------------
class Variable:
    #---[ Data Model Methods ]-------------------------------------------------
    def __init__(self, possibleValues: list[int], row: int, col: int, block) -> None:
        self.row = row
        self.col = col
        self.domain = Domain(possibleValues)
        self.block = block

        self.modified   = True
        self.changeable = False
        self.assigned   = True

        if self.size() != 1:
            self.modified   = False
            self.changeable = True
            self.assigned   = False
        
        return
    
    ##--[ Data Model Methods ]-------------------------------------------------
    
    # Accessors
    def getAssignedValue(self) -> int:
        if not self.assigned:
            return 0
        
        return self.domain.getFront()
    
    def getDomain(self) -> Domain:
        return self.domain
    
    def getValues(self) -> list[int]:
        return self.domain.getValues()

    def getSize(self) -> int:
        return self.domain.getSize()

    def isModified(self) -> bool:
        return self.modified
    
    def isChangeable(self) -> bool:
        return self.changeable
    
    def isAssigned(self) -> bool:
        return self.assigned

    # Mutators
    def assignValue(self, valueToAssign: int) -> None:
        if not self.changeable:
            return

        self.assigned = True
        self.domain = Domain([valueToAssign])

        return
    
    def setDomain(self, domain: Domain) -> None:
        if not self.changeable:
            return
        
        if self.domain != domain:
            self.domain = domain
            self.modified = True

        return
    
    def removeValueFromDomain(self, valueToRemove: int) -> None:
        if not self.changeable:
            return
        
        self.domain.removeValue(valueToRemove)
        self.modified = self.domain.isModified()

        return

    def setModifier(self, newModifier: bool) -> None:
        self.modified = newModifier
        self.domain.setModified(newModifier)
        return
    
    def setUnassigned(self) -> None:
        self.assigned = False

##--[ Variable Class ]---------------------------------------------------------


#---[ Constraint Class ]-------------------------------------------------------
class Constraint:
    pass

##--[ Constraint Class ]-------------------------------------------------------


#---[ Trail Class ]------------------------------------------------------------
class Trail:
    '''
        - stack holding CSP changes. used for backtracking
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

##--[ Trail Class ]------------------------------------------------------------


#---[ Constraint Network Class ]-----------------------------------------------
class ConstraintNetwork:
    pass

##--[ Constraint Network Class ]-----------------------------------------------