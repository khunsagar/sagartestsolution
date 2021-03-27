from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\\Users\\QA\\PycharmProjects\\Zipmex_test\\drivers\\chromedriver.exe')
# URL of the website
url = "https://trade.zipmex.com/trade/"
driver.maximize_window()
# opening link in the browser
driver.get(url)
driver.refresh()
driver.implicitly_wait(30)
driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[1]/div[8]').click()
print("Trade ", driver.find_element_by_xpath('//span[@class="instrument-selector__symbol"]').text)
print("with side = Buy")
BuyValue = driver.find_element_by_xpath(
    '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[6]/div[3]/div[1]').text
FloatBuyValue = float(BuyValue)
Percentage = FloatBuyValue * 0.001
Newprice = FloatBuyValue + Percentage
roundnewstring = round(Newprice, 4)
print("With Price ", roundnewstring)
NepriceSring = str(roundnewstring)
driver.find_element_by_xpath(
    '//*[@id="root"]/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/form[1]/div[1]/div[1]/div/div/div[2]/input').clear()
driver.find_element_by_xpath(
    '//*[@id="root"]/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/form[1]/div[1]/div[1]/div/div/div[2]/input').send_keys(
    str(NepriceSring))

driver.find_element_by_xpath(
    '//*[@id="root"]/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/form[1]/div[1]/div[2]/div/div/div[2]/input').clear()
withamount = 1.0
withamountstr = str(withamount)
driver.find_element_by_xpath(
    '//*[@id="root"]/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/form[1]/div[1]/div[2]/div/div/div[2]/input').clear()
driver.find_element_by_xpath(
    '//*[@id="root"]/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/form[1]/div[1]/div[2]/div/div/div[2]/input').click()
driver.find_element_by_xpath(
    '//*[@id="root"]/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/form[1]/div[1]/div[2]/div/div/div[2]/input').send_keys("1.0")
print("with amount ", withamount)
TotalAmount = round(roundnewstring * withamount,1)
TotalAmountString = str(TotalAmount)
print("TotalAmount ", TotalAmount)

print("===========================Sell Side========================================")


print("Trade ", driver.find_element_by_xpath('//span[@class="instrument-selector__symbol"]').text)
print("with side = Sell")
SellValue1 = driver.find_element_by_xpath(
    '//*[@id="root"]/div[1]/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div[2]/div[3]/div[1]/div[3]/div[1]').text
FloatBuyValue1 = float(SellValue1)
Percentage1 = FloatBuyValue1 * 0.001
Newprice1 = (FloatBuyValue1) - (Percentage1)
roundnewstring1 = round(Newprice1, 4)
print("With Price ", roundnewstring1)
NepriceSring1 = str(roundnewstring1)
driver.find_element_by_xpath(
    '//*[@id="root"]/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/form[2]/div[1]/div[1]/div/div/div[2]/input').clear()
driver.find_element_by_xpath(
    '//*[@id="root"]/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/form[2]/div[1]/div[1]/div/div/div[2]/input').send_keys(
    str(NepriceSring1))

driver.find_element_by_xpath(
    '//*[@id="root"]/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/form[1]/div[1]/div[2]/div/div/div[2]/input').clear()
withamount1 = 1.0
withamountstr1 = str(withamount1)
driver.find_element_by_xpath(
    '//*[@id="root"]/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/form[2]/div[1]/div[2]/div/div/div[2]/input').clear()
driver.find_element_by_xpath(
    '//*[@id="root"]/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/form[2]/div[1]/div[2]/div/div/div[2]/input').click()
driver.find_element_by_xpath(
    '//*[@id="root"]/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/form[2]/div[1]/div[2]/div/div/div[2]/input').send_keys("1.0")
print("with amount ", withamount1)
TotalAmount1 = round(roundnewstring1 * withamount1,1)
TotalAmountString1 = str(TotalAmount1)
print("TotalAmount ", TotalAmount1)