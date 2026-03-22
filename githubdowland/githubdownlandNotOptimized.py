from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url='https://github.com/FabianS-Privat/CyclonCheatSheetSite/tree/master/docs/PoE1/Act%2010/img' #switch act here

def SiteDictionarySearch(url):
    driver.get(url)
    folders=driver.find_elements(By.XPATH, '//tr[contains(@id,"folder-row")]//a')
    folderNames=[folder.get_attribute('href') for folder in folders]
    listofurls=[]
    for urls in folderNames:
        if listofurls.__contains__(urls) or urls.__contains__('blob') or urls.__contains__('commit') or not urls.__contains__('Act%2010'): # switch act here
            continue
        else:
            listofurls.append(urls)
    return listofurls
    
def GetImagesFromDictionary(url):
    driver.get(url)
    images=driver.find_elements(By.XPATH, '//tr[contains(@id, "folder-row")]//a')
    imagelinks=[image.get_attribute('href') for image in images]
    listofimages=[]
    for urls in imagelinks:
        if urls in listofimages or urls.__contains__('commit') or urls.__contains__('tree') :
            continue
        elif 'png' in urls:
            listofimages.append(urls)   
    for x in listofimages:
        if "Clean" in x or "clean" in x:
            driver.get(x)
            buttonxpath='//*[@id="repos-sticky-header"]/div[1]/div[2]/div[2]/div[1]/button[1]'
            driver.find_element(By.XPATH, buttonxpath).click()
            time.sleep(1)
        else:
            continue
        driver.back()
    return listofimages 

driver=webdriver.Chrome()
try:
    listofmaps=SiteDictionarySearch(url)
    for x in listofmaps:
        map=SiteDictionarySearch(x)
        for y in map:
            z=GetImagesFromDictionary(y)
            driver.back()
        driver.back()
    time.sleep(5)

except Exception as e:
    print(f'Error: {e}')
driver.quit()