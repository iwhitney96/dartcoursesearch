from scraper import Scraper


scraper = Scraper("dart_course_catalogue.html")
scraper.get_courses()
scraper = Scraper("16f.html")
scraper.get_median_grades()
