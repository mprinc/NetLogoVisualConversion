from __future__ import division

import re
import math;

from Turtle import Turtle;
from Link import Link;
from Patch import Patch;

class NetLogoWorld(object):

    COLORS = [
        [141, 141, 141],
        [215, 50, 41],
        [241, 106, 21],
        [157, 110, 72],
        [237, 237, 49],
        [89, 176, 60],
        [44, 209, 59],
        [29, 159, 120],
        [84, 196, 196],
        [45, 141, 190],
        [52, 93, 169],
        [124, 80, 164],
        [167, 27, 106],
        [224, 127, 150] 
    ];

    @staticmethod
    def colorNetlotoToRgb(netlogoColor):
        colorIndex = int(math.floor(netlogoColor/10));
        colorRgbMiddle = NetLogoWorld.COLORS[colorIndex];
        netLogoColorOffset = netlogoColor - (colorIndex*10.0+5.0);
        colorRgb = [];
        if(netLogoColorOffset < 0):
            colorCoef = 1.0 + netLogoColorOffset/5.0;
            colorRgb = [color*colorCoef for color in colorRgbMiddle];
        else:
            colorCoef = netLogoColorOffset/5.0;
            colorRgb = [color + (255-color)*colorCoef for color in colorRgbMiddle];
            
        #print ("netlogoColor=%f, colorIndex=%d, netLogoColorOffset=%f, colorRgb=%s" % (netlogoColor, colorIndex, netLogoColorOffset, str(colorRgb)));
        return colorRgbMiddle;

    def __init__(self):
        print("NetLogo created");
        self.turtles = [];
        self.links = [];
        self.patches = [];
        self.maxTurtleWho = 0;
        self.linksMatrix = [];
        self.patchesMatrix = [];
        self.minPatchX = 0;
        self.maxPatchX = 0;
        self.minPatchY = 0;
        self.maxPatchY = 0;

    def empty(self):
        self.turtles = [];
        self.links = [];
        self.patches = [];
        self.maxTurtleWho = 0;
        self.linksMatrix = [];
        # row first (y), then column (x)
        self.patchesMatrix = [];

    def addTurtle(self, turtle):
        self.turtles.append(turtle);
        if(self.maxTurtleWho < turtle.who):
            self.maxTurtleWho = turtle.who;
        return turtle;

    def addTurtleParams(self, who, color, heading, xcor, ycor, shape, label, labelColor, breed, isHidden, size, penSize, penMode, additionalParams):
        rex_string = re.compile(r'\"(.*)\"');

        turtle = Turtle();
        turtle.who = int(who);
        turtle.color = float(color);
        turtle.heading = heading;
        turtle.xcor = float(xcor);
        turtle.ycor = float(ycor);
        
        turtle.additionalParams = additionalParams;

        match = rex_string.search(shape);
        if(match != None): turtle.shape = match.group(1);
        else: turtle.shape = shape;

        match = rex_string.search(label);
        if(match != None): turtle.label = match.group(1);
        else: turtle.label = label;

        turtle.labelColor = float(labelColor);
        turtle.breed = breed;
        turtle.isHidden = isHidden == 'true';
        turtle.size = float(size);
        turtle.penSize = float(penSize);

        match = rex_string.search(penMode);
        if(match != None): turtle.penMode = match.group(1);
        else: turtle.penMode = penMode;
        
        self.addTurtle(turtle);
        return turtle;

    def allTurtlesEntered(self):
        self.linksMatrix = [None]*(self.maxTurtleWho+1);
        for i in range(self.maxTurtleWho+1):
            self.linksMatrix[i] = [None]*(self.maxTurtleWho+1);

    def addLink(self, link):
        self.links.append(link);
        self.linksMatrix[link.end1][link.end2] = link;
        return link;
    
    def addLinkParams(self, end1, end2, color, label, labelColor, isHidden, breed, thickness, shape, tieMode, additionalParams):
        link = Link();
        rex_who = re.compile(r'\{\S*\s+(\d+)\}');

        rex_string = re.compile(r'\"(.*)\"');

        match = rex_who.search(end1);
        if(match != None): link.end1 = int(match.group(1));
        else: link.end1 = int(end1);

        match = rex_who.search(end2);
        if(match != None): link.end2 = int(match.group(1));
        else: link.end2 = int(end2);
        
        link.color = float(color);
        link.additionalParams = additionalParams;

        match = rex_string.search(label);
        if(match != None): link.label = match.group(1);
        else: link.label = label;

        link.labelColor = float(labelColor);
        link.isHidden = isHidden == 'true';
        link.breed = breed;
        link.thickness = float(thickness);

        match = rex_string.search(shape);
        if(match != None): link.shape = match.group(1);
        else: link.shape = shape;

        match = rex_string.search(tieMode);
        if(match != None): link.tieMode = match.group(1);
        else: link.tieMode = tieMode;
        
        self.addLink(link);
        return link;

    def addPatch(self, patch):
        self.patches.append(patch);
        if(self.minPatchX > patch.pxcor):
            self.minPatchX = patch.pxcor;
        if(self.maxPatchX < patch.pxcor):
            self.maxPatchX = patch.pxcor;
        if(self.minPatchY > patch.pycor):
            self.minPatchY = patch.pycor;
        if(self.maxPatchY < patch.pycor):
            self.maxPatchY = patch.pycor;
        return patch;
    
    def addPatchParams(self, pxcor, pycor, pcolor, plabel, plabelColor):
        rex_string = re.compile(r'\"(.*)\"');

        patch = Patch();
        patch.pxcor = int(pxcor);
        patch.pycor = int(pycor);
        patch.pcolor = float(pcolor);

        match = rex_string.search(plabel);
        if(match != None): patch.plabel = match.group(1);
        else: patch.plabel = plabel;

        patch.plabelColor = float(plabelColor);
        
        self.addPatch(patch);
        return patch;

    def allPatchesEntered(self):
        self.patchesMatrix = [None]*(abs(self.minPatchY)+1+self.maxPatchY);
        for i in range(abs(self.minPatchY)+1+self.maxPatchY):
            self.patchesMatrix[i] = [None]*(abs(self.minPatchX)+1+self.maxPatchX);
        for patch in self.patches:
            self.patchesMatrix[patch.pycor][patch.pxcor] = patch;