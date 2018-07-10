__author__ = 'Ellisa Khoja'

from cassandra.cluster import Cluster
import datetime,pandas as pd


KEYSPACE = 'mykeyspace'

class Cassandra_waveforms:



    def query_waveforms(self,param_1, param_2, param_3, param_4):

        cluster = Cluster(['127.0.0.1'])
        session = cluster.connect(KEYSPACE)

        session.set_keyspace(KEYSPACE)


        if param_1 ==  'something':
            rslt = session.execute("select x,y from table where param_1 =%s  and param_2 =%s   ",
                                   (param_1, param_2))
        elif param_2 == 'something':
            rslt = session.execute("select x,y from table where param_1 =%s  and param_2 =%s   ",
                                   (param_1, param_2))

        df = pd.DataFrame(list(rslt))


        print (df.head())


        print(len(df))

        return df

if __name__ == "__main__":
    Cassandra_waveforms.query_waveforms('1','2','3','4')





