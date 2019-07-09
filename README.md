# wiktionary-python-automation
Automation Test using Python programming language +  Selenium + Behave + Allure
## Installation:
* [VSCODE](https://code.visualstudio.com/)
* [Python](https://www.python.org/downloads/)

>Open Terminal (Mac) / CMD (Windows)
>Go to project folder

Run:
>pip install -r requirements.txt

## Requeriments changes:
* lauch.json - "cwd": "CHANGE/TO/YOUR/PROJECT/FOLDER"

## Build, Run and Check:
Run Test Execution:

Go to project folder
>behave -f allure_behave.formatter:AllureFormatter -o allure-results ./features/definition.feature

Run Test Report:
>allure serve allure-results

## Examples:
what should do:
* Open: https://en.wiktionary.org/
* Look up the definition of the word: 
'apple',  'pear'
* Check for each yours specifics definitions


## Info:
* Programming Language: Python
* Repository Design Pattern: Page Object
* Testing Structure Model: BDD
* Testing Structure Framework : Behave 
* Testing Framework: Pytest
* Testing export Report: Allure Report
* Additional Recurse: [Suggestions to make the web site faster through](https://developers.google.com/speed/pagespeed/insights/?hl=pt-BR&url=https%3A%2F%2Fen.wiktionary.org%2Fwiki%2Fapple)


## Develop by:
[Site](http://www.renato.pw/)

[GitHub](https://github.com/renatojoa/)
