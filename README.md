# All_Products_Scraper
This Python script automates the extraction of product data (URLs, titles, and prices) from e-commerce websites using Selenium. Users can specify the website's URL pattern along with the necessary XPath selectors for product details. The extracted data is saved in a CSV file.

## Features
- Scrapes product URLs, titles, and prices from paginated e-commerce websites.
- Uses Selenium to navigate and extract data.
- Random delays to mimic human browsing behavior.
- Saves extracted data into a CSV file.
- Customizable via user input (URL, XPath selectors, page range, etc.).

## Requirements
- Python 3.7+
- Firefox Web Browser
- GeckoDriver (compatible with your Firefox version)
- Selenium library

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/your-username/ecommerce-product-scraper.git
   cd ecommerce-product-scraper
   ```
2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Mac/Linux
   venv\Scripts\activate  # On Windows
   ```
3. Install dependencies:
   ```sh
   pip install selenium
   ```

## Usage
1. Run the script:
   ```sh
   python scraper.py
   ```
2. Provide the required inputs:
   - Path to `geckodriver`
   - Base URL with `{page}` placeholder for pagination (e.g., `https://example.com/page/{page}/items`)
   - XPath selectors for product links, titles, and prices
   - Page range (start and end page numbers)
   - Output CSV file path
3. The script will navigate through the pages, extract product data, and save it in the specified CSV file.

## Example Output
Example of a CSV file output:
```
URL, Title, Price
https://example.com/product1, "Product 1", "$19.99"
https://example.com/product2, "Product 2", "$29.99"
```

## Notes
- Ensure you have the correct XPath selectors for the e-commerce site you are scraping.
- Some websites implement bot protection, so frequent scraping may result in being blocked.
- Modify `random_delay()` values to reduce detection risks.

## License
This project is licensed under the MIT License.

## Author
Vigneshwaran

