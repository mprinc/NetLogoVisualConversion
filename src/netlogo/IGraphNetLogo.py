# extra deendencies
import igraph;

class IGraphNetLogo(object):

    def __init__(self):
        print("iGraphNetLogo created");
        self.fileNameOut = None;
        self.graph = None;

    def generateGraph(self):
        print("Generating graph started ...");
        print "Igraph version %s" % (igraph.__version__);
        self.graph = igraph.Graph();
        #self.graph.add_vertices(3);
        #self.graph.add_edges([(0,1), (1,2)]);
        igraph.summary(self.graph);
        #self.graph.write_graphml("data/examples/Gephi/iGraph exported - People.graphml")
        print("Generating graph finished ...");

    def testCreateSaveGraph(self, fileNameOut):
        print("testCreateSaveGraph started ...");
        print "Igraph version %s" % (igraph.__version__);
        self.graph = igraph.Graph();
        self.graph.add_vertices(3);
        self.graph.add_edges([(0,1), (1,2)]);
        self.graph.vs['id'] = [5, 7, 9];
        self.graph.vs['size'] = [50, 30, 40];
        self.graph.vs['r'] = [255, 255, 0];
        self.graph.vs['g'] = [0, 0, 0];
        self.graph.vs['b'] = [0, 0, 255];
        self.graph.vs['x'] = [0, 100, 100];
        self.graph.vs['y'] = [0, 0, 100];
        self.graph.vs['label'] = ["Nada", "Zhenia", "Sasha"];

        self.graph.es['Edge Id'] = [57, 79];
        self.graph.es['Edge Label'] = ['Nada-Zhenia', 'Zhenia-Sasha'];
        self.graph.es['label'] = ['Nada-Zhenia-l', 'Zhenia-Sasha-l'];
        self.graph.es['weight'] = [1, 5];

        igraph.summary(self.graph);
        self.graph.write_graphml(fileNameOut);
        print("testCreateSaveGraph finished ...");

    def testLoadSaveGraph(self, fileNameIn, fileNameOut):
        print("testLoadSaveGraph started ...");
        print "Igraph version %s" % (igraph.__version__);
        self.graph = igraph.Graph.Read_GraphML(fileNameIn);
        print("node parameters(%s): %s" %('id', self.graph.vs['id']));
        print("node parameters(%s): %s" %('label', self.graph.vs['label']));
        print("edge parameters(%s): %s" %('Edge Id', self.graph.es['Edge Id']));
        print("edge parameters(%s): %s" %('Edge Label', self.graph.es['Edge Label']));
        print("edge parameters(%s): %s" %('weight', self.graph.es['weight']));
        print("edge parameters(edge %d): %s" %(0, self.graph.es[0]));
        
        # fixing edge label
        self.graph.es['label'] = self.graph.es['Edge Label'];
        
        igraph.summary(self.graph);
        self.graph.write_graphml(fileNameOut);
        print("testLoadSaveGraph finished ...");