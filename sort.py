def q_sort(lists:list):
    if len(lists)<=1:
        return lists
    elem=lists[0]
    low = list(filter(lambda x:x<elem,lists))
    avg = [i for i in lists if i==elem]
    higth = list(filter(lambda x:x>elem,lists))
    return q_sort(low)+avg+q_sort(higth)
