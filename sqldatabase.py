import sqlite3
import os
import sys


class Image(object):
    def __init__(self, dbname="Images.db"):

        self.image_name = []
        self.dbname = dbname

    def load_directory(self, path='/home/hydro/person_detection-master/Pictures'):
        """
        :param path: Provide Path of File Directory
        :return: List of image Names

        """
        for x in os.listdir(path):
            self.image_name.append(x)
        return self.image_name

    def create_database(self, name, image, person):

        """
        :param name: String
        :param image:  BLOP Data
        :return: None
        """
        conn = sqlite3.connect(self.dbname)
        cursor = conn.cursor()
        cursor.execute("""

        CREATE TABLE IF NOT EXISTS my_table 

        (name TEXT,image BLOP, starttime DATETIME DEFAULT CURRENT_TIMESTAMP, endtime DATETIME DEFAULT CURRENT_TIMESTAMP, 

        person Object)""")

        cursor.execute(""" insert into my_table(`name`,`image`, `person`) values(?,?,?)""",(name,image,person))
        cursor.close()
        conn.commit()
        conn.close()
def main():

    obj = Image()
    os.chdir("./Pictures/")
for x in obj.load_directory():



        if ".png" in x:

            with open(x,"rb") as f:

                data = f.read()

                obj.create_database(name=x, image=data, person='Person')

                print("{} Added to database ".format(x))



        elif ".jpg" in x:

            with open(x,"rb") as f:

                data = f.read()

                obj.create_database(name=x,image=data, person='Person')

                print("{} added to Database".format(x))





if __name__ == "__main__":

    main()
