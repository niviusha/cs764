import sys
sys.path.append("../database_parser")
from connect_to_mysql import MySQLConn
from table_processor import TableOps
from helper import parse_query_data

class Trainer:
    def __init__(self):
        self.conn = MySQLConn(user='', passwd='', host='127.0.0.1', db='train')
        self.tbops = TableOps(self.conn)

    def train(self, sentence, query):
        values = "'" + sentence + "'" + "," + "'" + query + "'"
        self.tbops.insert_into_table("train", values)

    def get_trained_value(self, sentence):
        db_query = "select query from train where sentence = '" + sentence + "'"
        sentence_query = parse_query_data(self.conn.execute_and_retrieve_data(db_query))
        if len(sentence_query) == 0:
            return None
        return sentence_query[0]

    def get_all_train_data(self):
        return self.conn.execute_and_retrieve_data("select * from train")

if __name__ == "__main__":
    trainer = Trainer()
    trainer.train("tihs", "trial")
    print(trainer.get_trained_value('tihs'))
