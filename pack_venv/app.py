from src import pack
from src import space

xml_fi = 'DATA/jan_pack.xlsx'
location = {}
location['location 1'] = ( 3, [(96,120,60),(96,96,60),(48,48,60)], [['Custom Crate', 'Cardboard Box', 'Taco Shell', 'Slipcase', 'slipcase', 'Tube'], ['Tube', 'Custom Crate', 'Cardboard Box'], ['Taco Shell', 'slipcase'] ], 'Big Blue' )

def cleanup(i):
    wrong = i.in_wrong_location()
    didnt_fit = i.cant_fit()
    return wrong, didnt_fit

def get_ls(xml_fi):

    # gen packlist
    i = pack.item_ls(xml_fi)
    dic = i.ls_xml()

    # filter list for possible packing combinations
    i = space.storage_spaces(location, dic)
    possible_dics = i.pack_types_in_spaces()
    master_list = i.in_right_location()

    # grab items in the wrong space
    # grab items that didn't fit
    if len(master_list) != len(dic):
        dirt = cleanup(i)
        print(len(dirt[0]), len(dirt[1]))



    

get_ls(xml_fi=xml_fi)