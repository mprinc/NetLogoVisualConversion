import csv;

from text.TextDemultiplexer import TextDemultiplexer;
 
class ImportNetLogoWorld(object):
    TYPE_TURTLES = "TURTLES";
    TYPE_LINKS = "LINKS";
    TYPE_PATCHES = "PATCHES";

    def __init__(self):
        print("ImportNetLogoWorld created");
        self.fileNameIn = None;
        self.fileIn = None;
        self.streamsNames = [ImportNetLogoWorld.TYPE_TURTLES, ImportNetLogoWorld.TYPE_LINKS, ImportNetLogoWorld.TYPE_PATCHES];
        self.demultiplexingContex = TextDemultiplexer.newDict();
        self.demultiplexingContex['type'] = None;
        self.textDemultiplexer = None;

    def importWorld(self, fileNameIn):
        self.fileNameIn = fileNameIn;
        print("Importing started ...");
        
        self.fileIn = open(self.fileNameIn);
        self.textDemultiplexer = TextDemultiplexer();
        self.textDemultiplexer.init(self.fileIn, self.streamsNames);
        self.textDemultiplexer.demultiplex(self.demultiplexedLine, self.demultiplexingContex);
        
        self.loadComponents();
        print("Importing finished ...");

    def loadComponents(self):
        turtleStream = self.textDemultiplexer.getStream(ImportNetLogoWorld.TYPE_TURTLES);
        
        #for line in turtleStream:
        #    print line;
        
        #turtlesReader = csv.reader(turtleStream);
        #for row in turtlesReader:
        #    print "who: %s, color: %s" % (row[0], row[1]);

        turtlesReader = csv.DictReader(turtleStream);
        for row in turtlesReader:
            print "who: %s, color: %s" % (row['who'], row['color']);

        linksStream = self.textDemultiplexer.getStream(ImportNetLogoWorld.TYPE_LINKS);
        linksReader = csv.DictReader(linksStream);
        for row in linksReader:
            print "end1: %s, end2: %s, color: %s" % (row['end1'], row['end2'], row['color']);
        
        patchesStream = self.textDemultiplexer.getStream(ImportNetLogoWorld.TYPE_PATCHES);
        patchesReader = csv.DictReader(patchesStream);
        for row in patchesReader:
            print "pxcor: %s, pycor: %s, pcolor: %s" % (row['pxcor'], row['pycor'], row['pcolor']);
        
    def demultiplexedLine(self, line, context):
        #print "DemultiplexedLine started..."
        if(context['type'] == None):
            if(line == ('"'+ImportNetLogoWorld.TYPE_TURTLES+'"')):
                context['type'] = ImportNetLogoWorld.TYPE_TURTLES;
                print "Context switched to: %s" % (context['type'] );
                return None;
            elif(line == ('"'+ImportNetLogoWorld.TYPE_LINKS+'"')):
                context['type'] = ImportNetLogoWorld.TYPE_LINKS;
                print "Context switched to: %s" % (context['type'] );
                return None;
            elif(line == ('"'+ImportNetLogoWorld.TYPE_PATCHES+'"')):
                context['type'] = ImportNetLogoWorld.TYPE_PATCHES;
                print "Context switched to: %s" % (context['type'] );
                return None;
        if(line == '' and context['type']):
            context['type'] = None;
            print "Context switched to: %s" % (context['type'] );
        
        # print line;
        #print "DemultiplexedLine finished..."
        # direct demultiplexter to put line to stream identified by the value of context['type']
        return context['type'];
