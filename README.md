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
