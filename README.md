## Dartcoursesearch -- making class selection better

## How to set up this project for the first time
Clone the github repository

### Install dependencies
``` brew install mysql ```

``` pip install -r requirements.txt ```

#### Set up Virtual Environment
``` virtualenv venv ```


### To start the project
. ./venv/bin/activate


### Notes on data processing:
To update for a new term go to the Dartmouth Timetable of Classes and open
the page for the upcoming term. Then right click and view page source. Download
the HTML and copy it into a document. Search for ``` <div class="data-table"> ```
and then delete everything above that line. find the next ``` </table> ``` and
then delete everything below that line. Then do find and replace ```</tr>``` with ```</tr><tr>``` Then run the document through the scraper



### Setup Database
1. ``` mysqld_safe ```
2. ``` mysql -u root ``` in new terminal window
3. ``` CREATE DATABASE dartcoursesearch; ```
4. ``` SET PASSWORD FOR 'root'@'localhost' = PASSWORD(''); ```
5. ``` CONNECT dartcoursesearch; ```
6. ```
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
```
```
CREATE TABLE medians(
    term TINYTEXT,
    coursedept TINYTEXT,
    coursenum FLOAT,
    median FLOAT,
    enrollment SMALLINT
    );
```


### Notes on Database Troubles

If you get the message
```
ImportError: dlopen(/Users/USER/Documents/dartcoursesearch/venv/lib/python2.7/site-packages/_mysql.so, 2): Library not loaded: libcrypto.1.0.0.dylib
  Referenced from: /Users/ianwhitney/Documents/dartcoursesearch/venv/lib/python2.7/site-packages/_mysql.so
  ```
run the following command in your terminal
``` sudo ln -s /usr/local/Cellar/openssl/1.0.2j/lib/libcrypto.1.0.0.dylib /usr/local/lib/libcrypto.1.0.0.dylib ```
