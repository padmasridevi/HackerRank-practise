n=int(input())
numbers=tuple(map(int,input().split()))
if len(numbers) == n:
    print(hash(numbers))
