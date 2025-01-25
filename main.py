import os
from dotenv import load_dotenv
from initialize_driver import initialize_driver
from login_to_linkedin import login_to_linkedin
from search_jobs import search_jobs
from apply_for_jobs import apply_for_jobs

# Load environment variables
load_dotenv()

def main():
    driver = initialize_driver()

    username = os.getenv("LINKEDIN_USERNAME")
    password = os.getenv("LINKEDIN_PASSWORD")

    application_data = {
        "resume": "resume/Vishal.pdf",
        "first_name": "Vishal",
        "last_name": "Patil",
        "email": "vishal.v.patil@ucdenver.edu",
        "phone": "7207429281",
        "location": "Denver,COLORADO",
    }

    try:
        login_to_linkedin(driver, username, password)
        search_jobs(driver, "Data Engineer")
        apply_for_jobs(driver, application_data)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
         print("Session will remain active.")

if __name__ == "__main__":
    main()
