from bloom_filter import BloomFilter
import csv


class EventValidator:

    last = -1
    current = -1
    bloom = BloomFilter(4980000, 0.01)

    orderErrors = []
    uniqueErrors = []

    def __init__(self):
        self

    def checkOrder(self, value):

        if self.last == -1:
            self.last = value
        else:
            self.current = value
            if self.last > self.current:
                self.orderErrors.append(self.current)
            else:
                self.last = self.current

    def checkUnique(self, value):

        inside = value in self.bloom

        if inside:
            self.uniqueErrors.append(value)
        else:
            self.bloom.add(value)


def main():

    event = EventValidator()

    with open("catalog_incorrect.csv", encoding="UTF8") as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        for header in reader:
            try:
                event.checkUnique(header[0])
                event.checkOrder(int(header[0]))
            except:
                pass

    print("ERROR! Values not in order: ")
    for elem in event.orderErrors:
        print(elem)

    print()  # Print new line.

    print("ERROR! Values not unique: ")
    for elem in event.uniqueErrors:
        print(elem)


if __name__ == "__main__":
    main()
