from src import pack
from src import space
from src.pack import pack_tight_shelves
import os

# Change to argparse and os
xml_fi = 'DATA/jan_pack.xlsx'
xml = 'DATA/Works.csv'

#location['24th st'] = (num_spaces, [space_id], [(space_dims)], [(space_allows)], facility)
space_ids = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'd10', 'd11', 'd12', 'd13', 'd14', 'd15']
# w,h,l
space_dims = [(58, 31.5, 43), (58, 48, 43), (58, 39, 43), (23, 60, 70), (23, 31, 70), (23, 60, 70), (19, 86, 70), (29, 86, 70), (19, 86, 70), (67, 84, 21), (31, 24, 21), (16, 24, 21), (18, 24, 21), (39, 30, 21), (18, 30, 21), (9, 30, 21), (31, 25, 21), (36, 25, 21), (23, 44, 18), (23, 44, 18), (19, 40, 18), (14, 29, 15), (13, 29, 15), (14, 29, 15), (14, 29, 15), (13, 29, 15), (14, 29, 15), (19, 31, 19), (14, 29, 18), (13, 29, 18), (13, 29, 18), (10, 29, 18), (29, 12, 18)]
num_spaces = len(space_ids)
num_space_dims = len(space_dims)
space_alloted = [('Cardboard Box', 'Taco Shell', 'Tube', 'Framed', 'UnFramed'), ('Cardboard Box', 'Taco Shell', 'Tube', 'Framed', 'UnFramed'), ('Supplies'), ('Cardboard Box', 'Taco Shell', 'Tube', 'Framed', 'UnFramed'), ('Cardboard Box', 'Taco Shell', 'Tube', 'Framed', 'UnFramed'), ('Empty Boxes'), ('Cardboard Box', 'Taco Shell', 'Tube', 'Framed', 'UnFramed'), ('Cardboard Box', 'Taco Shell', 'Tube', 'Framed', 'UnFramed'), ('Supplies'), ('Cardboard Box', 'Taco Shell', 'Tube', 'Framed', 'UnFramed'),('Cardboard Box', 'Taco Shell', 'Tube', 'Framed', 'UnFramed'),('Cardboard Box', 'Taco Shell', 'Tube', 'Framed', 'UnFramed'),('Cardboard Box', 'Taco Shell', 'Tube', 'Framed', 'UnFramed'),('Cardboard Box', 'Taco Shell', 'Tube', 'Framed', 'UnFramed'),('Cardboard Box', 'Taco Shell', 'Tube', 'Framed', 'UnFramed'),('Cardboard Box', 'Taco Shell', 'Tube', 'Framed', 'UnFramed'),('Cardboard Box', 'Taco Shell', 'Tube', 'Framed', 'UnFramed'),('Cardboard Box', 'Taco Shell', 'Tube', 'Framed', 'UnFramed'),('Cardboard Box', 'Taco Shell', 'Tube', 'Framed', 'UnFramed'),('Cardboard Box', 'Taco Shell', 'Tube', 'Framed', 'UnFramed'),('Cardboard Box', 'Taco Shell', 'Tube', 'Framed', 'UnFramed'),('Cardboard Box', 'Taco Shell', 'Tube', 'Framed', 'UnFramed'),('Cardboard Box', 'Taco Shell', 'Tube', 'Framed', 'UnFramed'),('Cardboard Box', 'Taco Shell', 'Tube', 'Framed', 'UnFramed'),('Cardboard Box', 'Taco Shell', 'Tube', 'Framed', 'UnFramed'),('Cardboard Box', 'Taco Shell', 'Tube', 'Framed', 'UnFramed'),('Cardboard Box', 'Taco Shell', 'Tube', 'Framed', 'UnFramed'),('Cardboard Box', 'Taco Shell', 'Tube', 'Framed', 'UnFramed'),('Cardboard Box', 'Taco Shell', 'Tube', 'Framed', 'UnFramed'),('Cardboard Box', 'Taco Shell', 'Tube', 'Framed', 'UnFramed'),('Cardboard Box', 'Taco Shell', 'Tube', 'Framed', 'UnFramed'),('Cardboard Box', 'Taco Shell', 'Tube', 'Framed', 'UnFramed'),('Cardboard Box', 'Taco Shell', 'Tube', 'Framed', 'UnFramed')]
num_space_alloted = len(space_alloted)
print(num_space_alloted)

location = {}
location['cavalier 24thst'] = (num_spaces, space_dims, space_alloted, 'cavalier 24thst')
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
    print(len(possible_dics))
    print(len(master_list))

    # TODO pack master_list according to possible_dics
    # where each packed_item is removed from master_list
    # and sorted into storage_spaces

    packed_tight_shelves = pack_tight_shelves(master_list, possible_dics, location)
    print(packed_tight_shelves, 'returned from packed_tight_shelves')




    # cleanup func, grabs items that are in wrong loc & didn't fit

    #if len(master_list) != len(dic):
    #    dirt = cleanup(i)
        #print(len(dirt[0]), len(dirt[1]))


pack_shelves(xml_fi=xml, location = location)