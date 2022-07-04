import mechanicalsoup

browser = mechanicalsoup.StatefulBrowser(
    soup_config = {'features': 'lxml'},
    raise_on_404 = True,
    user_agent = "MyBot: "
)

# This functions are made in the util due to their frequent re

""" 
 * printing_format: stlye output
 
 * description: The does the printing in a nicer way
"""
def printing_format(n, *arg):
    print("\n====== page %d ======" % (n),)
    for list in arg:
        print(list)
    print("===== end of page %d ==== \n" % (n),)

"""
 * Description outputs the number of the giving pages
"""
def print_pages(browser,url,  n =5 ):
    browser.open(url)
    page = browser.get_current_page()
    
    tracker = 0
    
    while(tracker < n):
        parent = page.find_all('article')
        # scrape from parent
        for children in parent:
            book_title = "Title: %s" % (children.h3.text)
            star_rating = "Star Rating: %s" % children.p['class'][1]
            stalk_status = "Stalk Status: %s" % children.find('div', class_ = "product_price").find('p', class_ = "instock availability").i['class'][0][5:]
            price = "Price : %s" % children.find('div', class_ = "product_price").find('p', class_ = "price_color").text 
            #output
            printing_format(tracker, book_title, star_rating, stalk_status, price)

        # moving to the next page
        next_page = url + "/" + page.find_all('li', class_ = "next")[0].a['href']

        print("NEXT PAGE: " + next_page)
        # check page number
        # this is so because the link to page one and the rest are different
        if(next_page[-11:] != "page-2.html"):
            next_page = url + "/catalogue/" + page.find_all('li', class_ = "next")[0].a['href']
        
        print("======= %s ends totally =====" % next_page[len(url) + 1:])
        browser.open(next_page)
        page = browser.get_current_page()
        
        tracker += 1
        ...
    ...