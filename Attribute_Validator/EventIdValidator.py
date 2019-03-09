from bloom_filter import BloomFilter as bloom
import csv


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

    with open("catalog_incorrect.csv", encoding="UTF8") as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        for col in reader:
            try:
                value = int(col[0])
                event.checkOrder(value)
            except:
                pass

if __name__ == "__main__":
    main()
