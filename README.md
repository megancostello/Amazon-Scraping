# Amazon-Scraping
Python script that scrapes Amazon PDP info from a given URL, logs product and variation details into a spreadsheet.

Specifically, it gets Product Title, Brand, Style Count of Parent, Size Count of Parent, Color Count of Parent, Selected Style, Selected Size, Selected Color from the product URL. After logging it into the spreadsheet, it highlights cells that don't match the given specifications for each product. This was made to make "firewatching" / looking for broken Amazon product variations easier for Amazon Sellers/Vendors and their catalog managers.  

'Actual' sheet in Log.xlsx is for given and correct product specifications. 'Logged' sheet in Log.xlsx is where the current Amazon page data is stored after scraping. 

## **Steps to Use:**
  1. Download Log.xlsx and scraper.py to the same folder
  2. Modify 'Actual' sheet to reflect the products, correct variation info, and URLs you want to scrape
  3. Close the Log.xlsx file
  4. Run scraper.py
  5. Check 'Logged' sheet to review the collected data - cells will be highlighted in red if its data doesn't match the data from the same cell in the 'Actual' sheet
  
## **Troubleshooting Tips:**
- close the Excel file Log.xlsx before running scraper.py!!!
- put both Log.xlsx and scraper.py in the SAME folder
- make sure correct libraries are downloaded
- make sure URLs in Column I/9 are correct

## **Potential Improvement Ideas:**
- add a timestamp for each row
- add email alerts when a variation is incorrect (red highlighted cell)
