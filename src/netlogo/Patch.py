class Patch(object):

    def __init__(self):
        #print("Patch created");
        self.pxcor = None;
        self.pycor = None;
        self.pcolor = None;
        self.plabel = None;
        self.plabelColor = None;
    
    # readable version
    def __str__(self):
        return "Patch pxcor=%s pycor=%s pcolor=%s plabel=%s plabelColor=%s" % (self.pxcor, self.pycor, self.pcolor, self.plabel, self.plabelColor);

    # representation version
    def __repr__(self):
        return 'Patch(%s, %s %s, "%s")' % (self.pxcor, self.pycor, self.pcolor, self.plabel)