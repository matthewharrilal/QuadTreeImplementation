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
       
        if region is None:
            region = self.root_region
        
        if region.capacity == 0:
            # Meaning we found a valid subqaudrant
            region.point.append(point)
            region.capacity += 1
            return region  # Once you've inserted operation is done

        if region.capacity > 0 :  # Meaning that there is already a point in there
         
            if region.isDivided == False:
                region.subdivide()  # Subdivide into four different quadrants

                region.isDivided = True
                

            quadrant = region.region_index(point)

            # for existing_point in region.point:

            #     replacement_quadrant = region.region_index(existing_point) # Find new location
                

            #     # region.children[replacement_quadrant].point.append(existing_point)
               
                
            # region.point = [] # Reset regions points before subdivision to be clear
            self.insert(point, region.children[quadrant])
            

    def contains(self, point):
        '''Returns true if point is contained inside the quad tree'''
        region = self.root_region # Representing the starting region
        # Already been subdivided

        # Iterate through the regions until we find the point

        while region is not None: # If the region exists
            
            quadrant = region.region_index(point) # Find the corresponding quadrant


            if len(region.point) > 0: # If the region contains a point
                

                if region.point[0].x == point.x and region.point[0].y == point.y: # If the coordinates match
                    return True   
            
            region = region.children[quadrant]
        return False

    def pathway(self, point):
        '''Finds pathway through quadrants'''
        region = self.root_region
        pathway = ""

        # First lets check if point exists before we find the pathway
        if self.contains(point) is False:
            return "No pathway available"

        while region is not None: # If the region exists

            if point.x == region.point[0].x and point.y == region.point[0].y:
                return "ROOT REGION" if pathway == "" else pathway

            quadrant = region.region_index(point)
            pathway += str("Quadrant -> {} ".format(quadrant)) # Only add pathway if index of quadrant exists

            region = region.children[quadrant] # Keep going until you find specific quadrant that contains point
            
        return pathway

# Second element not working as a result of the subdivide
quad_tree = QuadTree(100, 100, [Point(150, 150),Point(50, 50), Point(60, 60), Point(89, 45)])

print(quad_tree.pathway(Point(150, 150)))
print("")
print("")
print(quad_tree.pathway(Point(150, 140)))
print("")
print("")
print(quad_tree.pathway(Point(50, 50)))
print("")
print("")
print(quad_tree.pathway(Point(60, 60)))
print("")
print("")
print(quad_tree.pathway(Point(89, 45)))
