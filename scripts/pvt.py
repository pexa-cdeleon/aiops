import asyncio
from selenium.webdriver.common.by import By
from aws_synthetics.selenium import synthetics_webdriver as syn_webdriver
from aws_synthetics.common import synthetics_logger as logger, synthetics_configuration

TIMEOUT = 10

async def main():
    url = "https://www.pexa.com.au/"
    browser = syn_webdriver.Chrome()


    # Set synthetics configuration
    synthetics_configuration.set_config({
       "screenshot_on_step_start" : True,
       "screenshot_on_step_success": True,
       "screenshot_on_step_failure": True
    });


    def navigate_to_page():
        browser.implicitly_wait(TIMEOUT)
        browser.get(url)

    await syn_webdriver.execute_step("navigateToUrl", navigate_to_page)

    # Execute customer steps
    def customer_actions_1():
        browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[1]/div[1]/div/div/div/div/div/div[2]/div[4]/a").click()

    await syn_webdriver.execute_step('click', customer_actions_1)

    def customer_actions_2():
        browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[1]/div[1]/div/div/div/div/div/div[2]/div[4]/div/div/div/div/div/div/div[2]/ul/li[8]/a")

    await syn_webdriver.execute_step('verifySelector', customer_actions_2)

    def customer_actions_3():
        browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[1]/div[1]/div/div/div/div/div/div[2]/div[4]/div/div/div/div/div/div/div[2]/ul/li[8]/a").click()

    await syn_webdriver.execute_step('click', customer_actions_3)

    def customer_actions_4():
        browser.find_element(By.XPATH, "//*[@id='__next']/div/div[2]/div[2]/div/div/div/div/div/div[2]/form/div[8]/div/div/div/button")

    await syn_webdriver.execute_step('verifySelector', customer_actions_4)



    logger.info("Canary successfully executed.")


async def handler(event, context):
    # user defined log statements using synthetics_logger
    logger.info("Selenium Python workflow canary.")
    return await main()
