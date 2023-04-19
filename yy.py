from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

url = "playlist link"


options = webdriver.ChromeOptions()

driver = webdriver.Chrome(executable_path="chromedriver path", options = options)


try:
    driver.get(url=url)
    driver.maximize_window()
    time.sleep(3)
    cancel_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[17]/div/span").click()


    #action = ActionChains(driver)
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    with open("pars_code_YANDEX_music.html", "w") as file:
        file.write(driver.page_source)


    #end_of_site = driver.find_element(By.XPATH, "/html/body/mvid-root/div/mvid-primary-layout/mvid-layout/div/div[2]/mvid-footer-container/mvid-footer/footer/div/div[1]/div/a/img")
    #action.move_to_element(end_of_site).perform()


    time.sleep(500)
except Exception as ex:
    print(ex)
finally:
        driver.close()
        driver.quit()
