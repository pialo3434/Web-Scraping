# lib/general/drawings.py

def draw_main_menu():
    print("=================================")
    print("=           MAIN MENU           =")
    print("=================================")
    print("1. Configure Scrape")
    print("2. Single-Scraping")
    print("3. Multi-Scraping")
    print("4. About Modes (Multi & Single)")
    print("5. Credits")
    print("6. Exit")
    print("=================================")

def draw_config_menu():
    print("=================================")
    print("=       CONFIGURE SCRAPE        =")
    print("=================================")
    print("To configure the scraping settings, please modify the 'config.json' file.")
    print("Here are some tips:")
    print("1. 'platform': Specify the website you want to scrape (Since this is just a mockup there is only pcdiga no caps just pcdiga).")
    print("2. 'website_url': Enter the URL of the page you want to scrape.")
    print("3. 'driver_path': Enter the path of your Edge driver. It must match your browser version.")
    print("4. 'saving_directory': Specify the directory where the platform folders will be created.")
    print("5. 'pages_to_scrape': Specify the number of times the multi-scrap will happen (Only work for multi-scrap).")
    print("=================================")

def explain_modes():
    print("=================================")
    print("=       ABOUT SCRAPING MODES    =")
    print("=================================")
    print("1. Single-Scraping: This mode will scrape only one page from the website.")
    print("2. Multi-Scraping: This mode will scrape multiple pages from the website. \nThe number of pages to scrape is specified in the 'pages_to_scrape' field in the 'config.json' file.")
    print("3. I made this to purely to learn how to make webscrap its actually insanly easy and it was an interesting experience.\nIf you want to contribute to this project let me know but hey code is all yours!\n")
    print("=================================")
    print("Press any key to return to the main menu...")
    input()

def credits():
    print("=================================")
    print("=             CREDITS           =")
    print("=================================")
    print("Hope this tool is helpfull to you! If you want to know more about my work let me know!\n")
    print("GITHUB: https://github.com/pialo3434\nLinkedin: https://www.linkedin.com/in/paulo-costa-b65ba9188/\nDiscord: pialo34\n")
    print("Press any key to return to the main menu...")
    input()