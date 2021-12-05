from tkinter import *
from tkinter import messagebox

def player_move(event):
    global x, y
    if event.keysym == "Up" and maze[y-1][x] != 1:
        canvas.move(player, 0, -70)
        y -= 1
    elif event.keysym == "Down" and maze[y+1][x] != 1:
        canvas.move(player, 0, 70)
        y += 1
    elif event.keysym == "Left" and maze[y][x-1] != 1:
        canvas.move(player, -70, 0)
        x -= 1
    elif event.keysym == "Right" and maze[y][x+1] != 1:
        canvas.move(player, 70, 0)
        x += 1
    if maze[y][x] ==2:
        messagebox.showinfo("미션 성공", "목적지에 도착! 축하합니다!")

window = Tk()
window.title("미로 그리기")

canvas = Canvas(window,width=700, height=490, bg="#FFF8E5")
canvas.pack()

maze=[
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,1,1,1,2,0,0,1],
    [1,1,0,1,1,1,1,1,0,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,1,0,0,1,0,1,0,1],
    [1,0,0,0,1,1,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
]

for y in range(7):
    for x in range(10):
        if maze[y][x] == 1:
            canvas.create_rectangle(x*70, y*70, (x+1)*70, (y+1)*70,
                                    fill="#C6D57E", outline="white")
x = 1
y = 1

img_end = PhotoImage(file="goal_img.png")
end = canvas.create_image(455, 105, image=img_end)

player_img = PhotoImage(file="player_img.png")
player = canvas.create_image(105, 105, image=player_img)

canvas.bind_all("<KeyPress>", player_move)

window.mainloop()
