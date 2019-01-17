from selenium import webdriver

browser = webdriver.Firefox()

#Go to homepage
browser.get('http://localhost:8000')

#page title and header say: "to-do Lists"
assert 'To-Do' in browser.title, "Browser title was " + browser.title

#enter a to-do item straight away

#types an item in text box (hobby)
#hits enter, page updates, page lists: 1:"item"



#textbox: add anorther item. he types another.
#page updates, show both items in list

#site remember items? generated unique URL for him
#visit and they are still there.

#exits site
browser.quit()