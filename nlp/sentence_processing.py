"""
This file is for processing the given sentence.

After installing nltk, you will need to run nltk.download in
the python command line for the functions to work.
"""
from nltk.corpus import wordnet
import nltk

class SentenceOps:
  def __init__(self, sentence):
    self.sentence = sentence

  # Splits the sentence on a word basis
  def get_tokens(self, sentence=None):
    sentence = self._get_sentence(sentence)
    return nltk.word_tokenize(sentence)

  # Assigns POS tags to the sentence
  def get_pos_tagged(self, sentence=None):
    return nltk.pos_tag(self.get_tokens(sentence))

  # Gets just the NER portions of the sentence
  def get_named_entities(self, sentence=None):
    ner_tagged = nltk.chunk.ne_chunk(self.get_pos_tagged(sentence))
    ner_portion = []
    for entity in ner_tagged:
      if isinstance(entity, nltk.tree.Tree):
        ner_portion.append(self._parse_nltk_tree(entity))
    return ner_portion

  def _get_sentence(self, sentence):
    if sentence == None:
      return self.sentence
    return sentence

  def _parse_nltk_tree(self, tree_instance):
    sentence_part = ' '.join([part[0] for part in tree_instance.leaves()])
    return tuple([tree_instance.label(), sentence_part])

  # Returns the list of synonyms for a word using wordnet
  def get_synonyms(self, word):
    return set([str(syn.name().split('.')[0]) for syn in wordnet.synsets(word)])

if __name__ == '__main__':
  sentence = "At eight o'clock on Thursday morning Arthur James didn't feel very good in India."
  obj = SentenceOps(sentence)
  print(obj.get_named_entities())
  print(obj.get_synonyms('dog'))
