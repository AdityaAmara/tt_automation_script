import time
from datetime import datetime
from selenium import webdriver
import psutil
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

mon = {
        #Replace with your subject names. It's case sensitive
        '10-11':'Subject A Name',
        '12-13':'Subject B Name',
        '15-16':'Subject C Name'
}

tue = {
        #fill it with your timetable
}

wed = {
        #fill it with your timetable
}

thu = {   
        #fill it with your timetable            
}

fri = {}
sat = {}
sun = {}

timetable = [mon,tue,wed,thu,fri,sat,sun]
chromedriver_path =  "/usr/local/bin/chromedriver"

def init():
    global driver
    global options
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=/path_to_Chrome_Profile")
    driver = webdriver.Chrome(options=options,executable_path=chromedriver_path)

def driver_status():
    global driver_process
    driver_process = psutil.Process(driver.service.process.pid)
    if driver_process.is_running():
        return True
    else:
        return False


def login():
    try:
        driver.get("https://learn.upes.ac.in/")
        driver.maximize_window()
        driver.find_element_by_id("user_id").send_keys("SAP@stu.upes.ac.in")
        driver.find_element_by_id("password").send_keys("SAP_PASSWORD")
        driver.find_element_by_id("entry-login").click()
        print("The USER is logged in")
    except NoSuchElementException:
        print("The USER is already logged in")

def find_day():
    day = datetime.today().weekday()  # Monday is 0 & Sunday is 6
    return day

def find_today_classes():
    today = find_day()
    today_classes = timetable[today]
    return today_classes

def find_now_class():
    now_time = datetime.now().time()
    val = str(now_time).split(":")
    today_classes = find_today_classes()
    for x in today_classes:
        temp_val = x.split('-')
        if int(val[0])==int(temp_val[0]):
            return today_classes[x]
    
    return "NO CLASS IS SCHEDULED"

def login_now_class():
    class_name = find_now_class()
    #print(class_name)
    if class_name != "NO CLASS IS SCHEDULED":
        time.sleep(15)
        driver.find_element_by_partial_link_text(class_name).click()
        time.sleep(20)
        driver.find_element_by_id('sessions-list-dropdown').click()
        time.sleep(5)
        driver.find_element_by_partial_link_text('Course Room').click()
        time.sleep(15)

def help_menu():
    print('\n')
    print('class [-h or help]    To see this menu')
    print('class [-n or now]     To check if any class is scheduled now')
    print('class [-t or today]   To see the list of today\'s classes')
    print('class [-ln or login]  To login a class which is scheduled now')
    print('\n')
