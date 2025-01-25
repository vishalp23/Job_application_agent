from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def fill_application_fields(driver, data):
    field_mappings = {
        "first_name": (By.ID, "first-name"),
        "last_name": (By.ID, "last-name"),
        "email": (By.ID, "email"),
        "phone": (By.ID, "phone-number"),
        "location": (By.ID, "location"),
    }
    
    for field, locator in field_mappings.items():
        try:
            element = WebDriverWait(driver, 5).until(EC.presence_of_element_located(locator))
            element.clear()
            element.send_keys(data[field])
        except Exception:
            print(f"Field {field} not found. Skipping.")
    
    try:
        resume_upload = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']"))
        )
        resume_upload.send_keys(data["resume"])
    except Exception:
        print("Resume upload field not found. Skipping.")
