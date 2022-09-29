# hudl

***

### Test harness for Hudl's web application login functionality.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Prerequisites](#prerequisites)
3. [Required Python Packages](#required-packages)
4. [Test Parameters](#test-parameters)

***

### Project Overview
#### This project is created to test the front-end functionality of the login page. Functionality includes: logging in, remember me, sign up, and need help. The tools and used for this project includes the following:
* Language: Python
* Testing Library: PyTest
* Reporting: Allure and PyTest built-in HTML reporter
* CI/CD: Jenkins
* IDE: PyCharm

***

### Prerequisites
#### The following items are required in order to successfully execute tests on a local machine:
* [Python](https://www.python.org/downloads/)
* PIP: `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`
* [Java SDK](https://www.oracle.com/java/technologies/sdk-downloads.html)

***

### Required Python Packages
#### The following python packages are required:
* [selenium](https://pypi.org/project/selenium/): Driver library required for automation testing
* [webdriver-manager](https://pypi.org/project/webdriver-manager/): used to run test on multiple browsers
* [pytest](https://pypi.org/project/pytest/): testing library
* [xdist](https://pypi.org/project/xdist/): used for parallel test execution

***

### Test Parameters
#### In order to successfully run tests on a local machine, the user will need to pass arguments via commandline:
ex: `py.test --email=test_email --password=password -n=4 --retries=2 --browser=chrome --headless=True
`
* py.test: the pytest command to execute test run
* email & password: credentials used ***NOTE: data is not stored in the repository***
* n: the number of parallel test runners
* retries: the number of retries for a failed test
* browser: browser to be used for test run, options include: `chrome`, `firefox`, and `edge`
* headless: test will run in headless mode if set to true, default is `False`