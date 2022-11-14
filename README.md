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

![image](https://user-images.githubusercontent.com/78736570/201707121-50863865-097c-43a9-8800-2e40b936c772.png)


# ImageResizer

This application uses open-cv to resize the image using the resize method.
This is only command line interface program.
Shows the final result and saves the resized file in root directry as 'resized_imaged.jpg'.

How to use:
1. Start "main.py"
2. Enter name of file you want to resize with its extension.
3. Enter Height and Width of the resized image you want to get.
4. Then the resized image will be saved in root directory and instantly results will be displayed while showing comparison between original and resized image.

# CLI
![image](https://user-images.githubusercontent.com/78736570/201713534-570c0ab2-41f5-4dd8-9212-df38f48b7d8e.png)

# Result
![image](https://user-images.githubusercontent.com/78736570/201713781-612ef70a-a6bb-4edf-9c53-75901e874a27.png)
