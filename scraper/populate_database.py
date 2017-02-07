from scraper import Scraper
from database import Database
import pdb


median_data = ["16f.html", "16x.html", "16s.html", "16w.html","15f.html", "15x.html", "15s.html", "15w.html","14f.html", "14x.html"]
for term in median_data:
    scraper = Scraper(term)
    scraper.add_median_grades()

scraper = Scraper("dartmouth_course_catalogue.html")
scraper.add_classes()
