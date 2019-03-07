# KattisWebScrapper

import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
  # https://open.kattis.com/universities/apsu.edu
  res = requests.get('https://open.kattis.com/universities/apsu.edu')
  print('type(res) = ' + str(type(res)))
  # print(res.text) # don't
  soup = BeautifulSoup(res.text, 'html.parser')
  print('type(soup) = ' + str(type(soup)))

  sections = soup.select('section')

  user_score_section = sections[1]

  user_positions = []
  user_names = []
  user_locations = []
  user_scores = []

  tds = user_score_section.select('td')

  print(len(tds))

  for i in range(0, len(tds), 4):
    user_positions.append(int(tds[i].getText().strip()))
    user_names.append(tds[i+1].getText().strip())
    user_locations.append(tds[i+2].getText().strip())
    user_scores.append(float(tds[i+3].getText().strip()))
    # print(' i = ' + str(i) + ', tds[i] = ' + str(tds[i]))

  # print('user_score_section = \n\n' + str(user_score_section))

  for i in range(len(user_positions)):
    print(str(i+1) + ' ' + str(user_positions[i]) + ' ' + user_names[i] + ' ' + str(user_scores[i]))
  # for i in range(len(hi)):
    # print('hi['+str(i)+'] getText = ' + str(hi[i].getText()))

  

  # NOTE: hi[1] has the table we need