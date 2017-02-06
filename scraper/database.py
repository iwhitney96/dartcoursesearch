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
            query = """INSERT INTO 17s (crn,coursedept,coursenum,coursetitle,coursesec,coursetime,instructor,wc,dist) VALUES (%d, %s, %f, %s, %s, %s, %s, %s, %s)""" % (int(Crn), "\"" + str(Dept) + "\"", float(Num), "\"" + str(Title) + "\"", "\"" + str(Sec) + "\"", "\"" + str(Time) + "\"", "\"" + str(Instructor) + "\"", "\"" + str(WC) + "\"","\"" + str(Dist) + "\"")
            self.cursor.execute(query)
            self.connection.commit()
        except Error as error:
            self.connection.rollback()

    def insert_median(self, Term, Dept, Num, Median, Enrollment):
        try:
            query = """INSERT INTO medians (term,coursedept,coursenum,median,enrollment) VALUES (%s, %s, %f, %f, %d)""" % ("\"" + str(Term) + "\"", "\"" + str(Dept) + "\"", float(Num), float(Median), int(Enrollment))
            self.cursor.execute(query)
            self.connection.commit()
        except Error as error:
            self.connection.rollback()
