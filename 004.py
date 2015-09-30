def get_elements(s):
    l = s.replace(",", "").replace(".", "").split(" ")
    nums = [1,5,6,7,8,9,15,16,19]
    elem_table = {}
    for (i, j) in enumerate(l):
        if i+1 in nums:
            elem_table[i+1] = j[0]
        else:
            elem_table[i+1] = j[:2]
    return elem_table

s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
print(get_elements(s))