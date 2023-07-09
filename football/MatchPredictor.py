
from random import randint
import webbrowser
from tkinter import Button, E, LabelFrame, messagebox, Label, Menu, W, Tk
from tkinter.ttk import Combobox

from PIL import Image, ImageTk


window = Tk()

#GUI window
window.title('Match Predictor')
window.geometry('660x700')
window.resizable(False, False)

#Logo
FRAME2 = LabelFrame(window)
FRAME2.grid(padx=10, pady=10)
IMAGEX = Image.open('messi.jpg')
PHOTOX = ImageTk.PhotoImage(IMAGEX)
LABELX = Label(FRAME2, image=PHOTOX)
LABELX.IMAGEX = PHOTOX
LABELX.grid(padx=3, pady=3)

def about_menu():
    """About program menu text."""
    messagebox.showinfo('Program Information', 'Match Predictor\n'  \
                        'For 2019-2020 Premier League season.\n\n')

def help_menu():
    """How to use the program menu help text."""
    messagebox.showinfo('How To...', 'Match Predictor\n\n'  \
                        'To obtain a prediction for any Premier League football'  \
                        ' match for the 2019-2020 season, first select the home'  \
                        ' team from the drop down list on the left, and then '  \
                        'select the away team from the drop down list on '  \
                        'the right.\n\nNow click on the green '  \
                        '<=-Predict Result-=> button to get the prediction.\n\n'  \
                        'You can also click on the <=- See Team Stats -=> '  \
                        'to get a webpage full of the latest stats for all PL teams.'  \
                        '\n\nIf you click on the Menu (top left of the program)'  \
                        ' you can view information about this program, '  \
                        'or quit the program.\n\n')

#Menu
MENU_BAR = Menu(window)
FILE_MENU = Menu(MENU_BAR, tearoff=0)
MENU_BAR.add_cascade(label='Menu', menu=FILE_MENU)
FILE_MENU.add_separator()
FILE_MENU.add_command(label='Help', command=help_menu)
FILE_MENU.add_separator()
FILE_MENU.add_command(label='About', command=about_menu)
FILE_MENU.add_separator()
FILE_MENU.add_command(label='Exit', command=window.destroy)
window.config(menu=MENU_BAR)

#Creating ratings
TEAM = {
    'Arsenal': 4,
    'Aston Villa': 1,
    'Bournemouth': 2,
    'Brighton': 1,
    'Burnley': 3,
    'Chelsea': 4,
    'Crystal Palace': 3,
    'Everton': 2,
    'Leicester': 4,
    'Liverpool': 7,
    'Man City': 5,
    'Man Utd': 4,
    'Newcastle': 1,
    'Norwich': 0,
    'Sheff Utd': 2,
    'Southampton': 0,
    'Tottenham': 4,
    'Watford': 0,
    'West Ham': 2,
    'Wolves': 3
}

def prediction():
    """Display dodgy prediction"""
    home_team = COMBO1.get()
    away_team = COMBO2.get()

    #Same team chosen
    if away_team == home_team:
        messagebox.showinfo('ERROR!', 'You have selected the same teams.\n'  \
                            'Please choose two different teams.')
        return


    htw = TEAM[home_team]
    htw += 1 # home advantage
    atw = TEAM[away_team]

    # Calculating score
    home_score = 0
    away_score = 0
    orig_diff = 0
    ratings_diff = abs(htw-atw)

    if ratings_diff > 3:
        orig_diff = ratings_diff
        ratings_diff = 3

    if htw == atw:
        result = 'A Draw'
        rnd_drawscore = (randint(0, 2))
        away_score = rnd_drawscore
        home_score = rnd_drawscore

    if htw > atw:
        result = 'Home Win'
        away_score = 0
        home_score = ratings_diff
        if abs(ratings_diff-orig_diff) > 2:
            away_score = 1

    if htw < atw:
        result = 'Away Win'
        home_score = 0
        away_score = ratings_diff
        if abs(ratings_diff-orig_diff) > 2:
            home_score = 1

    predicted_score = (str(home_score)+" - "+str(away_score))

    result_msg = ' You Selected:\n {} V {} \n\n Our prediction is:\n {}'  \
                 '\n\n Predicted score : {}'  \
                 .format(home_team, away_team, result, predicted_score)

    messagebox.showinfo('Match Predictor', 'Adjusted ratings:\n'  \
                        'Home team:' +str(htw)+'pts, Away Team:'+str(atw)+'pts.\n\n'+str(result_msg))


def view_pl_stats():
    """Open web browser to see current team and player stats."""
    webbrowser.open('https://www.premierleague.com/tables')

def info_creators():
    messagebox.showinfo('THE CREATOR', 'Israr Ahmad \n')

#List creation from dict
TEAM_LIST = (list(TEAM.keys()))
TEAM_VALUES = (list(TEAM.values()))

#To create button
FRAME0 = LabelFrame(window)
FRAME0.grid(padx=8, pady=8)
LAB1 = Label(FRAME0, bg='skyblue', text='Select Home Team')
LAB1.grid()
LAB2 = Label(FRAME0, bg='#F177BF', text='Select Away Team')
LAB2.grid(row=0, column=1)


# combo boxes.
COMBO1 = Combobox(FRAME0)
COMBO1['values'] = (TEAM_LIST)
COMBO1.current(7)
COMBO1.grid(padx=5, pady=5)

COMBO2 = Combobox(FRAME0)
COMBO2['values'] = (TEAM_LIST)
COMBO2.current(16)
COMBO2.grid(padx=5, pady=5, row=1, column=1)

# Stats button.
FRAME1 = LabelFrame(window)
FRAME1.grid(padx=8, pady=8)
STATS_BTN = Button(FRAME1, bg='darkcyan', text='See Team Stats',
                   command=view_pl_stats)
STATS_BTN.grid(sticky=W+E, padx=5, pady=5)

# Predict button.
BTN = Button(FRAME1, bg='lightgreen', text='Predict Result',
             command=prediction)
BTN.grid(sticky=W+E, padx=5, pady=5)

BTN1 = Button(FRAME1, bg='#CAF905', text='By',
             command=info_creators)
BTN1.grid(sticky=W+E, padx=15, pady=10)

window.mainloop()
