from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get('https://resonant-madeleine-516425.netlify.app/')

# Maximize the window to ensure full scrolling
driver.maximize_window()

time.sleep(2)
try:
    # Get current page height
    page_height = driver.execute_script("return document.body.scrollHeight;")

    # Scroll down slowly to the bottom
    scroll_increment = 10  # Adjust scroll increment (pixels) for slower scrolling
    current_position = 0

    while current_position < page_height:
        driver.execute_script(f"window.scrollTo(0, {current_position});")
        time.sleep(0.03)  # Adjust scroll speed (seconds) for slower scrolling
        current_position += scroll_increment

    # Wait for 3 seconds (adjust as necessary)
    time.sleep(2)

    # Scroll back slowly to the top
    while current_position > 0:
        driver.execute_script(f"window.scrollTo(0, {current_position});")
        time.sleep(0.03)  # Adjust scroll speed (seconds) for slower scrolling
        current_position -= scroll_increment

    # Scroll to exactly top to handle small adjustments
    driver.execute_script("window.scrollTo(0, 0);")

    print("Slow scroll to the bottom, waited, and scrolled back to the top successfully of Home Page!")

except Exception as e:
    print(f"Failed to scroll. Error: {str(e)}")


about_text = 'About'
about_link = driver.find_element(By.LINK_TEXT, about_text)
about_link.click()
time.sleep(4)
try:
    # Get current page height
    page_height = driver.execute_script("return document.body.scrollHeight;")

    # Scroll down slowly to the bottom
    scroll_increment = 10  # Adjust scroll increment (pixels) for slower scrolling
    current_position = 0

    while current_position < page_height:
        driver.execute_script(f"window.scrollTo(0, {current_position});")
        time.sleep(0.03)  # Adjust scroll speed (seconds) for slower scrolling
        current_position += scroll_increment

    # Wait for 3 seconds (adjust as necessary)
    time.sleep(2)

    # Scroll back slowly to the top
    while current_position > 0:
        driver.execute_script(f"window.scrollTo(0, {current_position});")
        time.sleep(0.03)  # Adjust scroll speed (seconds) for slower scrolling
        current_position -= scroll_increment

    # Scroll to exactly top to handle small adjustments
    driver.execute_script("window.scrollTo(0, 0);")

    print("Slow scroll to the bottom, waited, and scrolled back to the top successfully of AboutUs Page!")

except Exception as e:
    print(f"Failed to scroll. Error: {str(e)}")


time.sleep(4)

about_text = 'Contact'
about_link = driver.find_element(By.LINK_TEXT, about_text)
about_link.click()

time.sleep(3)

link_text = 'Login'
login_link = driver.find_element(By.LINK_TEXT, link_text)
login_link.click()

time.sleep(2)
username_field = driver.find_element(By.NAME, 'username')
time.sleep(2)
password_field = driver.find_element(By.NAME, 'password')
time.sleep(2)

# Now you can interact with these elements, for example:
username_field.send_keys('user')
password_field.send_keys('password')

login_button = driver.find_element(By.CSS_SELECTOR, 'input[type=\"submit\" i]')
time.sleep(2)
login_button.click()

time.sleep(1)

try:
    # Wait up to 10 seconds for the current URL to match the expected dashboard URL
    expected_dashboard_url = 'https://resonant-madeleine-516425.netlify.app/products.html'  # Replace with your expected dashboard URL
    current_url = driver.current_url

    if expected_dashboard_url == current_url:
        print(f"Success: Dashboard URL '{expected_dashboard_url}' accessed successfully!")
    else:
        print(f"Failed: Expected dashboard URL '{expected_dashboard_url}', but current URL is '{current_url}'")

except Exception as e:
    print(f"{str(e)}")

try:
    # Get current page height
    page_height = driver.execute_script("return document.body.scrollHeight;")

    # Scroll down slowly to the bottom
    scroll_increment = 10  # Adjust scroll increment (pixels) for slower scrolling
    current_position = 0

    while current_position < page_height:
        driver.execute_script(f"window.scrollTo(0, {current_position});")
        time.sleep(0.03)  # Adjust scroll speed (seconds) for slower scrolling
        current_position += scroll_increment

    # Wait for 3 seconds (adjust as necessary)
    time.sleep(2)

    # Scroll back slowly to the top
    while current_position > 0:
        driver.execute_script(f"window.scrollTo(0, {current_position});")
        time.sleep(0.03)  # Adjust scroll speed (seconds) for slower scrolling
        current_position -= scroll_increment

    # Scroll to exactly top to handle small adjustments
    driver.execute_script("window.scrollTo(0, 0);")

    print("Slow scroll to the bottom, waited, and scrolled back to the top successfully of Product Page!")

except Exception as e:
    print(f"Failed to scroll. Error: {str(e)}")

time.sleep(5)


product_element = driver.find_element(By.XPATH, "//h3[text()='Thar']/following-sibling::a[text()='Rent Now']")
product_element.click()


time.sleep(2)

rent_days_input = driver.find_element(By.ID, "rentDays")
rent_days_input.clear()
rent_days_input.send_keys('2')

# Find the confirm button and click it
confirm_button = driver.find_element(By.CLASS_NAME, "confirm-button")
confirm_button.click()

print("Order placed successfully!")

time.sleep(2)

home_text = 'Home'
home_link = driver.find_element(By.LINK_TEXT, home_text)
home_link.click()

time.sleep(3)


print('************************************************************')
print("Testing of Speedy car Rental Website is successfully Done......")
print('************************************************************')

driver.quit()




