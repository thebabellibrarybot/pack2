from src import pack

xml_fi = 'DATA/jan_pack.xlsx'

def get_ls(xml_fi):

    i = pack.item_ls(xml_fi)
    dic = i.ls_xml()
    print(dic, 'i')

get_ls(xml_fi=xml_fi)