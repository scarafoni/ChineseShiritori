# -*- coding: utf-8 -*-

import pico
    
subjects = [u'我',u'你'u'他']
joiners = [u'很']
verbs = [u'爱', u'恨']
objects = [u'狗',u'猫']

state = ""

def reset():
    update_start("start")

def parse_text_res(sent):
    return str(parse(sent))

def read_start():
    f = open("sentence_part.txt",'r')
    x = f.readline().strip().split(",")
    f.close()
    return x
    
def update_start(text):
    f = open("sentence_part.txt",'w')
    f.write(text)
    f.close()

"""Parses a sentence sent to determine whether it is a valid sentence
Precondition: sent is a string"""
def parse(sent):
    sent = sent.strip()
    state = read_start()
    print("state- ",state)
    print("sent- ",sent)
    if state in ["start","subject"]:
        return isSubject(sent)
    elif state == "verb":
        return isVerb(sent)
    elif state == "object":
        return isObject(sent)
    else:
        return False

"""Returns whether word is a subject
Precondition: word is a string"""
def isSubject(word):
    print('subject')
    print("in sub?",word in subjects)
    if word in subjects:
        update_start("verb,joiner")
        return True
    else:
        update_start("start")
        return False

"""Returns whether word is a verb
Precondition: word is a string"""
def isVerb(word):
    print('isVerb')
    if word in verbs:
        update_start("object")
        return True
    else:
        update_start("start")
        return False

"""Returns whether word is an object
Precondition: word is a string"""
def isObject(word):
    print('object')
    if word in objects:
        update_start("start")
        return True
    else:
        update_start("start")
        return False
