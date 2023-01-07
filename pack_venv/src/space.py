# args: location

# a location is a dictionary item that includes:
#   number of storage spaces,
#   array of storage space dims,
#   type of package storage space accepts
#   location of storage facility

# e.g. { 3, [(5,5,5),(5,5,5),(5,5,5)], [('Custom Crate', 'Cardboard Box', 'Taco Shell')], altanta }
location = {}
location['location 1'] = ( 3, [(5,5,5),(5,5,5),(5,5,5)], [('Custom Crate', 'Cardboard Box', 'Taco Shell')], 'altanta' )


class storage_spaces():

    def __init__(self, location):
        self.location = location
    
    # check to make sure the packages are all supposed to be going to the same place
    def right_location(self):
        print(type(self.location))
        return ('hello from space.py')


    # get location info
    #def location_info():
    #    pass

    # split the packages by packing type
    #def pack_types():
    #    pass
    # assign packages to their correct location
    #def assign_location():
    #    pass

i = storage_spaces(location)
dic = i.right_location()
print(dic)
