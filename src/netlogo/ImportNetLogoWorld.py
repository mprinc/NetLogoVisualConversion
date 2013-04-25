import csv;

from text.TextDemultiplexer import TextDemultiplexer;
from netlogo.NetLogoWorld import NetLogoWorld;

class ImportNetLogoWorld(object):
    TYPE_TURTLES = "TURTLES";
    TYPE_LINKS = "LINKS";
    TYPE_PATCHES = "PATCHES";
    #PARAMS_TURTLES = ['who', 'color', 'heading', 'xcor', 'ycor', 'shape', 'label', 'label-color', 'breed', 'hidden?', 'size', 'pen-size', 'pen-mode'];
    #PARAMS_TURTLES_EXTRA = ['popularity', 'calculation_actor_1', 'calculation_actor_2', 'calculation_actor_3'];
    #PARAMS_TURTLES_FORBIDDEN = ['id', 'name'];
    #PARAMS_LINKS_EXTRA = ['calculation_fs_1', 'calculation_fs_2', 'calculation_fs_3', \
    #                      'calculation_fs_1-end1', 'calculation_fs_2-end1', 'calculation_fs_3-end1', \
    #                      'calculation_fs_1-end2', 'calculation_fs_2-end2', 'calculation_fs_3-end2'];
    
    @staticmethod
    def getElementIndexInList(element, list_element):
        try:
            index_element = list_element.index(element)
            return index_element
        except ValueError:
            return -1
        
    def __init__(self):
        print("ImportNetLogoWorld created");
        self.fileNameIn = None;
        self.fileIn = None;
        # sub csv tables names in netlogo wolrd file
        self.streamsNames = [ImportNetLogoWorld.TYPE_TURTLES, ImportNetLogoWorld.TYPE_LINKS, ImportNetLogoWorld.TYPE_PATCHES];
        self.demultiplexingContex = TextDemultiplexer.newDict();
        self.demultiplexingContex['type'] = None;
        self.textDemultiplexer = None;
        self.netLogoWorld = NetLogoWorld();
        self.nParams = None;
        self.eParams = None;

    def importWorld(self, fileNameIn, nParams, eParams):
        self.fileNameIn = fileNameIn;
        self.nParams = nParams;
        self.eParams = eParams;
        print("Importing started ...");
        
        self.fileIn = open(self.fileNameIn);
        self.textDemultiplexer = TextDemultiplexer();
        self.textDemultiplexer.init(self.fileIn, self.streamsNames);
        self.textDemultiplexer.demultiplex(self.demultiplexedLine, self.demultiplexingContex);
        
        self.loadComponents();
        print("Importing finished ...");
        return self.netLogoWorld;

    def splitParams(self, additionalColumns):
        columnNames = [];
        columnTypes =TextDemultiplexer.newDict();
        for columnNameExtra in additionalColumns:
            if(columnNameExtra.find(":") < 0): columnNameExtra += ":string"; 
            (columnName, columnType) = columnNameExtra.split(":");
            columnNames.append(columnName);
            columnTypes[columnName] = columnType;
        return (columnNames, columnTypes);

    def loadComponents(self):
        self.netLogoWorld.empty();
        
        # get turtles from csv table and push them in NetLogo world
        turtleStream = self.textDemultiplexer.getStream(ImportNetLogoWorld.TYPE_TURTLES);
        turtlesReader = csv.DictReader(turtleStream);
        
        (columnNames, columnTypes) = self.splitParams(self.nParams);
        print("Additional node parameters to be imported from NetLogo world (with types): %s" %(self.nParams))
        print("Additional node parameters to be imported from NetLogo world (names): %s, (types): %s" %(columnNames, columnTypes.values()));
        for row in turtlesReader:
            additionalParams = TextDemultiplexer.newDict();
            for columnName in row.keys():
                #if( (0 > ImportNetLogoWorld.getElementIndexInList(columnName, ImportNetLogoWorld.PARAMS_TURTLES)) and \
                #   (0 > ImportNetLogoWorld.getElementIndexInList(columnName, ImportNetLogoWorld.PARAMS_TURTLES_FORBIDDEN))):
                if(0 <= ImportNetLogoWorld.getElementIndexInList(columnName, columnNames) ):
                    additionalParams[columnName] = row[columnName];
                
            self.netLogoWorld.addTurtleParams(row['who'], row['color'], row['heading'], row['xcor'], row['ycor'], row['shape'], row['label'], \
                                              row['label-color'], row['breed'], row['hidden?'], row['size'], row['pen-size'], row['pen-mode'], additionalParams, columnTypes);
        self.netLogoWorld.allTurtlesEntered();
        #print('Turtle 0 :%s' % (str(self.netLogoWorld.turtles[0])));

        # get links from csv table and push them in NetLogo world
        linksStream = self.textDemultiplexer.getStream(ImportNetLogoWorld.TYPE_LINKS);
        linksReader = csv.DictReader(linksStream);
        (columnNames, columnTypes) = self.splitParams(self.eParams);
        print("Additional edge parameters to be imported from NetLogo world (with types): %s" %(self.eParams))
        print("Additional edge parameters to be imported from NetLogo world (names): %s, (types): %s" %(columnNames, columnTypes.values()));
        for row in linksReader:
            additionalParams = TextDemultiplexer.newDict();
            for columnName in row.keys():
                if(0 <= ImportNetLogoWorld.getElementIndexInList(columnName, columnNames) ):
                    additionalParams[columnName] = row[columnName];
                
            self.netLogoWorld.addLinkParams(row['end1'], row['end2'], row['color'], row['label'], row['label-color'], row['hidden?'], row['breed'], \
                                              row['thickness'], row['shape'], row['tie-mode'], additionalParams, columnTypes);
        #print('Link 0 :%s' % (str(self.netLogoWorld.links[0])));
        #print('Link 0->0 :%s' % (str(self.netLogoWorld.linksMatrix[0][0])));
        #print('Link 0->1 :%s' % (str(self.netLogoWorld.linksMatrix[0][1])));
        
        # get patches from csv table and push them in NetLogo world
        patchesStream = self.textDemultiplexer.getStream(ImportNetLogoWorld.TYPE_PATCHES);
        patchesReader = csv.DictReader(patchesStream);
        for row in patchesReader:
            self.netLogoWorld.addPatchParams(row['pxcor'], row['pycor'], row['pcolor'], row['plabel'], row['plabel-color']);
        self.netLogoWorld.allPatchesEntered();
        #print('Patch 0 :%s' % (str(self.netLogoWorld.patches[0])));
        #print('Patch 0,0 :%s' % (str(self.netLogoWorld.patchesMatrix[0][0])));
        #print('Patch 50,-49 :%s' % (str(self.netLogoWorld.patchesMatrix[50][-49])));
        #print('Patch -50,49 :%s' % (str(self.netLogoWorld.patchesMatrix[-50][49])));
        #print('Patch -50,-50 :%s' % (str(self.netLogoWorld.patchesMatrix[-50][-50])));
        #print('Patch 50,50 :%s' % (str(self.netLogoWorld.patchesMatrix[50][50])));

    # =============
    # demuplexing netlogo world file that consists of few inner csv table
    # separated by empty line and then with the name of inner csv table (turtles, ...)
    # after the name we have csv table rows
    def demultiplexedLine(self, line, context):
        # if you check the netlogo-world csv export file you will see that before particular infile csv part there is an empty line 
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
            #print "Context switched to: %s" % (context['type'] );
        
        # print line;
        #print "DemultiplexedLine finished..."
        # this directs demultiplexter which stream to put the line: stream name is equal to the value of context['type']
        return context['type'];
