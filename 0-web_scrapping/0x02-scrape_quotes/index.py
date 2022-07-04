import mechanicalsoup

browser = mechanicalsoup.StatefulBrowser(
    soup_config = {'features': 'lxml'},
    raise_on_404 = True,
    user_agent = "MyBot: "
)

url = "http://quotes.toscrape.com"
browser.open(url)
page = browser.get_current_page()

def scrape_quotes(browser, url):
    for quote in page.find_all('div', class_ = "quote"):
        author = "Author: %s" % quote.find('span', class_ = "").small.text
        quotes = "Quote: %s" % quote.find('span', class_ = "text").text
        about_page = quote.find('span', class_ = "").a['href']
        
        print(author)
        scrape_about(browser, url + about_page)
        print(quotes)
        print("================== \n\n")
        
def scrape_about(browser, new_url):
    browser.open(new_url)
    page = browser.get_current_page()
    
    birth_date = "Birth Date: %s" % page.find('div', class_ = "author-details").find('span', class_ = "author-born-date").text

    nationality = "Nationality: %s" % page.find('div', class_ = "author-details").find('span', class_ = "author-born-location").text
    
    description = "Description: %s" %  page.find('div', class_ = "author-details").find('div', class_ = "author-description").text
    
    # outputs
    print(birth_date)
    print(nationality)
    print(description)
    
    


scrape_quotes(browser, url)