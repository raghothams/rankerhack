T = int(raw_input())

for i in xrange(T):
    N = int(raw_input())
    by3 = N/3
    by5 = N/5
    mod3 = N%3
    mod5 = N%5
    
    if N >= 8:
        
        if mod3 == 0:
            
            
            print '5' * N
            continue

        into3 = 3*by3
        into5 = 5*by5
        
        diff = 5 - mod3

        if diff > 0:
        
            x = into3 - diff
            y = mod3 + diff
            
            while x % 3 != 0:
                x = x - 5
                y = y + 5
        
        else:
            
            x = into3 + diff
            y = mod3 - diff
            
            while y % 5 != 0:
                x = x + 5
                y = y - 5
            
        print '5' * x + '3' * y
                    
    else:
        
        if mod3 == 0:
            print '5' * N
            continue
            
        elif mod5 == 0:    
            print '3' * N
        
        else:
            print '-1'
            
