from query_generator import QueryGenerator
from sentence_trainer import Trainer
from sys import exit, path
path.append("../database_parser")
from connect_to_mysql import MySQLConn

class Wrapper:
    conn = MySQLConn(user='', passwd='', host='', db='dummy')
    query_gen = QueryGenerator(conn = conn)
    trainer = Trainer()

    @staticmethod
    def get_query_and_result(sentence):
        query = Wrapper.trainer.get_trained_value(sentence)
        if query == None:
            Wrapper.query_gen.set_sentence(sentence)
            query = Wrapper.query_gen.generate_query()
        result = Wrapper.conn.execute_and_retrieve_data(query)
        return (query, result)

    @staticmethod
    def train_sentence(sentence, query):
        Wrapper.trainer.train(sentence, query)

if __name__ == "__main__":
    sentence = raw_input("Enter the sentence: ")
    if len(sentence.strip()) == 0:
        print("Invalid sentence!")
        exit()
    query, result = Wrapper.get_query_and_result(sentence)
    print("query is : ", query)
    print("result is : ", result)
    desired_query = raw_input("Enter the query that should have been generated: ")
    if len(desired_query.strip()) == 0:
        desired_query = query
    Wrapper.train_sentence(sentence, desired_query)
