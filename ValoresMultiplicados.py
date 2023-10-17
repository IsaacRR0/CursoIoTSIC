a = ['1','2','4']
b = [1,4,3]
ans=0
a = list(map(int,a))
for aa, bb in zip(a,b):
    ans += aa*bb
print(ans)