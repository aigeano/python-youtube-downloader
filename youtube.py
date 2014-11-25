from bs4 import BeautifulSoup
import os
import requests
def main():
  url = raw_input("enter the page url\n")
  r = requests.get(url)
  data = r.text
  soup = BeautifulSoup(data)

  for link in soup.find_all('a'):
    if "youtube" in link.get('href'):
      os.system("youtube-dl "+ link.get('href'))

if __name__ == "__main__":
  main()
