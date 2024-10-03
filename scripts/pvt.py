from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import selenium.common.exceptions
import boto3
import base64
import json
from botocore.exceptions import ClientError
from aws_synthetics.selenium import synthetics_webdriver as webdriver
from aws_synthetics.common import synthetics_logger as logger
from aws_synthetics.common import synthetics_configuration

TIMEOUT = 5
url = "https://workspaces.pexa.com.au/pexa_web/login.html"

async def main():
    browser = webdriver.Chrome()

    synthetics_configuration.set_config(
        {
            "screenshot_on_step_start": False,
            "screenshot_on_step_success": True,
            "screenshot_on_step_failure": True
        }
    )

    logger.info("------------------Production Verification Tests Started------------------")
    
    def navigate_to_home():
        browser.implicitly_wait(TIMEOUT)
        browser.get(url)
    await webdriver.execute_step("Navigate to PEXA Exchange", navigate_to_home)


    logger.info("------------------Production Verification Tests Completed------------------")
    
async def handler(event, context):
    return await main()
