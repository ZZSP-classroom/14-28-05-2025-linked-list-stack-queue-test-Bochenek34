class Ticket:
    def __init__(self, ticket_id, issue_description):
        self.ticket_id = ticket_id
        self.issue_description = issue_description

    def __repr__(self):
        return f"Ticket({self.ticket_id}:{self.issue_description})"
    
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
        
    def dequeue(self):
        return self.items.pop(0)
        

    def peek(self):
        
        return self.items[0]
       
        
    def __repr__(self):
        return "\n".join([str(item) for item in self.items])


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
        
    def peek(self):
        return self.items[-1]
    
    def __repr__(self):
        return "\n".join(self.items)
