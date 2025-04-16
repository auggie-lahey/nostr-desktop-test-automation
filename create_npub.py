import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.fixture(scope="session")
def signup(driver):
    driver.get("https://nostrudel.ninja/#/signup")
    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "name")) 
    )

    name = "selenium"
    relay = "damus"
    input_field.send_keys(name)
    logging.info("Inputted name: ", name)
    input_field.submit()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Skip for now']"))).click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Next']"))).click()
    driver.execute_script("localStorage.setItem('write-relays', 'wss://relay.damus.io/');")
    driver.execute_script("localStorage.setItem('read-relays', 'wss://relay.damus.io/');")

    write_relays_value = driver.execute_script("return localStorage.getItem('write-relays');")
    print(f"Value of 'write-relays': {write_relays_value}")


    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Create profile']"))).click()

    nsec = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((
            By.XPATH, "//input[starts-with(@value, 'nsec')]"))).get_attribute('value')
    print(nsec)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='I have saved my secret key']"))).click()
    input_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "input")))
    input_element.clear()
    input_element.send_keys(nsec[-4:])
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Confirm']"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Start exploring nostr']"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Relays']"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Popular Relays']"))).click()
    yield nsec
