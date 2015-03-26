from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.amazon.com")
assert "Amazon" in driver.title



def getCategories(keywords):
	driver.find_element_by_name("field-keywords").clear()
	searchField = driver.find_element_by_name("field-keywords")
	searchField.send_keys(keywords)
	searchField.send_keys(Keys.RETURN)
	categories = driver.find_element_by_css_selector("ul.forExpando").text
	categories = categories.split('\n')
	return {"category":categories[0], "subCategories": categories[1:]}


category = getCategories("League of Legends")