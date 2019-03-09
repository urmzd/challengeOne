from bloom_filter import BloomFilter
import csv


class EventValidator:

    last = -1
    current = -1
    bloom = BloomFilter(4980000, 0.01)

    def __init__(self):
        self

    def checkOrder(self, value):

        if self.last == -1:
            self.last = value
        else:
            self.current = value
            if self.last > self.current:
                print("Value @ %d is not in ASCENDING ORDER = %d" % self.current)
            else:
                self.last = self.current
 
    def checkUnique(self, value):

        inside = value in self.bloom

        if inside:
            print("Value @ %s is not UNIQUE" % (value))
        else:
            self.bloom.add(value)


def main():

    event = EventValidator()

    with open("catalog_incorrect.csv", encoding="UTF8") as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        for col in reader:
            try:
                event.checkUnique(col[0])
                event.checkOrder(int(col[0]))
            except:
                pass

if __name__ == "__main__":
    main()
