# Web Scraping Project

This project is a mockup for a web scraping application. It is designed to scrape product data from websites and save it in an Excel file. Currently, the application supports scraping from PCDiga.

![Web Scraping Image](https://i.imgur.com/1AxpyxV.png)

## Setup

To set up this project on your local machine, follow these steps:

1. **Clone the repository**: Use the command `git clone <repository_url>` to clone the repository to your local machine.

2. **Install the required packages**: This project requires several Python packages, including `selenium`, `pandas`, and `datetime`. You can install these packages using pip:

    ```bash
    pip install selenium pandas datetime
    ```

3. **Download the Edge driver**: This project uses the Selenium WebDriver with Microsoft Edge. You need to download the Edge driver that matches your browser version. You can download it from the Microsoft Edge Driver website.

4. **Update the config.json file**: The `config.json` file contains the configuration for the web scraper. Update this file with the correct platform, website URL, driver path, saving directory, and number of pages to scrape.

## Usage

The application has two modes: Single-Scraping and Multi-Scraping.

- **Single-Scraping**: This mode scrapes only one page from the website.

- **Multi-Scraping**: This mode scrapes multiple pages from the website. The number of pages to scrape is specified in the 'pages_to_scrape' field in the 'config.json' file.

To start the application, run the `main.py` script. A menu will be displayed where you can choose to configure the scrape, start single-scraping, start multi-scraping, or exit the application.

## Future Work

This project is a mockup and is still under development. In the future, I plan to add support for more websites and improve the scraping capabilities.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.
