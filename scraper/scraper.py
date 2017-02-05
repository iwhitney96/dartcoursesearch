import urllib2
from BeautifulSoup import BeautifulSoup
import os
import pdb
from database import Database

class Scraper(object):

    def __init__(self, url):
        self.url = "file://" + os.getcwd() + "/" + url
        self.soup = self.get_soup(url)

    def get_soup(self, url):
        html = urllib2.urlopen(self.url).read()
        return BeautifulSoup(html)
    #end

    def get_classes(self):
        database = Database()
        table = self.soup.findAll('table')
        everyrow = table[0].findAll("tr")
        for row in everyrow:
            ClassInfo = row.findAll("td")
            if len(row.findAll("td")) is not 18:
                continue;
            Crn = self.assign(ClassInfo[1].text)
            Dept = self.assign(ClassInfo[2].text)
            Num = self.assign(ClassInfo[3].text)
            Sec = self.assign(ClassInfo[4].text)
            Title = self.assign(ClassInfo[5].text)
            Time = self.assign(ClassInfo[8].text)
            Instructor = self.assign(ClassInfo[11].text)
            WC = self.assign(ClassInfo[12].text)
            Dist = self.assign(ClassInfo[13].text)

            database.insert_course(Crn, Dept, Num, Title, Sec, Time, Instructor, WC, Dist)
            print Crn, Dept, Num, Title, Sec, Time, Instructor, WC,Dist


    def assign(self, text):
        if text == "&nbsp;":
            return "NONE"
        else:
            return text.replace("&nbsp;","")

    def chunk_classes(self, text):
        chunkedstring = text.split('-')
        if len(chunkedstring) is not 3:
            return -1, -1
        return chunkedstring[0], chunkedstring[1]

    def process_grades(self, grade):
        if grade == 'A':
            return 4.000
        elif grade == 'A /A-':
            return 3.836
        elif grade == 'A-':
            return 3.667
        elif grade == 'A-/B+':
            return 3.495
        elif grade == 'B+':
            return 3.333
        elif grade == 'B+/B':
            return 3.165
        elif grade == 'B':
            return 3.000
        elif grade == 'B /B-':
            return 2.836
        elif grade == 'B-':
            return 2.667
        elif grade == 'B-/C+':
            return 2.495
        elif grade == 'C+':
            return 2.333
        elif grade == 'C+/C':
            return 2.165
        elif grade == 'C':
            return 2.000
        elif grade == 'C /C-':
            return 1.836
        elif grade == 'C-':
            return 1.667
        elif grade == 'C-/D+':
            return 1.495
        elif grade == 'D+':
            return 1.333
        elif grade == 'D+/D':
            return 1.165
        elif grade == 'D':
            return 1.000
        elif grade == 'E':
            return 0.000
        else:
            return -1



    def get_median_grades(self):
        table = self.soup.findAll('table')
        everyrow = table[0].findAll("tr")
        for row in everyrow:
            ClassInfo = row.findAll("td")
            term = ClassInfo[0].text
            dept, classnum = self.chunk_classes(ClassInfo[1].text)
            if dept is -1:
                continue
            enrollment = ClassInfo[2].text
            grade = self.process_grades(ClassInfo[3].text)
            if grade == -1:
                continue

            print term, dept, classnum, enrollment, grade
