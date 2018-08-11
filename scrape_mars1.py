from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import requests
import pymongo
import tweepy
import json
from config import (consumer_key, consumer_secret, 
                    access_token, access_token_secret)


def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    listings = []
    itemobject={}
    
    # url2 = "https://mars.nasa.gov/news/"
    # browser.visit(url2)
    # html=browser.html
    # news_soup = BeautifulSoup(html, 'lxml')
    # results = news_soup.find_all('div', class_='list_text')
    # article_title=[]
    # article_content=[]
    # for result in results:
    #     news_title = result.find('div', class_='content_title').text
    #     news_p = result.find('div', class_='article_teaser_body').text
    #     article_title.append(news_title)
    #     article_content.append(news_p)
    # itemobject['title']= article_title[0]
    # itemobject['p']=article_content[0]


    url2 = 'https://mars.nasa.gov/news/'
    browser.visit(url2)
    html = browser.html
    news_soup = BeautifulSoup(html, 'html.parser')
    news_title = news_soup.find('div', class_='content_title').text
    news_p = news_soup.find('div', class_='article_teaser_body').text
    itemobject['title'] = news_title
    itemobject['p'] = news_p


    # url2 = "https://mars.nasa.gov/news/"
    # browser.visit(url2)
    # html=browser.html
    # news_soup = BeautifulSoup(html, 'html.parser')
    # results = news_soup.find_all('div', class_='list_text')
    # article_title=[]
    # article_content=[]
    # article = {}
    # for result in results:
    #     news_title = result.find('div', class_='content_title').text
    #     news_p = result.find('div', class_='article_teaser_body').text
    #     article_title.append(news_title)
    #     article_content.append(news_p)
    # article['title'] = article_title[0]
    # article['p'] = article_content[0]
    # itemobject['article']= article

    # url2 = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    # browser.visit(url2)
    # html = browser.html
    # soup = BeautifulSoup(html,'lxml')
    # news={}
    # all_news=[]
    # results = soup.find_all('div', class_='list_text')
    # for result in results:
    #     news_title = result.find('div', class_='content_title').text
    #     news_p = result.find('div', class_='article_teaser_body').text
    #     news = {
    #         'title':news_title,
    #         'p':news_p
    #             }
    #     all_news.append(news.copy())
    # itemobject['news']= all_news
    
    url1 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url1)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    image_url = soup.find('article',class_='carousel_item')['style']
    featured_image_url='https://www.jpl.nasa.gov' + image_url[23:75]
    itemobject['featured_image_url']=featured_image_url

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
    target_user = "@MarsWxReport"
    mars_weather = []
    public_tweets = api.user_timeline(target_user, result_type="recent")
    for tweet in public_tweets:
        if list(tweet["text"])[0]=="S" and list(tweet["text"])[1]=="o" and list(tweet["text"])[2]=="l":
            mars_weather.append(tweet["text"])
    itemobject['mars_weather']= mars_weather[0]


    url3='https://space-facts.com/mars/'
    tables = pd.read_html(url3)
    df = tables[0]
    df.columns = ['Description', 'Value']
    df.set_index('Description', inplace=True)
    mars_table = df.to_html()
    itemobject['mars_table']= mars_table
    

    url4='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    response = requests.get(url4)
    usgs_soup = BeautifulSoup(response.text, 'html.parser')
    results = usgs_soup.find_all('div', class_="item")
    hemisphere_image_urls = []
    info={}
    for item in results:
        link= item.a['href']
        title =item.find('h3').text
        url5 = 'https://astrogeology.usgs.gov/' + link
        response = requests.get(url5)
        soup = BeautifulSoup(response.text, 'html.parser')
        more_info = soup.find_all('div', class_="wide-image-wrapper")
        for item in more_info:
            img_url = item.find('li').a['href']
            info = {
            'title':title,
            'img_url':img_url
            }
            hemisphere_image_urls.append(info.copy())
    itemobject['hemisphere']= hemisphere_image_urls

    listings.append(itemobject.copy())
    return listings

    
    

