import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from datetime import datetime
from lib.struct import table_layout
from lib.general.drawings import draw_main_menu, draw_config_menu, explain_modes, credits

# ========================================
# ========== GENERAL FUNCTIONS ===========
# ========================================

def prepare_file_path(config, company_name):
    # Prepare the saving directory
    saving_directory = os.path.join(config['saving_directory'], company_name)
    os.makedirs(saving_directory, exist_ok=True)

    # Prepare the file name with a more readable timestamp
    now = datetime.now()
    file_name = f"{company_name}_{now.strftime('%Y-%m-%d_%H.%M.%S')}.xlsx"  # Change .csv to .xlsx
    file_path = os.path.join(saving_directory, file_name)

    return file_path

def configure_scrape(config):
    draw_config_menu()
    print("Please modify the 'config.json' file directly to change the configuration.")
    print("Press any key to return to the main menu...")
    input()

def save_config(config):
    with open('lib/general/config.json', 'w') as f:
        json.dump(config, f)

# ========================================
# =========== PCDIGA FUNCTION ============
# ========================================

def scrape_amazon():
    print("This platform was not developed yet... Try 'pcdiga' instead :D")

def scrape_pcdiga(config, pages_to_scrape):
    # Load the configuration
    with open('lib/general/config.json') as f:
        config = json.load(f)

    # Set the webdriver.edge.driver system property to the path of your Edge driver
    os.environ['webdriver.edge.driver'] = config['driver_path']

    # Instantiate an instance of the Edge webdriver
    driver = webdriver.Edge()

    # Prepare a list to store the scraped data
    data = []

    # Define file_path before the loop
    file_path = prepare_file_path(config, 'pcdiga')

    for page in range(1, pages_to_scrape + 1):
        # Go to the webpage
        driver.get(config['website_url'] + '&page=' + str(page))

        # Wait for the page to load
        wait = WebDriverWait(driver, 5)

        # Find all divs representing a product card
        cards = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "flex") and contains(@class, "flex-col") and contains(@class, "bg-background-off") and contains(@class, "p-1.5") and contains(@class, "md:p-3") and contains(@class, "rounded-r4")]')))

        for card in cards:
            try:
                # Find the title
                title_element = card.find_element(By.XPATH, './/a//span')
                title = title_element.text

                # Find the description
                description_element = card.find_element(By.XPATH, './/div[contains(@class, "h-8") and contains(@class, "text-xs") and contains(@class, "mt-p3") and contains(@class, "md:h-12") and contains(@class, "line-clamp-2") and contains(@class, "md:line-clamp-3") and contains(@class, "md:leading-4") and contains(@class, "text-gray-dark")]')
                description = description_element.text

                # Find the tag
                id_tag = card.find_element(By.XPATH, './/div[contains(@class, "mt-2") and contains(@class, "mb-1.5") and contains(@class, "h-4") and contains(@class, "lg:h-4") and contains(@class, "text-xxs") and contains(@class, "md:text-xs")]')
                id_tag = id_tag.text

                 # Find the stock status
                stock_status_element = card.find_element(By.XPATH, './/div[contains(@class, "stock_status_component") and contains(@class, "flex") and contains(@class, "items-center") and contains(@class, "md:items-start") and contains(@class, "gap-x-2")]')
                stock_status_class = stock_status_element.get_attribute("class")

                # Determine the stock status based on the color
                if "text-red" in stock_status_class:
                    stock_status = "Not available"
                elif "text-green" in stock_status_class or "text-yellow" in stock_status_class:
                    stock_status = "Available"
                else:
                    stock_status = "Unknown"

                # Find the price
                price_element = card.find_element(By.XPATH, './/div[contains(@class, "flex") and contains(@class, "flex-wrap") and contains(@class, "items-center") and contains(@class, "justify-between") and contains(@class, "mt-1") and contains(@class, "gap-x-2")]//div[contains(@class, "flex") and contains(@class, "justify-between") and contains(@class, "flex-grow") and contains(@class, "price_special_price_wrapper")]//div[contains(@class, "text-lg") and contains(@class, "font-extrabold") and contains(@class, "md:text-2xl") and contains(@class, "text-primary")]')
                price = price_element.text

                # Append the title and description to the data list
                data.append([title, description, id_tag, stock_status, price])
            except Exception as e:
                print(f"An error occurred: {e}")

     # Format the Excel file
    table_layout.format_excel_file(data, ['Product Title', 'Product Description', 'Serial Tag', 'Stock Status (At the time)', 'Product Price'], file_path)

    # Don't forget to close the driver
    driver.quit()

# ========================================
# =========== AMAZON FUNCTION ============
# ========================================

    # TO BE DONE ANYTIME!

# ========================================
# ============ SCRAPER FUNC ==============
# ========================================

def scrape_website(platform, pages_to_scrape):
    # Load the configuration
    with open('lib/general/config.json') as f:
        config = json.load(f)

    if platform == 'pcdiga':
        scrape_pcdiga(config, pages_to_scrape)
    elif platform == 'amazon':
        return scrape_amazon()
    else:
        print("Invalid platform")

# ========================================
# ============== MAIN STUFF ==============
# ========================================

def main():
    with open('lib/general/config.json') as f:
        config = json.load(f)

    while True:
        draw_main_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            configure_scrape(config)
        elif choice == "2":
            # Set the webdriver.edge.driver system property to the path of your Edge driver
            os.environ['webdriver.edge.driver'] = config['driver_path']

            # Call the scrape_website function directly for single page scraping
            scrape_website(config['platform'], 1)
        elif choice == "3":
            # Set the webdriver.edge.driver system property to the path of your Edge driver
            os.environ['webdriver.edge.driver'] = config['driver_path']

            # Call the scrape_website function directly with multi-scraping
            scrape_website(config['platform'], config['pages_to_scrape'])
        elif choice == "4":
            explain_modes()
        elif choice == "5":
            credits()
        elif choice =="6":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
