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
