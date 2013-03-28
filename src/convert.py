#!/usr/bin/python

# Necessary to avoid rounding on integer numbers
from __future__ import division

import argparse;

from netlogo.ImportNetLogoWorld import ImportNetLogoWorld

print("Converting NetLogo World file started ...");
print("Converting NetLogo World file finished");

parser = argparse.ArgumentParser(description='NetLogo World to Graph file conversion (Sasha Mile Rudan @ HeadsWare)');
parser.add_argument('--phase', '-p', action='store',help='Phase of conversion', default='convert');
parser.add_argument('--filein', '-fin', action='store',help='Input file name');
parser.add_argument('--fileout', '-fout', action='store',help='Output file name');
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
        
    importNetLogoWorld = ImportNetLogoWorld();
    importNetLogoWorld.importWorld(args.filein);
