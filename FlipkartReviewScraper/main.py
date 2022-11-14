import csv
from bs4 import BeautifulSoup
import requests

def_webpage = "https://www.flipkart.com/redmi-note-10-pro-dark-nebula-128-gb/product-reviews/itm4cfcbeb29b31c?pid=MOBGB725FTZ3HMNF&lid=LSTMOBGB725FTZ3HMNF9INGUW&marketplace=FLIPKART&q=redmi+note+10+pro&store=tyy%2F4io&srno=s_1_8&otracker=search&otracker1=search&fm=Search&iid=ddf4996d-8812-4c5c-aaa7-6934dc74deb5.MOBGB725FTZ3HMNF.SEARCH&ppt=sp&ppn=sp&ssid=myyisogmqo0000001668210331726&qH=20ef7d326dcad8f3&"


def mainfn(webpage, num_revs):
    page_num = int(int(num_revs) / 10)
    print(num_revs)
    print(page_num)
    page = webpage + f"&page={page_num}"

    def get():
        # Finding parts of reviews with their respective classes
        reviews = soup.find_all('div', class_="col _2wzgFH K0kLPL")
        rev_titles = soup.find_all('p', class_="_2-N8zT")
        rev_descriptions = soup.find_all('div', class_="t-ZTKy")
        rev_upl_times = soup.find_all('p', class_="_2sc7ZR")

        names = []
        times = []
        desc_revs = []
        titles = []
        ratings = []

        # Upload Time
        for index, rev_upl_time in enumerate(rev_upl_times):
            rev_up_text = rev_upl_time.text
            if index % 2 == 0:
                names.append(rev_up_text)
            else:
                times.append(rev_up_text)

        # Descriptive Review
        for rev_desc in rev_descriptions:
            rev_desc_text = rev_desc.text.split("READ MORE")[0]
            desc_revs.append(rev_desc_text)

        # Title
        for rev_title in rev_titles:
            rev_title_text = rev_title.text
            titles.append(rev_title_text)

        # Rating
        for review in reviews:
            rev_upl_time = soup.find('p', class_="_2sc7ZR")
            review_text = review.text
            rating = review_text[0]
            ratings.append(rating)


        # Saving data in csv with csv library
        filename = "flpkrt_prodrevs.csv"
        with open(filename, 'a', encoding="utf-8") as f:
            f.write = csv.writer(f)
            f.write.writerow(['S.No.', 'Rating', 'Title', 'Description', 'Name', 'Timestamp'])

            for i in range(len(ratings)):
                f.write.writerow([i + 1, ratings[i], titles[i], desc_revs[i], names[i], times[i]])

        f.close()


    # Looping through pages and getting all reviews
    if page_num == 1:
        source_text = requests.get(webpage).text
        soup = BeautifulSoup(source_text, 'lxml')
        get()
    else:
        for i in range(1, page_num + 1):
            page = webpage + f"&page={i}"
            source_text = requests.get(page).text
            soup = BeautifulSoup(source_text, 'lxml')
            get()


# Run program if run indivisually with default settings (for testing only)
if __name__ == "__main__":
    mainfn(def_webpage, 10)
