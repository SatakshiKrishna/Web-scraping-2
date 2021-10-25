from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import csv
START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"
browser = webdriver.Chrome("/Users/apoorvelous/Downloads/chromedriver")
browser.get(START_URL)
time.sleep(10)
headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date","hyperlink","planet_type","planet_radius","orbital_radius","orbital_period","eccentricity"]
planet_data = []
new_planet_data = []
def scrape():
    for i in range (0,428):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            for index, li_tag in enumerate(li_tags):
                if index == 0:
                     temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            hyperlink_li_tag = li_tags[0]
            temp_list.append("https://exoplanets.nasa.gov"+hyperlink_li_tag.find_all("a",href = True)[0]["href"])
            planet_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
def scrapemoredata(hyperlink):
    page = requests.get(hyperlink)
    soup = BeautifulSoup(page.content,"html.parser")
    temp_list = []
    for tr_tag in soup.find_all("tr",attrs = {"class":"fact_"}):
        td_tags = tr_tag.find_all("td")
scrape()       
 #with open("scrapper_2.csv", "w") as f:csvwriter = csv.writer(f)csvwriter.writerow(headers)csvwriter.writerows(planet_data)