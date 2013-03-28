import sys;
from collections import defaultdict;

from StringLinesIterator import StringLinesIterator;

class TextDemultiplexer(object):
    @staticmethod
    def newDict():
        return defaultdict(TextDemultiplexer.newDict);

    def __init__(self):
        print("TextDemultiplexer created");
        self.readStream = None;
        self.parseCallbackFunc = None;
        self.streamsNames = [];
        self.streams = TextDemultiplexer.newDict();

    def init(self, readStream, streamsNames):
        self.readStream = readStream;
        self.streamsNames = streamsNames;
        self.parseCallbackFunc = None;
        self.parseCallbackContext = None;

        print("Init started ...");
        for streamsName in self.streamsNames:
            self.streams[streamsName] = StringLinesIterator();
        
        print("Init finished ...");

    def getStream(self, streamName):
        if(self.streams.has_key(streamName)):
            return self.streams[streamName];
        else: return None;

    def demultiplex(self, parseCallbackFunc, parseCallbackContext):
        print("Demultiplexing started ...");
        self.parseCallbackFunc = parseCallbackFunc;
        self.parseCallbackContext = parseCallbackContext;

        self.error = False;
        try:
            lineNo = 1;
            for line in self.readStream:
                line = line.rstrip("\r\n");
                # debugging
                lineDebug = "Line [%d]: %s\n" % (lineNo, line);
                # sys.stdout.write(lineDebug);
                
                streamName = self.parseCallbackFunc(line, self.parseCallbackContext);
                if(self.streams.has_key(streamName)):
                    self.streams[streamName].addLine(line);

                lineNo = lineNo+1;
        finally:
            self.error = True;
        print("Demultiplexing finished ...");
