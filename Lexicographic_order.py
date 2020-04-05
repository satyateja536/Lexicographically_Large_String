def get_count(temp_list, char, k):
    # Function to get the available count to place the character consecutively
    no = k
    if len(temp_list) == 0:
        no = k
    elif temp_list[-1] == char and len(temp_list) == 1:
        no = k - 1
    elif temp_list[-1] == char and len(temp_list) > k - 1:
        for z in range(1, k + 1):
            if temp_list[-z] == char:
                no = no - 1
    else:
        no = k

    return no


def find_next_char(main_list, char):
    # Function to find the next unique character in the given list provided the first repeating character
    temp_char = char
    for i in range(0, len(main_list) - 1):
        if main_list[i] != main_list[i + 1]:
            temp_char = main_list[i + 1]
            break
    return temp_char


def get_largest_string(s, k):
    result = []
    sorted_characters = list(s[:])
    print(" Given Input List of Characters: ", sorted_characters)
    sorted_characters.sort(reverse=True)
    print("\n List in Lexicographical order without applying k filter: ", sorted_characters)
    while len(sorted_characters) > 0:
        char = sorted_characters[0]
        count = get_count(result, char, k)
        if count > 0:
            result.append(char)
            sorted_characters.remove(char)
        else:
            next_char = find_next_char(sorted_characters, char)
            if next_char != char:
                result.append(next_char)
                sorted_characters.remove(next_char)
            else:
                break
    print("\n Result List: ", result)
    print("\n Result String: ", str(result))


s = "zzzazz"
k = 2
get_largest_string(s,k)
