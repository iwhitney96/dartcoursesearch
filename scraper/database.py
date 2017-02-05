import MySQLdb
import pdb
from mysql.connector import MySQLConnection, Error


class Database(object):
    host = 'localhost'
    user = 'root'
    password = ''
    db = 'dartcoursesearch'

    def __init__(self):
        self.connection = MySQLdb.connect(self.host, self.user, self.password, self.db)
        self.cursor = self.connection.cursor()

    def insert_course(self, Crn, Dept, Num, Title, Sec, Time, Instructor, WC, Dist):
        try:
            #pdb.set_trace()
            query = """INSERT INTO 17s (crn,coursedept,coursenum,coursetitle,coursesec,coursetime,instructor,wc,dist) VALUES (%d, %s, %f, %s, %s, %s, %s, %s, %s)""" % (int(Crn), "\"" + str(Dept) + "\"", float(Num), "\"" + str(Title) + "\"", "\"" + str(Sec) + "\"", "\"" + str(Time) + "\"", "\"" + str(Instructor) + "\"", "\"" + str(WC) + "\"","\"" + str(Dist) + "\"")
            self.cursor.execute(query)
            self.connection.commit()
        except Error as error:
            pdb.set_trace()

            self.connection.rollback()

'''
CREATE TABLE 17s(
    crn MEDIUMINT,
    coursedept TINYTEXT,
    coursenum FLOAT,
    coursetitle TINYTEXT,
    coursesec TINYTEXT,
    coursetime VARCHAR(100),
    instructor VARCHAR(100),
    wc VARCHAR(10),
    dist VARCHAR(10)
    );


INSERT QUERY
query = """INSERT INTO 17s (crn,coursedept,coursenum,coursetitle,coursesec,coursetime,instructor,wc,dist) VALUES (%d, %s, %f, %s, %s, %s, %s, %s, %s)""" % (int(Crn), "\"" + str(Dept) + "\"", float(Num), "\"" + str(Title) + "\"", "\"" + str(Sec) + "\"", "\"" + str(Time) + "\"", "\"" + str(Instructor) + "\"", "\"" + str(WC) + "\"","\"" + str(Dist) + "\"")

'''
