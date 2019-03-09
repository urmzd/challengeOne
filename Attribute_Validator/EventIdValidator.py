from bloom_filter import BloomFilter as bloom
import csv


class EventValidator:

    bloom = bloomFilter
    last = -1;
    current = -1;

    def __init__(self, values):
        self.values = values

    def checkOrder(self, value):
        
        if (last == current and last == -1) :
            last = value
        else:
            current = value;
            if (last > current) :
                print("Error")
            else :
                last = current
