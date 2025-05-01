import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.fixture(scope="session")
def create_kind_1(driver):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Write Note']"))).click()
    textarea_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//textarea[@class='chakra-textarea rta__textarea css-1pvfnso']")))
    textarea_element.clear()
    note_text="""
this npub and note was automatically (fully) generated via selenium on noStrudel.

3rd line
    """
    textarea_element.send_keys(note_text)
    # cc: nostr:npub16ux4qzg4qjue95vr3q327fzata4n594c9kgh4jmeyn80v8k54nhqg6lra7
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Post']"))).click()

    nevent = driver.find_element(By.XPATH, "//a[contains(@class, 'chakra-link ') and contains(@href, 'nevent')]").get_attribute('href')
    print(nevent)
    nevent = nevent.split('/')[-1]  # Get the last segment after the last '/'
    print("nevent:", nevent)
    time.sleep(5)
#     nevent = "nevent1qqsqxnh8daxuugkvzqrt2ult4068hmv3asxn3k8xjw9uvyucxz7fkmss3h99a"
#     note_text = """
# this npub and note was automatically (fully) generated via selenium on noStrudel.

# 3rd line"""

    yield nevent, note_text

def fetch_kind_1(driver, clients, client, nevent):
    url = clients[client].kind_1.url + nevent
    print("fetching " + url)
    driver.get(url)
    driver.execute_script("localStorage.setItem('write-relays', 'wss://relay.damus.io/');") # NOSTRUDEL DOESN'T SET DEFAULT RELAY
    driver.execute_script("localStorage.setItem('read-relays', 'wss://relay.damus.io/');")

    note = WebDriverWait(driver, 30).until(
        lambda d: (element := d.find_element(By.XPATH, clients[client].kind_1.content)).text != "Loading..." and element.text
    )
    return note

def create_kind_1_reply(driver, clients, client, nevent, reply):
    fetch_kind_1(driver, clients, client, nevent)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Reply']"))).click()
    textarea_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//textarea[@class='chakra-textarea rta__textarea css-1pvfnso']")))
    textarea_element.clear()
    textarea_element.send_keys(reply)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Submit']"))).click()
    replied = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'css-1743pet')]")))
    return replied.text