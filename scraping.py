
###############################################
# This script is used to scrape a test        #
# website and decrypt any messages contained  #
# within the html of the site                 #
###############################################


# import libraries needed to simplify the scraping process
import requests
import bs4


def get_hidden_message():

    # Create a GET request to https://www.thegoldbugs.com/blog,
    # if the response is successful assign it to a response variable
    blog_url = 'https://www.thegoldbugs.com/blog'
    response = requests.get(blog_url)

    # Parse response using Beautiful Soup object and use it's methods to extract 
    # the HTML text from the site. 
    soup = bs4.BeautifulSoup(response.text, 'lxml')

    # Select the CSS class and the pre tag contained in this class
    # to create a list with one element that contains all text within the pre tag
    # as well as the tag itself
    blog = soup.select('.sqs-block-content > pre')

    
    # Extract text from list and remove any tags from HTML
    text = blog[0].getText()

    # Create empty string to hold decrypted text. 
    # Loop through text that is split on '-----'
    # Skip the first element since it is empty
    # Then grab the first character of each element
    # and add that character to the result string 
    result = ''
    for sentence in text.split('-----')[1:]:
        result += sentence[0]
    return result


# Print the result of the decrypted text
print(get_hidden_message())