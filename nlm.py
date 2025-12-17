

class DataObject():
    def __init__(self,data:bytes):
        self.data=data
    def __call__(self):
        return(self.data)
    def que(self,i:int):
        return(int(str(self.data)[2:][i]))


# logic:
def AND_B(ADD1:DataObject,ADD2:DataObject):
    constructor=""
    for i in range(len(str(ADD2.data)[2:-1])):
        if ADD1.que(i) == 1 and ADD2.que(i) == 1:
            constructor=f"{constructor}{1}"
        else:
            constructor=f"{constructor}0"
    return(f"b'{constructor}'")

def OR_B(ADD1:DataObject,ADD2:DataObject):
    constructor=""
    for i in range(len(str(ADD2.data)[2:-1])):
        if ADD1.que(i) == 1 or ADD2.que(i) == 1:
            constructor=f"{constructor}{1}"
        else:
            constructor=f"{constructor}0"
    return(f"b'{constructor}'")

def XOR_B(ADD1:DataObject,ADD2:DataObject):
    constructor=""
    for i in range(len(str(ADD2.data)[2:-1])):
        if (ADD1.que(i) + ADD2.que(i)) == 1:
            constructor=f"{constructor}{1}"
        else:
            constructor=f"{constructor}0"
    return(f"b'{constructor}'")

# assignment:
def MOV_B():
    pass

def LSL_B():
    pass

def LSR_B():
    pass

def ASR_B():
    pass

def ROR():
    pass

comma=DataObject(b"0")
dash=DataObject(b"1")


for i in [AND_B,OR_B,XOR_B]:
    print(f"{i}")
    
    print(i(comma,comma))
    print(i(comma,dash))
    print(i(dash,comma))
    print(i(dash,dash))