from point import Point


class RegionNode(object):
    def __init__(self, x, y):  # User passes in an array of points that they want
        # Center point in which the sub quadrants are based off of
        self.center = Point(x, y)

        self.point = []  # Made array because didn't have position of an initializer point

        self.capacity = 0  # Represents counter for when to subdivide

        # List of 0 or 4 Region objects that are children of this Region
        self.children = [None] * 4

        self.isDivided = False # So depending if capacity is full check for available spots without subdividing first

        # POINTS ARE CONTAINED BY THE REGION NODE

        # SUBDIVISION CHILDREN ARE CONTAINED BY NODES

    def subdivide(self):
        '''Splits the region into 4 separate quadrants based of center point of the region'''
        # Can do so by updating the center of the children region objects to be half the region's x and y coordinate

        # Northwest Region
        self.children[0] = RegionNode(self.center.x // 2, (self.center.y + self.center.y // 2))

        # Northeast Region
        self.children[1] = RegionNode((self.center.x + self.center.x // 2), (self.center.y + self.center.y // 2))
        
        # Southeast region
        self.children[2] = RegionNode((self.center.x + self.center.x // 2), self.center.y // 2)
       

        # Southwest region
        self.children[3] = RegionNode(self.center.x // 2, self.center.y // 2)
    

    def region_index(self, point):
        '''Return an index in range [0...3] (0: NW, 1: NE, 2: SE, 3: SW) that specifies which
        subregion (child) the given point belongs to relative to this region's center.'''
        # Not handling edge case where data lies directly on the axis

        # SELF NOT REFERRING TO THE NEW REGION
        if point.x < self.center.x and point.y > self.center.y:
            return 0  # Representing the Northwest region

        elif point.x >= self.center.x and point.y >= self.center.y:

            return 1  # Representing NE region

        elif point.x > self.center.x and point.y < self.center.y:
            return 2  # Representing the SE region

        else:
            return 3  # Representing the southwest region


class QuadTree(object):
    def __init__(self, x, y, point_collection=None):
        self.root_region = RegionNode(x, y)

        if point_collection is not None:
            for point in point_collection:
                self.insert(point)

    # Insert because it is across multiple nodes


    # SOMETHING WRONG WITH THE ACT OF REASSIGNING POINTS
    def insert(self, point, region=None):
        '''Inserts point inside region that contains that coordinate space'''
        # TODO: Find quadrant that the point lies in
        # TODO: Find insert then check if it is at capacity ... if so then subdivide which reogranizes those nodes into the correct regions
        if region is None:
            region = self.root_region
        
        if region.capacity == 0:
            # Meaning we found a valid subqaudrant
            print("Only point ", region.children)
            region.point.append(point)
            region.capacity += 1
            return region  # Once you've inserted operation is done so filter back up the recursive call and pathway of quadrants it took to get to that subquadrant

        if region.capacity > 0:  # Meaning that we have to keep subdividing
         
            if region.isDivided == False:

                region.subdivide()  # Subdivide into four different quadrants
                region.isDivided = True
         

            quadrant = region.region_index(point)

            # for existing_point in region.point:

            #     replacement_quadrant = region.region_index(existing_point) # Find new location
                

            #     region.children[replacement_quadrant].point.append(existing_point) # Append that point as well to the proper quadrant

            #     region.point = [] # Reset regions points before subdivision to be clear
                
            
            self.insert(point, region.children[quadrant])
            

    def contains(self, point):
        '''Returns true if point is contained inside the quad tree'''
        region = self.root_region # Representing the starting region
        # Already been subdivided
        pathway = ""

        # Iterate through the regions until we find the point

        while region is not None: # While there are caculated regions to traverse through
            quadrant = region.region_index(point)
            pathway += str(quadrant)
            
            # When are you traversing you want to check which region contains the point when subdividing do you
            # First check if that regions point exists

            if len(region.point) > 0 and region is not None: # Meaning that a point exists
                # Have to compare attributes as opposed to point objects?? Better way to do this?
                if region.point[0].x == point.x and region.point[0].y == point.y: # If the coordinates match
                    print(pathway)
                    return True     
                
                # Else keep traversing buddy
        
            region = region.children[quadrant]
        return False


# Second element not working as a result of the subdivide
quad_tree = QuadTree(100, 100, [Point(150, 150), Point(50, 50)])

print(quad_tree.contains(Point(50, 50)))
print(quad_tree.contains(Point(150, 50)))
print(quad_tree.contains(Point(150, 150)))
print(quad_tree.contains(Point(150, 60)))

