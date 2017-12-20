from tkinter import *
import random

tk = Tk()
tk.title("Kuki kliker")
canvas = Canvas(tk, width = 1000, height = 600, bg = "#9400D3")
canvas.pack()
tk.resizable(width = False, height = False)

para = 0
cps = 0
babki = [0, 100, 1]
farms = [0, 5000, 20]

def updateLabel(array):
    text = StringVar()
    text.set("cost: " + shortScore(int(array[1])) + " count: " + shortScore(int(array[0])))

    return Label(tk, height = 1, width = 30, textvariable = text, bg = "#9400D3")


#effect = [promenlivka, s kolko promenqme, za kolko vreme]
effects = []

class Potionka:
    def __init__(self, effect, img, x, y):
        self.effect = effect
        self.button = Button(tk, image = img, width = 50, height = 50, command = self.applyEffect, state = ENABLED)

    def applyEffect(self):
        effects.append(self.effect)



class Kopche:
    def __init__(self, items, img, x, y):
        self.items = items
        self.button = Button(tk, image = img, width = 200, height = 60, command = self.add, state = DISABLED)
        self.label = updateLabel(self.items)
        self.x = x
        self.y = y
        self.label.place(x = self.x, y = self.y-20)
        self.button.place(x = self.x, y = self.y)

    def updateButton(self):
        if para >= self.items[1]:
            self.button.config(state = "normal")
        else:
            self.button.config(state = "disabled")

    def add(self):
        global para
        global cps

        self.items[0] += 1
        para -= self.items[1]
        self.items[1] *= 1.1
        cps += self.items[2]
        self.label = updateLabel(self.items)
        self.label.place(x = self.x, y = self.y-20)

        self.updateButton()

def clicks():
    global para
    para += 100
    num1.set(shortScore(int(para)) + "\nPer second: " + shortScore(cps))
    baba.updateButton()
    farm.updateButton()
    fabrika.updateButton()
    kolichka.updateButton()
    passat.updateButton()

def shortScore(score):
    char = ""
    if(score >= 10**3 and score < 10**6):
        score /= 1000
        char = "K"
    if(score >= 10**6 and score < 10**9):
        score /= 1000000
        char = "M"
    if(score >= 10**9):
        score /= 1000000000
        char = "B"

    return str(round(score, 1)) + char


num1 = StringVar()

img1 = PhotoImage(file = "babka.png")
baba = Kopche([0, 100, 1], img1, 650, 30)

img2 = PhotoImage(file = "farm.png")
farm = Kopche([0, 1000, 20], img2, 650, 150)

img3 = PhotoImage(file = "kolichka.png")
kolichka = Kopche([0, 30000, 50], img3, 650, 270)

img4 = PhotoImage(file = "factory.png")
fabrika = Kopche([0, 100000, 100], img4, 650, 390)

img5 = PhotoImage(file = "passat.png")
passat = Kopche([0, 2000000, 1000], img5, 650, 510)

pikture = PhotoImage(file = "kuki.png")

score = Label(tk, height = 2, width = 15, textvariable = num1, bg = "#9400D3", font = "Helvetica 17 bold")
score.place(x = 425, y = 228)

cookie = Button(tk, image = pikture, width = 160, height = 160, bg = "#9400D3", highlightthickness = 0, bd = 0, activebackground = "#9400D3", command = clicks)
cookie.place(x = 440, y = 60)

img6 = PhotoImage(file = "kolec.png")
pot1 = Potionka(["para", para, 5], img6, 100, 200)


def getHighScore():
    return open("score.txt", "r").read()

hss = StringVar()
hss.set("High Score : \n" + shortScore(int(getHighScore())))
highScore = Label(tk, height = 2, width = 13, textvariable = hss, bg = "#9400D3", font = "Helvetica 17 bold")
highScore.place(x = 425, y = 480)

label = Label(tk)

def checkRandom():
    a = random.uniform(0, 1)
    if a < 0.001:
        return True
    return False

def saveHighScore():
    file = open("score.txt", "r")
    if int(file.read()) < para:
        open("score.txt", "w").close()
        file = open("score.txt", "w")
        file.write(str(int(para)))

def updateTimer():
    global para
    global hss

    for effect in effects:
        if effect == []:
            continue
        eval(effect[0] = effect[0] + effect[1]/10)
        effect[2] -= 0.1
        if effect[2] == 0:
            effect = []

    if checkRandom():
        print("ebago")
    saveHighScore()
    para += cps/10
    hss.set("High Score: \n" + shortScore(int(getHighScore())))
    num1.set(shortScore(int(para)) + "\nPer second: " + shortScore(cps))
    score['text'] = str(num1)
    label.after(100, updateTimer)

updateTimer()
