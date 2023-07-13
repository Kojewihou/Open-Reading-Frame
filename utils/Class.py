# No Gobal Imports

# No Local Imports

class ORF():
    def __init__(self, start, end, seq, reverse=False) -> None:
        self.start = start
        self.end = end
        self.sequence = seq
        self.length = end-start
        self.frame = start%3
        self.reversed = reverse
