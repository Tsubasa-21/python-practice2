n=int(input())
C=[[None]*(i+1)+list(map(int,input().split()))for i in range(n-1)]
print(C)
ans="No"
for a in range(n):
    for b in range(a+1,n):#ここでa+1なのはaよりも小さい値をbに代入しない様にするため、cのときも同じ
        for c in range(b+1,n):
            if C[a][b]+C[b][c] < C[a][c]:
                ans="Yes"
print(ans)