# Article-Aggregator
Gets headers and different links from popular tech sites

# To Operate
First go into gmail and turn on two step verification.
Set it up anyway you want, then go back to security and underneath 2 step verification slect App Passwords.
Select the mail app and a custom device and name it.
Then click generate.
Copy the text highlighted in yellow.
In the code find username and password and make the username your email address and the password the text you copied.
This will allow the program to send emails.

You are all set!

# To Automate
Go to the Actions tab.
Click configure on the Python Application.
Replace the code with:
```
# This workflow will install Python dependencies, run tests and lint with a single version of Python
# For more information see: https://help.github.com/actions/language-and-framework-guides/using-python-with-github-actions

name: Python application

on:
  schedule:
  - cron: "0 13 * * *"

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python 3.10
      uses: actions/setup-python@v2
      with:
        python-version: "3.10"
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install flake8 pytest
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
    - name: Install bs4
      run: |
        python -m pip install beautifulsoup4
    - name: Install requests
      run: |
        python -m pip install requests
    - name: Lint with flake8
      run: |
        # stop the build if there are Python syntax errors or undefined names
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
        # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
        flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
    - name: Test with pytest
      run: |
        python Start.py
 ```
This will send the email everyday at 8:00 am EST.

