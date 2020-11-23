from selenium import webdriver


for i in range(20000):
    options = webdriver.ChromeOptions()
    options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
    options.add_argument("--incognito")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    browser = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'),options=options)
    browser.get('https://vote.globesoccer.com/vote/2020-century-player')
    scroll_el= browser.find_element_by_xpath('/html/body/div/div/div[2]/form/div/label[10]')
    messi_el = browser.find_element_by_xpath('/html/body/div/div/div[2]/form/div/label[14]')
    messi_el.click();
    browser.find_element_by_xpath('/html/body/div/div/div[2]/div/button').click();
    print(i)
    browser.quit()
