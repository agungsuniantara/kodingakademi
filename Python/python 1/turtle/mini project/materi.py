import turtle
import time

# Inisialisasi library Turtle dan objek Turtle
t = turtle.Turtle()

# Inisialisasi screen
ts = turtle.Screen()
ts.bgcolor("#ffeb86")
ts.title("Turtle Game")

# Menggambar latar belakang
t.penup()
t.goto(200, 300)
t.pendown()
t.color("blue")
t.begin_fill()
t.goto(400, 300)
t.goto(400, -300)
t.goto(100, -300)
t.goto(100, 300)
t.end_fill()

# Membuat Turtle
t.penup()
t.goto(-200, 0)
t.shape("turtle")
t.shapesize(2)
t.color("green")


# Fungsi untuk Turtle bergerak
def spasi():
    t.penup()
    t.forward(20)
    t.pendown()
    check_goal()


def kanan():
    t.penup()
    t.right(90)
    t.pendown()
    check_goal()


def kiri():
    t.penup()
    t.left(90)
    t.pendown()
    check_goal()


def check_goal():
    x, y = t.pos()
    if 100 <= x <= 400 and -300 <= y <= 300:
        t.hideturtle()
        t.color("white")
        t.write("YOU WIN", align="center", font=("Arial", 24, "normal"))
        ts.update()  # Memperbarui layar
        time.sleep(2)  # Jeda selama 2 detik sebelum menutup
        ts.bye()  # Menutup jendela Turtle saat selesai

# Menghubungkan fungsi gerakan dengan tombol
ts.onkey(spasi, "space")
ts.onkey(kanan, "Right")
ts.onkey(kiri, "Left")

ts.listen()

# Menutup jendela Turtle saat selesai
ts.mainloop()
