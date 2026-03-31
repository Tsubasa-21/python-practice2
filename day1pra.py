def f(x):
    for i in range(0,x):
        a=[]
        a.append(i)
        print(a)

print(f(3))
print("hello world")
# なぜかvscodeだと実行できない？
# このままだとからのリストにアペンドされたてないのに加えて、返り値がNONEになってしまっている。