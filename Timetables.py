from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

with open('config.txt', 'r') as conf:
    username = conf.readline()
    username = username.rstrip('\n')
    password = conf.readline()
    password = password.rstrip('\n')
    Save_Location = conf.readline()
    Save_Location = Save_Location.rstrip('\n')


chromeOptions = Options()
chromeOptions.headless = False
PATH = "driver/chromedriver"


driver = webdriver.Chrome(PATH, options = chromeOptions)

# Access the timetable website
driver.set_window_size(1920,933)
driver.get("https://timetabling.nottingham.ac.uk/SWS/2021/")


#Find the login field and enter username
search = driver.find_element_by_css_selector("#tUserName")
try:
    search.send_keys(username)

#find the password field and enter the password
    search = driver.find_element_by_css_selector("#tPassword")
    search.send_keys(password)


#find the login button and click it
    search = driver.find_element_by_css_selector("#bLogin")
    search.click()
except:
    print()
try:
#find the "My Student Timetable" button and click it
    search = driver.find_element_by_css_selector("#LinkBtn_StudentMyTimetable")
    search.click()
except:
    print("Error: Please check Login credentials")
    driver.quit()
    quit()

try:
    #find the "This Week option" and click it
    search = driver.find_element_by_css_selector("#lbWeeks > option:nth-child(1)")
    search.click()

    #Find the list selector radio button and click it
    search = driver.find_element_by_css_selector("#RadioType_1")
    search.click()

    #Find the "Get Timetable" button and click it
    search = driver.find_element_by_css_selector("#bGetTimetable")
    search.click()

    driver.get("https://timetabling.nottingham.ac.uk/SWS/2021/showtimetable.aspx")
    driver.get_screenshot_as_file(f"/{Save_Location}ThisWeekTimetable.png")
    print("This Week Grabbed")
except:
    print("Error: Please ensure save location is valid")
    driver.quit()
    quit()

try:
    driver.get("https://timetabling.nottingham.ac.uk/SWS/2021/")

    #find the "My Student Timetable" button and click it
    search = driver.find_element_by_css_selector("#LinkBtn_StudentMyTimetable")
    search.click()

    #find the "This Week option" and click it
    search = driver.find_element_by_css_selector("#lbWeeks > option:nth-child(2)")
    search.click()

    #Find the list selector radio button and click it
    search = driver.find_element_by_css_selector("#RadioType_1")
    search.click()

    #Find the "Get Timetable" button and click it
    search = driver.find_element_by_css_selector("#bGetTimetable")
    search.click()

    driver.get("https://timetabling.nottingham.ac.uk/SWS/2021/showtimetable.aspx")
    driver.get_screenshot_as_file(f"/{Save_Location}NextWeekTimetable.png")
    print("Next Week Grabbed")
except:
    driver.quit()
    quit()
driver.quit()
quit()
