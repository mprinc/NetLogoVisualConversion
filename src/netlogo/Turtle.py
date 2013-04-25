from text.TextDemultiplexer import TextDemultiplexer
class Turtle(object):

    def __init__(self):
        #print("Turtle created");
        self.who = None;
        self.color = None;
        self.heading = None;
        self.xcor = None;
        self.ycor = None;
        self.shape = None;
        self.label = None;
        self.labelColor = None;
        self.breed = None;
        self.isHidden = None;
        self.size = None;
        self.penSize = None;
        self.penMode = None;
        self.additionalParams = TextDemultiplexer.newDict();
        self.columnTypes = TextDemultiplexer.newDict();
    
    # readable version
    def __str__(self):
        return "Turtle who=%s color=%s heading=%s xcor=%s ycor=%s shape=%s label=%s labelColor=%s breed=%s isHidden=%s size=%s penSize=%s penMode=%s" % (self.who, self.color, self.heading, self.xcor, self.ycor, \
                                                                                                                                               self.shape, self.label, self.labelColor, self.breed, \
                                                                                                                                               self.isHidden, self.size, self.penSize, self.penMode);

    # representation version
    def __repr__(self):
        return 'Turtle(%s, %s, %s, "%s", "%s")' % (self.who, self.xcor, self.ycor, self.label, self.breed)