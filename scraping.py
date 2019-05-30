
###############################################
# This script is used to scrape a test        #
# website and decrypt any messages contained  #
# within the html of the site                 #
###############################################


# import libraries needed to simplify the scraping process
import requests
import bs4


# Use methods within the requests library to obtain html from https://www.thegoldbugs.com
# Before making the request check to see what endpoint contains the encrypted message.
# Once the proper html is recieved via a get request use the Beautiful Soup library
# to parse the HTML. It is neccessary to view the website's source code to
# determine which tag, tags or classes which encapsulte the encrypted message. After the appropriate tags
# are found, use select method in Beautiful Soup to extract any data within the tags or CSS classes.
# Finally determine how to decrypt the message based on information found within the site.

def get_html():
    blog_url = 'https://www.thegoldbugs.com/blog'
    res = requests.get(blog_url)

    soup = bs4.BeautifulSoup(res.text, 'lxml')
    blog = soup.select('.sqs-block-content > pre')

    text = blog
    print(text)

get_html()