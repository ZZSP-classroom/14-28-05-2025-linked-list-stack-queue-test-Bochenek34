import unittest
from support_ticket import *

class TestSupportTicket(unittest.TestCase):

    def setUp(self):
        self.ticket1 = Ticket(1, "issue1")
        self.ticket2 = Ticket(2, "issue2")
        self.ticket3 = Ticket(3, "issue3")

        self.queue = Queue()
        self.stack = Stack()

        self.queue.enqueue(self.ticket1)
        self.queue.enqueue(self.ticket2)
        self.queue.enqueue(self.ticket3)

    def test_enqueue_order(self):
        self.assertEqual(self.queue.items[0], self.ticket1)
        self.assertEqual(self.queue.items[1], self.ticket2)

    def test_transfer_to_stack(self):
        ticket = self.queue.dequeue()
        self.stack.push(ticket)
        self.assertEqual(self.stack.peek(), self.ticket1)



if __name__ == "__main__":
    unittest.main()