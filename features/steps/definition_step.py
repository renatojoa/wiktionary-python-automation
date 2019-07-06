#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from behave import *
from features.pages.definition_page import DefinitionPage
import time

use_step_matcher("re")


@given("I prepare myself to be on definition page")
def step_impl(context):
    time.sleep(2)
    context.definition_page = DefinitionPage(context.driver)

@then("I am on (?P<searchTxt>.+) definition page by title")
def step_impl(context):
    context.definition_page.assertPage(searchTxt)

@then("I am on (?P<searchTxt>.+) definition page by address")
def step_impl(context, searchTxt):
    context.definition_page.assertAddress(searchTxt)

@then("I am on (?P<searchTxt>.+) definition page by header")
def step_impl(context, searchTxt):
    context.definition_page.assertHeader(searchTxt)

@then("I am on definition page of the word: (?P<searchTxt>.+)")
def step_impl(context, searchTxt):
    context.definition_page.onDefinitionPage(searchTxt)

@then("list array")
def step_impl(context):
    context.definition_page.listArray()