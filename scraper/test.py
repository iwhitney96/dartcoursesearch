from scraper import Scraper


scraper = Scraper("dartmouth_course_catalogue.html")
scraper.get_classes()
scraper = Scraper("16f.html")
scraper.get_median_grades()
