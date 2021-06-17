# Enter your code here. Read input from STDIN. Print output to STDOUT

n,m = map(int,input().split())
N = list(map(int,input().split()))
A = set(map(int,input().split()))
B = set(map(int,input().split()))
c = A|B
N = (i for i in N if i in c)
print(sum(1 if i in A else -1 for i in N))
