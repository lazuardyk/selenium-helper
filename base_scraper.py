"""Base scraper class here."""
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.ui import WebDriverWait

class BaseScraper:
    """Base scraper class for general purpose scraping methods."""

    def launch_browser(self, headless: bool) -> webdriver.Chrome:
        """Launch a chrome browser."""
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36")
        if headless:
            options.add_argument("--headless")
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        return browser

    def wait_by_xpath(
        self, browser: webdriver.Chrome, xpath: str, timeout: int
    ) -> bool:
        """Wait until the element is present."""
        try:
            WebDriverWait(browser, timeout).until(
                presence_of_element_located((By.XPATH, xpath))
            )
            return True
        except TimeoutException:
            return False
    
    def wait_by_selector(
        self, browser: webdriver.Chrome, selector: str, timeout: int
    ) -> bool:
        """Wait until the element is present by selector."""
        try:
            WebDriverWait(browser, timeout).until(
                presence_of_element_located((By.CSS_SELECTOR, selector))
            )
            return True
        except TimeoutException:
            return False

    def click_by_xpath(self, browser: webdriver.Chrome, xpath: str) -> None:
        """Click an element by xpath."""
        browser.find_element_by_xpath(xpath).click()
    
    def click_by_selector(self, browser: webdriver.Chrome, selector: str) -> None:
        """Click an element by selector."""
        browser.find_element_by_css_selector(selector).click()

    def type_by_selector(self, browser: webdriver.Chrome, selector: str, input: str) -> None:
        """Click an element by selector."""
        browser.find_element_by_css_selector(selector).send_keys(input)
    
    def get_text_by_selector(self, browser: webdriver.Chrome, selector: str) -> None:
        """Click an element by selector."""
        try:
            text = browser.find_element_by_css_selector(selector).text
            return text.strip()
        except:
            return ""
    
    def get_text_by_xpath(self, browser: webdriver.Chrome, xpath: str) -> None:
        """Click an element by xpath."""
        try:
            text = browser.find_element_by_xpath(xpath).text
            return text.strip()
        except:
            return ""
        
    def get_text_in_child_by_xpath(self, parent_element, xpath):
        try:
            text = parent_element.find_element_by_xpath(xpath).text
            return text.replace("\n", " ").strip()
        except:
            return ""
    
    def get_inner_text_in_child_by_xpath(self, parent_element, xpath):
        try:
            text = parent_element.find_element_by_xpath(xpath).get_attribute("innerText")
            return text.replace("\n", " ").strip()
        except:
            return ""
    
    def get_href_in_child_by_xpath(self, parent_element, xpath):
        try:
            href = parent_element.find_element_by_xpath(xpath).get_attribute("href")
            return href.strip()
        except:
            return ""