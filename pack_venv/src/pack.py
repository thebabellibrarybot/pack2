import pandas as pd
import numpy as np

xml_fi = '../Data/jan_pack.xlsx'

class item_ls():
    def __init__(self, xml_fi):
        self.xml_fi = xml_fi
    def ls_xml(self):

        #create a dic from xml fi
        hm_dic = {}

        df = pd.read_excel(self.xml_fi)
        workbook = df.rename(columns={'Unnamed:0': 'view', 'Unnamed: 1': 'Pack_ID', 'Unnamed: 2': 'HM', 'Unnamed: 3': 'ARTnum', 'Unnamed: 6': 'dims'})

        book_len = workbook.shape[0]

        for num in (range(book_len)):
            info = tuple((
                    workbook.ARTnum[num],
                    float(workbook.dims[num].split(' x ')[0]),
                    float(workbook.dims[num].split(' x ')[0]),
                    float(workbook.dims[num].split(' x ')[0])
                    ))

            hm_dic[workbook.HM[num]] = info


        return hm_dic





i = item_ls(xml_fi)
dic = i.ls_xml()
print(dic, 'i')