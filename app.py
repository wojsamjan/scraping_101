# import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup


# specify the url
quote_page = 'http://www.bloomberg.com/quote/SPX:IND'

# query the website and return the html to the variable 'page'
page = urlopen(quote_page)

# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')

# Take out the <div> of name and get its value
name_box = soup.find('h1', attrs={'class': 'name'})

name = name_box.text.strip()  # strip() is used to remove starting and trailing
print(name)

# get the index price
price_box = soup.find('div', attrs={'class': 'price'})
price = price_box.text
print(price)


# specify the url
quote_page = 'https://www.bloomberg.com/markets/stocks'

# query the website and return the html to the variable 'page'
page = urlopen(quote_page)

# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')

names = [td.text.strip() for td in (td.find('td', attrs={'class': 'data-table-row-cell', 'data-type': 'name'}) for td in
                                    soup.find_all('tr', attrs={'class': 'data-table-row'})) if td]
for name in names:
    print(name)
