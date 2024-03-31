from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import cv2 as cv


def show_images(query, n_query):
    # Creating a webdriver instance
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(options=options)
    driver.get("https://images.google.com/")

    box = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
    box.send_keys(query)
    box.send_keys(Keys.ENTER)

    def scroll_to_bottom():

        last_height = driver.execute_script(
            "\
        return document.body.scrollHeight"
        )

        while True:
            driver.execute_script(
                "\
            window.scrollTo(0,document.body.scrollHeight)"
            )

            # waiting for the results to load
            # Increase the sleep time if your internet is slow
            time.sleep(3)

            new_height = driver.execute_script(
                "\
            return document.body.scrollHeight"
            )

            # click on "Show more results" (if exists)
            try:
                driver.find_element_by_css_selector(".YstHxe input").click()

                # waiting for the results to load
                # Increase the sleep time if your internet is slow
                time.sleep(3)

            except:
                pass

            # checking if we have reached the bottom of the page
            if new_height == last_height:
                break

            last_height = new_height

    # scroll_to_bottom()

    for i in range(2, n_query + 2):
        try:
            obj = driver.find_element(
                By.XPATH, '//*[@id="islrg"]/div[1]/div[' + str(i) + "]/a[1]/div[1]/img"
            )
            obj.click()
            img = driver.find_element(
                By.XPATH,
                '//*[@id="Sva75c"]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div/div[3]/div[1]/a/img[1]',
            )
            img.screenshot(
                "D:/Ameya/MS/NEU/[1]Academics/Sem 2/Innovate Hackaton/images/"
                + query
                + str(i)
                + ".png"
            )
            time.sleep(0.2)

        except:
            continue

    # Finally, we close the driver
    driver.close()


if __name__ == "__main__":
    show_images("dog", 4)
