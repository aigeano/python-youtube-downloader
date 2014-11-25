from bs4 import BeautifulSoup
import os
import requests
def main():

  r = requests.get("http://web.stanford.edu/class/cs106b/lecture-videos.shtml")
  data = r.text
  soup = BeautifulSoup(data)

  for link in soup.find_all('a'):
    if "youtube" in link.get('href'):
      os.system("youtube-dl "+ link.get('href'))

if __name__ == "__main__":
  main()
