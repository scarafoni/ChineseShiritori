# -*- coding: utf-8 -*-

import pico
    
def parse_text_res(sent):
    return str(parse(sent))

"""Parses a sentence sent to determine whether it is a valid sentence
Precondition: sent is a string"""
def parse(sent):
    f = open("sentence_part.txt",'r')
    last_part = f.readline().strip()
    f.close()
    print(last_part)
    sent = sent.strip()
    if last_part in ["start","subject"]:
        return isSubject(sent)
    elif last_part == "verb":
        return isVerb(sent)
    elif last_part == "object":
        return isObject(sent)
    else:
        return False

"""Returns whether word is a subject
Precondition: word is a string"""
def isSubject(word):
    print("subject")
    f = open("sentence_part.txt",'w')
    subjects = [u'我',u'你'u'他']
    if word in subjects:
        f.write("verb")
        f.close()
        return True
    else:
        f.write("start")
        f.close()
        return False

"""Returns whether word is a verb
Precondition: word is a string"""
def isVerb(word):
    f = open("sentence_part.txt",'w')
    verbs = [u'爱', u'恨']
    if word in verbs:
        f.write("object")
        f.close()
        return True
    else:
        f.write("start")
        f.close()
        return False

"""Returns whether word is an object
Precondition: word is a string"""
def isObject(word):
    f = open("sentence_part.txt",'w')
    objects = [u'狗',u'猫']
    print("in objects, word- "+word)
    if word in objects:
        f.write("subject")
        f.close()
        return True
    else:
        f.write("start")
        f.close()
        return False
