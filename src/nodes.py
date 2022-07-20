from logicope import *

#this is just an idea. it doesn't work at
class Nodes:
    def __init__(self, type, state, wireTo):
        self.type = type
        self.state = state
        self.wireTo = wireTo

    def _log(self):
        pass
    
print(Nodes(LogiCope._and(True, True), False, False))