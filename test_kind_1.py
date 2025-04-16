import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from create_kind_1 import create_kind_1
from create_npub import signup

# Set up logging
logging.basicConfig(level=logging.INFO)
@pytest.fixture(scope="session")
def driver():
    # Set up the WebDriver
    driver = webdriver.Firefox()
    yield driver
    driver.quit()  # This will close the browser after all tests in the module are done

class Kind:
    def __init__(self, url, content):
        self.url = url 
        self.content = content

class Client:
    def __init__(self, base_url, kind_1):
        self.base_url = base_url  
        self.kind_1 = Kind(
            url = base_url + kind_1['suffix'],   
            content = kind_1['content']
        )

clients = {
            "coracle": Client(
                base_url = "https://coracle.social/",
                kind_1 = {
                    "suffix": "notes/",
                    "content": "//div[contains(@class, 'note-content')]"
                }
            ),
            "iris": Client(
                base_url = "https://iris.to/", 
                kind_1 = {
                    "suffix": "",
                    "content": "//div[@class='px-4']"
                }
            ),
            "nostrudel": Client(
                base_url = "https://nostrudel.ninja/", 
                kind_1 = {
                    "suffix": "#/n/",
                    "content": "//span[@class='chakra-text css-0']"
                }
            ),
        }
    
def fetch_kind_1(driver, client, nevent):
    url = clients[client].kind_1.url + nevent
    print("fetching " + url)
    driver.get(url)
    driver.execute_script("localStorage.setItem('write-relays', 'wss://relay.damus.io/');") # NOSTRUDEL DOESN'T SET DEFAULT RELAY
    driver.execute_script("localStorage.setItem('read-relays', 'wss://relay.damus.io/');")

    note = WebDriverWait(driver, 30).until(
        lambda d: (element := d.find_element(By.XPATH, clients[client].kind_1.content)).text != "Loading..." and element.text
    )
    return note

@pytest.mark.parametrize("client", clients.keys())
def test_kind_1(driver, signup, create_kind_1, client):
    nsec = signup
    nevent, kind_1 = create_kind_1
    print("Testing " + client)
    note = fetch_kind_1(driver, client, nevent)
    expected_message = kind_1.replace('\n', ' ')
    actual_message = note.replace('\n', ' ')
    assert note.strip() == kind_1.strip(), f"Assertion failed for client: {client}. Expected: '{expected_message}', but got: '{actual_message}'"