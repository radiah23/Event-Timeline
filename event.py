class event: 
    def __init__(self, date, description=None, next=None, previous=None):
        self.date = date 
        self.description = description
        self.next = next
        self.previous = previous
    
    def __gt__(self, other):
        if other != None: 
            return self.date > other.date 
        else:
            return False
    
    def __lt__(self, other):
        if other != None: 
            return self.date < other.date 
        else:
            return False
    
    def __eq__(self, other): 
        if other != None:
            return self.date == other.date 
        else:
            return False
    
    def __str__(self): 
        return f"{self.date}, {self.description}"
    
    def __repr__(self): 
        return f"{self.date}, {self.description}, {self.next}, {self.previous}"
    
    
    
    




