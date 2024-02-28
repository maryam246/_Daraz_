from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
import datetime
from colorama import Fore, Style
import os

class DarazScraper:
    current_datetime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S%p")

    def __init__(self, browser):
        self.browser = browser
        self.browser.implicitly_wait(10)
        self.output_directory = 'output'

    def create_output_directory(self):
        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory)

    def save_data_to_file(self, subcategory_name, data):
        filename = f"{self.output_directory}/{subcategory_name}_{DarazScraper.current_datetime}.txt"
        with open(filename, 'a', encoding='utf-8') as output_file:
            output_file.write(data)

    def scrape_product_data(self, url, min_discount_percentage, last_page_css_selector, subcategory_name):
        try:
            self.browser.get(url)

            products_found = 0
            product_count = 1

            while True:
                title_css_selector = f"div.gridItem--Yd0sa:nth-child({product_count}) > div:nth-child(1) > a:nth-child(1) > div:nth-child(2) > div:nth-child(1)"
                link_css_selector = f"div.gridItem--Yd0sa:nth-child({product_count}) > div:nth-child(1) > a:nth-child(1)"
                actual_price_css_selector = f"div.gridItem--Yd0sa:nth-child({product_count}) > div:nth-child(1) > a:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > del:nth-child(1)"
                discount_price_css_selector = f"div.gridItem--Yd0sa:nth-child({product_count}) > div:nth-child(1) > a:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > span:nth-child(2)"

                try:
                    title_element = self.browser.find_element(By.CSS_SELECTOR, title_css_selector)
                    link_element = self.browser.find_element(By.CSS_SELECTOR, link_css_selector)
                    actual_price_element = self.browser.find_element(By.CSS_SELECTOR, actual_price_css_selector)
                    discount_price_element = self.browser.find_element(By.CSS_SELECTOR, discount_price_css_selector)

                    title_text = title_element.text
                    link_text = link_element.get_attribute("href")
                    actual_price_text = actual_price_element.text
                    discount_price_text = discount_price_element.text
                    actual_price_value = float(actual_price_text.replace("Rs. ", "").replace(",", ""))
                    discount_price_value = float(discount_price_text.replace("Rs. ", "").replace(",", ""))
                    discount_percentage = int(((actual_price_value - discount_price_value) / actual_price_value) * 100)

                    if discount_percentage >= min_discount_percentage:
                        # Colorize the print statements
                        print(f"{Fore.GREEN}[DATETIME] {DarazScraper.current_datetime}{Style.RESET_ALL}")
                        print(f"{Fore.CYAN}[TITLE] {title_text}{Style.RESET_ALL}")
                        print(f"{Fore.YELLOW}[URL] {link_text}{Style.RESET_ALL}")
                        print(f"{Fore.BLUE}[Actual Price] {actual_price_text}{Style.RESET_ALL}")
                        print(f"{Fore.RED}[Discount Price] Rs. {discount_price_text}{Style.RESET_ALL}")
                        print(f"{Fore.MAGENTA}[Discount Percentage] {discount_percentage}%{Style.RESET_ALL}\n")

                        self.create_output_directory()
                        self.save_data_to_file(subcategory_name, f"[DATETIME] {DarazScraper.current_datetime}\n[TITLE] {title_text}\n[URL] {link_text}\n[Actual Price] {actual_price_text}\n[Discount Price] Rs. {discount_price_text}\n[Discount Percentage] {discount_percentage}%\n\n")

                        products_found += 1

                    product_count += 1
                except Exception as e:
                    break

            if self.is_last_page(last_page_css_selector):
                print(f"{Fore.YELLOW}0 Product found on this Last page.{Style.RESET_ALL}")
                return False

            self.browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)

            print(f"{products_found} products found on this page.")

        except WebDriverException as wde:
            print(f"{Fore.RED}WebDriverException: {wde}{Style.RESET_ALL}")

        return True

    def is_last_page(self, last_page_css_selector):
        try:
            return self.browser.find_element(By.CSS_SELECTOR, last_page_css_selector) is not None
        except NoSuchElementException:
            return False
