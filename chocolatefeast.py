
T = int(raw_input())

for i in range (0,T):
    N,C,M = [int(x) for x in raw_input().strip().split(' ')]
    
    total_choc = 0
    chocs = 0
    
    if N > C:
        chocs = N / C
        rem = N % C
        total_choc += chocs
        
        while chocs >= M :
            chocs = chocs / M            
            rem = chocs % M
            total_choc += chocs
            
        while (rem+chocs) >= M :
            chocs = (rem+chocs) / M            
            rem = (rem+chocs) % M
            total_choc += chocs
        
        print total_choc
        
