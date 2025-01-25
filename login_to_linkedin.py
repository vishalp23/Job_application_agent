from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_to_linkedin(driver, username, password):
    driver.get("https://www.linkedin.com/login")

    try:
        # Check if already logged in
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "global-nav"))
        )
        print("Already logged in.")
        return
    except Exception:
        print("Not logged in. Proceeding to log in.")

    # Perform login if not already logged in
    username_field = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    username_field.send_keys(username)

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys(password)

    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()

    # Wait for navigation after login
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "global-nav"))
    )
    print("Logged in successfully.")
