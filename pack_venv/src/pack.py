import pandas as pd

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

# args: master_list, possible_dics

# where master_list == a dictionary of all items that are in the correct 
# storage facility. this list will be chipped away at until it is empty or 
# the space is full
# from: src/space.py

# where possible_dics == a dictionary of all storage_spaces in the storage_facility
# along with all the dictionary items from the master_list which fit into that
# particular storage_space. master_list items being packed must also be in the 
# possible_dics list in order to be allowed into a storage_space

def pack_tight(master_list, possible_dics, location):

    loc = list(location['location 1'])
    print(loc[0])

    return 'hello world'

# allow stacking?

# room for err?

# append all info?

# cavalier == guest password