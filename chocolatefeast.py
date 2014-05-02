
T = int(raw_input())
for i in range (0,T):
    N,C,M = [int(x) for x in raw_input().strip().split(' ')]
    
    total_choc = 0
    chocs = 0
    if N > C:
       
        total_choc = N / C
        wrappers = total_choc
        
        while wrappers >= M:
            chocs = wrappers / M
            wrappers = (wrappers % M) + chocs
            total_choc = total_choc + chocs
        
        print total_choc
        
