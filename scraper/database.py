import MySQLdb
import pdb
from mysql.connector import MySQLConnection, Error


class Database(object):
    host = 'localhost'
    user = 'root'
    password = ''
    db = 'dartcoursesearch'

    def __init__(self, term="17s"):
        self.connection = MySQLdb.connect(self.host, self.user, self.password, self.db)
        self.cursor = self.connection.cursor()
        self.term = term

    def insert_course(self, Crn, Dept, Num, Title, Sec, Time, Instructor, WC, Dist, median):
        try:
            query = """INSERT INTO %s (crn,coursedept,coursenum,coursetitle,coursesec,coursetime,instructor,wc,dist,median) VALUES (%d, %s, %f, %s, %s, %s, %s, %s, %s, %f)""" % (str(self.term), int(Crn), "\"" + str(Dept) + "\"", float(Num), "\"" + str(Title) + "\"", "\"" + str(Sec) + "\"", "\"" + str(Time) + "\"", "\"" + str(Instructor) + "\"", "\"" + str(WC) + "\"","\"" + str(Dist) + "\"", float(median))
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

    def get_class_list(self):
        try:
            query = """SELECT * FROM %s;""" % (self.term)
            self.cursor.execute(query)
            classes = []
            for (crn,coursedept,coursenum,coursetitle,coursesec,coursetime,instructor,wc,dist,medians) in self.cursor:
                row = []
                row.append(crn)
                row.append(coursedept)
                row.append(coursenum)
                row.append(coursetitle)
                row.append(coursesec)
                row.append(coursetime)
                row.append(instructor)
                row.append(wc)
                row.append(dist)
                row.append(medians)
                classes.append(row)
            return classes
        except Error as error:
            self.connection.rollback()

    def get_array_medians(self, dept, num):
        try:
            query = """SELECT * FROM medians where coursedept = "%s" and coursenum = %f""" % (dept, float(num))
            self.cursor.execute(query)
            classes = []
            for (term, coursedept, coursenum, median, enrollment) in self.cursor:
                row = []
                row.append(term)
                row.append(coursedept)
                row.append(coursenum)
                row.append(median)
                row.append(enrollment)
                classes.append(row)
            return classes
        except Error as error:
            self.connection.rollback()

    def get_median(self, dept, num):
        medians = self.get_array_medians(dept, num)
        if len(medians) is 0:
            return -1
        total = 0
        for row in medians:
            total += row[3]
        return total/len(medians)

    def close(self):
        self.cursor.close()
