"""
This class takes in the keywords and tries to
generate a query
"""
from __future__ import print_function
import sys
sys.path.append("../database_parser")
from connect_to_mysql import MySQLConn
from database_processor import DatabaseOps
from table_processor import TableOps
from sentence_processing import SentenceOps

class QueryGenerator:
  def __init__(self, sentence):
    self.conn = MySQLConn(user='', passwd='', host='', db='')
    self.dbops = DatabaseOps(self.conn)
    self.tbops = TableOps(self.conn)
    self.sentops = SentenceOps(sentence)
    self.sentence = sentence

  # Right now we are restricting the
  # sentence to questions. Based on this
  # how, wh-: how would accumulate to
  # counting and wh- questions would be
  # selects with some condition
  # there are two type: select and count
  def get_query_type(self):
    if "how" in sentence:
      return "count"
    return "select"

  # Gets the relations that are relevant for the
  # purpose of query generation
  def get_relevant_relations(self):
    possible_rels = self.sentops.get_nouns()
    all_relations = [rel.lower() for rel in self.dbops.get_all_tables()]
    relevant_relations = set()
    for rel in possible_rels:
      rel_synonyms = self.sentops.get_synonyms(rel)
      for word in rel_synonyms:
        if word in all_relations:
          relevant_relations.add(word)
    return relevant_relations

  # Gets the attributes and the value that should
  # match with the specific query
  def get_compatible_attributes(self):
    possible_attribute_value = self.sentops.get_nouns()
    relevant_relation = self.get_relevant_relations()
    attr_pairing = {}
    for rel in relevant_relation:
      cols = self.tbops.get_columns(rel)
      for col in cols:
        col_values = list()
        for val in  self.tbops.get_distinct_column_data(col, rel):
            try:
              if '"' in val:
                col_values.append(val[1:-1])
            except:
                col_values.append(val)
        for pos_word in possible_attribute_value:
            pos_word_syn = self.sentops.get_synonyms(pos_word)
            pos_word_syn.add(pos_word)
            word = self._check_presence(pos_word, col_values)
            if word != None:
                if pos_word not in attr_pairing:
                    attr_pairing[pos_word] = list()
                attr_pairing[pos_word].append((rel + '.' + col, word))
                break
    self.filter_attr_pairing(attr_pairing)
    return attr_pairing

  def get_relevant_entity_map(self):
    entities = self.sentops.get_named_entities()
    entity_relevant = {
      'person': ['name'],
      'location': ['city', 'country'],
      'time': ['timezone'],
      'gsp': ['city', 'country'],
      'gpe': ['city', 'country'],
    }
    entity_map = {}
    for entity in entities:
      entity_map[entity[1]] = entity_relevant[entity[0].lower()]
    return entity_map

  def generate_query(self):
    relations = self.get_relevant_relations()
    entities = self.sentops.get_named_entities()
    attribute_relation = self.filter_attr_pairing(self.get_compatible_attributes())
    query = 'select * from ' + ','.join(relations) + ' where ' + self.generate_where_string(attribute_relation)
    return query

  def generate_where_string(self, attribute_relation):
    string_types = ['varchar', 'char']
    where_string = ''
    for attr_rel in attribute_relation:
        table, col = attr_rel[0].split('.')
        data_type = self.tbops.get_column_data_type(col, table)
        if data_type in string_types:
          where_string += str(attr_rel[0]) + ' = "' + str(attr_rel[1]) + '"'
        else:
          where_string += str(attr_rel[0]) + ' = ' + str(attr_rel[1])
    return where_string

  def filter_attr_pairing(self, attr_pairing):
    final_pairs = []
    entity_map = self.get_relevant_entity_map()
    for (k,v) in attr_pairing.items():
        if len(v) > 1:
            for vals in v:
                if vals[0].split('.')[1] in entity_map[k]:
                    final_pairs.append(vals)
                    break
    return final_pairs

  def _check_presence(self, word, values):
    if word in values:
        return word
    if type(word) != type(values[0]):
        return None
    for val in values:
        if val == None:
            continue
        if word.lower() == val.lower():
            return val
        if word.lower() == ("_".join(val.split())).lower():
            return val
        first_letter_abbr = "".join([part[0] for part in val.split()])
        if word.lower() == first_letter_abbr.lower():
            return val
    return None

if __name__ == "__main__":
    sentence = "How many airports in US?"
    query_gen = QueryGenerator(sentence)
    query = query_gen.generate_query()
    print(sentence)
    print(query)
