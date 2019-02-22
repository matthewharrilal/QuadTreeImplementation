from point import Point

class Region(object):
    def __init__(self, x, y, points_collection=None): # User passes in an array of points that they want
        # Center point in which the sub quadrants are based off of
        self.center = Point(x, y)
        
        self.capacity = 0 # Represents counter for when to subdivide

        self.children = []  # List of 0 or 4 Region objects that are children of this Region


        # What does this mean? For each point in the point collection we insert, recursively finding the region that we can contain the point to 
        if len(points_collection) > 0:
            for point in points_collection:
                self.insert(point)

    def region_index(self, point):
        '''Return an index in range [0...3] (0: NW, 1: NE, 2: SE, 3: SW) that specifies which
        subregion (child) the given point belongs to relative to this region's center.'''

        # Not handling edge case where data lies directly on the axis
        if point.x < self.center.x and point.y > self.center.y:
            return 0 # Representing the Northwest region

        elif point.x > self.center.x and point.y > self.center.y:
            return 1 # Representing NE region

        elif point.x > self.center.x and point.y < self.center.y:
            return 2 # Representing the SE region

        elif point.x < self.center.x and point.y < self.center.y:
            return 3 # Representing the southwest region 

    def contains(self, point):
        '''Returns true if point is contained inside given region'''
        pass

    def insert(self, point, region=None, quadrant=None):

        '''Inserts point inside region that contains that coordinate space'''
        # TODO: Find quadrant that the point lies in
        # TODO: Find insert then check if it is at capacity ... if so then subdivide which reogranizes those nodes into the correct regions
        if quadrant is None and region is None:
            region = self

            # You only have a quadrant when you subdivide though
            quadrant = region.region_index(point) # Find the initial region
            

        if region.capacity > 0: # Meaning that we have to keep subdividing
            # Do we insert that subdivide

            region.subdivide() # Subdivide into four different quadrants 

            # Already have region subchildren at this time ... then find position of quadrant to be able to subscript
            quadrant = region.region_index(point)
            self.insert(point, region.children[quadrant])

        return region # Return region that the point is finally inserted to ... proper return statement
        
    

        # Check if this region node is over capacity, and if so call subdivide

    def subdivide(self):
        '''Splits the region into 4 separate quadrants based of center point of the region'''
        # Can do so by updating the center of the children region objects to be half the region's x and y coordinate

        # Northwest Region
        self.children[0] = Region(self.center.x // 2, self.center.y // 2)

        # Northeast Region
        self.children[1] = Region((self.center.y + self.center.x // 2), (self.center.y + self.center.y // 2))

        # Southeast region
        self.children[2] = Region((self.center.x + self.center.x // 2), self.center.y // 2)

        # Southwest region
        self.children[3] = Region(self.center.x // 2, self.center.y // 2)

        # create 4 region quadrants and append to self.children
        