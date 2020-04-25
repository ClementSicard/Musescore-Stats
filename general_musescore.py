from time import sleep
import platform
from os import system, get_terminal_size
import sys
import re
from tabulate import tabulate
from prettytable import PrettyTable
from selenium.common.exceptions import TimeoutException, InvalidArgumentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver

clear_command = "cls" if platform.system() == "Windows" else "clear"
system(clear_command)

print("""
  __  __                                                      ____   _          _        
 |  \/  | _   _  ___   ___  ___   ___  ___   _ __  ___       / ___| | |_  __ _ | |_  ___ 
 | |\/| || | | |/ __| / _ \/ __| / __|/ _ \ | '__|/ _ \ _____\___ \ | __|/ _` || __|/ __|
 | |  | || |_| |\__ \|  __/\__ \| (__| (_) || |  |  __/|_____|___) || |_| (_| || |_ \__ |
 |_|  |_| \__,_||___/ \___||___/ \___|\___/ |_|   \___|      |____/  \__|\__,_| \__||___/
                                                                                         

""")
print("Setting things up...")

offset = 50


def print_user_stats(username, nb_followers, nb_following, nb_scores):
    system(clear_command)
    s = "*" * offset + " " + username + " " + "*" * offset
    print(s)
    for k, v in {"Followers": nb_followers, "Following": nb_following, "Number of scores": nb_scores}.items():
        print(k.upper() + ": " + v.rjust(23 - len(k), ' '))


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

while True:
    while True:
        try:
            username = input(
                "Please enter a valid Musescore username/ID : \n> ")
            if username == "":
                print("Incorrect input. Try again")
            elif username.isnumeric():
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
            sys.exit()
        except:
            print("\nError: user not found or page could not be loaded. Please try again later or try inputting user ID directly.\n")

    print("Loading userpage for user", username, "...")

    user_class_name = "_3-vzW"
    user_details_class_name = "k1Ae2"
    sheet_music_url = driver.find_element_by_partial_link_text('Sheet')

    user_name = driver.find_elements_by_class_name(user_class_name)[0].text
    user_details = driver.find_elements_by_class_name(user_details_class_name)

    nb_followers = user_details[0].text
    nb_following = user_details[1].text
    nb_scores = user_details[2].text

    views = dict()
    fav = dict()

    if nb_scores == 0:
        print("\n" + user_name + " has not published any scores yet.")
        # break
        quit()
    sheet_music_url.click()

    sheets = driver.find_elements_by_tag_name('article')
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

    sorted_views = sorted(views.items(), key=lambda x: x[1], reverse=True)
    viewed = [["", "SHEET NAME", "VIEW COUNT", "FAVORITES COUNT"]]
    for i, e in zip([i + 1 for i in range(0, len(sorted_views))], sorted_views):
        viewed.append([i, e[0][:offset], "{:,d}".format(
            e[1]), "{:,d}".format(fav[e[0]])])
    views_tab = PrettyTable(viewed[0])
    for v in viewed[1:]:
        views_tab.add_row(v)
    sorted_fav = sorted(fav.items(), key=lambda x: x[1], reverse=True)
    faved = [["", "SHEET NAME", "FAVORITES COUNT", "VIEW COUNT"]]
    for i, e in zip([i + 1 for i in range(0, len(sorted_fav))], sorted_fav):
        faved.append([i, e[0][:offset],
                      "{:,d}".format(e[1]), "{:,d}".format(views[e[0]])])

    most_viewed = max(views, key=views.get)
    most_fav = max(fav, key=fav.get)

    print_user_stats(user_name, nb_followers, nb_following, nb_scores)

    print("\n\"" + most_viewed + "\" is the most viewed sheet with " +
          "{:,d}".format(views[most_viewed]) + " views.")

    print("\"" + most_fav + "\" is the most favorited sheet with " +
          "{:,d}".format(fav[most_fav]) + " favorites.\n")

    print("\nTOTAL VIEWS:", "{:,d}".format(sum(views.values())))
    print("TOTAL FAVORITES:", "{:,d}".format(sum(fav.values())))

    # print(tabulate(viewed[1:], headers=viewed[0], tablefmt='orgtbl'))
    print("\n Most viewed sheets :\n")

    print(views_tab)

    print("\n Most favorited sheets :\n")

    fav_tab = PrettyTable(faved[0])
    for f in faved[1:]:
        fav_tab.add_row(f)
    print(fav_tab)

    while True:
        a = input(
            "\nPress [ENTER] to see stats for another user, [Q] to exit\n> ")
        if a == "":
            system(clear_command)
            break
        elif a.lower() == "q":
            system(clear_command)
            quit()
