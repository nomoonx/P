def solve(n, m):
    prime=[1 for i in range(2002)]
    prime[0]=0
    prime[1]=0
    for i in range(2,50):
        if prime[i]>0:
            for j in range(2,int(2000/i)):
                prime[i*j]=0
    print(prime[577])
    prod=1
    arr={i:1 for i in range(m-1,0,-1)}
    count=0
    bbb=[]
    # for i in range(m-1,0,-1):
    for i in range(1,m):
        b=(n+i)
        # if prime[b]==0:
        # print("1",prod,arr)
        print(b,end = ' ')
        if count<m:
            keysToDelete=[]
            for j in arr:
                if b%j==0:
                    print(j,end=' ')
                    b=int(b/j)
                    keysToDelete.append(j)
                    count+=1
            for key in keysToDelete:
                del arr[key]
        # print("2",bbb,arr)
        if b>1:
            bbb.append(b)
        print()
        
    print(count)
    print(bbb)
    print(arr)
    # for i in range(1,m-1):
    #     if arr[i]==1:
    #         print(i+1)
    for b in bbb:
        if b>=m and prime[b]>0:
            continue
        prod*=b
        print(prod)
        if count<m:
            keysToDelete=[]
            for j in arr:
                if prod%j==0:
                    print(prod,j)
                    prod=int(prod/j)
                    keysToDelete.append(j)
                    count+=1
            for key in keysToDelete:
                del arr[key]
    print(count)
    print(arr)
    return int(prod)

print(solve(121,175))