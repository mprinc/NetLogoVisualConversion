import sys;
from collections import defaultdict;

def new_dict(): return defaultdict(new_dict)

class StringLinesIterator(object):
    def __init__(self):
        #print("StringLinesIterator created");
        self.lines = [];
        self.lineIndex = -1;

    def addLine(self, line):
        self.lines.append(line);
        
    def __iter__(self):
        # reset iterator
        self.lineIndex = -1;
        return self;

    def next(self):
        self.lineIndex = self.lineIndex + 1;
        if self.lineIndex >= len(self.lines):
            raise StopIteration;
        return self.lines[self.lineIndex];

