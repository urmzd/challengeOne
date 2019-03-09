from bloom_filter import BloomFilter as bloom


class EventValidator:

    last = -1
    current = -1

    def __init__(self):
        self.last = -1
        self.current = -1

    def checkOrder(self, value):

        if self.last == -1:
            self.last = value
        else:
            self.current = value
            if self.last > self.current:
                print("Error @ EventID = %d" % self.current)
            else:
                self.last = self.current

def main():

    event = EventValidator()

    event.checkOrder(1)
    event.checkOrder(0)
    event.checkOrder(2)
    event.checkOrder(0)
    print("hello")
