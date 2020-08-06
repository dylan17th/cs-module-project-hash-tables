
def word_count(s):
    cache = {}
    array_string = s.split()
    my_arr_needed = [""] * len(array_string)
    if len(array_string) == 1:
        array_string = [char for char in array_string[0]]
    for i, ele in enumerate(array_string):
        for letter in ele:
            if letter.isalnum() or letter == "'":
                my_arr_needed[i] += letter
    if s is "":
        return {}
    else: 
        for ele in my_arr_needed:
            if ele == "":
                return {}
            if ele.lower() not in cache:
                cache[ele.lower()] = 1
            else:
                cache[ele.lower()] = cache[ele.lower()] + 1
        return cache

if __name__ == "__main__":
    print(word_count("Hello     hello"))
    print(word_count(":;,.-+=/\\|[]{}()*^&"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))