def pattern(n):
    for row in range(1,n+1):
        for space  in range(n-row,0,-1):
            print('  ',end='')
        for Star in range(1,row+1):
            print('* ',end = '')
        print('\n')
        
        
pattern(5)

# output

'''
        * 

      * * 

    * * * 

  * * * * 

* * * * * 

'''