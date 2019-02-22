from point import Point

class Region(object):
    def __init__(self, x_coordinate, y_coordinate, width, height, points_collection=None): # User passes in an array of points that they want
        # Center point in which the sub quadrants are based off of
        self.center = Point(x_coordinate, y_coordinate)
        
        self.width = width
        self.height = height
        self.capacity = 0 # Represents counter for when to subdivide

        self.children = []  # List of 0 or 4 Region objects that are children of this Region


        # What does this mean? For each point in the point collection we insert, recursively finding the region that we can contain the point to 
        if len(points_collection) > 0:
            for point in points_collection:
                self.insert(point)

    def region_index(self, point):
        '''Return an index in range [0...3] (0: NW, 1: NE, 2: SE, 3: SW) that specifies which
        subregion (child) the given point belongs to relative to this region's center.'''
        pass

    def contains(self, point):
        '''Returns true if point is contained inside given region'''
        pass

    def insert(self, point):
        '''Inserts point inside region that contains that coordinate space'''

        # recursive has to find region it can populate

        # check if the given point relative to this region's center is northwest
        # region_index = self.region_index(point)  # 0: NW, 1: NE, 2: SE, 3: SW

        # Check if region contains point if true then you can insert
        pass

        # Check if this region node is over capacity, and if so call subdivide

    def subdivide(self, region):
        '''Splits the region into 4 separate quadrants based of center point of the region'''
        

        # create 4 region quadrants and append to self.children
        pass