from src import pack
from src import space
from src.pack import pack_tight_shelves
import os

# Change to argparse and os
xml_fi = 'DATA/jan_pack.xlsx'
location = {}
location['location 1'] = ( 3, [(96,120,60),(96,96,60),(48,48,60)], [['Custom Crate', 'Cardboard Box', 'Taco Shell', 'Slipcase', 'slipcase', 'Tube'], ['Tube', 'Custom Crate', 'Cardboard Box'], ['Taco Shell', 'slipcase'] ], 'Big Blue' )
# change to artparse adn os

def cleanup(i):
    wrong = i.in_wrong_location()
    didnt_fit = i.cant_fit()
    # TODO map and list wrong & didnt_fit
    return wrong, didnt_fit

def pack_shelves(xml_fi, location):

    # gen packlist
    i = pack.item_ls(xml_fi)
    dic = i.ls_xml()

    # filter list for possible packing combinations
    i = space.storage_spaces(location, dic)
    possible_dics = i.pack_types_in_spaces()
    master_list = i.in_right_location()

    # TODO pack master_list according to possible_dics
    # where each packed_item is removed from master_list
    # and sorted into storage_spaces

    packed_tight_shelves = pack_tight_shelves(master_list, possible_dics, location)
    print(packed_tight_shelves, 'returned from packed_tight_shelves')




    # cleanup func, grabs items that are in wrong loc & didn't fit

    #if len(master_list) != len(dic):
    #    dirt = cleanup(i)
        #print(len(dirt[0]), len(dirt[1]))


pack_shelves(xml_fi=xml_fi, location = location)