def histo(filename):
    with open(f"{filename}") as f:
        opened_file = f.read().split()

    arr_without_symbols = [""] * len(opened_file)
    bad_symbols = False

    for i, ele in enumerate(opened_file):
        for letter in ele:
            if letter.isalnum():
                arr_without_symbols[i] += letter.lower()
            else:
                bad_symbols = True
    my_cache = {}

    if bad_symbols is False:
        return {}

    for word in arr_without_symbols:
        if word not in my_cache:
            my_cache[word] = "#"
        else:
            my_cache[word] =  my_cache[word] + "#"

    sorted_arr = sorted(my_cache.items(), key=lambda x: x[1], reverse=True)
    
    for ele in sorted_arr:
        print(ele[0], ele[1])

if __name__ == "__main__":
    print(histo("robin.txt"))