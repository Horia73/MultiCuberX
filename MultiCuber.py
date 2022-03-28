from tkinter import *
from tkmacosx import Button
import math
import sys


class Window(object):

    def __init__(self, master):

        self.master = master

        self.master.title("RUBIKon Project")

        self.master.geometry("1200x900+250+80")

        self.master.config(bg="#fff")

        self.master.resizable(0, 0)

        self.AddCubes()

    def AddCubes(self):
        self.TopFrame = Frame(self.master, bg="#42f498", width=1200, height=100)
        self.TopFrame.grid(column=0, row=1)

        self.TextLabel = Label(self.master, text="Please select a cube:", font=("Laksaman",25), fg="#333", bg="#fff")
        self.TextLabel.grid(column=0, row=2, padx=10, pady=10)

        self.x3 = Button(self.master, text="3x3x3",font=("Laksaman",20), width=400, height=80, bd=0, bg="#42f498", fg="#333",
                         command=self.cub3)
        self.x3.grid(column=0, row=3, padx=10, pady=10)

        self.x4 = Button(self.master, text="4x4x4",font=("Laksaman",20), width=400, height=80, bd=0, bg="#FFD700", fg="#333",
                         command=self.cub4)
        self.x4.grid(column=0, row=4, padx=10, pady=10)

        self.x5 = Button(self.master, text="5x5x5",font=("Laksaman",20), width=400, height=80, bd=0, bg="#FF7F50", fg="#333",
                         command=self.cub5)
        self.x5.grid(column=0, row=5, padx=10, pady=10)

        self.close = Button(self.master, text="Exit",font=("Laksaman",20), width=400, height=80, bd=0, bg="#4d79ff", fg="#333",
                            command=self.closeall)
        self.close.grid(column=0, row=10, padx=10, pady=10)

    def closeall(self):
        sys.exit()

    def clos3(self):
        cube3.close()
        sys.exit()

    def clos4(self):
        cube4.close()
        sys.exit()

    def clos5(self):
        cube5.close()
        sys.exit()

    def cub3(self):
        import cube3
        global cube3
        cube3.prepare()
        self.TextLabel = Label(self.master, text="Please select the speed of motors:", font=("Laksaman",25), fg="#333",
                               bg="#fff")
        self.TextLabel.grid(column=0, row=2, padx=10, pady=10)

        self.TopFrame = Frame(self.master, bg="#42f498", width=1200, height=100)
        self.TopFrame.grid(column=0, row=1)

        self.Slow = Button(self.master, text="Slow mode",font=("Laksaman",20), width=400, height=80, bd=0, bg="#42f498", fg="#333",
                           command=self.small3)
        self.Slow.grid(column=0, row=3, padx=10, pady=10)

        self.Medium = Button(self.master, text="Medium mode",font=("Laksaman",20), width=400, height=80, bd=0, bg="#FFD700", fg="#333",
                             command=self.mid3)
        self.Medium.grid(column=0, row=4, padx=10, pady=10)

        self.Fast = Button(self.master, text="Fast mode",font=("Laksaman",20), width=400, height=80, bd=0, bg="#FF7F50", fg="#333",
                           command=self.big3)
        self.Fast.grid(column=0, row=5, padx=10, pady=10)

        self.close3 = Button(self.master, text="Exit",font=("Laksaman",20), width=400, height=80, bd=0, bg="#4d79ff", fg="#333",
                             command=self.clos3)
        self.close3.grid(column=0, row=10, padx=10, pady=10)

        self.close.destroy()

    def cub4(self):
        import cube4
        global cube4
        cube4.prepare()
        self.TextLabel = Label(self.master, text="Please select the speed of motors:", font=("Laksaman",20), fg="#333",
                               bg="#fff")
        self.TextLabel.grid(column=0, row=2, padx=10, pady=10)

        self.TopFrame = Frame(self.master, bg="#42f498", width=1200, height=100)
        self.TopFrame.grid(column=0, row=1)

        self.Slow = Button(self.master, text="Slow mode",font=("Laksaman",20), width=400, height=80, bd=0, bg="#42f498", fg="#333",
                           command=self.small4)
        self.Slow.grid(column=0, row=3, padx=10, pady=10)

        self.Medium = Button(self.master, text="Medium mode",font=("Laksaman",20), width=400, height=80, bd=0, bg="#FFD700", fg="#333",
                             command=self.mid4)
        self.Medium.grid(column=0, row=4, padx=10, pady=10)

        self.Fast = Button(self.master, text="Fast mode",font=("Laksaman",20), width=400, height=80, bd=0, bg="#FF7F50", fg="#333",
                           command=self.big4)
        self.Fast.grid(column=0, row=5, padx=10, pady=10)

        self.close4 = Button(self.master, text="Exit",font=("Laksaman",20), width=400, height=80, bd=0, bg="#4d79ff", fg="#333",
                             command=self.clos4)
        self.close4.grid(column=0, row=10, padx=10, pady=10)

        self.close.destroy()

    def cub5(self):
        import cube5
        global cube5
        cube5.prepare()
        self.TextLabel = Label(self.master, text="Please select the speed of motors:", font=("Laksaman",20), fg="#333",
                               bg="#fff")
        self.TextLabel.grid(column=0, row=2, padx=10, pady=10)

        self.TopFrame = Frame(self.master, bg="#42f498", width=1200, height=100)
        self.TopFrame.grid(column=0, row=1)

        self.Slow = Button(self.master, text="Slow mode",font=("Laksaman",20), width=400, height=80, bd=0, bg="#42f498", fg="#333",
                           command=self.small5)
        self.Slow.grid(column=0, row=3, padx=10, pady=10)

        self.Medium = Button(self.master, text="Medium mode",font=("Laksaman",20), width=400, height=80, bd=0, bg="#FFD700", fg="#333",
                             command=self.mid5)
        self.Medium.grid(column=0, row=4, padx=10, pady=10)

        self.Fast = Button(self.master, text="Fast mode",font=("Laksaman",20), width=400, height=80, bd=0, bg="#FF7F50", fg="#333",
                           command=self.big5)
        self.Fast.grid(column=0, row=5, padx=10, pady=10)

        self.close5 = Button(self.master, text="Exit",font=("Laksaman",20), width=400, height=80, bd=0, bg="#4d79ff", fg="#333",
                             command=self.clos5)
        self.close5.grid(column=0, row=10, padx=10, pady=10)

        self.close.destroy()

    def first3(self):

        cube3.scanner()
        cube3.analyzer()
        a = cube3.solver()
        if a > 60:
            m = a / 60
            m = math.floor(m)
            s = a - m * 60

        else:
            m = 0
            s = a

        if m == 1:
            minutes = ' minute and '
        else:
            minutes = ' minutes and '

        self.TextLabel.config(
            text="C U B E  S O L V E D ! Total time: " + str(round(m)) + str(minutes) + str(round(s, 2)) + ' seconds.')

    def first4(self):

        cube4.scanner()
        cube4.analyzer()
        a = cube4.solver()
        if a > 60:
            m = a / 60
            m = math.floor(m)
            s = a - m * 60

        else:
            m = 0
            s = a

        if m == 1:
            minutes = ' minute and '
        else:
            minutes = ' minutes and '

        self.TextLabel.config(
            text="C U B E  S O L V E D ! Total time: " + str(round(m)) + str(minutes) + str(round(s, 2)) + ' seconds.')

    def first5(self):
        cube5.scanner()
        cube5.analyzer()
        a = cube5.solver()
        if a > 60:
            m = a / 60
            m = math.floor(m)
            s = a - m * 60

        else:
            m = 0
            s = a

        if m == 1:
            minutes = ' minute and '
        else:
            minutes = ' minutes and '

        self.TextLabel.config(
            text="C U B E  S O L V E D ! Total time: " + str(round(m)) + str(minutes) + str(round(s, 2)) + ' seconds.')

    def custom3(self):

        self.TextLabel.config(text="Please select a pattern below:")

        self.TopFrame = Frame(self.master, bg="#EE82EE", width=1200, height=100)
        self.TopFrame.grid(column=0, row=1)

        self.p2 = Button(self.master, text="Checkboard",font=("Laksaman",20), width=400, height=80, bd=0, bg="#EE82EE", fg="#333",
                         command=self.check3)
        self.p2.grid(column=0, row=3, padx=10, pady=10)

        self.p4 = Button(self.master, text="Six Spots",font=("Laksaman",20), width=400, height=80, bd=0, bg="#FF7F50", fg="#333",
                         command=self.spots3)
        self.p4.grid(column=0, row=4, padx=10, pady=10)

        self.p3 = Button(self.master, text="Union Jack",font=("Laksaman",20), width=400, height=80, bd=0, bg="#FFD700", fg="#333",
                         command=self.union3)
        self.p3.grid(column=0, row=5, padx=10, pady=10)

        self.Back = Button(self.master, text="Back",font=("Laksaman",20), width=400, height=80, bd=0, bg="#40E0D0", fg="#333",
                           command=self.back3)
        self.Back.grid(column=0, row=9, padx=10, pady=10)

        self.p1 = Button(self.master, text="Six Crosses",font=("Laksaman",20), width=400, height=80, bd=0, bg="#42f498", fg="#333",
                         command=self.crosses3)
        self.p1.grid(column=0, row=6, padx=10, pady=10)

        self.pattern.destroy()
        self.solve.destroy()

    def custom4(self):

        self.TextLabel.config(text="Please select a pattern below:")

        self.TopFrame = Frame(self.master, bg="#EE82EE", width=1200, height=100)
        self.TopFrame.grid(column=0, row=1)

        self.p2 = Button(self.master, text="Cube in cube",font=("Laksaman",20), width=400, height=80, bd=0, bg="#EE82EE", fg="#333",
                         command=self.check4)
        self.p2.grid(column=0, row=3, padx=10, pady=10)

        self.p4 = Button(self.master, text="Six Spots",font=("Laksaman",20), width=400, height=80, bd=0, bg="#FF7F50", fg="#333",
                         command=self.spots4)
        self.p4.grid(column=0, row=4, padx=10, pady=10)

        self.p3 = Button(self.master, text="Union Jack",font=("Laksaman",20), width=400, height=80, bd=0, bg="#FFD700", fg="#333",
                         command=self.union4)
        self.p3.grid(column=0, row=5, padx=10, pady=10)

        self.Back = Button(self.master, text="Back",font=("Laksaman",20), width=400, height=80, bd=0, bg="#40E0D0", fg="#333",
                           command=self.back4)
        self.Back.grid(column=0, row=9, padx=10, pady=10)

        self.p1 = Button(self.master, text="Six Crosses",font=("Laksaman",20), width=400, height=80, bd=0, bg="#42f498", fg="#333",
                         command=self.crosses4)
        self.p1.grid(column=0, row=6, padx=10, pady=10)

        self.pattern.destroy()
        self.solve.destroy()

    def custom5(self):

        self.TextLabel.config(text="Please select a pattern below:")

        self.TopFrame = Frame(self.master, bg="#EE82EE", width=1200, height=100)
        self.TopFrame.grid(column=0, row=1)

        self.TopFrame2 = Frame(self.master, bg="#EE82EE", width=600, height=60)
        self.TopFrame2.grid(column=0, row=1)

        self.p2 = Button(self.master, text="Checkboard",font=("Laksaman",20), width=400, height=80, bd=0, bg="#EE82EE", fg="#333",
                         command=self.check5)
        self.p2.grid(column=0, row=3, padx=10, pady=10)

        self.p4 = Button(self.master, text="Six Spots",font=("Laksaman",20), width=400, height=80, bd=0, bg="#FF7F50", fg="#333",
                         command=self.spots5)
        self.p4.grid(column=0, row=4, padx=10, pady=10)

        self.p3 = Button(self.master, text="Union Jack",font=("Laksaman",20), width=400, height=80, bd=0, bg="#FFD700", fg="#333",
                         command=self.union5)
        self.p3.grid(column=0, row=5, padx=10, pady=10)

        self.Back = Button(self.master, text="Back",font=("Laksaman",20), width=400, height=80, bd=0, bg="#40E0D0", fg="#333",
                           command=self.back5)
        self.Back.grid(column=0, row=9, padx=10, pady=10)

        self.p1 = Button(self.master, text="Six Crosses",font=("Laksaman",20), width=400, height=80, bd=0, bg="#42f498", fg="#333",
                         command=self.crosses5)
        self.p1.grid(column=0, row=6, padx=10, pady=10)

        self.pattern.destroy()
        self.solve.destroy()

    def crosses3(self):

        cube3.pattern4()
        self.TextLabel.config(text="C U B E  S O L V E D !")

    def check3(self):

        cube3.pattern1()
        self.TextLabel.config(text="C U B E  S O L V E D !")

    def spots3(self):

        cube3.pattern2()
        self.TextLabel.config(text="C U B E  S O L V E D !")

    def union3(self):

        cube3.pattern3()
        self.TextLabel.config(text="C U B E  S O L V E D !")

    def crosses4(self):

        cube4.pattern4()
        self.TextLabel.config(text="C U B E  S O L V E D !")

    def check4(self):

        cube4.pattern1()
        self.TextLabel.config(text="C U B E  S O L V E D !")

    def spots4(self):

        cube4.pattern2()
        self.TextLabel.config(text="C U B E  S O L V E D !")

    def union4(self):

        cube4.pattern3()
        self.TextLabel.config(text="C U B E  S O L V E D !")

    def crosses5(self):

        cube5.pattern4()
        self.TextLabel.config(text="C U B E  S O L V E D !")

    def check5(self):

        cube5.pattern1()
        self.TextLabel.config(text="C U B E  S O L V E D !")

    def spots5(self):

        cube5.pattern2()
        self.TextLabel.config(text="C U B E  S O L V E D !")

    def union5(self):

        cube5.pattern3()
        self.TextLabel.config(text="C U B E  S O L V E D !")

    def back3(self):

        self.TextLabel.config(text="Please select the speed of motors:")

        self.TopFrame = Frame(self.master, bg="#42f498", width=1200, height=100)
        self.TopFrame.grid(column=0, row=1)

        self.Slow = Button(self.master, text="Slow mode",font=("Laksaman",20), width=400, height=80, bd=0, bg="#42f498", fg="#333",
                           command=self.small3)
        self.Slow.grid(column=0, row=3, padx=10, pady=10)

        self.Medium = Button(self.master, text="Medium mode",font=("Laksaman",20), width=400, height=80, bd=0, bg="#FFD700", fg="#333",
                             command=self.mid3)
        self.Medium.grid(column=0, row=4, padx=10, pady=10)

        self.Fast = Button(self.master, text="Fast mode",font=("Laksaman",20), width=400, height=80, bd=0, bg="#FF7F50", fg="#333",
                           command=self.big3)
        self.Fast.grid(column=0, row=5, padx=10, pady=10)

        self.solve = Button(self.master, text="Solve",font=("Laksaman",20), width=400, height=80, bd=0, bg="#EE82EE", fg="#333",
                            command=self.first3)
        self.solve.grid(column=0, row=7, padx=10, pady=10)

        self.bck2 = Button(self.master, text="Back",font=("Laksaman",20), width=400, height=80, bd=0, bg="#40E0D0", fg="#333",
                           command=self.back23)
        self.bck2.grid(column=0, row=9, padx=10, pady=10)

        self.pattern = Button(self.master, text="Custom pattern",font=("Laksaman",20), width=400, height=80, bd=0, bg="#66b3ff", fg="#333",
                              command=self.custom3)
        self.pattern.grid(column=0, row=8, padx=10, pady=10)

        self.p1.destroy()
        self.p2.destroy()
        self.p3.destroy()
        self.p4.destroy()
        self.Back.destroy()

    def back4(self):

        self.TextLabel.config(text="Please select the speed of motors:")

        self.TopFrame = Frame(self.master, bg="#42f498", width=400, height=60)
        self.TopFrame.grid(column=1, row=1)

        self.TopFrame2 = Frame(self.master, bg="#42f498", width=600, height=60)
        self.TopFrame2.grid(column=0, row=1)

        self.Slow = Button(self.master, text="Slow mode",font=("Laksaman",20), width=400, height=80, bd=0, bg="#42f498", fg="#333",
                           command=self.small4)
        self.Slow.grid(column=0, row=3, padx=10, pady=10)

        self.Medium = Button(self.master, text="Medium mode",font=("Laksaman",20), width=400, height=80, bd=0, bg="#FFD700", fg="#333",
                             command=self.mid4)
        self.Medium.grid(column=0, row=4, padx=10, pady=10)

        self.Fast = Button(self.master, text="Fast mode",font=("Laksaman",20), width=400, height=80, bd=0, bg="#FF7F50", fg="#333",
                           command=self.big4)
        self.Fast.grid(column=0, row=5, padx=10, pady=10)

        self.solve = Button(self.master, text="Solve",font=("Laksaman",20), width=400, height=80, bd=0, bg="#EE82EE", fg="#333",
                            command=self.first4)
        self.solve.grid(column=0, row=7, padx=10, pady=10)

        self.bck2 = Button(self.master, text="Back",font=("Laksaman",20), width=400, height=80, bd=0, bg="#40E0D0", fg="#333",
                           command=self.back24)
        self.bck2.grid(column=0, row=9, padx=10, pady=10)

        self.pattern = Button(self.master, text="Custom pattern",font=("Laksaman",20), width=400, height=80, bd=0, bg="#66b3ff", fg="#333",
                              command=self.custom4)
        self.pattern.grid(column=0, row=8, padx=10, pady=10)

        self.p1.destroy()
        self.p2.destroy()
        self.p3.destroy()
        self.p4.destroy()
        self.Back.destroy()

    def back5(self):

        self.TextLabel.config(text="Please select the speed of motors:")

        self.TopFrame = Frame(self.master, bg="#42f498", width=400, height=60)
        self.TopFrame.grid(column=1, row=1)

        self.TopFrame2 = Frame(self.master, bg="#42f498", width=600, height=60)
        self.TopFrame2.grid(column=0, row=1)

        self.Medium = Button(self.master, text="Medium mode",font=("Laksaman",20), width=400, height=80, bd=0, bg="#FFD700", fg="#333",
                             command=self.mid5)
        self.Medium.grid(column=0, row=4, padx=10, pady=10)

        self.Fast = Button(self.master, text="Fast mode",font=("Laksaman",20), width=400, height=80, bd=0, bg="#FF7F50", fg="#333",
                           command=self.big5)
        self.Fast.grid(column=0, row=5, padx=10, pady=10)

        self.solve = Button(self.master, text="Solve",font=("Laksaman",20), width=400, height=80, bd=0, bg="#EE82EE", fg="#333",
                            command=self.first5)
        self.solve.grid(column=0, row=7, padx=10, pady=10)

        self.bck2 = Button(self.master, text="Back",font=("Laksaman",20), width=400, height=80, bd=0, bg="#40E0D0", fg="#333",
                           command=self.back25)
        self.bck2.grid(column=0, row=9, padx=10, pady=10)

        self.pattern = Button(self.master, text="Custom pattern",font=("Laksaman",20), width=400, height=80, bd=0, bg="#66b3ff", fg="#333",
                              command=self.custom5)
        self.pattern.grid(column=0, row=8, padx=10, pady=10)

        self.p1.destroy()
        self.p2.destroy()
        self.p3.destroy()
        self.p4.destroy()
        self.Back.destroy()

    def back23(self):

        self.TopFrame = Frame(self.master, bg="#42f498", width=1200, height=100)
        self.TopFrame.grid(column=0, row=1)

        self.TextLabel.config(text="Please select a cube:")

        self.x3 = Button(self.master, text="3x3x3",font=("Laksaman",20), width=400, height=80, bd=0, bg="#42f498", fg="#333",
                         command=self.cub3)
        self.x3.grid(column=0, row=3, padx=10, pady=10)

        self.x4 = Button(self.master, text="4x4x4",font=("Laksaman",20), width=400, height=80, bd=0, bg="#FFD700", fg="#333",
                         command=self.cub4)
        self.x4.grid(column=0, row=4, padx=10, pady=10)

        self.x5 = Button(self.master, text="5x5x5",font=("Laksaman",20), width=400, height=80, bd=0, bg="#FF7F50", fg="#333",
                         command=self.cub5)
        self.x5.grid(column=0, row=5, padx=10, pady=10)

        self.close = Button(self.master, text="Exit",font=("Laksaman",20), width=400, height=80, bd=0, bg="#FF7F50", fg="#333",
                            command=self.closeall)
        self.close.grid(column=0, row=10, padx=10, pady=10)

        cube3.close()
        self.close3.destroy()
        self.bck.destroy()
        try:
            self.bck2.destroy()
            self.pattern.destroy()
        except (NameError, AttributeError):
            pass
        self.solve.destroy()

    def back24(self):

        self.TopFrame = Frame(self.master, bg="#42f498", width=1200, height=100)
        self.TopFrame.grid(column=0, row=1)

        self.TextLabel.config(text="Please select a cube:")

        self.x3 = Button(self.master, text="3x3x3",font=("Laksaman",20), width=400, height=80, bd=0, bg="#42f498", fg="#333",
                         command=self.cub3)
        self.x3.grid(column=0, row=3, padx=10, pady=10)

        self.x4 = Button(self.master, text="4x4x4",font=("Laksaman",20), width=400, height=80, bd=0, bg="#FFD700", fg="#333",
                         command=self.cub4)
        self.x4.grid(column=0, row=4, padx=10, pady=10)

        self.x5 = Button(self.master, text="5x5x5",font=("Laksaman",20), width=400, height=80, bd=0, bg="#FF7F50", fg="#333",
                         command=self.cub5)
        self.x5.grid(column=0, row=5, padx=10, pady=10)

        self.close = Button(self.master, text="Exit",font=("Laksaman",20), width=400, height=80, bd=0, bg="#FF7F50", fg="#333",
                            command=self.closeall)
        self.close.grid(column=0, row=10, padx=10, pady=10)

        cube4.close()
        self.close4.destroy()
        self.bck.destroy()
        try:
            self.bck2.destroy()
            self.pattern.destroy()
        except (NameError, AttributeError):
            pass
        self.solve.destroy()

    def back25(self):

        self.TopFrame = Frame(self.master, bg="#42f498", width=1200, height=100)
        self.TopFrame.grid(column=0, row=1)

        self.TextLabel.config(text="Please select a cube:")

        self.x3 = Button(self.master, text="3x3x3",font=("Laksaman",20), width=400, height=80, bd=0, bg="#42f498", fg="#333",
                         command=self.cub3)
        self.x3.grid(column=0, row=3, padx=10, pady=10)

        self.x4 = Button(self.master, text="4x4x4",font=("Laksaman",20), width=400, height=80, bd=0, bg="#FFD700", fg="#333",
                         command=self.cub4)
        self.x4.grid(column=0, row=4, padx=10, pady=10)

        self.x5 = Button(self.master, text="5x5x5",font=("Laksaman",20), width=400, height=80, bd=0, bg="#FF7F50", fg="#333",
                         command=self.cub5)
        self.x5.grid(column=0, row=5, padx=10, pady=10)

        self.close = Button(self.master, text="Exit",font=("Laksaman",20), width=400, height=80, bd=0, bg="#FF7F50", fg="#333",
                            command=self.closeall)
        self.close.grid(column=0, row=10, padx=10, pady=10)

        cube5.close()
        self.close5.destroy()
        self.bck.destroy()
        try:
            self.bck2.destroy()
            self.pattern.destroy()
        except (NameError, AttributeError):
            pass
        self.solve.destroy()

    def small3(self):

        cube3.slow()
        self.TextLabel.config(text="Slow mode selected!")

        self.solve = Button(self.master, text="Solve",font=("Laksaman",20), width=400, height=80, bd=0, bg="#EE82EE", fg="#333",
                            command=self.first3)
        self.solve.grid(column=0, row=7, padx=10, pady=10)

        self.bck = Button(self.master, text="Back",font=("Laksaman",20), width=400, height=80, bd=0, bg="#40E0D0", fg="#333",
                          command=self.back23)
        self.bck.grid(column=0, row=9, padx=10, pady=10)


    def mid3(self):

        cube3.normal()
        self.TextLabel.config(text="Medium mode selected!")

        self.solve = Button(self.master, text="Solve",font=("Laksaman",20), width=400, height=80, bd=0, bg="#EE82EE", fg="#333",
                            command=self.first3)
        self.solve.grid(column=0, row=7, padx=10, pady=10)

        self.bck = Button(self.master, text="Back",font=("Laksaman",20), width=400, height=80, bd=0, bg="#40E0D0", fg="#333",
                          command=self.back23)
        self.bck.grid(column=0, row=9, padx=10, pady=10)


    def big3(self):

        cube3.fast()
        self.TextLabel.config(text="Fast mode selected! Note that this may cause the cube to fall or stuck.")

        self.solve = Button(self.master, text="Solve",font=("Laksaman",20), width=400, height=80, bd=0, bg="#EE82EE", fg="#333",
                            command=self.first3)
        self.solve.grid(column=0, row=7, padx=10, pady=10)

        self.bck = Button(self.master, text="Back",font=("Laksaman",20), width=400, height=80, bd=0, bg="#40E0D0", fg="#333",
                          command=self.back23)
        self.bck.grid(column=0, row=9, padx=10, pady=10)


    def small4(self):

        cube4.slow()
        self.TextLabel.config(text="Slow mode selected!")

        self.solve = Button(self.master, text="Solve",font=("Laksaman",20), width=400, height=80, bd=0, bg="#EE82EE", fg="#333",
                            command=self.first4)
        self.solve.grid(column=0, row=7, padx=10, pady=10)

        self.bck = Button(self.master, text="Back",font=("Laksaman",20), width=400, height=80, bd=0, bg="#40E0D0", fg="#333",
                          command=self.back24)
        self.bck.grid(column=0, row=9, padx=10, pady=10)


    def mid4(self):

        cube4.normal()
        self.TextLabel.config(text="Medium mode selected!")

        self.solve = Button(self.master, text="Solve",font=("Laksaman",20), width=400, height=80, bd=0, bg="#EE82EE", fg="#333",
                            command=self.first4)
        self.solve.grid(column=0, row=7, padx=10, pady=10)

        self.bck = Button(self.master, text="Back",font=("Laksaman",20), width=400, height=80, bd=0, bg="#40E0D0", fg="#333",
                          command=self.back24)
        self.bck.grid(column=0, row=9, padx=10, pady=10)


    def big4(self):

        cube4.fast()
        self.TextLabel.config(text="Fast mode selected! Note that this may cause the cube to fall or stuck.")

        self.solve = Button(self.master, text="Solve",font=("Laksaman",20), width=400, height=80, bd=0, bg="#EE82EE", fg="#333",
                            command=self.first4)
        self.solve.grid(column=0, row=7, padx=10, pady=10)

        self.bck = Button(self.master, text="Back",font=("Laksaman",20), width=400, height=80, bd=0, bg="#40E0D0", fg="#333",
                          command=self.back24)
        self.bck.grid(column=0, row=9, padx=10, pady=10)


    def small5(self):

        cube5.slow()
        self.TextLabel.config(text="Slow mode selected!")

        self.solve = Button(self.master, text="Solve",font=("Laksaman",20), width=400, height=80, bd=0, bg="#EE82EE", fg="#333",
                            command=self.first5)
        self.solve.grid(column=0, row=7, padx=10, pady=10)

        self.bck = Button(self.master, text="Back",font=("Laksaman",20), width=400, height=80, bd=0, bg="#40E0D0", fg="#333",
                          command=self.back25)
        self.bck.grid(column=0, row=9, padx=10, pady=10)


    def mid5(self):

        cube5.normal()
        self.TextLabel.config(text="Medium mode selected!")

        self.solve = Button(self.master, text="Solve",font=("Laksaman",20), width=400, height=80, bd=0, bg="#EE82EE", fg="#333",
                            command=self.first5)
        self.solve.grid(column=0, row=7, padx=10, pady=10)

        self.bck = Button(self.master, text="Back",font=("Laksaman",20), width=400, height=80, bd=0, bg="#40E0D0", fg="#333",
                          command=self.back25)
        self.bck.grid(column=0, row=9, padx=10, pady=10)


    def big5(self):

        cube5.fast()
        self.TextLabel.config(text="Fast mode selected! Note that this may cause the cube to fall or stuck.")

        self.solve = Button(self.master, text="Solve",font=("Laksaman",20), width=400, height=80, bd=0, bg="#EE82EE", fg="#333",
                            command=self.first5)
        self.solve.grid(column=0, row=7, padx=10, pady=10)

        self.bck = Button(self.master, text="Back",font=("Laksaman",20), width=400, height=80, bd=0, bg="#40E0D0", fg="#333",
                          command=self.back25)
        self.bck.grid(column=0, row=9, padx=10, pady=10)



app = Tk()

Window = Window(app)

app.mainloop()
