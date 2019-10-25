from selenium import webdriver
import time
import pytest


def test_button(browser):
	browser.get(r"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
	time.sleep(30)
	try:
		browser.find_element_by_css_selector(r'[class="btn btn-lg btn-primary btn-add-to-basket"]')
	except:
		assert False, 'Не найдена кнопка "Добавить в корзину"'

