if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    list1=list(arr)

max1=max(list1)

max_no=list1.count(max1)

[list1.remove(max1) for i in range(0,max_no)]

print(max(list1))
        
