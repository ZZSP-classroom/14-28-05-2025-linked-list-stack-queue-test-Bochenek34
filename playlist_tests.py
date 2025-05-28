import unittest
from library_reservation import *

class TestReservationQueue(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()
        self.res1 = Reservation("Oski", "book1")
        self.res2 = Reservation("Marek", "book2")
        self.res3 = Reservation("Szymon", "book3")
        self.queue.enqueue(self.res1)
        self.queue.enqueue(self.res2)
        self.queue.enqueue(self.res3)

    def test_enqueue_order(self):
        self.assertEqual(self.queue.items, [self.res1, self.res2, self.res3])

    def test_dequeue(self):
        removed = self.queue.dequeue()
        self.assertEqual(removed, self.res1)
        self.assertEqual(self.queue.items, [self.res2, self.res3])



if __name__ == "__main__":
    unittest.main()