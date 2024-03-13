import requests
from bs4 import BeautifulSoup

url = 'https://www.ons.gov.uk/'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, 'html.parser')


def main():
    print("******* UK ECONOMICAL STATISTICS *******")
    try:
        employment_rate()
        unemployment_rate()
        inflation()
        gdp()
        population()
        
    except:
        print("Webscraper no longer working")
    print("*****************************************")

def employment_rate():
    article = soup.find('article')
    section = article.find('section')
    er = section.find('div', class_="tile__figure").get_text()
    ertext = section.find('div', class_="margin-top-md--2").get_text()
    change = section.find('p')
    arrow = change.find('span', class_="tile__trend__icon").get_text().strip()
    change_text = change.find('span', class_="tile__trend__text").get_text()
    print(f"Employment Rate: {er}, {arrow} {change_text}. {ertext}")


def unemployment_rate():
    article = soup.find('article')
    uner_sec = article.find('section', class_="inline-block margin-left--1 col--lg-12 text-align-top")
    ur = uner_sec.find('div', class_="tile__figure").get_text()
    urtext = uner_sec.find('div', class_="margin-top-md--2").get_text()
    ur_change = uner_sec.find('p')
    ur_arrow = ur_change.find('span', class_="tile__trend__icon").get_text().strip()
    ur_change_text = ur_change.find('span', class_="tile__trend__text").get_text()
    print(f"Unemployment Rate: {ur}, {ur_arrow} {ur_change_text}. {urtext}")


def inflation():
    main = soup.find('main')
    section = main.find('section')
    article = section.find('article',
                           class_="tile tile__content col col--md-14 margin-left-md--1 margin-bottom-md--2 height-md--52")
    infaltion = article.find('div', class_="tile__figure").get_text()
    change = section.find('p')
    arrow = change.find('span', class_="tile__trend__icon").get_text().strip()
    change_text = change.find('span', class_="tile__trend__text").get_text()
    print(f"Infaltion Rate: {infaltion}, {arrow} {change_text}.")


def gdp():
    article = soup.find_all('article',
                            class_="tile tile__content col col--md-14 margin-left-md--1 margin-bottom-md--2 height-md--52")
    div = article[1].find('div', class_="tile__figure").get_text()
    change = article[1].find('p')
    arrow = change.find('span', class_="tile__trend__icon").get_text().strip()
    change_text = change.find('span', class_="tile__trend__text").get_text()
    print(f"GDP: {div}, {arrow} {change_text}")


def population():
    article = soup.find('article', class_="tile tile__content margin-top-md--6 margin-left-md--1 height-md--43")
    figure = article.find('div', class_="tile__figure").get_text()
    text = article.find('div', class_="margin-top--2").get_text()
    print(f"Population: {figure}. {text}")


main()
