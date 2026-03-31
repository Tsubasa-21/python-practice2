def f(x):
    a=[]
    for i in range(0,x):
        # a=[]ここに入れてしまうと毎回リストをリセットすることになってしまう
        a.append(i)
        print(a)
    return a

f(3)#print関数wp使わないと表示できない

print(f(3))
print("hello world")
# なぜかvscodeだと実行できない？
# このままだとからのリストにアペンドされたてないのに加えて、返り値がNONEになってしまっている。