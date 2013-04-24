class Link(object):

    def __init__(self):
        #print("Link created");
        self.end1 = None;
        self.end2 = None;
        self.color = None;
        self.label = None;
        self.labelColor = None;
        self.isHidden = None;
        self.breed = None;
        self.thickness = None;
        self.shape = None;
        self.tieMode = None;
        self.additionalParams = None;
    
    # readable version
    def __str__(self):
        return "Link end1=%s end2=%s color=%s label=%s labelColor=%s isHidden=%s breed=%s thickness=%s shape=%s tieMode=%s" \
            % (self.end1, self.end2, self.color, self.label, self.labelColor, self.isHidden, self.breed, self.thickness, self.shape, self.tieMode);

    # representation version
    def __repr__(self):
        return 'Link(%s, %s, "%s", "%s")' % (self.end1, self.end2, self.label, self.breed)
