# Amazon-Scraping
Python script that scrapes Amazon PDP info from a given URL, logs product and variation details into a spreadsheet.

Steps to Use:
  1. Download Log.xlsx and scraper.py to the same folder
  2. Modify 'Actual' sheet to reflect the products, correct variation info, and URLs you want to scrape
  3. Close the Log.xlsx file
  4. Run scraper.py
  5. Check 'Logged' sheet to review the collected data - cells will be highlighted in red if its data doesn't match the data from the same cell in the 'Actual' sheet
  
Troubleshooting Tips:
- close the Excel file Log.xlsx before running scraper.py!!!
- make sure correct libraries are downloaded
- make sure URLs in Column I/9 are correct
