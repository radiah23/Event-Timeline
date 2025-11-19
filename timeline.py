
from event import event as Event
class timeline:
    def __init__(self): 
        self.start = None 
        self.end = None 
        self.count = 0 

    def __len__(self) : 
        return self.count
    
    def __str__(self): 
        result = [] 
        current = self.start 
        while current != None: #if we are pointing to an event we keep going 
            result.append(current.date) #result = result.append() didnt work because its already there and it returns nothing so we directly use this
            current = current.next 
        results = "→".join(result)
        return results #print in the main [ print(timeline1._string_()), Timeline1 = timeline() ]
    
    def add(self, event, front=False): 
        if not isinstance(event, Event): 
            raise NotImplementedError
        if event.next != None or event.previous != None :
            raise NotImplementedError
        #Empty case 
            #what if the timeline is empty --> check this case 
            #if its empty --> dont look for the last event --> just insert it in the list 
            #add +1 to self.count --> because we are adding one event 
        
        if self.count == 0: 
            self.start = event 
            self.end = event
            self.count = 1 
        elif front: 
            self.start.previous = event 
            event.next = self.start 
            self.start = event 
            self.count += 1 
        else: 
        #Not an empty timeline --> consider of we add it to the front and end
            self.end.next = event
            event.previous = self.end 
            self.end = event 
            self.count += 1 
    
    def remove(self, target, front= False) : #Front = False : it just means we want to check from backwards 
        if not isinstance(target, Event): 
            raise NotImplementedError
        isFound = False 
        if front == True : 
            current = self.end
            while current != None: 
                if current == target: 
                    isFound = True 
                    if current.previous == None and current.next == None: 
                        self.start = None 
                        self.end = None 
                    elif current.previous == None : 
                        self.start = current.next 
                        current.next.previous = None 
                    elif current.next == None : 
                        current.previous.next = None 
                        self.end = current.previous 
                    else: 
                        new_next  = current.next 
                        new_prev = current.previous 
                        new_next.previous = new_prev 
                        new_prev.next = new_next       
                    return
                current = current.previous 
            if not isFound:
                raise ValueError
        if front == False: 
            current = self.start 
            while current != None: 
                if current == target: 
                    isFound = True 
                    if current.previous == None and current.next == None: 
                        self.start = None 
                        self.end = None 
                    elif current.previous == None : 
                        self.start = current.next 
                        current.next.previous = None 
                    elif current.next == None : 
                        current.previous.next = None 
                        self.end = current.previous 
                    else: 
                        new_next  = current.next 
                        new_prev = current.previous 
                        new_next.previous = new_prev #Look at the diagram again 
                        new_prev.next = new_next     
                        current.next = None     
                        current.previous = None  
                    return
                current = current.next #We want this to be the next one now 
            if not isFound:
                raise ValueError

    def isSorted(self, rev):
     if self.start == None or self.start.next == None:
        return True
        
     if rev == False: 
        current = self.start 
        while current.next != None: 
            if current > current.next: 
                return False
            current = current.next
        return True 
        
     if rev == True:
        current = self.start 
        while current.next != None: 
            if current < current.next:
                return False 
            current = current.next 
        return True 

    def sort(self, rev=False): 
        if self.count == 0 or self.count == 1:
            return 
        
        if self.isSorted(rev):
            return 
        
        if rev == False:  
            current = self.start.next
            
            while current != None: 
                next_node = current.next
                prev = current.previous
                
                if current.previous != None:
                    current.previous.next = current.next
                if current.next != None:
                    current.next.previous = current.previous
                else:
                    self.end = current.previous
                
                temp = prev
                while temp != None and current < temp:
                    temp = temp.previous 
                
                if temp == None: 
                    current.next = self.start 
                    current.previous = None
                    self.start.previous = current 
                    self.start = current
                else:
                    current.next = temp.next
                    current.previous = temp
                    if temp.next != None:
                        temp.next.previous = current
                    else:
                        self.end = current
                    temp.next = current
                
                current = next_node 
                
        else: 
            current = self.start.next
            
            while current != None: 
                next_node = current.next
                prev = current.previous
                
                if current.previous != None:
                    current.previous.next = current.next
                if current.next != None:
                    current.next.previous = current.previous
                else:
                    self.end = current.previous
                
                temp = prev
                while temp != None and current > temp:
                    temp = temp.previous 
                
                if temp == None: 
                    current.next = self.start 
                    current.previous = None
                    self.start.previous = current 
                    self.start = current
                else:
                    current.next = temp.next
                    current.previous = temp
                    if temp.next != None:
                        temp.next.previous = current
                    else:
                        self.end = current
                    temp.next = current
                
                current = next_node
        
    # def add_sorted(self, event, rev=False): 
    #     if not isinstance(event, Event):
    #         raise ValueError
    #     if event.next != None and event.previous != None:
    #         raise NotImplementedError
        
    #     self.sort(rev = rev)

    #     if self.count == 0:
    #         self.start = event 
    #         self.end = event 
    #         self.count +=1 
    #         return 

    #     if rev == False and event < self.start : 
    #         event.next = self.start 
    #         self.start.previous = event 
    #         self.start = event 
    #         return 
        
    #     temp = self.start 

    #     while temp != None and event > temp: 
    #             temp = temp.next

    #     if temp != None: 
    #         temp.previous.next = event 
    #         event.previous = temp.previous 
    #         event.next = temp
    #         temp.previous = event 
    #         self.count +=1 
        
    #     else :
    #         event.previous = self.end
    #         self.end.next = event
    #         self.end = event 
    #         self.count +=1 


    def add_sorted(self, event, rev=False):
        if not isinstance(event, Event):
            raise ValueError("Argument must be of type Event")

        if self.count == 0:
            self.add(event)
            return
        current = self.start
        while current:
            if (not rev and event < current) or (rev and event > current):
                if current.previous is None:
                    self.add(event, front=True)
                else:
                    prev = current.previous
                    event.previous = prev
                    event.next = current
                    prev.next = event
                    current.previous = event
                    self.count += 1
                return
            current = current.next

        self.add(event, front=False)


#part of the list is sorted, rest is unsorted--> variable to keep track to see where it ends 
def main():
    e1 = Event("1999-12-25")
    e2 = Event("2005-07-13")
    e3 = Event("2019-04-04")
    e4 = Event("2024-03-04")
    e5=  Event("2004-0222-23")

    t1 = timeline()
    t1.add(e3)
    t1.add(e1)
    t1.add(e2)
    t1.sort()
    t1.add_sorted(e5)
    t1.remove(e1)

    print(t1)
print("HI!")
main()

        
    
    

        
           




    















         


            

        
    



