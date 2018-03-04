import requests
from bs4 import BeautifulSoup, NavigableString

def get_session(username, password):
  url = 'http://sturc.birjand.ac.ir/tm.php'
  # Set connection through requests
  session = requests.Session()
  # Post user and pass to the login form
  response = session.post(url, data = {'user': username ,'pass':password})

  return requests.utils.dict_from_cookiejar(session.cookies)


def panel(session):
  list = []
  url = 'http://sturc.birjand.ac.ir/panel/index.php'
  # Get the panel page data after login
  page = requests.get(url, cookies=session)
  # -------------------------------------
  soup = BeautifulSoup(page.content,'lxml')
  trs = soup.findAll("tr")
  
  counter = 0

  for tr in trs[3:]:
    tds = tr.findAll('td')
    for td in tds:
      counter = (counter + 1) % 8
      if counter == 1:
        td.insert(0, NavigableString('درس شماره '))
        td.insert(0, NavigableString('\n'))
      elif counter == 3:
        td.insert(0, NavigableString('غیبت موجه: '))
      elif counter == 4:
        td.insert(0, NavigableString('غیبت غیر موجه: '))
      elif counter == 5:
        td.insert(0, NavigableString('کل غیبت ها: '))
      elif counter == 6:
        td.insert(0, NavigableString('حد مجاز: '))

      list.append(td.text)

  return '\n'.join(list), ((trs[1].find('td')).text) + '👇👇👇'
