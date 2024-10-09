
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep
# Define your credential sets
credentials = [
    {"username": "email1@example.com", "password": "password1"},
    {"username": "toto.burgos@gmail.com", "password": "mane1346"},
    # Add more credentials here
]

# Initialize the WebDriver
driver = webdriver.Chrome()

# URL of the Codecademy login page
login_url = "https://www.codecademy.com/login"

# Loop through each credential set
for credential in credentials:
    try:
        # Load the login page
        driver.get(login_url)
        sleep(2)  # Allow the page to load

        # Locate the username and password fields
        username_field = driver.find_element(By.ID, 'user_login')  # Change as per actual field ID or NAME
        password_field = driver.find_element(By.ID, 'login__user_password')  # Change as per actual field ID or NAME

        # Clear any pre-existing values
        username_field.clear()
        password_field.clear()

        # Enter the credentials
        username_field.send_keys(credential['username'])
        password_field.send_keys(credential['password'])

        # Submit the form (by pressing the Enter key)
        password_field.send_keys(Keys.RETURN)

        # Wait for login to complete
        sleep(3)

        # Check for a successful login by looking for a dashboard element or user profile
        try:
            # This is an example; replace with an actual element that appears upon successful login
            element = driver.find_element(By.XPATH, "//span[@data-testid='error-text']")
            print(f"login failed : {credential['username']}")
        except NoSuchElementException:
            # If the invalid username or password  is not found, assume login failed
            print(f"loogin successfully: {credential['username']}")

        driver.find_element(By.CSS_SELECTOR,".gamut-1hetoga-ResetElement-createButtonComponent")
        print('login successfully')
    except NoSuchElementException:
        print("selenium cant locate this element ")
    finally:print('seession completed')




# Close the browser after testing
driver.quit()











