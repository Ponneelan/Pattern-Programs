def pattern(n):
    for row in range(1,n+1):
        for outerSpace in range(n-row):
            print('  ',end = '')
        for inner in range(1,2*row):
            if inner == 1 or inner == 2*row-1:
                print('* ',end = '')
            else:
                if row  == n:
                    print('* ',end='')
                else :
                    print('  ',end='')
        print('\n')
        
        
pattern(5)


#output


'''
        * 

      *   * 

    *       * 

  *           * 

* * * * * * * * * 

'''