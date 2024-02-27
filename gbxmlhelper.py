def search_its_idx(node, tag):
    for idx, key in enumerate(node):
        key_tag = key.tag.replace('{http://www.gbxml.org/schema}', '')
        if key_tag == tag:
            return idx
    return None

def find_thekey(node):
    list_keys = []
    list_num_keys = []
    
    for key in node:
        key_tag = key.tag.replace('{http://www.gbxml.org/schema}', '')
        if key_tag not in list_keys:
            list_keys.append(key_tag)
            list_num_keys.append(1)
        else:
            idx = list_keys.index(key_tag)
            list_num_keys[idx] += 1
            
    return list_keys, list_num_keys