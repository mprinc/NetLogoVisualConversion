#!/usr/bin/python

# Necessary to avoid rounding on integer numbers
from __future__ import division

import argparse;

from netlogo.ImportNetLogoWorld import ImportNetLogoWorld;
from netlogo.IGraphNetLogo import IGraphNetLogo;

print("Converting NetLogo World file started ...");
print("Converting NetLogo World file finished");

parser = argparse.ArgumentParser(description='NetLogo World to Graph file conversion (Sasha Mile Rudan @ HeadsWare)');
parser.add_argument('--phase', '-p', action='store',help='Phase of conversion', default='convert');
parser.add_argument('--filein', '-fin', action='store',help='Input file name');
parser.add_argument('--fileout', '-fout', action='store',help='Output file name');
parser.add_argument('--node_size_multiplyer', '-nsize', action='store',help='Node Size Multiplyer');
parser.add_argument('--edge_weight_multiplyer', '-eweight', action='store',help='Edge Weight Multiplyer');
parser.add_argument('--edge_weight_ignore', '-ewign', action='store',help='Ignore Edge Weight (do not set it at all)');
parser.add_argument('--coord_multiplyer', '-coord', action='store',help='Coordinate Multiplyer');
parser.add_argument('--node-name-prefix', '-nname', action='store',help='Node Name Prefix (added to the who parameter of turle');
args = parser.parse_args();

if not args.phase:
    print "ERROR: You should provide a --phase parameter\n";
    parser.print_help();
    exit(0);
print("Phase: " + args.phase);

if(args.phase == 'convert'):
    if(not args.filein):
        print "ERROR: You should provide --filein parameter\n";
        exit(0);

    if(not args.fileout):
        print "ERROR: You should provide --fileout parameter\n";
        exit(0);
    
    nodeSizeMultiplyer = 1.0;
    if(args.node_size_multiplyer):
        nodeSizeMultiplyer = float(args.node_size_multiplyer);
        
    coordMultiplyer = 1.0;
    if(args.coord_multiplyer):
        coordMultiplyer = float(args.coord_multiplyer);
        
    edgeWeightMultiplyer = 1.0;
    if(args.edge_weight_multiplyer):
        edgeWeightMultiplyer = float(args.edge_weight_multiplyer);
        
    edgeWeightIgnore = False;
    if(args.edge_weight_ignore):
        edgeWeightIgnore = True;
        
    nodeNamePrefix = "";
    if(args.node_name_prefix):
        nodeNamePrefix = args.node_name_prefix;

    # creating NetLogo world importer
    importNetLogoWorld = ImportNetLogoWorld();
    # importing wolrd from file
    print("Graph is about to be imported from file: %s" % (args.filein));
    netLogoWorld = importNetLogoWorld.importWorld(args.filein);

    # creating component for exporting NetLogo to graph document
    iGraphNetLogo = IGraphNetLogo();
    
    # testing: loading graph file and saving it back to another file
    #iGraphNetLogo.testLoadSaveGraph("data/examples/Gephi/People.graphml", "data/examples/Gephi/iGraph exported - People.graphml");
    
    # testing: creating a new graph and saving it back to another file
    # iGraphNetLogo.testCreateSaveGraph("data/examples/Gephi/iGraph exported - Test.graphml");
    iGraphNetLogo.generateGraph(netLogoWorld, args.fileout, nodeSizeMultiplyer, coordMultiplyer, edgeWeightMultiplyer, edgeWeightIgnore, nodeNamePrefix);
    print("Graph is written to file: %s" % (args.fileout));