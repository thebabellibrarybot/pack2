import re
import os
import dotenv

dotenv.load_dotenv()
BOX_RATIO = os.environ.get('BOX_RATIO')

# takes a single pos_dic full of dics and returns each dic as a ls
# e.g. {"HM001": ['art001', 3,21,22, 'nyc-la', 'jane doe - artword', 2021, 'acrylic on cavas', 'big blue', 'taco shell']}
# into [21,3, HM001-art001]
def ls_item_dic(pos_dics):
    print(type(pos_dics))
    rect_ls = []
    for k,v in pos_dics.items():
        #print(k, v)
        rects = ((k+v[0]))
        print(rects)
    return 'hello from ls_item_dic'

def will_fit(master_list, location):
    # TODO if master_list > location return false
    # if master_list < location return true
    pass

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



# func that addjusts pack_type of box_like_pack to 'Cardboard Box'
def is_box(item):

    # TODO this math needs to be made a little more complex to accomadate for a lot
    # of different types of rectangles tubes and such ************************

    w,h,l = item[3], item[1], item[2]
    if w > float(BOX_RATIO) * l or w > float(BOX_RATIO) * h:
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


# charting func: mk_bird_graph, mk_shelf_graph, mk_graph_pdf, mk_list_pdf,
#                mk_meterics_analysis, mk_artist_by_volume_graph, mk_avg_dims