def message_converter(message):
    list_char=list(message)
    for i in range(len(list_char)):
        print(hex(ord(list_char[i])).replace("0x","").upper(),end="")
message_converter("Hello")