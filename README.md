# Mission to Mars

## Preview
This application scrapes various websites for data related to Mars and displays the information in a single HTML page. 

[View Website](https://mission-mars0703.herokuapp.com/)

## Method & Usage

Step 1 - Scraping
Initial scraping is completed using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

Data source:
* The latest News from [NASA Mars News Site](https://mars.nasa.gov/news/) 
* Current Featured Mars Image from [JPL Featured Space Image](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars)     
* Mars Weather from [Mars Weather twitter account](https://twitter.com/marswxreport?lang=en)
* [Mars Facts](http://space-facts.com/mars/) about the planet including Diameter, Mass, etc. 
* High resolution images for Mar's hemispheres from [USGS Astrogeology site](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) 
    
Step 2 - MongoDB and Flask Application
Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.
