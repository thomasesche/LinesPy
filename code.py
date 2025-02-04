def display(n):
    cls()
    cls(color="#F6DEC1")
    for i in range(n):
        frect(100 + i * 23, 100, 10, 200, color="#B29464", radius=6)

print("NiPlusNimMoins", 200, 200, size=20, color="black", anchor="no", blink=0)
pause(2000)

display(20)

stickCounter = 20

while True:
	n = int(input("combiens de batonets veut tu enlever ? "))
	display(stickCounter - n)
	stickCounter -= n