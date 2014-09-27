# -*- coding: utf-8 -*-
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
    subjects = [u'我',u'你'u'他']
    return lword in subject

"""Returns whether word is a verb
Precondition: word is a string"""
def isVerb(word):
    lword = word.lower()
    verbs = [u'爱', u'恨']
    return lword in verbs

"""Returns whether word is an object
Precondition: word is a string"""
def isObject(word):
    lword = word.lower()
    objects = [u'狗',u'猫']
    return lword in objects

if __name__ == "__main__":
    main()
