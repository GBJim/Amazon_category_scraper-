from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://www.amazon.com")

assert "Amazon" in driver.title



def getCategories(keywords, timesout=10):
	driver.find_element_by_name("field-keywords").clear()
	searchField = driver.find_element_by_name("field-keywords")
	searchField.send_keys(keywords)
	searchField.send_keys(Keys.RETURN)
	wait = WebDriverWait(driver, timesout)
	stopWord = "+ See more"

	try:
		wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "forExpando")))

		#wait.until(EC.presence_of_element_located((By.CLASS_NAME,'childRefinementLink'),))

		
	except:
		return "Time Limit Exceeded"

	categories = driver.find_element_by_css_selector("ul.forExpando").text
	categories = categories.split('\n')
	try:
		categoryEnd = categories.index("+ See more")
	except:
		categoryEnd = None
	return {"category":categories[0], "subCategories": categories[1:categoryEnd]}




category = getCategories("League of Legends")
print(getCategories("survival guide"))
print(getCategories("hiking guide"))