# wiktionary-python-automation
Automation Test using Python programming language using Selenium + Behave + Allure
## Installation
* [VSCODE](https://code.visualstudio.com/)
* [Python](https://pypi.org/project/Appium-Python-Client/)https://www.python.org/downloads/)
* [Appium-Python-Client](https://pypi.org/project/Appium-Python-Client/)


```
Open Terminal(Windows) / CMD (Mac)
Go to project folder

Run:
pip install -r requirements.txt
```
##Requeriments changes
* lauch.json - "cwd": "CHANGE/TO/YOUR/PROJECT/FOLDER",
* environment.py - change for 
## Usage
Run Tests

```
behave
Go to project folder
behave -f allure_behave.formatter:AllureFormatter -o allure-results ./features
```


Run Test Report
```
allure
allure serve allure-results
```
## Develop by
[Site](http://www.renato.pw/)
[GitHub](https://github.com/renatojoa/)
