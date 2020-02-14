def heapify(A,i,n):
    l = i
    if 2*i <= n and A[2*i]>A[i]:
        l = 2*i
    if 2*i +1 <=n  and A[2*i+1]>A[l]:
        l = 2*i+1
    if l !=i:
        (A[i],A[l]) = (A[l],A[i])
        A = heapify(A,l,n)
    return A

def buildHeap(A,n):
    for i in range(n,0,-1):
        A=heapify(A,i,n)
    return A

def heapsort(A):
    n = len(A)
    A = buildHeap([None]+A,len(A))
    for i in range(len(A)-1,0,-1):
        if i == 2:
            print(3)
            ...
        (A[i],A[1]) = (A[1],A[i])
        n=n-1
        A=heapify(A,1,n)
    print(A)


    print(A)

A=[10,13,6,3,9,12,14,4,7,5,8,11,15,2,1]
heapsort(A)