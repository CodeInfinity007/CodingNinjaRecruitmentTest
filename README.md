# FlipkartReviewScraper

This application uses BeautifulSoup library to scrape reviews of any flipkart product and stores them in a csv file with the help of csv library.
This can be run with or without the UI.

How to use:
1. Install all the requirements through "reuirements.txt"
2. Run "ui.py" for use with UI or "main.py" to use directly.
3. The program may hang if there are more than 20 reviews to fetch.
4. It stores all the reviews in "flpkrt_prodrevs.csv" in the root directory itself.
5. If number of reviews to fetch is not a multiple of 10 then the value is flored and that many number of reviews are fetched.

![image](https://user-images.githubusercontent.com/78736570/201704931-419e0037-208d-49c4-956c-7e3e0bb0bc05.png)
