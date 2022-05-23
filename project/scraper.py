from csv import reader

base_url = "https://www.amazon.{country}/dp/{asin}"
print(base_url)
url_list = []

with open('/home/vostroraf/Documents/credicxo/project/Amazon Scraping - Sheet1.csv', 'r') as linklist:
    csv_read = reader(linklist)
    count  = 0
    for row in csv_read:
        if count > 0:
            url_list.append(base_url.format(country = row[3], asin = row[2]))
        count += 1
for i in url_list:
    print(i)
