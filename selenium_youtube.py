from selenium.webdriver import Chrome

url = 'https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Dzh-TW%26next%3D%252F&hl=zh-TW&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin'

driver = Chrome('./chromedriver')

driver.get(url)

driver.find_element_by_id('identifierId').send_keys('aegis12321.test@gmail.com')
driver.find_element_by_id('identifierNext').click()