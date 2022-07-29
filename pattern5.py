from turtle import st


def pattern(n):
    for row in range(1,n+1):
        for sapce in range(1,row):
            print('  ',end='')
        for star in range(n+1-row,0,-1):
            print('* ',end='')
        print('\n')
        
pattern(5)

#output

'''
* * * * * 

  * * * * 

    * * * 

      * * 

        * 
        
'''