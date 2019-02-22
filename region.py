from point import Point

class Region(object):
    def __init__(self, x, y, points_collection=None): # User passes in an array of points that they want
        # Center point in which the sub quadrants are based off of
        self.center = Point(x, y)

        self.point = [] # Made array because didn't have position of an initializer point
        
        self.capacity = 0 # Represents counter for when to subdivide

        self.children = [None] * 4 # List of 0 or 4 Region objects that are children of this Region


        # What does this mean? For each point in the point collection we insert, recursively finding the region that we can contain the point to 
        if points_collection is not None:
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
        '''Returns true if point is contained inside the quad tree'''
        region = self

        quadrant = region.region_index(point)

        # print(region.children[quadrant].point)
        if point == region.point:
            return True
        return False

        # while region is not None: # Deep off in the maze
        #     quadrant = self.region_index(point)
            
            
        #     region = region.children[quadrant]
        
        #     if point == region.point[0]:
        #         return True
        # return False
    
    def insert(self, point, region=None):

        '''Inserts point inside region that contains that coordinate space'''
        # TODO: Find quadrant that the point lies in
        # TODO: Find insert then check if it is at capacity ... if so then subdivide which reogranizes those nodes into the correct regions
        if region is None:
            region = self

        if region.capacity == 0:
            # Meaning we found a valid subqaudrant
            
            region.point.append(point)
            # print(region.point[0].x, region.point[0].y)
            region.capacity += 1
            return region # Once you've inserted operation is done so filter back up the recursive call and pathway of quadrants it took to get to that subquadrant

        if region.capacity > 0: # Meaning that we have to keep subdividing
            # Do we insert that subdivide
            # Mutating the instance that calls the method
            region.subdivide() # Subdivide into four different quadrants 

            quadrant = region.region_index(point) # Find the quadrant in which the point lies in after you mutate the region
            self.insert(point, region.children[quadrant]) # Find valid subquadrant and insert point
            
       


    def subdivide(self):
        '''Splits the region into 4 separate quadrants based of center point of the region'''
        # Can do so by updating the center of the children region objects to be half the region's x and y coordinate

        # Northwest Region
        self.children[0] = Region(self.center.x // 2, (self.center.y + self.center.y // 2))
        point1 = Point(self.center.x // 2, (self.center.y + self.center.y // 2))
        print(self.region_index((point1)))

        # Northeast Region
        self.children[1] = Region((self.center.x + self.center.x // 2), (self.center.y + self.center.y // 2))
        point2 = Point((self.center.x + self.center.x // 2), (self.center.y + self.center.y // 2))
        print(self.region_index(point2))

        # Southeast region
        self.children[2] = Region((self.center.x + self.center.x // 2), self.center.y // 2)
        point3 = Point((self.center.x + self.center.x // 2), self.center.y // 2)
        print(self.region_index(point3))

        # Southwest region
        self.children[3] = Region(self.center.x // 2, self.center.y // 2)
        point4 = Point(self.center.x // 2, self.center.y // 2)
        print(self.region_index(point4))




region = Region(100, 100, [Point(50, 50), Point(150, 50)])

print(region.contains(Point(50, 50)))
print(region.contains(Point(150, 50)))
# print(region.contains(Point(150, 150)))
# print(region.contains(Point(50, 150))) 