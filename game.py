import random
import time
from tkinter import *

class Mono():
    # init
    def __init__(self, master):
        self.master = master
        window.title("MONO")
        window.geometry("1600x1002")
        navbar = Menu(self.master)
        self.master.config(menu=navbar)
        file_menu = Menu(navbar)
        file_menu.add_command(label="New Game", command=self.userDetails)
        file_menu.add_command(label="Load Game", command=self.load)
        file_menu.add_command(label="Exit", command=self.end_program)
        navbar.add_cascade(label="File", menu=file_menu)
        option_menu = Menu(navbar)
        option_menu.add_command(label="SFW!", command=self.bossKey)
        navbar.add_cascade(label="Options", menu=option_menu)
        self.backgroundImage = PhotoImage(file="gamejungle.png")
        self.mainBGImage = PhotoImage(file="jungle.png")
        self.playerSpriteImage = PhotoImage(file="monkey.png")
        self.fireballSpriteImage = PhotoImage(file="fireball.png")
        self.livesHeartImage = PhotoImage(file="lives.png")
        self.vineImage = PhotoImage(file="vine.png")
        self.bossKeyImage = PhotoImage(file="bosskey.png")
        self.instructionImage = PhotoImage(file="instruction.png")
        self.game_over_image = PhotoImage(file="gameover.png")
        self.bananas = []
        self.fireballs = []
        self.create_fball = False
        labelMenu = Label(window, image=self.mainBGImage)
        labelMenu.place(x=0, y=0, relwidth=1, relheight=1)
        window.resizable(False, False)
        Button(self.master, text="NEW GAME", command=self.userDetails,
               height="3", width="30").place(x="530", y="350")
        Button(self.master, text="LOAD GAME", command=self.load, height="3",
               width="30").place(x="530", y="450")
        Button(self.master, text="INSTRUCTIONS", command=self.instructions,
               height="3", width="30").place(x="530", y="550")
        Button(self.master, text="LEADERBOARD", command=self.leaderboard,
               height="3", width="30").place(x="530", y="650")
        Button(self.master, text="QUIT", command=self.end_program, height="3",
               width="30").place(x="530", y="750")

    def instructions(self):
        global instWindow
        instWindow = Toplevel(self.master)
        instWindow.geometry("1600x1002")
        labelInstructions = Label(instWindow, image=self.instructionImage)
        labelInstructions.place(x=0, y=0, relwidth=1, relheight=1)
        instWindow.resizable(False, False)
        Button(instWindow, text="BACK", command=instWindow.destroy, height="2",
               width="15").place(x="620", y="890")

    def gameOver(self):
        global gameoverWindow
        gameoverWindow = Toplevel(self.master)
        gameoverWindow.geometry("1600x1002")
        labelGameOver = Label(gameoverWindow, image=self.game_over_image)
        labelGameOver.place(x=0, y=0, relwidth=1, relheight=1)
        gameoverWindow.resizable(False, False)
        Button(gameoverWindow, text="MAIN MENU", command=self.restart,
               height="3", width="20").place(x="200", y="600")
        Button(gameoverWindow, text="LEADERBOARD", command=self.leaderboard,
               height="3", width="20").place(x="600", y="600")
        Button(gameoverWindow, text="QUIT", command=self.end_program,
               height="3", width="20").place(x="1000", y="600")

    def end_program(self):
        sys.exit(0)

    def restart(self, event=None):
        window.after_cancel(self.bananaMoveAfter)
        window.after_cancel(self.createBananaAfter)
        window.after_cancel(self.fireballMoveAfter)
        window.after_cancel(self.createFireballAfter)
        self.bananas = []
        self.fireballs = []
        self.create_fball = False
        window.destroy()

    def leaderboard(self):
        leaderboard_file = open("leaderboardFile.txt", "r")
        leaderboard_names = []
        leaderboard_scores = []
        leaderboard_displayNames = []
        leaderboard_displayScores = []

        leaderboard_info = leaderboard_file.readlines()
        leaderboard_info = [item.rstrip("\n") for item in leaderboard_info]

        for desired_output in leaderboard_info:
            try:
                desired_output = int(desired_output)
                leaderboard_scores.append(desired_output)
            except ValueError:
                leaderboard_names.append(desired_output)
        for i in range(5):
            check = leaderboard_scores.index(max(leaderboard_scores))
            leaderboard_displayNames.append(leaderboard_names[check])
            leaderboard_displayScores.append(leaderboard_scores[check])
            leaderboard_scores.pop(check)
            leaderboard_names.pop(check)
        print (leaderboard_displayNames)
        print (leaderboard_displayScores)
        self.leaderboard_window = Toplevel(self.master)
        self.leaderboard_window.title("Leaderboard")
        self.leaderboard_window.geometry("1600x1002")
        self.leaderboard_window.config(bg='black')

        canvas4 = Canvas(self.leaderboard_window, width=1600, height=1002,
                         bg="black")
        canvas4.pack(expand=True, fill=BOTH)

        canvas4.create_text(800, 100, text='Leaderboard:', fill="white",
                            font=('Times New Roman', 40))

        canvas4.create_text(180, 250, text='1: ', fill="yellow",
                            font=('Helvetica', 24), anchor="w")
        canvas4.create_text(750, 250, text=leaderboard_displayNames[0],
                            fill="yellow", font=('Times New Roman', 24),
                            anchor="w")
        canvas4.create_text(1350, 250, text=str(leaderboard_displayScores[0]),
                            fill="yellow", font=('Times New Roman', 24),
                            anchor="w")

        canvas4.create_text(180, 350, text='2: ', fill="grey",
                            font=('Helvetica', 20), anchor="w")
        canvas4.create_text(750, 350, text=leaderboard_displayNames[1],
                            fill="grey", font=('Times New Roman', 20),
                            anchor="w")
        canvas4.create_text(1350, 350, text=str(leaderboard_displayScores[1]),
                            fill="grey", font=('Times New Roman', 20),
                            anchor="w")

        canvas4.create_text(180, 450, text='3: ', fill="brown",
                            font=('Helvetica', 18), anchor="w")
        canvas4.create_text(750, 450, text=leaderboard_displayNames[2],
                            fill="brown", font=('Times New Roman', 18),
                            anchor="w")
        canvas4.create_text(1350, 450, text=str(leaderboard_displayScores[2]),
                            fill="brown", font=('Times New Roman', 18),
                            anchor="w")

        canvas4.create_text(180, 550, text='4: ', fill="white",
                            font=('Helvetica', 18), anchor="w")
        canvas4.create_text(750, 550, text=leaderboard_displayNames[3],
                            fill="white", font=('Times New Roman', 18),
                            anchor="w")
        canvas4.create_text(1350, 550, text=str(leaderboard_displayScores[3]),
                            fill="white", font=('Times New Roman', 18),
                            anchor="w")

        canvas4.create_text(180, 650, text='5: ', fill="white",
                            font=('Helvetica', 18), anchor="w")
        canvas4.create_text(750, 650, text=leaderboard_displayNames[4],
                            fill="white", font=('Times New Roman', 18),
                            anchor="w")
        canvas4.create_text(1350, 650, text=str(leaderboard_displayScores[4]),
                            fill="white", font=('Times New Roman', 18),
                            anchor="w")

        canvas4.create_text(800, 800,
                            text='Press the ESCAPE (Esc) key to go back:',
                            fill="white", font=('Times New Roman', 20))

        canvas4.bind("<Escape>", self.destroy_leaderboard)
        canvas4.focus_set()

    def destroy_leaderboard(self, event):
        self.leaderboard_window.destroy()

    def userDetails(self):
        global userWindow, userEntry
        userWindow = Toplevel(self.master)
        userWindow.title("MONO: Enter Details")
        userWindowMessage = Message(userWindow,
                                    text="To continue"
                                    ", enter your player name:")
        userWindowMessage.pack()
        userEntry = Entry(userWindow, text="Name")
        userEntry.pack()
        Button(userWindow, text="CONTINUE",
               command=self.createPlayer).pack()  # Validate!

    def createPlayer(self):
        global currentPlayer
        window.withdraw()
        currentPlayer = Monkey(userEntry.get())
        print(currentPlayer.playerName)
        userWindow.destroy()
        self.startGame()

    def startGame(self):
        global playerSprite, canvas, canvasHeight
        global canvasWidth, score, lives, bossKeyCheck, gameWindow

        gameWindow = Toplevel(self.master)
        gameWindow.geometry("1600x1002")
        navbar = Menu(self.master)
        self.master.config(menu=navbar)
        file_menu = Menu(navbar)
        file_menu.add_command(label="Save", command=self.save)
        file_menu.add_command(label="Exit", command=window.destroy)
        navbar.add_cascade(label="File", menu=file_menu)
        option_menu = Menu(navbar)
        option_menu.add_command(label="Pause", command=self.pause)
        option_menu.add_command(label="SFW!", command=self.bossKey)
        navbar.add_cascade(label="Options", menu=option_menu)
        canvas = Canvas(gameWindow, width=1600, height=1002)
        canvas.pack(expand=True, fill=BOTH)
        gameWindow.resizable(False, False)
        bgImage = canvas.create_image(0, 0, anchor="nw",
                                      image=self.backgroundImage)
        wordScore = canvas.create_text(180, 110, text='Score:', fill="white",
                                       font=('Helvetica', 18))
        score = canvas.create_text(180, 170, text=str(currentPlayer.score),
                                   fill="white", font=('Helvetica', 18))
        livesHeart = canvas.create_image(1425, 140, image=self.livesHeartImage)
        lives = canvas.create_text(1425, 140, text=str(currentPlayer.lives),
                                   fill="white",
                                   font=('Helvetica', 16, "bold"))
        canvasHeight = int(canvas.cget("height"))
        canvasWidth = int(canvas.cget("width"))
        x = int(canvasWidth / 4)
        y = int((4 * canvasHeight) / 7)
        self.paused = 0
        self.bossActive = 0
        self.playerSprite = canvas.create_image(x, y,
                                                image=self.playerSpriteImage)
        canvas.focus_set()

        self.createBanana()
        self.bananaMove()
        self.createFireball()
        self.fireballMove()
        self.collisionDetection()
        self.fbCollisionDetection()

        canvas.bind("p", self.pause)
        canvas.bind("b", self.bossKey)
        canvas.bind("s", self.save)
        canvas.bind("<Escape>", self.restart)

        canvas.bind("<Up>", self.moveUp)
        canvas.bind("<Down>", self.moveDown)
        canvas.bind("<Left>", self.moveLeft)
        canvas.bind("<Right>", self.moveRight)

        canvas.bind("1", self.cheat_one)
        canvas.bind("2", self.cheat_two)
        # canvas.bind("3", self.cheat_three)

    def cheat_one(self, event):
        currentPlayer.score += 100
        canvas.itemconfig(score, text=str(currentPlayer.score))

    def cheat_two(self, event):
        currentPlayer.lives += 1
        canvas.itemconfig(lives, text=str(currentPlayer.lives))

    # def cheat_three(self):

    def pause(self, event):
        if self.paused == 1:
            self.paused = 0
            canvas.unbind("p")
            canvas.delete(self.pauseText)
            self.pauseText = canvas.create_text(800, 500, text='3',
                                                fill="white",
                                                font=('Times New Roman', 30))
            time.sleep(1)
            canvas.update()
            canvas.delete(self.pauseText)
            self.pauseText = canvas.create_text(800, 500, text='2',
                                                fill="white",
                                                font=('Times New Roman', 20))
            time.sleep(1)
            canvas.update()
            canvas.delete(self.pauseText)
            self.pauseText = canvas.create_text(800, 500, text='1',
                                                fill="white",
                                                font=('Times New Roman', 30))
            time.sleep(1)
            canvas.update()
            canvas.delete(self.pauseText)
            self.pauseText = canvas.create_text(800, 500, text='GO!',
                                                fill="white",
                                                font=('Times New Roman', 50))
            time.sleep(0.5)
            canvas.update()
            canvas.delete(self.pauseText)
            canvas.delete(self.pauseRect)
            self.createBanana()
            self.bananaMove()
            self.createFireball()
            self.fireballMove()
            canvas.bind("<Up>", self.moveUp)
            canvas.bind("<Down>", self.moveDown)
            canvas.bind("<Left>", self.moveLeft)
            canvas.bind("<Right>", self.moveRight)
            canvas.bind("1", self.cheat_one)
            canvas.bind("2", self.cheat_two)
            canvas.bind("p", self.pause)
            canvas.bind("s", self.save)
            canvas.bind("b", self.bossKey)

        elif self.paused == 0:
            canvas.unbind("<Up>")
            canvas.unbind("<Down>")
            canvas.unbind("<Left>")
            canvas.unbind("<Right>")
            canvas.unbind("1")
            canvas.unbind("2")
            canvas.unbind("s")
            canvas.unbind("b")
            self.pauseRect = canvas.create_rectangle(400, 300, 1200, 700,
                                                     fill='green')
            self.pauseText = canvas.create_text(800, 500, text='PAUSED',
                                                font=('Times New Roman', 20))
            canvas.update()
            window.after_cancel(self.bananaMoveAfter)
            window.after_cancel(self.createBananaAfter)
            window.after_cancel(self.fireballMoveAfter)
            window.after_cancel(self.createFireballAfter)
            self.paused = 1

    def moveUp(self, event):
        currentPlayer.playerPosition = canvas.coords(self.playerSprite)
        if currentPlayer.playerPosition[1] <= ((canvasHeight * 4) / 7):
            canvas.coords(self.playerSprite, currentPlayer.playerPosition[0],
                          ((canvasHeight * 4) / 7))
        else:
            canvas.move(self.playerSprite, 0, -50)

    def moveDown(self, event):
        currentPlayer.playerPosition = canvas.coords(self.playerSprite)
        if currentPlayer.playerPosition[1] >= (canvasHeight - 80):
            canvas.coords(self.playerSprite, currentPlayer.playerPosition[0],
                          int(canvasHeight - 80))
        else:
            canvas.move(self.playerSprite, 0, 50)

    def moveLeft(self, event):
        currentPlayer.playerPosition = canvas.coords(self.playerSprite)
        if currentPlayer.playerPosition[0] <= int(canvasWidth / 4):
            canvas.coords(self.playerSprite, int(canvasWidth / 4),
                          currentPlayer.playerPosition[1])
        else:
            canvas.move(self.playerSprite, int(-canvasWidth / 4), 0)

    def moveRight(self, event):
        currentPlayer.playerPosition = canvas.coords(self.playerSprite)
        if currentPlayer.playerPosition[0] >= int((3 * canvasWidth) / 4):
            canvas.coords(self.playerSprite, int((3 * canvasWidth) / 4),
                          currentPlayer.playerPosition[1])
        else:
            canvas.move(self.playerSprite, int(canvasWidth / 4), 0)

    def bossKey(self, event):
        if self.bossActive == 1:
            self.canvas3.unbind("b")
            self.bossWindow.destroy()
            self.bananaMove()
            self.fireballMove()
            self.createFireball()
            self.createBanana()
            canvas.bind("<Up>", self.moveUp)
            canvas.bind("<Down>", self.moveDown)
            canvas.bind("<Left>", self.moveLeft)
            canvas.bind("<Right>", self.moveRight)
            canvas.bind("1", self.cheat_one)
            canvas.bind("2", self.cheat_two)
            canvas.bind("p", self.pause)
            canvas.bind("b", self.bossKey)
            canvas.bind("s", self.save)

            self.bossActive = 0
        elif self.bossActive == 0:
            window.after_cancel(self.bananaMoveAfter)
            window.after_cancel(self.createBananaAfter)
            window.after_cancel(self.fireballMoveAfter)
            window.after_cancel(self.createFireballAfter)
            canvas.unbind("<Up>")
            canvas.unbind("<Down>")
            canvas.unbind("<Left>")
            canvas.unbind("<Right>")
            canvas.unbind("1")
            canvas.unbind("2")
            canvas.unbind("p")
            canvas.unbind("b")
            canvas.unbind("s")
            self.bossWindow = Toplevel(self.master)
            self.bossWindow.geometry("1600x1002")
            self.canvas3 = Canvas(self.bossWindow, width=1600, height=1002)
            self.canvas3.pack(expand=True, fill=BOTH)
            self.bossWindow.resizable(False, False)
            bgImage = self.canvas3.create_image(0, 0, anchor="nw",
                                                image=self.bossKeyImage)
            self.canvas3.bind("b", self.bossKey)
            self.canvas3.focus_set()
            self.bossActive = 1

    def bananaMove(self):
        canvasHeight = int(canvas.cget("height"))
        self.remove_list = []
        for enum, banana in enumerate(self.bananas):
            if canvas.coords(banana.banana)[1] > canvasHeight:
                self.remove_list.append(enum)
                canvas.delete(banana.banana)
            else:
                banana.move_banana(canvas)
        for index in self.remove_list:
            self.bananas.pop(index)

        self.bananaMoveAfter = window.after(50,
                                            self.bananaMove)

    def createBanana(self):
        global positionChoice
        bananaPosXList = [400, 800, 1200]
        positionChoice = random.choice(bananaPosXList)
        self.bananas.append(Banana(canvas, positionChoice))
        self.createBananaAfter = window.after(500, self.createBanana)

    def collisionDetection(self):
        monkey_bbox = canvas.bbox(self.playerSprite)
        for enum, banana in enumerate(self.bananas):
            banana_bbox_c = banana.banana_bbox
            if (banana_bbox_c[0] in range(monkey_bbox[0], monkey_bbox[2]) or (
                    banana_bbox_c[2] in range(monkey_bbox[0],
                                              monkey_bbox[2]))) and ((
                                                             banana_bbox_c[
                                                                 1] in range(
                                                                monkey_bbox[
                                                                 1],
                                                                monkey_bbox[
                                                                 3])) or (
                                                               banana_bbox_c[
                                                                 3] in range(
                                                                monkey_bbox[
                                                                 1],
                                                                monkey_bbox[
                                                                 3]))):
                canvas.delete(banana.banana)
                currentPlayer.score += 50
                canvas.itemconfig(score, text=str(currentPlayer.score))
                self.bananas.pop(enum)
        canvas.update()
        window.after(100, self.collisionDetection)

    def fbCollisionDetection(self):
        monkey_bbox = canvas.bbox(self.playerSprite)
        for enum, fireball in enumerate(self.fireballs):
            fireball_bbox_c = fireball.fireball_bbox
            if (fireball_bbox_c[0] in range(monkey_bbox[0],
                                            monkey_bbox[2]) or (
                        fireball_bbox_c[2] in range(monkey_bbox[0],
                                                    monkey_bbox[2]))) and (
                    (fireball_bbox_c[1] in range(monkey_bbox[1],
                                                 monkey_bbox[3])) or (
                            fireball_bbox_c[3] in range(monkey_bbox[1],
                                                        monkey_bbox[3]))):
                canvas.delete(fireball.fireball)
                currentPlayer.lives -= 1
                self.save()
                if currentPlayer.lives == 0:
                    self.gameOver()
                canvas.itemconfig(lives, text=str(currentPlayer.lives))

                self.fireballs.pop(enum)
        canvas.update()
        window.after(100, self.fbCollisionDetection)

    def fireballMove(self):
        canvasHeight = int(canvas.cget("height"))
        remove_list = []
        for enum, fireball in enumerate(self.fireballs):
            if canvas.coords(fireball.fireball)[1] > canvasHeight:
                remove_list.append(enum)
                canvas.delete(fireball.fireball)
            else:
                fireball.move_fireball(canvas)
        for index in remove_list:
            self.fireballs.pop(index)
        if currentPlayer.score < 1000:
            speed = 40
        elif currentPlayer.score < 2000:
            speed = 20
        else:
            speed = 10
        self.fireballMoveAfter = window.after(speed,
                                              self.fireballMove)
        if self.create_fball:
            self.create_fball = not self.create_fball
            self.createFireballAfter = window.after(4000, self.createFireball)

    def createFireball(self):
        global fPositionChoice
        print(len(self.fireballs), 'before')
        if len(self.fireballs) <= 1:
            self.create_fball = not self.create_fball
            fireballPoxXList = [400, 800, 1200]
            fPositionChoice = random.choice(fireballPoxXList)
            print(len(self.fireballs), 'after')
            self.fireballs.append(Fireball(canvas, fPositionChoice))

    def save(self, event=None):
        playerFile = open("playerFile.txt", "w+")
        playerFile.write(currentPlayer.playerName + "\n" + str(
            currentPlayer.score) + "\n" + str(currentPlayer.lives))
        leaderboardFile = open("leaderboardFile.txt", "a+")
        leaderboardFile.write(
            currentPlayer.playerName + "\n" + str(currentPlayer.score) + "\n")

    def load(self):
        global currentPlayer
        playerFile = open("playerFile.txt", "r")
        f1 = playerFile.readlines()
        f1 = [item.rstrip("\n") for item in f1]
        loadName = f1[0]
        loadScore = int(f1[1])
        loadLives = int(f1[2])
        currentPlayer = Monkey(loadName)
        currentPlayer.score = int(loadScore)
        currentPlayer.lives = int(loadLives)
        self.startGame()


class Monkey:
    def __init__(self, name):
        self.playerName = name
        self.playerPosition = 0, 0
        self.score = 0
        self.lives = 3


class Banana:
    def __init__(self, canvas, bananaPosX):
        imageList = ["banana.png", "apple.png", "grape.png"]
        randomImage = random.choice(imageList)
        self.bananaSpriteImage = PhotoImage(file=randomImage)
        self.banana = canvas.create_image(bananaPosX, -50,
                                          image=self.bananaSpriteImage)
        self.pointWorth = 50
        self.banana_bbox = canvas.bbox(self.banana)

    def move_banana(self, canvas):
        canvas.move(self.banana, 0, 20)
        self.banana_bbox = canvas.bbox(self.banana)


class Fireball:
    def __init__(self, canvas, fireballPosX):
        self.fireballSpriteImage = PhotoImage(file="fireball.png")
        self.fireball = canvas.create_image(fireballPosX, -50,
                                            image=self.fireballSpriteImage)
        self.fireball_bbox = canvas.bbox(self.fireball)

    def move_fireball(self, canvas):
        canvas.move(self.fireball, 0, 20)
        self.fireball_bbox = canvas.bbox(self.fireball)


class Score:
    def __init__(self, canvas, color):
        self.score = 0
        self.canvas = canvas
        self.id = canvas.create_text(250, 10, text='Score:' + str(self.score),
                                     fill=color, font=('Helvetica', 20))

    def increase(self):
        self.score += 50

        self.canvas.itemconfig(self.id, text='Score:' + str(self.score))


while True:
    window = Tk()
    app = Mono(window)
    window.mainloop()
