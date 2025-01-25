from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from openai import OpenAI
import os
import time

# Set up OpenAI client with API key
client = OpenAI(api_key=os.getenv("API_KEY"))

def gpt_identify_buttons(driver):
    """
    Use GPT to analyze the page and identify the Easy Apply button or any Apply button.
    """
    page_source = driver.page_source
    prompt = f"""
    You are an AI assistant helping with job applications on LinkedIn. Analyze the following HTML and determine:
    1. If there is an 'Easy Apply' button or any 'Apply' button present.
    2. Provide instructions on how to proceed with the application process based on the available buttons.

    HTML Content:
    {page_source[:3000]}  # Limit to 3000 characters for token constraints
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant for navigating LinkedIn job applications."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.5
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error analyzing page with GPT: {e}")
        return None

def handle_continue_applying(driver):
    """
    Locate and click the 'Continue applying' button in the modal if present.
    """
    try:
        continue_applying_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Continue applying')]"))
        )
        continue_applying_button.click()
        print("Clicked 'Continue applying' button.")
    except TimeoutException:
        print("No 'Continue applying' button found. Proceeding without modal.")

def apply_for_jobs(driver, application_data):
    try:
        # Wait for job listings to load
        job_listings = WebDriverWait(driver, 50).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".job-card-container"))
        )
        print(f"Found {len(job_listings)} job listings.")

        for i in range(5):  # Limit to first 5 jobs
            try:
                # Refetch job listings to avoid stale element reference
                job_listings = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".job-card-container"))
                )
                job = job_listings[i]
                job.click()
                print("Clicked on a job listing.")
                time.sleep(2)  # Allow the job details to load

                # Use GPT to analyze the page
                ai_analysis = gpt_identify_buttons(driver)
                print("GPT Analysis:", ai_analysis)

                if "Easy Apply" in ai_analysis:
                    try:
                        easy_apply_button = WebDriverWait(driver, 10).until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, ".jobs-apply-button"))
                        )
                        easy_apply_button.click()
                        print("Easy Apply button clicked.")
                        time.sleep(2)
                        handle_easy_apply(driver, application_data)  # Handle the Easy Apply process
                    except Exception as e:
                        print(f"Easy Apply button not found for this job. Skipping. Error: {e}")
                        continue
                elif "Apply" in ai_analysis:
                    try:
                        apply_button = WebDriverWait(driver, 10).until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, ".jobs-apply-button"))
                        )
                        apply_button.click()
                        print("Apply button clicked. Redirecting to external portal...")
                        handle_external_portal(driver, application_data)
                    except Exception as e:
                        print(f"Apply button not found for this job. Skipping. Error: {e}")
                        continue
                else:
                    print("No Apply option found. Skipping job.")
                    continue

                print("Applied to a job successfully!")
                time.sleep(2)
            except StaleElementReferenceException:
                print("Stale element detected. Refetching job listing.")
                continue
            except Exception as e:
                print(f"Error interacting with job listing: {e}")
                continue
    except Exception as e:
        driver.save_screenshot("apply_jobs_error.png")
        print(f"Error during job application process: {e}")

def handle_easy_apply(driver, application_data):
    """
    Handle Easy Apply process dynamically.
    """
    try:
        while True:
            try:
                # Fill form fields dynamically
                fill_form_fields(driver, application_data)

                # Locate and click the Next or Review button
                next_or_review_button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "//button[contains(@aria-label, 'Continue') or contains(@aria-label, 'Next') or contains(@aria-label, 'Review')]")
                    )
                )
                next_or_review_button.click()
                print("Clicked Next or Review button.")
                time.sleep(2)

            except TimeoutException:
                print("No 'Next' or 'Review' button found. Trying to locate 'Submit' button.")
                break

        # Locate and click the Submit button
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'Submit')]"))
        )
        submit_button.click()
        print("Application submitted successfully!")

    except Exception as e:
        driver.save_screenshot("easy_apply_error.png")
        print(f"Error during Easy Apply process: {e}")

def handle_external_portal(driver, application_data):
    """
    Handles job applications redirected to an external company portal.
    """
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        print("Redirected to external portal.")
        # Implement portal login, resume upload, and form filling
        fill_form_fields(driver, application_data)
    except Exception as e:
        print(f"Error handling external portal: {e}")

def fill_form_fields(driver, application_data):
    """
    Fill out form fields dynamically based on the detected input elements.
    """
    try:
        # Locate input fields and fill them
        input_fields = driver.find_elements(By.CSS_SELECTOR, "input[type='text'], input[type='number']")
        for field in input_fields:
            label = field.get_attribute("aria-label")
            if label:
                print(f"Filling field: {label}")
                if "SQL" in label:
                    field.send_keys("8")
                elif "Microsoft Azure" in label:
                    field.send_keys("5")
                elif "Databases" in label:
                    field.send_keys("5")
        
        # Handle radio buttons (e.g., Yes/No questions)
        radio_buttons = driver.find_elements(By.CSS_SELECTOR, "input[type='radio']")
        for button in radio_buttons:
            label = button.get_attribute("aria-label")
            if label and "Yes" in label:
                driver.execute_script("arguments[0].click();", button)
                print(f"Selected radio button: {label}")

    except Exception as e:
        print(f"Error filling form fields: {e}")
