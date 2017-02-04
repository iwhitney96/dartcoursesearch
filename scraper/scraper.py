import urllib2
from BeautifulSoup import BeautifulSoup
import os
import pdb

class Scraper(object):

    def __init__(self, url):
        self.url = "file://" + os.getcwd() + "/" + url
        self.soup = self.get_soup(url)

    def get_soup(self, url):
        html = urllib2.urlopen(self.url).read()
        return BeautifulSoup(html)
    #end

    def get_row(self):
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
            print Crn, Dept, Num, Sec, Time, Instructor, WC,Dist

    def assign(self, text):
        if text == "&nbsp;":
            return "NONE"
        else:
            return text.replace("&nbsp;","")
