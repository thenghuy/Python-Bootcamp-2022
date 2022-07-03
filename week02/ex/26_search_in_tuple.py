def search_in_tuple(tuple,ele_need_to_find):
    for i in range(len(tuple)):
        if tuple[i] == ele_need_to_find:
            return f"Element not found at index: {i}"
    return "Element not found in the tuple"
res=search_in_tuple((25,15,10,30),10)
print(res)
res=search_in_tuple((25,15,10,30),70)
print(res)


