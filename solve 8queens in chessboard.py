from tkinter import *

solutions = []
solutionTest = [0,0,0,0,0,0,0,0]

def isPossible(testRow, testCol):
    if testRow == 0:
        return True
    for row in range(0, testRow):
        #عمود
        if testCol == solutionTest[row]:
            return False
        # قطر
        if abs(testRow - row) == abs(testCol - solutionTest[row]):
            return False
    return True

def queen(row):
    global solutions,solutionTest
    for col in range(8):
        if isPossible(row, col)==False:
            continue
        else:
            solutionTest[row] = col
            if row == 7:
                solutions.append(solutionTest.copy())
            else:
                queen(row + 1)

queen(0)

gamePage = Tk()
gamePage.geometry("620x640")
canvas = Canvas(gamePage,bg="skyblue")
canvas.pack(fill="both",expand=True)
img_back = PhotoImage(file="images.png")
img_queen = PhotoImage(file="queen.png")

count= 0

def print_queen(array):
    for i in range(0,8):
        canvas.create_image(30+70*i,30+70*array[i],image=img_queen,anchor=NW)

def startBtn():
    canvas.create_image(30,30,image=img_back,anchor=NW)
    btn_start.destroy()
    btn_rest.place(x=300,y=600)
    btn_next.place(x=500,y=600)
    btn_pre.place(x=100,y=600)

def preBtn():
    global count
    if count>1:
        count-=1
        delete_queen()
        print_queen(solutions[count-1])

def resetBtn():
    global count
    count=0
    delete_queen()

def nextBtn():
    global count
    global solutions
    if count<92:
        count+=1
        delete_queen()
        print_queen(solutions[count-1])

def delete_queen():
    canvas.delete('all')
    canvas.create_image(30,30,image=img_back,anchor=NW)


btn_start = Button(gamePage,text="Start",command=lambda:startBtn())
btn_start.place(x=300,y=600)
btn_next = Button(gamePage,text="Next",command =lambda:nextBtn())
btn_pre = Button(gamePage,text="Prev",command =lambda:preBtn())
btn_rest = Button(gamePage,text="Rest",command =lambda:resetBtn())
gamePage.mainloop()