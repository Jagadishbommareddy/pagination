PAGE_LIMIT = 20

def get_offset(data):
    if 'offset' in data:
        offset = data['offset']
    else:
        offset = 0
    limit = offset+PAGE_LIMIT
    return offset,limit



