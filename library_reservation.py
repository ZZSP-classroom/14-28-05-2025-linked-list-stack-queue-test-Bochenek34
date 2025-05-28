class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, reservation):
        self.items.append(reservation)
        
    def dequeue(self):
        return self.items.pop(0)
        

    def peek(self):
        if not self.items:
            return self.items[0]
        return None
    
    def remove_reservation(self, user_name, book_title):
        for i, res in enumerate(self.items):
            if res.user_name == user_name and res.book_title == book_title:
                return self.items.pop(i)
            raise ValueError("Reservation not found")
        
    def __repr__(self):
        return "\n".join([str(item) for item in self.items])
   


class Reservation:
    def __init__(self, user_name, book_title):
        self.user_name = user_name
        self.book_title = book_title

    def __repr__(self):
        return self.user_name
    

        
    