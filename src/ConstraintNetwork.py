#---[ Domain Class ]-----------------------------------------------------------
class Domain:
    def __init__(self, valuesList: list[int]) -> None:
        self.valuesList = valuesList
        self.modified  = False
        
        return

    #---[ Accessors ]----------------------------------------------------------
    def getValuesList(self) -> list[int]:
        return self.valuesList

    def isModified(self) -> bool:
        return self.modified
    
    def containsValue(self, value: int) -> bool:
        return value in self.valuesList
    
    def getSize(self) -> int:
        return len(self.valuesList)

    def isEmpty(self) -> bool:
        return not self.valuesList
    
    def getFront(self) -> int:
        if self.getSize() < 1:
            return 0
        
        return self.valuesList[0]
    
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
    def __init__(self, possibleValues: list[int], row: int, col: int) -> None:
        self.row = row
        self.col = col
        self.domain = Domain(possibleValues)

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

    def checkIfModified(self) -> bool:
        return self.modified
    
    def checkIfChangable(self) -> bool:
        return self.changeable
    
    def checkIfAssigned(self) -> bool:
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
    def __init__(self) -> None:
        self.variableList: list[Variable] = []
        return
    
    # Accessors
    def getVariableList(self) -> list[Variable]:
        return self.variableList

    def getSize(self) -> int:
        return len(self.variableList)

    # Constraint Methods
    def addVariable(self, variable: Variable) -> None:
        self.variableList.append(variable)
        return
    
    def containsVariable(self, variable: Variable) -> bool:
        return variable in self.variableList
    
    def checkIfModified(self) -> bool:
        res = False

        for variable in self.variableList:
            if not variable.checkIfModified():
                res = True
                break

        return res

    def checkIfConsistent(self) -> bool:
        for variableOne in self.variableList:
            if not variableOne.checkIfAssigned():
                continue

            for variableTwo in self.variableList:
                if not variableTwo.checkIfAssigned() or variableOne == variableTwo:
                    continue

                if variableOne.getAssignedValue() == variableTwo.getAssignedValue():
                    return False

        return True

##--[ Constraint Class ]-------------------------------------------------------


#---[ Trail Class ]------------------------------------------------------------
class Trail:
    '''
        - stack holding CSP changes. used for backtracking
    '''
    
    def __init__(self) -> None:
        self.stateStack = []
        self.sizeStack  = []

        self.pushCount   = 0
        self.rewindCount = 0

    #---[ Accessors ]----------------------------------------------------------
    def getSize(self) -> int:
        return len(self.stateStack)

    def getPushCount(self) -> int:
        return self.pushCount
    
    def getRewindCount(self) -> int:
        return self.rewindCount
    ##--[ Accessors ]----------------------------------------------------------


    def saveCurrSize(self) -> None:
        self.sizeStack.append(self.getSize())
        return

    def pushState(self, variable: Variable) -> None:
        listCopy = [value for value in variable.getValues()]
        currDomain = Domain(listCopy)
        
        state = tuple(variable, currDomain)
        self.stack.append(state)

        self.pushCount += 1
        return
    
    def rewindState(self) -> None:
        targetStackSize = self.sizeStack.pop()
        currStackSize   = self.getSize()

        for i in range(currStackSize, targetStackSize-1, -1):
            state = self.stateStack.pop()

            stateVar: Variable  = state[0]
            stateDomain: Domain = state[1]
            stateVar.setDomain(stateDomain)
            stateVar.setModifier(False)
            stateVar.setUnassigned() 

        self.rewindCount += 1
        return
    
    def clearTrail(self) -> None:
        self.stateStack = []
        self.sizeStack  = []

        return

##--[ Trail Class ]------------------------------------------------------------


#---[ Constraint Network Class ]-----------------------------------------------
class ConstraintNetwork:
    pass

##--[ Constraint Network Class ]-----------------------------------------------