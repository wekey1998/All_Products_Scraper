#!/usr/bin/env python
# coding: utf-8

# In[ ]:


###Description: 
###This script automates the extraction of product data (URLs, titles, and prices) from e-commerce websites using Selenium. 
###Users can specify the website's URL pattern, along with the necessary XPath selectors for product details. 
###The extracted data is saved in a CSV file.

import csv
import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def random_delay(min_delay=5, max_delay=8):
    """Introduce a random delay to mimic human behavior."""
    time.sleep(random.uniform(min_delay, max_delay))

class ProductData:
    """Class to store product data."""
    def __init__(self, url, title, price):
        self.url = url
        self.title = title
        self.price = price

def main():
    # User input for driver path
    gecko_path = input("Enter the path to GeckoDriver: ").strip()
    
    # Set up Firefox options
    options = Options()
    options.add_argument("--headless")  # Run in headless mode (optional)
    
    driver = webdriver.Firefox(executable_path=gecko_path, options=options)

    try:
        # Prompt user for base website URL with page number placeholder
        base_url = input("Enter the base URL with {page} as a placeholder for pagination:\n"
                         "Example: https://example.com/page/{page}/items\n").strip()
        if "{page}" not in base_url:
            print("Invalid URL. Ensure it includes {page} as a placeholder. Exiting.")
            return

        # Prompt user for XPath of product details
        link_xpath = input("Enter the XPath for product links: ").strip()
        title_xpath = input("Enter the XPath for product titles: ").strip()
        price_xpath = input("Enter the XPath for product prices: ").strip()

        # Page range input
        try:
            start_page = int(input("Enter the starting page number: "))
            end_page = int(input("Enter the ending page number: "))
            if start_page < 1 or end_page < start_page:
                raise ValueError
        except ValueError:
            print("Invalid page range. Exiting.")
            return

        # Output file path
        output_file = input("Enter the output CSV file path: ").strip()

        all_product_data = []

        # Loop through the specified pages
        for page in range(start_page, end_page + 1):
            driver.get(base_url.replace("{page}", str(page)))
            random_delay()

            # Wait for page to load
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

            # Extract product links, titles, and prices
            product_links = driver.find_elements(By.XPATH, link_xpath)
            product_titles = driver.find_elements(By.XPATH, title_xpath)
            product_prices = driver.find_elements(By.XPATH, price_xpath)

            for i in range(len(product_links)):
                href = product_links[i].get_attribute("href")
                title = product_titles[i].text if i < len(product_titles) else "N/A"
                price = product_prices[i].text if i < len(product_prices) else "N/A"

                if href:
                    all_product_data.append(ProductData(url=href, title=title, price=price))

        # Write data to CSV
        with open(output_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["URL", "Title", "Price"])
            for data in all_product_data:
                writer.writerow([data.url, data.title, data.price])

        print(f"Scraping complete! Data saved to {output_file}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()

