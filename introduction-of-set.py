def average(array):
    s = set(array)        # remove duplicate values
    avg = sum(s) / len(s) # calculate average
    return avg


       
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
