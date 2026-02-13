# Weaver dictionary not public? so using wordfreq
def get_words(length: int):
    from wordfreq import top_n_list
    words = top_n_list("en", 100000)
    return [word for word in words if len(word) == length and word.isalpha()]

def is_one_letter_off(base: str, check: str):
    if len(base) != len(check):
        return False
    return True if letters_differing(base, check) == 1 else False

def letters_differing(base: str, check: str):
    differing_letters = 0
    for i in range(len(base)):
        if base[i] != check[i]:
            differing_letters += 1
    return differing_letters

def get_words_one_letter_off(base: str):
    words = get_words(len(base))
    return [word for word in words if is_one_letter_off(base, word) and word != base]   
if __name__ == "__main__":
    # print(get_words(5))
    # print(is_one_letter_off("hello", "hully"))
    print(get_words_one_letter_off("hello"))
    
