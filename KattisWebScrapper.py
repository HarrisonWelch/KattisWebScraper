# KattisWebScrapper

import requests
from bs4 import BeautifulSoup
import tkinter
import sched, time
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

def getScoreboard():
  # https://open.kattis.com/universities/apsu.edu
  res = requests.get('https://open.kattis.com/universities/apsu.edu')
  # print('type(res) = ' + str(type(res)))
  # print(res.text) # don't
  soup = BeautifulSoup(res.text, 'html.parser')
  # print('type(soup) = ' + str(type(soup)))

  sections = soup.select('section')

  user_score_section = sections[1]

  user_positions = []
  user_names = []
  user_locations = []
  user_scores = []

  tds = user_score_section.select('td')

  # print(len(tds))

  for i in range(0, len(tds), 4):
    user_positions.append(int(tds[i].getText().strip()))
    user_names.append(tds[i+1].getText().strip())
    user_locations.append(tds[i+2].getText().strip())
    user_scores.append(float(tds[i+3].getText().strip()))

  return user_positions, user_names, user_locations, user_scores

########
# MAIN #
########

if __name__ == "__main__":
    # print(' i = ' + str(i) + ', tds[i] = ' + str(tds[i]))

  # print('user_score_section = \n\n' + str(user_score_section))
  
  
  s = sched.scheduler(time.time, time.sleep)

  def main_loop(sc): 
      print("Doing stuff...")
      # do your stuff
      user_positions = []
      user_names = []
      user_locations = []
      user_scores = []

      user_positions, user_names, user_locations, user_scores = getScoreboard()

      for i in range(len(user_positions)):
        print(str(i+1) + ' ' + str(user_positions[i]) + ' ' + user_names[i] + ' ' + str(user_scores[i]))
      s.enter(5, 1, main_loop, (sc,))

  s.enter(5, 1, main_loop, (s,))
  s.run()

  print("after the run")

  root = tk.Tk()
  app = Application(master=root)
  app.mainloop()

  # NOTE: hi[1] has the table we need