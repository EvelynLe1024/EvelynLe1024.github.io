import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url = 'https://www.newegg.com/Cell-Phones/Category/ID-450?Tpk=cell%20phone'
  
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("div", {"class":"item-container"})

filename = 'cell_phones.csv'
f = open(filename, "w")

headers = "Brand, Product_Name, Shipping_Price, Current_price \n"

f.write(headers)

for container in containers:
	brand_container = container.findAll("img", {"class":"lazy-img"})
	brand = brand_container[1]["title"]
	product_name = container.a.img["title"]
	price_ship_container = container.findAll("li", {"class":"price-ship"})
	shipping_price = price_ship_container[0].text.strip()
	price_container = container.findAll("li", {"class":"price-current"})
	current_price = price_container[0].get_text(strip=True).replace("|","")

	print("Brand: " + brand)
	print("Product_Name: " + product_name)
	print("Shipping_Price: " + shipping_price)
	print("Current_Price: " + current_price)

	f.write(brand + "," + product_name.replace(",", "|") + "," + shipping_price + "," + current_price + "\n")

f.close()


