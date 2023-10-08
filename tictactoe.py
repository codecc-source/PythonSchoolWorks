import turtle
import copy
import random

screen = turtle.Screen()
screen.setup(800, 800)
screen.title("Tic Tac Toe Game")
screen.setworldcoordinates(-5, -5, 5, 5)
screen.bgcolor('black')
turtle.hideturtle()

choice = turtle.numinput("Choose side: ", "1 for X / 2 for O")
if choice != 1 and choice != 2:
    errorMess = turtle.Turtle()
    errorMess = turtle.textinput("Error", "Not 1 or 2")
    exit()


def draw_board():
    welcomeScreen = turtle.Turtle()
    welcomeScreen.color('white')
    welcomeScreen.up()
    welcomeScreen.hideturtle()
    welcomeScreen.goto(0, 4)
    welcomeScreen.write('TIC TAC TOE', align='center', font=('Courier', 40, 'italic'))

    instructions = turtle.Turtle()
    instructions.color('white')
    instructions.up()
    instructions.hideturtle()
    instructions.goto(0, -4)
    if choice == 1:
        instructions.write(f"Player:X " " AI:O", align='center', font=('Courier', 40, 'italic'))
    else:
        instructions.write(f"Player:O " " AI:X", align='center', font=('Courier', 40, 'italic'))

    message = turtle.Turtle()
    message.color('green')
    message.up()
    message.hideturtle()
    message.goto(0, -4.3)
    message.write("Uses Turtle and MiniMax Algorithm", align='center', font=('Courier', 15, 'italic'))

    board = turtle.Turtle()
    board.speed(5)
    board.shape('circle')
    board.color('cyan')
    board.pensize(3)
    board.up()
    board.goto(-3, -1)
    board.seth(0)
    board.down()
    board.fd(6)
    board.up()
    board.goto(-3, 1)
    board.seth(0)
    board.down()
    board.fd(6)
    board.up()
    board.goto(-1, -3)
    board.seth(90)
    board.down()
    board.fd(6)
    board.up()
    board.goto(1, -3)
    board.seth(90)
    board.down()
    board.fd(6)
    board.goto(-3, 3)
    board.goto(-3, -3)
    board.goto(3, -3)
    board.goto(3, 3)
    board.goto(1, 3)
    board.hideturtle()


def draw_circle(x, y):
    turtle.up()
    turtle.pensize(10)
    turtle.goto(x, y - 0.75)
    turtle.seth(0)
    turtle.color('red')
    turtle.down()
    turtle.tracer(0,0)
    turtle.circle(0.75, steps=100)


def draw_x(x, y):
    turtle.pensize(10)
    turtle.color('blue')
    turtle.up()
    turtle.goto(x - 0.75, y - 0.75)
    turtle.down()
    turtle.goto(x + 0.75, y + 0.75)
    turtle.up()
    turtle.goto(x - 0.75, y + 0.75)
    turtle.down()
    turtle.goto(x + 0.75, y - 0.75)
    turtle.tracer(0,0)



def draw_piece(i, j, p):
    if p == 0: return
    x, y = 2 * (j - 1), -2 * (i - 1)
    if choice != p:
        turtle.bgcolor('orange')
        draw_x(x, y)
    else:
        turtle.bgcolor('dark blue')
        draw_circle(x, y)


def draw(b):
    draw_board()
    for i in range(3):
        for j in range(3):
            draw_piece(i, j, b[i][j])
    screen.update()

def gameover(b):
    if b[0][0] > 0 and b[0][0] == b[0][1] and b[0][1] == b[0][2]: return b[0][0]
    if b[1][0] > 0 and b[1][0] == b[1][1] and b[1][1] == b[1][2]: return b[1][0]
    if b[2][0] > 0 and b[2][0] == b[2][1] and b[2][1] == b[2][2]: return b[2][0]
    if b[0][0] > 0 and b[0][0] == b[1][0] and b[1][0] == b[2][0]: return b[0][0]
    if b[0][1] > 0 and b[0][1] == b[1][1] and b[1][1] == b[2][1]: return b[0][1]
    if b[0][2] > 0 and b[0][2] == b[1][2] and b[1][2] == b[2][2]: return b[0][2]
    if b[0][0] > 0 and b[0][0] == b[1][1] and b[1][1] == b[2][2]: return b[0][0]
    if b[2][0] > 0 and b[2][0] == b[1][1] and b[1][1] == b[0][2]: return b[2][0]
    p = 0
    for i in range(3):
        for j in range(3):
            p += (1 if b[i][j] > 0 else 0)
    if p == 9:
        return 3
    else:
        return 0


def play(x, y):
    global turn
    if turn == 'X': return

    i = 3 - int(y + 5) // 2
    j = int(x + 5) // 2 - 1
    if i > 2 or j > 2 or i < 0 or j < 0 or b[i][j] != 0: return
    if turn == 'X':
        b[i][j], turn = 1, 'O'
    else:
        b[i][j], turn = 2, 'X'
    draw(b)
    r = gameover(b)
    if r == 1:
        screen.textinput("Game over!", "X won!")
    elif r == 2:
        screen.textinput("Game over!", "O won!")
    elif r == 3:
        screen.textinput("Game over!", "Tie!")
    if r > 0: turtle.bye()
    _, move = max_node(b, -2, 2)
    b[move[0]][move[1]] = 1
    draw(b)
    r = gameover(b)
    if r == 1:
        screen.textinput("Game over!", "X won!")
    elif r == 2:
        screen.textinput("Game over!", "O won!")
    elif r == 3:
        screen.textinput("Game over!", "Tie!")
    if r > 0: turtle.bye()
    turn = 'O'


b = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
turn = 'X'
screen.onclick(play)


def max_node(b, alpha, beta):
    r = gameover(b)
    if r == 1:
        return 1, None
    elif r == 2:
        return -1, None
    elif r == 3:
        return 0, None

    score = -2
    pm = list()
    for i in range(3):
        for j in range(3):
            if b[i][j] == 0: pm.append((i, j))
    random.shuffle(pm)
    for (i, j) in pm:
        if b[i][j] == 0:
            nb = copy.deepcopy(b)
            nb[i][j] = 1
            cs, _ = min_node(nb, alpha, beta)
            if score < cs:
                score = cs
                move = (i, j)
            alpha = max(alpha, cs)
            if alpha >= beta: return score, move
    return score, move


def min_node(b, alpha, beta):
    r = gameover(b)
    if r == 1:
        return 1, None
    elif r == 2:
        return -1, None
    elif r == 3:
        return 0, None

    score = 2
    pm = list()
    random.shuffle(pm)
    for i in range(3):
        for j in range(3):
            if b[i][j] == 0: pm.append((i, j))
    for (i, j) in pm:
        if b[i][j] == 0:
            nb = copy.deepcopy(b)
            nb[i][j] = 2
            cs, _ = max_node(nb, alpha, beta)
            if score > cs:
                score = cs
                move = (i, j)
            beta = min(beta, cs)
            if alpha >= beta: return score, move
    return score, move


_, move = max_node(b, -2, 2)
b[move[0]][move[1]] = 1
draw(b)
screen.tracer(0,0)
turn = 1
screen.mainloop()