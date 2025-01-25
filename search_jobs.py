from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def search_jobs(driver, job_title):
    try:
        print("Navigating to LinkedIn Jobs page...")
        driver.get("https://www.linkedin.com/jobs/")
        
        # Locate the search input field
        print("Waiting for search input field...")
        search_input = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//input[contains(@id, 'jobs-search-box-keyword-id')]"))
        )
        search_input.clear()
        search_input.send_keys(job_title)
        search_input.send_keys(Keys.RETURN)

        # Wait for search results to load
        print("Waiting for job results to load...")
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.CLASS_NAME, "job-card-container"))
        )
        print("Job search completed.")
    except Exception as e:
        driver.save_screenshot("search_error.png")
        print(f"Error during job search: {e}")
        raise
