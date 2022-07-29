def pattern(n):
    for row in range(1,n+1):
        for space in range(row-1):
            print('  ',end='')
        for star in range((2*n+1)-2*row):
            print('* ',end='')
        print('\n')
    
pattern(5)


#output

'''

* * * * * * * * * 

  * * * * * * * 

    * * * * * 

      * * * 

        * 

'''
    