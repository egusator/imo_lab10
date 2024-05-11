import matplotlib.pyplot as plt

class Team:
    name = ""
    wins = 0
    ties = 0
    losses = 0
    points = 0

    def __init__(self, team_name):
        self.name = team_name

teams = [Team("Bulls"),
         Team("Raptors"),
         Team("Lakers"),
         Team("CSKA MOSKVA"),
         Team("LOKOMOTIV")]

import random
import math
def calc_goals_poisson():
    lam = 100 #среднее количество очков (матожидание)
    m = 0
    S = 0
    while S >= -1 * lam:
        S += math.log(random.random())
        m += 1
    return m

average_goals = 5

for team_first in teams:
    for team_second in teams:
        if team_first.name != team_second.name:
            first_goals = calc_goals_poisson()
            second_goals = calc_goals_poisson()
            if first_goals > second_goals:
                team_first.wins += 1
                team_second.losses += 1
                team_first.points += 3
            elif first_goals == second_goals:
                team_first.ties += 1
                team_second.ties += 1
                team_first.points += 1
                team_second.points += 1
            else:
                team_second.wins += 1
                team_first.losses += 1
                team_second.points += 3


teams = sorted(teams, key=lambda team: team.points, reverse=True)

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Team Results")

tree = ttk.Treeview(root, columns=("Name", "Points", "Wins", "Ties", "Losses"), show="headings")
tree.heading("Name", text="Team Name")
tree.heading("Points", text="Points")
tree.heading("Wins", text="Wins")
tree.heading("Ties", text="Ties")
tree.heading("Losses", text="Losses")

for team in teams:
    tree.insert("", "end", values=(team.name, team.points, team.wins, team.ties, team.losses))

tree.column("#0", width=0, stretch=tk.NO)
tree.column("Name", anchor=tk.W, width=150)
tree.column("Points", anchor=tk.E, width=100)
tree.column("Wins", anchor=tk.E, width=100)
tree.column("Ties", anchor=tk.E, width=100)
tree.column("Losses", anchor=tk.E, width=100)

tree.pack(fill=tk.BOTH, expand=True)

root.mainloop()

for team in teams:
    print(team.name, " ", team.wins, " ", team.ties)
