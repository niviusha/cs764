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

  # Get the nouns in the sentence
  def get_nouns(self, sentence=None):
    pos_tagged = self.get_pos_tagged(sentence)
    nouns = []
    for pair in pos_tagged:
      if "NN" in pair[1] or pair[1] == "VBZ":
        nouns.append(pair[0])
    return nouns

  # Returns the list of synonyms for a word using wordnet
  def get_synonyms(self, word):
    return set([str(syn.name().split('.')[0]) for syn in wordnet.synsets(word)])

  def _get_sentence(self, sentence):
    if sentence == None:
      return self.sentence
    return sentence

  def _parse_nltk_tree(self, tree_instance):
    sentence_part = ' '.join([part[0] for part in tree_instance.leaves()])
    return tuple([tree_instance.label(), sentence_part])

if __name__ == '__main__':
  sentence = "What airlines run in the US?"
  obj = SentenceOps(sentence)
  print(obj.get_named_entities())
  print(obj.get_pos_tagged())
  print(obj.get_synonyms('dog'))
  print(obj.get_nouns())
