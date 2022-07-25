from selenium import webdriver

chrome_driver="D:\chrome driver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)
# driver.get("https://www.amazon.in/ASUS-G531GU-ES511T-Graphics-i5-9300H-Windows/dp/B083P599GG/ref=sr_1_17?crid=167IJ1OI4AX20&dchild=1&keywords=asus+rog+strix+g15&qid=1630902801&sprefix=asus+rog+%2Caps%2C361&sr=8-17")
# price = driver.find_element_by_id("priceblock_ourprice")
#print(price.text)
driver.get("https://www.python.org/")
search_bar=driver.find_element_by_name("q")
print(search_bar)
print(search_bar.get_attribute("placeholder"))
driver.quit()