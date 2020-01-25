# csv validator
csv validator for AnalyzeRe Hackathon

# DESIGN:

1. Create seperate modules so different file types can still be validated.
2. Read in a file, read the headers and determine what modules to use.
3. Use the appropriate modules to validate the file and return output.

# NOTES:

1. The Bloom Filter is a probabilitisic data structure used to determine whether an element exists within the set. In this case, its used to determine whether all elements of the ID column are unique. Reduced time from ~5 minutes (Naive Method) to ~30 seconds (Using the Bloom Filter).
