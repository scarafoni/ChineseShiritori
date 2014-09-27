import pico

def parse_text_res(sent):
    return str(parse(sent))

"""Parses a sentence sent to determine whether it is a valid sentence
Precondition: sent is a string"""
def parse(sent):
    sent = sent.strip()
    words = sent.split()
    print words
    if len(words) == 1:
        return isSubject(words[0])
    if len(words) == 2:
        return isSubject(words[0]) and isVerb(words[1])
    else:
        return isSubject(words[0]) and isVerb(words[1]) and isObject(words[2])

"""Returns whether word is a subject
Precondition: word is a string"""
def isSubject(word):
    lword = word.lower()
    subjects = ["i", "you"]
    return contains(subjects, lword)

"""Returns whether word is a verb
Precondition: word is a string"""
def isVerb(word):
    lword = word.lower()
    verbs = ["love", "hate"]
    return contains(verbs, lword)

"""Returns whether word is an object
Precondition: word is a string"""
def isObject(word):
    lword = word.lower()
    objects = ["him", "this", "that"]
    return contains(objects, lword)

"""Takes in a list and an element and returns true if the element is in the
list and false if it is not
Preconditions: l is a list"""
def contains(l, word):
    for ele in l:
        if (ele == word):
            return True
    return False
    
if __name__ == "__main__":
    main()