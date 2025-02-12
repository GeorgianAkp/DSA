def AnagramCheck(str1,str2) : 
    # check if str1 and str2 are anagrams 
    str1_data_dict = get_dict_from_string(str1)
    str2_data_dict = get_dict_from_string(str2)
    print(str1_data_dict,str2_data_dict)
    for key,val in str1_data_dict.items() : 
        if key.lower() not in str2_data_dict.keys() or val != str2_data_dict[key]:
            return False 
    return True 
        

def get_dict_from_string(str) : 
    str_dict = dict()
    for ch in str : 
        if ch == ' ' : 
            continue
        if ch.lower() not in str_dict.keys():
            str_dict[ch.lower()] = 1 
            continue
        str_dict[ch.lower()] += 1 
    return str_dict


str1 = 'G o d'
str2 = 'Dog'

print(AnagramCheck(str1,str2))