# LinkedIn Job Application Automation

## Overview
This project is an automation tool designed to streamline the job application process on LinkedIn. Using **Selenium** for browser automation and **OpenAI GPT-4** for intelligent analysis, the tool automates the "Easy Apply" process and handles job applications redirected to external portals. 

The project is capable of:
- Navigating LinkedIn job listings.
- Identifying "Easy Apply" and standard "Apply" buttons using AI.
- Automatically filling out job application forms.
- Handling dynamic fields, such as text inputs, radio buttons, and dropdowns.
- Redirecting and interacting with external job portals for standard applications.
- Managing common edge cases, such as modal pop-ups and multi-step forms.

## Features
1. **AI Integration**: 
   - GPT-4 is used to analyze LinkedIn job listings and identify actionable buttons like "Easy Apply" or "Apply."
2. **Automated Form Filling**:
   - Automatically populates text fields, selects radio buttons, and submits the application.
3. **External Portal Support**:
   - Handles job applications redirected to external company portals.
4. **Error Handling**:
   - Manages issues such as stale elements, pop-ups, and unexpected navigations gracefully.
5. **Dynamic Form Filling**:
   - Detects and completes fields based on form labels and user-provided data.

## Installation

### Prerequisites
1. Python 3.8 or higher
2. Selenium WebDriver
3. Google Chrome (compatible version with the Chromedriver)
4. OpenAI API key

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/job-apply-automation.git
   cd job-apply-automation
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   - Create a `.env` file in the root directory and add the following:
     ```
     LINKEDIN_USERNAME=your_username
     LINKEDIN_PASSWORD=your_password
     API_KEY=your_openai_api_key
     ```
4. Run the script:
   ```bash
   python main.py
   ```

## Usage
1. Log in to LinkedIn using your credentials.
2. The script will navigate to the job listings, analyze the page, and begin applying to jobs.
3. Handles both "Easy Apply" and redirected applications to external portals.

### Dynamic Field Mapping
- Fields such as "SQL experience" or "Databases experience" are populated with predefined values. These mappings can be customized in the `fill_form_fields` function.

## File Structure
```
├── main.py                 # Entry point for the project
├── apply_for_jobs.py       # Logic for handling job applications
├── initialize_driver.py    # Sets up the Selenium WebDriver
├── login_to_linkedin.py    # Automates LinkedIn login
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (not included in the repository)
├── README.md               # Project documentation
```

## Contributors
- **Vishal Patil**
- **Vidyaranya Javalgi**

## Future Improvements
1. Enhance GPT-based decision-making for complex forms.
2. Add support for advanced job search filters.
3. Integrate error recovery mechanisms for failed applications.
4. Expand support for additional job platforms beyond LinkedIn.

---

Feel free to reach out with suggestions or issues!
