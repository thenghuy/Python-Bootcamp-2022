paragraph = str(input("""Please input a paragraph:\n"""))
search_string = input("Please input a search string:\n")
no_of_search_string_in_para = paragraph.count((search_string))
print(f"There are {no_of_search_string_in_para} occurances.")
def replacestring():
    paragraph = input("Please input a paragraph:\n")
    search_string = input("Please input a search string:\n")
    no_of_search_string_in_para = paragraph.count((search_string))
    print(f"There are {no_of_search_string_in_para} occurances.")
    replace_str = input("Please input a replacement string:\n")
    result = paragraph.replace(search_string, replace_str)
    no_of_replace_str = result.count(replace_str)
    print(result)
    print(f"{no_of_replace_str} words has been replaced from the paragraph")
while True:
    choice = input("Do you want to replace the text[Y/N]?\n")
    if choice == "Y" or choice == "y":
        replacestring()
    elif choice == "N" or choice == "n":
        check = input("Oh!you dont like to replace,Do you want to check again[Y/N]?\n")
        if check == "y" or check == "Y":
            replacestring()
        elif check == "N" or check == "n":
            break
    else:
        print("" "Please give proper input" "")
        choice = input("Do you want to replace the text[Y/N]?\n")
        if choice == "Y" or choice == "y":
            replacestring()
        elif choice == "N" or choice == "n":
            check = input("Oh!you dont like to replace,Do you want to check again[Y/N]?\n")
            if check == "y" or check == "Y":
                replacestring()
            elif check == "N" or check == "n":
                break
'''On july 16,1969, the apollo 11 spacecraft launched from the kennedy Space center in florida. Its mission was to go where no human bring had gone before-the moon!the crewconsisted of Neil armstrong,Michael collins and buzz aldrin.the spacecraft landed on the moon in the sea of tranquility, a basaltic flood plain,on July 20,1969.the moonwalk took place the following day.On July 21,1969 at precise 10:56 EDT,commander Neil Armstrong from the lunar Module and took his famous first step onto the moon's surface.He declared ."That's one small step for man, one giant leap for mankind,"It was a monumental moment in human historyOn july 16,1969, the apollo 11 spacecraft launched from the kennedy Space center in florida. Its mission was to go where no human bring had gone before-the moon!The crewconsisted of Neil armstrong,Michael collins and buzz aldrin.The spacecraft landed on the moon in the sea of tranquility, a basaltic flood plain,on July 20,1969.The moonwalk took place the following day.On July 21,1969 at precise 10:56 EDT,commander Neil Armstrong from the lunar Module and took his famous first step onto the moon's surface.He declared ."That's one small step for man, one giant leap for mankind,"It was a monumental moment in human history'''
