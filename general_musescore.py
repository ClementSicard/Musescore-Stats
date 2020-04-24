from time import sleep
import platform
from os import system, get_terminal_size
import sys
import re
from selenium.common.exceptions import TimeoutException, InvalidArgumentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver

clear_command = "cls" if platform.system() == "Windows" else "clear"
system(clear_command)
print("Setting things up...")


def print_user_stats(username, nb_followers, nb_following, nb_scores):
    system(clear_command)
    s = "*" * 35 + " " + username + " " + "*" * 35
    print(s)
    for k, v in {"Followers": nb_followers, "Following": nb_following, "Number of scores": nb_scores}.items():
        print(k.upper() + ": " + str(v).rjust(23 - len(k), ' '))


try:
    width, height = get_terminal_size(0)
except OSError:
    width, height = get_terminal_size(1)
except:
    print("Could not get terminal sizes. Exiting")
    quit()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(
    '--executable-path="C://Users//cleme//Documents//Chromedriver//chromedriver.exe"')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--log-level=OFF')
chrome_options.add_argument('--window-size=1920x1080')
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=chrome_options)
print("Everything is ok!\n")

# while True:
while True:
    try:
        username = input(
            "Please enter a valid Musescore username/ID : \n> ")
        if username.isnumeric():
            driver.get('https://musescore.com/user/' + username)
            if len(driver.find_elements_by_class_name("error-page")) != 0:
                raise Exception()
            else:
                break
        else:
            driver.get('https://musescore.com/' + username)
            if len(driver.find_elements_by_class_name("error-page")) != 0:
                raise Exception()
            else:
                break
    except (KeyboardInterrupt, EOFError):
        system(clear_command)
        print("Quitting. Goodbye!")
        driver.quit()
        sleep(2)
        sys.exit()
    except:
        print("\nError: user not found or page could not be loaded. Please try again later or try inputting user ID directly.\n")

print("Loading userpage for user", username, "...")

user_class_name = "_3-vzW"
user_details_class_name = "k1Ae2"

user_name = driver.find_elements_by_class_name(user_class_name)[0].text
user_details = driver.find_elements_by_class_name(user_details_class_name)

nb_followers = int(user_details[0].text)
nb_following = int(user_details[1].text)
nb_scores = int(user_details[2].text)
print_user_stats(user_name, nb_followers, nb_following, nb_scores)

sheet_music_url = driver.find_element_by_partial_link_text('Sheet')
if nb_scores == 0:
    print("\n" + user_name + " has not published any scores yet.")
    # break
    quit()
sheet_music_url.click()

sheets = driver.find_elements_by_tag_name('article')

views = dict()
dow = dict()
lect = dict()
comm = dict()
fav = dict()

for sheet in sheets:
    line = sheet.text.split("\n")
    if "pro" in line:
        line.remove("pro")
    if "Original" in line:
        line.remove("Original")
    name = line[0]
    stats = re.split('[^a-zA-Z0-9 :,]', line[2])
    stats = [s.strip() for s in stats]
    views[name] = int(re.sub("[^0-9]", "", stats[4]))
    fav[name] = int(re.sub("[^0-9]", "", stats[5]))

    # views : 5
    # favorites: 6


# break


# driver.quit()
