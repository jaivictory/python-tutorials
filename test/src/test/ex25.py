def break_words(stuff):
    """ this function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """ Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """ prints first word after poping it off"""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """ prints last word after poping it off"""
    word = words.pop(-1)
    print(word)


def sort_sentence(sentence):
    """print the last word after popping it off"""()
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """sorts the words then print the first and last one."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """sorts the words then print the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)