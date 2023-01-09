# get info from storage location to see what type of packages it accepts
import re

# get volume for dims or storage space that are structured as a list of 3 dims
def get_volume(dims):
    return dims[0]*dims[1]*dims[2]


# mk a func that says best rotation
# if dims.could_be_smaller() == true:
#   dims = roate(dims)
# will return dims as w, h, l where:
# sorted(sm = w, med = height, lg = len)
def best_rotation(dims):
    sorted_dims = sorted(dims)
    return sorted_dims



# mk a func that says 
# if dims == square_like
# pack_type == 'cardboard box'
def is_box(item):

    # this math needs to be made a little more complex to accomadate for a lot
    # of different types of rectangles tubes and such ************************

    w,h,l = item[3], item[1], item[2]
    if w > .4 * l or w > .4 * h:
        item[7] = 'Cardboard Box'
        return item
    return item


# make sure item has packing info description and if not
# either infer the packing type from above util functions
# or just assign default of 'taco shell'
def append_pack_info(item, arr):
    item = is_box(item)
    ls = []
    for i in arr: 
        ls.extend(i)
    if item[7] not in ls:
        pack_type = str(item[7])
        pack = re.sub(r'.*', 'Taco Shell', pack_type)
        pack = pack.replace('Taco ShellTaco Shell', 'Taco Shell')
        item[7] = pack

    return item


