
# ## Web Scraping Homework (Week 12)



# import dependencies

import requests
import pymongo
import pandas as pd

from splinter import Browser
from bs4 import BeautifulSoup
import time


# #### Open chrome driver

# open chrome driver browser
def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

# ## NASA Mars News - Collect Latest News Title and Paragraph Text

def scrape():
    browser = init_browser()
    
    # define url

    mars_news_url = "https://mars.nasa.gov/news/"
    browser.visit(mars_news_url)

    # create beautiful soup object 
    html = browser.html
    mars_news_soup = BeautifulSoup(html, 'html.parser')

    # find the first news title
        
    news_title = mars_news_soup.body.find("div", class_="content_title").text

    # find the paragraph associated with the first title

    news_paragraph = mars_news_soup.body.find("div", class_="article_teaser_body").text

    # print(f"The title is: \n{news_title}")
    # print()
    # print(f"The descriptive paragraph is:  \n{news_paragraph}")
            
    # ## JPL Mars Space Images

    # define the url and visit it with browser

    time.sleep(3)

    mars_image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"

    browser.visit(mars_image_url)

    # click on the Full Image button. I couldn't get it to work with partial text, so used the id.

    browser.click_link_by_id('full_image')

    # click on the more info button to get to the large image

    browser.click_link_by_partial_text('more info')

    # create the soup item

    image_html = browser.html
    mars_image_soup = BeautifulSoup(image_html, 'html.parser')

    # the large image is within the figue element with class = lede
    image = mars_image_soup.body.find("figure", class_="lede")

    # the url is within the a element, so search for a element and then extract the url
    link = image.find('a')
    href = link['href']

    # define the beginning of the url as the returned href doesn't included it
    base_url='https://www.jpl.nasa.gov'

    # create the full url
    featured_image_url = base_url + href

    featured_image_url

    # ## Mars Weather

    # open url in browser
    
    time.sleep(3)

    mars_weather_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(mars_weather_url)

    # create a soup item

    html = browser.html
    mars_weather_soup = BeautifulSoup(html, 'html.parser')

    # find the tweet text

    tweet_container = mars_weather_soup.body.find('div','js-tweet-text-container')

    mars_weather = tweet_container.find('p').text

    mars_weather


    # ## Mars Facts
    time.sleep(3)

    # define url
    mars_facts_url = "https://space-facts.com/mars/"

    # read html into pandas
    tables = pd.read_html(mars_facts_url)

    # It returns 3 tables. The first has the data needed, so will convert to a dataframe and clean up naming

    df1 = tables[0]
    df1.columns = ["Description", "Value"]

    # convert to html table

    mars_facts_html=df1.to_html()

    mars_facts_html

    # ## Mars Hemispheres

    # define url and open in browser

    time.sleep(3)

    mars_hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    browser.visit(mars_hemispheres_url)


    # #### Cerberus hemisphere

    # click on the link for the Cerberus hemisphere

    browser.click_link_by_partial_text('Cerberus')

    # click on the open button to get to enhanced picture
    browser.click_link_by_partial_text('Open')

    # create a soup item
    hemispheres_html = browser.html
    cerberus_soup = BeautifulSoup(hemispheres_html, 'html.parser')

    cerberus = cerberus_soup.body.find('img', class_ = 'wide-image')
    cerberus_img = cerberus['src']

    hem_base_url = 'https://astrogeology.usgs.gov'
    cerberus_url = hem_base_url + cerberus_img
    # print(cerberus_url)

    # #### Schiaperelli hemisphere

    # define url and open in browser

    time.sleep(3)

    mars_hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    browser.visit(mars_hemispheres_url)

    # click on the link for the Cerberus hemisphere

    browser.click_link_by_partial_text('Schiaparelli')

    # click on the open button to get to enhanced picture
    browser.click_link_by_partial_text('Open')

    # create a soup item
    schiap_html = browser.html
    schiap_soup = BeautifulSoup(schiap_html, 'html.parser')

    schiap = schiap_soup.body.find('img', class_ = 'wide-image')
    schiap_img = schiap['src']

    hem_base_url = 'https://astrogeology.usgs.gov'
    schiap_url = hem_base_url + schiap_img
    # print(schiap_url)

    # #### Syrtis hemisphere

    # define url and open in browser

    time.sleep(3)

    mars_hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    browser.visit(mars_hemispheres_url)

    # click on the link for the Cerberus hemisphere

    browser.click_link_by_partial_text('Syrtis')

    # click on the link for the Cerberus hemisphere

    browser.click_link_by_partial_text('Open')

    # create a soup item
    syrtis_html = browser.html
    syrtis_soup = BeautifulSoup(syrtis_html, 'html.parser')

    syrtis = syrtis_soup.body.find('img', class_ = 'wide-image')
    syrtis_img = syrtis['src']

    hem_base_url = 'https://astrogeology.usgs.gov'
    syrtis_url = hem_base_url + syrtis_img
    # print(syrtis_url)

    # #### Valles hemisphere

    # define url and open in browser

    time.sleep(3)

    mars_hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    browser.visit(mars_hemispheres_url)

    # click on the link for the Valles hemisphere

    browser.click_link_by_partial_text('Valles')

    # click on the link for the Valles hemisphere

    browser.click_link_by_partial_text('Open')

    # create a soup item
    valles_html = browser.html
    valles_soup = BeautifulSoup(valles_html, 'html.parser')

    valles = valles_soup.body.find('img', class_ = 'wide-image')
    valles_img = valles['src']

    hem_base_url = 'https://astrogeology.usgs.gov'
    valles_url = hem_base_url + valles_img
    # print(valles_url)


    # #### Define list of dictionaries that include each hemisphere

    hemispheres_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": valles_url},
        {"title": "Cerberus Hemisphere", "img_url": cerberus_url},
        {"title": "Schiaparelli Marineris Hemisphere", "img_url": schiap_url},
        {"title": "Syrtis Major Hemisphere", "img_url": syrtis_url}
    ]

    # I know I didn't do a good job of defining this dictionary.  My orginal definition didn't
    # allow me to use the rendered data correctly in my html app.  I didn a quick fix to get
    # it too work, but ran out of time to figure out a better way to set it up
    
    mars_dict = {
        'latestheadline': news_title,
        'latestparagraph':  news_paragraph,
        'featuredimage': featured_image_url,
        'currentweather': mars_weather,
        'factstable': mars_facts_html,
        "va_title": "Valles Marineris Hemisphere", "va_img_url": valles_url,
        "ce_title": "Cerberus Hemisphere", "ce_img_url": cerberus_url,
        "sc_title": "Schiaparelli Marineris Hemisphere", "sc_img_url": schiap_url,
        "sy_title": "Syrtis Major Hemisphere", "sy_img_url": syrtis_url 
        }

    # print(mars_dictionary)
    browser.quit()
    return mars_dict
    
