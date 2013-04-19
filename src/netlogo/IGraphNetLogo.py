from __future__ import division

# extra deendencies
import igraph;

from netlogo.NetLogoWorld import NetLogoWorld;
from netlogo.Turtle import Turtle;
from netlogo.Link import Link;

class IGraphNetLogo(object):

    def __init__(self):
        print("iGraphNetLogo created");
        self.fileNameOut = None;
        # we need to initialize here just to trick IDE (Eclipse) to associate variable with appropriate class
        self.netLogoWorld = NetLogoWorld();
        self.graph = None;

    def generateGraph(self, netLogoWorld, fileNameOut, nodeSizeMultiplyer, coordMultiplyer, edgeWeightMultiplyer, edgeWeightIgnore, nodeNamePrefix):
        self.netLogoWorld = netLogoWorld;
        self.fileNameOut = fileNameOut;
        print("Generating graph started ...");
        print("nodeSizeMultiplyer=%f, coordMultiplyer=%f, edgeWeightMultiplyer=%f, edgeWeightIgnore=%s, , nodeNamePrefix='%s'" \
              % (nodeSizeMultiplyer, coordMultiplyer, edgeWeightMultiplyer, edgeWeightIgnore, nodeNamePrefix))
        print "Igraph version %s" % (igraph.__version__);
        self.graph = igraph.Graph();

        # populating graph nodes from turtles
        self.graph.add_vertices(len(self.netLogoWorld.turtles));
        turtle = Turtle();
        i = 0;
        for turtle in self.netLogoWorld.turtles:            
            self.graph.vs[i]['id'] = turtle.who;
            self.graph.vs[i]['size'] = turtle.size * nodeSizeMultiplyer;
            rgbColor = NetLogoWorld.colorNetlotoToRgb(turtle.color);
            self.graph.vs[i]['r'] = rgbColor[0];
            self.graph.vs[i]['g'] = rgbColor[1];
            self.graph.vs[i]['b'] = rgbColor[2];
            self.graph.vs[i]['x'] = turtle.xcor * coordMultiplyer;
            self.graph.vs[i]['y'] = turtle.ycor * coordMultiplyer;
            if(turtle.label == None or turtle.label == ""):
                self.graph.vs[i]['label'] = "%s%d" % (nodeNamePrefix, turtle.who);
            else:
                self.graph.vs[i]['label'] = turtle.label;

            i =i+1;

        # populating edges nodes from links
        link = Link();
        i = 0;
        for link in self.netLogoWorld.links:            
            self.graph.add_edges([(link.end1, link.end2)]);
            self.graph.es[i]['Edge Id'] = link.end1 * 1000 + link.end2;
            if(link.label == None or link.label == ""):
                self.graph.es[i]['Edge Label'] = self.graph.es[i]['label'] = "%d-%d" % (link.end1, link.end2);
            else:
                self.graph.es[i]['Edge Label'] = self.graph.es[i]['label'] = turtle.label;
            if(not edgeWeightIgnore):
                self.graph.es[i]['weight'] = link.thickness*edgeWeightMultiplyer;
            i =i+1;

        igraph.summary(self.graph);
        self.graph.write_graphml(fileNameOut);
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