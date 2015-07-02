def haversine(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    km = 6371 * c
    return km 
def binary_search(val_list, val, _lt, _gt, _eq, label, bound): 
    if _gt(val_list[0], val, label):
        return 0
    if _lt(val_list[-1], val, label):
        return len(val_list)
    imax = len(val_list)
    imin = 0 
    while (imin < imax):
        imid = imin + (imax-imin)/2
        if _lt(val_list[imid], val, label):
            imin = imid+1
        else:
            imax = imid
    if (imax == imin) and _eq(val_list[imin], val, label):
        return imin
    else:
        if bound == 'lower':
            return imin
        if bound == 'upper':
            return imin + 1
def get_nearby_places(pxi, pyi, loc_type, workplaces_and_schools, num_loc_needed):
    return nearby_places, positions_found
def select_nearest_school(px, py, nearby_places, workplaces_and_schools, workplace_lookup):
    return closest_school, min_dist
def x_to_col_num(x):
    return int(round((x - min_x_center)/pixel_size))
def y_to_row_num(y):
    return int(round((y - min_y_center)/pixel_size))
def xy_cmp(a,b):
    if a['xi'] < b['xi']:
        return -1
    elif a['xi'] > b['xi']:
        return 1
    else:
        if a['yi'] < b['yi']:
            return -1
        elif a['yi'] > b['yi']:
            return 1
        else:
            return 0
def dict_val_lt(A,b,label):
    if A[label] < b:
        return True
    else:
        return False
def dict_val_gt(A,b,label):
    if A[label] > b:
        return True
    else:
        return False
def dict_val_eq(A,b,label):
    if A[label] == b:
        return True
    else:
        return False

