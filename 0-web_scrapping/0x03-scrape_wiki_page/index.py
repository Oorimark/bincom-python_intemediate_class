import mechanicalsoup

browser = mechanicalsoup.StatefulBrowser(
    soup_config = {'features': 'lxml'},
    raise_on_404 = True,
    user_agent = "MyBot"
)

url = "https://en.wikipedia.org/wiki"

def format_word(word):
    return word.replace(" ","_")

def search_in_wiki(word):
    browser.open(url + format_word(word))
    page = browser.get_current_page()
    topic = page.find('h1', id = "firstHeading").text
    print(topic)
    content = page.find('div', id = "mw-content-text").text
    return content


result = search_in_wiki('software engineering')
print(result)