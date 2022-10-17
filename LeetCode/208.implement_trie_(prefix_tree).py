"""
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys
in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before),
and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the
"prefix" prefix, and false otherwise.
"""


from collections import defaultdict


class Trie(object):

    def __init__(self):
        self.children = defaultdict(Trie)
        self.isWord = False

    def insert(self, word):
        current = self
        for letter in word:
            current = current.children[letter]
        current.isWord = True

    def search(self, word):
        searched_trie = self
        for letter in word:
            if letter not in searched_trie.children:
                return False
            searched_trie = searched_trie.children[letter]
        return searched_trie.isWord

    def startsWith(self, prefix):
        searched_trie = self
        for letter in prefix:
            if letter not in searched_trie.children:
                return False
            searched_trie = searched_trie.children[letter]
        return True
