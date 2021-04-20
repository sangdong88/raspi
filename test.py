import time
a = 1
while a <=10:
    print("Cycle :->>", a)
    for i in range(0, 101, 10):
        print(i,"for문")
        time.sleep(0.3)
    for i in range(100, -1, -10):
        print(i,"for문")
        time.sleep(0.3)
    a += 1
    