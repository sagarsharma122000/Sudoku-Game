from tkinter import *
board = []
def main_screen():
    top = Tk()
    top.title("SUDOKU")
    top.configure(background='antiquewhite1')
    top.geometry("300x360")

    lb = Label(top, text="Select Level",fg='navy',bg='antiquewhite1', font=("Arial Black", 30))
    lb.pack(pady=5)

    l1 = Button(top, text="Level 1",bg='cyan4',bd=5,fg='white',font=("Arial Black", 12), command=level1)
    l1.pack(pady=15)

    l2 = Button(top, text="Level 2",bg='cyan4',bd=5, fg='white',font=("Arial Black", 12),command=level2)
    l2.pack(pady=10)

    l3 = Button(top, text="Level 3",bg='cyan4',bd=5,fg='white', font=("Arial Black", 12),command=level3)
    l3.pack(pady=10)

    l4 = Button(top, text="Level 4", bg='cyan4',fg='white',bd=5,font=("Arial Black", 12),command=level4)
    l4.pack(pady=10)
    top.mainloop()

def level1():
    level = [[5,1,7,6,0,0,0,3,4],
         [2,8,9,0,0,4,0,0,0],
         [3,4,6,2,0,5,0,9,0],
         [6,0,2,0,0,0,0,1,0],
         [0,3,8,0,0,6,0,4,7],
         [0,0,0,0,0,0,0,0,0],
         [0,9,0,0,0,0,0,7,8],
         [7,0,3,4,0,0,5,6,0],
         [0,0,0,0,0,0,0,0,0]]
    load_game(level, 1)


def sol1():
    solution = [[5,1,7,6,9,8,2,3,4],
    [2,8,9,1,3,4,7,5,6],
    [3,4,6,2,7,5,8,9,1],
    [6,7,2,8,4,9,3,1,5],
    [1,3,8,5,2,6,9,4,7],
    [9,5,4,7,1,3,6,8,2],
    [4,9,5,3,6,2,1,7,8],
    [7,2,3,4,8,1,5,6,9],
    [8,6,1,9,5,7,4,2,3], ]
    solution_lvl(solution, 1)


def level2():
    level = [[5,1,7,6,0,0,0,3,4],
         [0,8,9,0,0,4,0,0,0],
         [3,0,6,2,0,5,0,9,0],
         [6,0,0,0,0,0,0,1,0],
         [0,3,0,0,0,6,0,4,7],
         [0,0,0,0,0,0,0,0,0],
         [0,9,0,0,0,0,0,7,8],
         [7,0,3,4,0,0,5,6,0],
         [0,0,0,0,0,0,0,0,0]]
    load_game(level, 2)


def sol2():
    solution = [[5,1,7,6,9,8,2,3,4],
        [2,8,9,1,3,4,7,5,6],
        [3,4,6,2,7,5,8,9,1],
        [6,7,2,8,4,9,3,1,5],
        [1,3,8,5,2,6,9,4,7],
        [9,5,4,7,1,3,6,8,2],
        [4,9,5,3,6,2,1,7,8],
        [7,2,3,4,8,1,5,6,9],
        [8,6,1,9,5,7,4,2,3], ]
    
    solution_lvl(solution, 1)


def level3():
    level = [[8,5,0,0,0,2,4,0,0],
         [7,2,0,0,0,0,0,0,9],
         [0,0,4,0,0,0,0,0,0],
         [0,0,0,1,0,7,0,0,2],
         [3,0,5,0,0,0,9,0,0],
         [0,4,0,0,0,0,0,0,0],
         [0,0,0,0,8,0,0,7,0],
         [0,1,7,0,0,0,0,0,0],
         [0,0,0,0,3,6,0,4,0]]
    load_game(level, 3)


def sol3():
    solution = [[8,5,9,6,1,2,4,3,7],
                [7,2,3,8,5,4,1,6,9],
                [1,6,4,3,7,9,5,2,8],
                [9,8,6,1,4,7,3,5,2],
                [3,7,5,2,6,8,9,1,4]
                ,[2,4,1,5,9,3,7,8,6],
                [4,3,2,9,8,1,6,7,5],
                [6,1,7,4,2,5,8,9,3],
                [5,9,8,7,3,6,2,4,1] ]
    solution_lvl(solution, 3)
def level4():
    level =[[0,0,5,3,0,0,0,0,0],
         [8,0,0,0,0,0,0,2,0],
         [0,7,0,0,1,0,5,0,0],
         [4,0,0,0,0,5,3,0,0],
         [0,1,0,0,7,0,0,0,6],
         [0,0,3,2,0,0,0,8,0],
         [0,6,0,5,0,0,0,0,9],
         [0,0,4,0,0,0,0,3,0],
         [0,0,0,0,0,9,7,0,0]]
    load_game(level, 3)


def sol4():
    solution = [[1,4,5,3,2,7,6,9,8],
        [8,3,9,6,5,4,1,2,7],
        [6,7,2,9,1,8,5,4,3],
        [4,9,6,1,8,5,3,7,2],
        [2,1,8,4,7,3,9,5,6],
        [7,5,3,2,9,6,4,8,1],
        [3,6,7,5,4,2,8,1,9],
        [9,8,4,7,6,1,2,3,5],
        [5,2,1,8,3,9,7,6,4]]
    solution_lvl(solution, 4)
def check():
    flag=1
    x=0
    for i in range(0,9):
        if (board[i].get())=='':
            root6=Tk()
            root6.configure(background='antiquewhite1')
            root6.title("LOST")
            EMPTY=Label(root6, text="Entry in 1st Row is Empty", bg='antiquewhite1',fg='red',font=("Arial Black", 24))
            EMPTY.pack(padx=20,pady=20)
        x=(x+(int(board[i].get())))
    if x!=45:
        flag=1
    x=0
    for i in range(9,18):
        if (board[i].get())=='':
            root6=Tk()
            root6.configure(background='antiquewhite1')
            root6.title("LOST")
            EMPTY=Label(root6, text="Entry in 2nd Row is Empty", bg='antiquewhite1',fg='red',font=("Arial Black", 24))
            EMPTY.pack(padx=20,pady=20)
        x=(x+(int(board[i].get())))
    if x!=45:
        flag=1
    x=0
    for i in range(18,27):
        if (board[i].get())=='':
            root6=Tk()
            root6.configure(background='antiquewhite1')
            root6.title("LOST")
            EMPTY=Label(root6, text="Entry in 3rd Row is Empty", bg='antiquewhite1',fg='red',font=("Arial Black", 24))
            EMPTY.pack(padx=20,pady=20)
        x=(x+(int(board[i].get())))
    if x!=45:
        flag=1
    x=0
    for i in range(27,36):
        if (board[i].get())=='':
            root6=Tk()
            root6.configure(background='antiquewhite1')
            root6.title("LOST")
            EMPTY=Label(root6, text="Entry in 4th Row is Empty", bg='antiquewhite1',fg='red',font=("Arial Black", 24))
            EMPTY.pack(padx=20,pady=20)
        x=(x+(int(board[i].get())))
    if x!=45:
        flag=1
    x=0
    for i in range(36,45):
        if (board[i].get())=='':
            root6=Tk()
            root6.configure(background='antiquewhite1')
            root6.title("LOST")
            EMPTY=Label(root6, text="Entry in 5th Row is Empty", bg='antiquewhite1',fg='red',font=("Arial Black", 24))
            EMPTY.pack(padx=20,pady=20)
        x=(x+(int(board[i].get())))
    if x!=45:
        flag=1
    x=0
    for i in range(45,54):
        if (board[i].get())=='':
            root6=Tk()
            root6.configure(background='antiquewhite1')
            root6.title("LOST")
            EMPTY=Label(root6, text="Entry in 6th Row is Empty", bg='antiquewhite1',fg='red',font=("Arial Black", 24))
            EMPTY.pack(padx=20,pady=20)
        x=(x+(int(board[i].get())))
    if x!=45:
        flag=1
    x=0
    for i in range(54,63):
        if (board[i].get())=='':
            root6=Tk()
            root6.configure(background='antiquewhite1')
            root6.title("LOST")
            EMPTY=Label(root6, text="Entry in 7th Row is Empty", bg='antiquewhite1',fg='red',font=("Arial Black", 24))
            EMPTY.pack(padx=20,pady=20)
        x=(x+(int(board[i].get())))
    if x!=45:
        flag=1
    x=0
    for i in range(63,72):
        if (board[i].get())=='':
            root6=Tk()
            root6.configure(background='antiquewhite1')
            root6.title("LOST")
            EMPTY=Label(root6, text="Entry in 8th Row is Empty", bg='antiquewhite1',fg='red',font=("Arial Black", 24))
            EMPTY.pack(padx=20,pady=20)
        x=(x+(int(board[i].get())))
    if x!=45:
        flag=1
    x=0
    for i in range(72,81):
        if (board[i].get())=='':
            root6=Tk()
            root6.configure(background='antiquewhite1')
            root6.title("LOST")
            EMPTY=Label(root6, text="Entry in 9th Row is Empty", bg='antiquewhite1',fg='red',font=("Arial Black", 24))
            EMPTY.pack(padx=20,pady=20)
        x=(x+(int(board[i].get())))
    if x!=45:
        flag=1
    if flag==1:
        root3=Tk()
        root3.title("LOST")
        root3.configure(background='antiquewhite1')
        fail=Label(root3, text="YOU LOST TRY AGAIN", bg='antiquewhite1',fg='red',font=("Arial Black", 24))
        fail.pack(padx=20,pady=20)
    else:
        root4=Tk()
        root4.title("WON")
        root4.configure(background='antiquewhite1')
        pas=Label(root4 ,text="YOU PASSED", bg='antiquewhite1',fg='green',font=("Arial Black", 24))
        pas.pack(padx=20,pady=20)
    
def load_game(level, lvl):
    if lvl == 1:
        sol = sol1
    elif lvl == 2:
        sol = sol2
    elif lvl == 3:
        sol = sol3
    elif lvl == 4:
        sol = sol4
    root = Tk()
    root.title("Level "+str(lvl))
    root.geometry("720x650")

    game = Frame(root, bg='misty rose')
    board_frame = Frame(game, bg='powder blue')
    button_frame = Frame(game,bg='misty rose')

    for x1 in range(0, 3):
        for y1 in range(0, 3):
            if (x1+y1) % 2 == 0:
                Frame(board_frame, bg="gold2", height=200,
                      width=240).grid(row=x1, column=y1)
            else:
                Frame(board_frame, bg="red2", height=200,
                      width=240).grid(row=x1, column=y1)
    board.clear()
    for x1 in range(9):
        for y1 in range(9):
            if level[x1][y1] != 0:
                var = StringVar(board_frame, value=str(level[x1][y1]))

                entry = Entry(board_frame, state=DISABLED, textvariable=var, justify=CENTER,
                              bd=5, bg="light grey", width=3, font=("Arial Black", 24))
                board.append(entry)
                entry.place(relx=y1*(1/9), rely=x1*(1/8.9))
            else:
                entry = Entry(board_frame, justify=CENTER, fg="maroon", bd=5,
                              bg="light grey", width=3, font=("Arial Black", 24))
                board.append(entry)

                entry.place(relx=y1*(1/9), rely=x1*(1/8.9))

    board_frame.pack()
    solution_button = Button(button_frame,bg='tan1',fg='white', font=("Arial Black", 14),text="Solution",
                           bd=3,height=50, command=sol)
    check_button = Button(button_frame,bg='lime green', fg='white',font=("Arial Black", 14), text="Submit",
                           bd=3,height=50, command=check)
    check_button.pack(side=LEFT,padx=20)
    solution_button.pack()
    button_frame.pack()
    game.pack()


def solution_lvl(level, lvl):
    root1 = Tk()
    root1.title("Solution "+str(lvl))
    root1.geometry("380x320")

    game = Frame(root1, bg='thistle1')
    board_frame = Frame(game, bg='cyan4')
    button_frame = Frame(game, bg='blue')

    for x1 in range(0, 3):
        for y1 in range(0, 3):
            if (x1+y1) % 2 == 0:
                Frame(board_frame, bg="red4", height=100,
                      width=120).grid(row=x1, column=y1)
            else:
                Frame(board_frame, bg="green4", height=100,
                      width=120).grid(row=x1, column=y1)
    for x1 in range(9):
        for y1 in range(9):
            if level[x1][y1] != 0:
                var = StringVar(board_frame, value=str(level[x1][y1]))

                entry = Entry(board_frame, state=DISABLED, textvariable=var, justify=CENTER,
                              bd=5, bg="light grey", width=2, font=("Arial Black", 12))
                entry.place(relx=y1*(1/9), rely=x1*(1/8.9))
            else:
                entry = Entry(board_frame, justify=CENTER, fg="maroon", bd=5,
                              bg="light grey", width=2, font=("Arial Black", 12))
                entry.place(relx=y1*(1/9), rely=x1*(1/8.9))

    board_frame.pack(padx=10,pady=10)
    button_frame.pack()
    game.pack()

main_screen()
