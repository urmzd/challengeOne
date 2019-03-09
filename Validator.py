# Shiftkey Labs
# Challenge One: CSV Validator

import csv
from bloom_filter import BloomFilter as bloom


class Validator:

    def __init__(self, foo, foo2):

        self.foo = foo
        self.foo2 = foo2

    def checkHeader(self, header):
        self.header = header
