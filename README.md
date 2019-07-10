# wiktionary-python-automation

**Automation Tests** using Python + Selenium + Behave + Allure.

## Installation:

- [VSCode](https://code.visualstudio.com/)
- [Python](https://www.python.org/downloads/)

> Into the project folder run the following command to install dependencies:
>
> `$ pip install -r requirements.txt`

> To build on vscode 
>
> Open lauch.json and change the "cwd" param to your project folder: "c:/CHANGE/TO/YOUR/PROJECT/FOLDER"

## Execution and Reporting:

> Test execution:
>
> `$ behave -f allure_behave.formatter:AllureFormatter -o allure-results ./features/definition.feature`

> Test Report:
>
> `$ allure serve allure-results`

## Example:

1. Open: https://en.wiktionary.org/
2. Look up the definition of the words: **`apple`** and **`pear`**
3. Check for each yours specifics definitions

## General Info:

- Programming Language: Python
- Repository Design Pattern: Page Object
- Testing Structure Model: BDD
- Testing Structure Framework : Behave
- Testing Framework: Pytest
- Testing export Report: Allure Report
- Additional Resource: [Suggestions to make the web site faster through](https://developers.google.com/speed/pagespeed/insights/?hl=pt-BR&url=https%3A%2F%2Fen.wiktionary.org%2Fwiki%2Fapple)

## Develop by:

Renato José <renatojoa@gmail.com>

[Site](http://www.renato.pw/)
