# Web Scraping

This is a personal project aimed at collecting financial data from companies listed on the B3 stock exchange (formerly Bovespa) on the Infomoney website. The project is developed in Django and uses the BeautifulSoup library for data scraping.

## Project Overview

The project consists of three main functionalities:

1. URL Listing: Users can view a list of URLs representing pages of companies and stocks on the stock exchange. Each URL is constructed based on the data entered by the user (company name and stock name).

2. URL Registration: Users can register new URLs. By providing the company name and stock name, the system creates the URL of the corresponding page on the Infomoney website and saves it in the database.

3. Data Scraping: The system performs scraping of financial data from the pages of registered companies and stocks. Scraped data includes information such as title, stock price, variation, day's low, day's high, and trading volume. The scraped information is then presented to the user.

## Configuration and Execution

To run this project on your own machine, follow these steps:

1. Make sure you have Python and Django installed in your environment.

2. Clone this repository to your machine:


```
git clone 
cd 
```

3. Install the necessary dependencies, including Django and BeautifulSoup:


```
pip install django
pip install beautifulsoup4
pip requests
```

4. Perform database migrations:


```
python manage.py makemigrations
python manage.py migrate
```

5. Start the development server:


```
python manage.py runserver
```

6. Access the application in your browser at http://localhost:8000/.

## Using the Application

1. Access the application's home page.
2. You will see the available URLs for usage (http://127.0.0.1:8000/list_urls/, http://127.0.0.1:8000/register_url/, http://127.0.0.1:8000/scrape_data/).
3. To register a new URL, access the URL (http://127.0.0.1:8000/register_url/), fill out the form with the company name and stock name, and click the "Register URL" button.
4. After registration, you will be redirected to the data scraping page, where the financial data of the registered companies is displayed.

## Notes

1. This project is intended for demonstration and learning purposes only.
2. This project can be extended by adding more features, such as scheduling scraping tasks.
