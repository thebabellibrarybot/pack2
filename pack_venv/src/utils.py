# get info from storage location to see what type of packages it accepts
def append_location_info(item, arr):
    print(arr)
    if any(ar != item[7] for ar in arr):
        print(item[7])

    return item