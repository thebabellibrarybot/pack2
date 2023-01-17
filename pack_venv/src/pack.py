import pandas as pd
import numpy as np
from src import utils
import csv
import math
from rectpack import PackingMode, PackingBin, SORT_LSIDE, PackerBBF, newPacker, MaxRectsBssf

# creates a dict of items found in the input xml_fi
# needs a xml_fi formated so that
# 'Unnamed:0': 'view',
#    'Unnamed: 1': 'Pack_ID',
#    'Unnamed: 2': 'HM',
#   'Unnamed: 3': 'ARTnum',
#   'Unnamed: 4': 'client',
#    'Unnamed: 5': 'artist',
#    'Unnamed: 6': 'dims',
#   'Unnamed: 7': 'location',
#    'Unnamed: 12': 'packed'

class item_ls():

    def __init__(self, xml_fi):
        self.xml_fi = xml_fi

    def ls_xml(self):

        file = self.xml_fi
        print(file, 'file from pack')

        if file.endswith('.xlsx'):
            print('file endswith xlsx')
            #create a dic from xml fi
            hm_dic = {}

            df = pd.read_excel(self.xml_fi)
            workbook = df.rename(columns={'Unnamed:0': 'view',
                                            'Unnamed: 1': 'Pack_ID',
                                            'Unnamed: 2': 'HM',
                                            'Unnamed: 3': 'ARTnum',
                                            'Unnamed: 4': 'client',
                                                'Unnamed: 5': 'artist',
                                                'Unnamed: 6': 'dims',
                                                'Unnamed: 7': 'location',
                                                'Unnamed: 12': 'packed'})

            book_len = workbook.shape[0]

            for num in (range(book_len)):
                info = tuple((
                        workbook.ARTnum[num],
                        float(workbook.dims[num].split(' x ')[0]),
                        float(workbook.dims[num].split(' x ')[1]),
                        float(workbook.dims[num].split(' x ')[2]),
                        workbook.client[num],
                        workbook.artist[num],
                        workbook.location[num],
                        workbook.packed[num]
                        ))

                hm_dic[workbook.HM[num]] = info

            return hm_dic

        elif file.endswith('.csv'):

            hm_dic = {}

            with open(file) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for num, row in enumerate(csv_reader):

                    # tuple = artword, dim1, dim2, dim3, client, artist, location, materials

                    info = tuple((
                        row[3:5],
                        int(math.ceil(float(row[-2].split(' x ')[0].split(' ')[0]))),
                        int(math.ceil(float(row[-2].split(' x ')[-1].replace('in.','').split(' ')[0]))),
                        int(math.ceil(float(1.5))),
                        row[0],
                        row[2],
                        'cavalier 24thst',
                        row[-3]
                    ))
                    hm_dic[num] = info

                return hm_dic 



# setup Packer funcs and algo's
def newPacker(mode = PackingMode.Offline,
                bin_algo = PackingBin.BBF,
                pack_algo = MaxRectsBssf,
                sort_algo = SORT_LSIDE,
                rotation = False):
    packer_class = None

    # offline mode
    if mode == PackingMode.Offline:
        if bin_algo == PackingBin.BBF:
            packer_class = PackerBBF
        if sort_algo:
            return packer_class(pack_algo=pack_algo, sort_algo=sort_algo)
        else:
            return packer_class(pack_algo=pack_algo, rotation=rotation)


# SHELF PACKING FUNC
# args: master_list, possible_dics

# where master_list == a dictionary of all items that are in the correct 
# storage facility. this list will be chipped away at until it is empty or 
# the space is full
# from: src/space.py

# where possible_dics == a dictionary of all storage_spaces in the storage_facility
# along with all the dictionary items from the master_list which fit into that
# particular storage_space. master_list items being packed must also be in the 
# possible_dics list in order to be allowed into a storage_space

def pack_tight_shelves(master_list, possible_dics, location):


    m_ls = master_list
    pos_dic = possible_dics
    in_bin = {}


    loc = list(location['cavalier 24thst'])
    for num in range(loc[0]):
        cur_packed = {}
        if num < 1:
            print(num)
            cur_space = num
            print('cur_space', cur_space)
            #cur_space_dims = loc[1][num]
            #cur_pos_items = pos_dic[cur_space]
            #i = utils.ls_item_dic(pos_dic[cur_space])
        elif num >= 1: 
            print(num, 'over one')
    return 'hello world'

# allow stacking?

# room for err?

# append all info?

# cavalier == guest password

# michael with the retail management