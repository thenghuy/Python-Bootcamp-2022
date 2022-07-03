def dict_values(dict):
    dict_key = list(dict.keys())
    dict_value = list(dict.values())
    for i in range(len(dict_key)):
        value_string = str(dict_value[i])
        value_remove_comma = value_string.replace(",", "")
        value_remove_bracket = value_remove_comma.strip("()")
        dict_value_remove_symbol= value_remove_bracket.replace("'", "")
        print(dict_key[i], ":", dict_value_remove_symbol,"\n*****")
dict_values({120:("Visal","Borey","Sovann"),130:("Hout","Mouyleng","Pidor"),140:("Nary","Misora","Masaki")})