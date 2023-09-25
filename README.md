# API Automation Framework using Pytest
## PythonPyTestFrameWorkAPI

This is a Python automation framework for API testing using Python, pytest, requests, and allure. This framework provides a structured and organized way to create and execute API tests, generate test reports, and manage configuration settings. It also includes utilities for logging, generating temporary email and more.
### Project Structure

The project is structured as follows:

- `pytest.ini`: Configuration file for pytest.
- `__init__.py`: Initialization file for the project.
#### apis
- `apis.py`: Contains API request logic which can be used to create test cases.
#### configs
- `config.ini`: Configuration settings for the framework.
- `config.py`: Python module to read and manage configuration settings.
#### reports
- `allure_reports`: Directory to store Allure test reports.
- `html_reports`: Directory to store HTML test reports.
- `logs`: Directory to store log files.
#### tests
- `base.py`: Base test class for common test setup and teardown.
- `temp_company.py`: common method which can be used. Actually is used by base.py when the credentials are not provided and requires of creating new company using register api.
- `test_cases_login_api.py`: Sample Test cases for login API.
#### test_data
- Test data that might be used by tests.
#### utils
- `common.py`: Common utility like send request, authentication, get_json, assertions of status code/ body etc., functions.
- `custom_logger.py`: Custom logger for logging test execution details.
- `helpers.py`: Helper functions for various tasks.
- `mail_grabber.py`: Utility to grab and process email notifications. This is using an extrnal service called Mailsac.com and which provides us with email service ( temporary email).  We can create a temporary email and read the mail as-well. 
- `venv`: Virtual environment directory.

### Project Tree
``` tree -O
PythonPyTestFrameWorkAPI
│   .gitattributes
│   pytest.ini
│   __init__.py
│
├───apis
│      apis.py
│      __init__.py
│   
│
├───configs
│     config.ini
│     config.py
│     __init__.py
│   
│
├───reports
│   ├───allure_reports
│   │       023d49da-41b8-4953-bdc7-179174d605f3-result.json
│   │  
│   │
│   ├───html_reports
│   │       Test_Automation_Report.html
│   │
│   └───logs
│           logs.log
│
├───tests
│      base.py
│      temp_company.py
│      test_cases_login_api.py
│      test_cases_register_api.py
│      __init__.py
│   
│
├───test_data
├───utils
│      common.py
│      custom_logger.py
│      helpers.py
│      mail_grabber.py
│      __init__.py
│   
│
├───venv
```

## Getting Started

1. Clone this repository to your local machine.
2. Set up a virtual environment in the `venv` directory.
3. Install required dependencies using `pip install -r requirements.txt`.
4. Update configuration files in the `Configurations` directory as needed.
5. Define page locators in the `Locators` directory.
6. Create Page Object classes in the `Pages` directory.
7. Organize test data in the `TestData` directory.
8. Create test case files in the `TestCases` directory.
9. Run tests using `pytest `.

## _Tools & Technologies Used_
_Python_, _requests_, _pytest_, _Allure_.

## Running Tests

To run the tests, navigate to the project root directory and execute the following command:

```bash
pytest test_cases
```
## Reporting
* HTML reports can be found in the `reports/html_reports` directory.
* Logs are stored in the `reports/logs` directory.

## Contributing
Contributions to this project are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.
