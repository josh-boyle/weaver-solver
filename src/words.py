# Weaver dictionary not public? so using wordfreq
def get_words_with_length(length: int, popularity: int = 100000):
    from wordfreq import top_n_list
    words = top_n_list("en", popularity)
    excludes = get_excludes()
    return [word for word in words if len(word) == length and word.isalpha() and word not in excludes]
def get_words(popularity: int = 100000):
    from wordfreq import top_n_list
    words = top_n_list("en", popularity)
    excludes = get_excludes()
    return [word for word in words if word.isalpha() and word not in excludes]
def get_excludes():
    from pathlib import Path
    base_dir = Path(__file__).resolve().parent
    file_path = base_dir.parent / "data" / "exclude.txt"
    with open(file_path, "r", encoding="utf-8") as file:
        words = [line.strip() for line in file]
    return words
def print_dictionary(words: list[str]):
    from pathlib import Path
    base_dir = Path(__file__).resolve().parent
    file_path = base_dir.parent / "data" / "dictionary.txt"
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("\n".join(words))
def is_one_letter_off(base: str, check: str):
    if len(base) != len(check):
        return False
    return True if letters_differing(base, check) == 1 else False

def neighbor_list_x(base: str, dictionary: list[str]):
    return [word for word in dictionary if len(word) in range(len(base)-1,len(base)+1) and letters_differing_x(base,word)]

def letters_differing_x(base:str, check:str) -> bool:
    if len(base) == len(check): return letters_differing(base,check) == 1
    elif len(base) > len(check):
        longer = base
        templates = [(check[:i] + '*' + check[i:]) for i in range(len(check)+1)]
    else: 
        longer = check
        templates = [(base[:i] + '*' + base[i:]) for i in range(len(base)+1)]
    for template in templates:
        if letters_differing(longer, template) == 1:
            return True
    return False
    

def letters_differing(base: str, check: str):
    differing_letters = 0
    for i in range(len(base)):
        if base[i] != check[i]:
            differing_letters += 1
    return differing_letters

def get_words_one_letter_off(base: str):
    words = get_words_with_length(len(base))
    return [word for word in words if is_one_letter_off(base, word) and word != base]   
if __name__ == "__main__":
    # print(get_words(5))
    # print(is_one_letter_off("hello", "hully"))
    # print(get_words_one_letter_off("hello"))
    # print(letters_differing_x("hello", "bell"))
    print(neighbor_list_x("hello", get_words()))
    
