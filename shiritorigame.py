import pico
import nltk
import rhine
import goslate

class Shiritori(object):
    """Instance of game. As words are added to the sentence, the score gets
    incremented. Score for new word depends on how much it relates to other
    words in the sentence. Only relevant words are selected. Articles have no
    effect on score. Repeated words are worth nothing.
    
    Fields:
        nodes[Node list]: List of current relevant words
        p1score [int]: Player1's score
        p2score [int]: Player2's score
        p1 [boolean]: If it is p1's turn
        BASE_POINTS: Fixed number that average entropy of a node is subtracted
        from to determine how many points that word is worth
        valid_tags [string list]: List of tags that indicate word should be a node
        rh [Rhine]: Instance of rhine to determine distance between words
        translator [Goslate]: Translator used for Chinese to English
        used_words [string list]: List of words that have been used"""
    def __init__(self):
        self.nodes = []
        self.p1score = 0
        self.p2score = 0
        self.p1 = True
        self.BASE_POINTS = 100
        self.valid_tags = ['N','J','V']
        self.rh = rhine.Rhine('sdf0b913e4b07b5243b7f527')
        self.translator = goslate.Goslate()
        self.used_words = []

    def play(self, word):
        if word not in self.used_words:
            trans_word = self.translate(word)
            if self.is_node(trans_word):
                self.used_words.append(word)
                new_node = self.create_node(trans_word)
                self.update_score(new_node)
                self.nodes.append(new_node)
        self.p1 = not self.p1
        
    def translate(self, word):
        translated = self.translator.translate(word, "en")
        print translated
        return translated

    def is_node(self, word):
        tag = nltk.pos_tag([word])[0][1][0]
        if (tag in self.valid_tags):
            return True
        else:
            return False

    def create_node(self, word):
        rel_entr = 0
        if len(self.nodes) > 0:
            for n in self.nodes:
                this_entr = self.rh.distance(word, n.word)
                if this_entr > 0:
                    rel_entr = rel_entr + this_entr
            rel_entr = (int) (rel_entr/(len(self.nodes)))
        new_node = Node(word, rel_entr)
        return new_node

    def update_score(self, node):
        if len(self.nodes) > 0 and node.relative_entropy > 0:
            if self.p1:
                self.p1score = self.p1score + (self.BASE_POINTS - node.relative_entropy)
            else:
                self.p2score = self.p1score + (self.BASE_POINTS - node.relative_entropy)
                
    def get_p1score(self):
        return self.p1score
    
    def get_p2score(self):
        return self.p2score

class Node(object):
    """Object of class node representing a word belonging to a sentence
    
    Fields:
        word [string]: The word itself
        relative_entropy [float list]: The entropy between it and other nodes
        in the sentence it belongs to at the time of its creation"""
    def __init__(self, word, relative_entropy):
        self.word = word
        self.relative_entropy = relative_entropy

game = Shiritori()

def play(word):
    game.play(word)
    
def noop():
    return "noop"

def get_p1score():
   return game.get_p1score

def get_p2score():
   return game.get_p2score