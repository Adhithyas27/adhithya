def comb(L):
      
    for i in range(3):
        for j in range(3):
            for k in range(3):
                  if (i!=j and j!=k and i!=k):
                    print(L[i], L[j], L[k])
                      
# Driver Code
comb([1, 2, 3])
