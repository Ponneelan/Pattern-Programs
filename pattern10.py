def pattern(n):
    for i in range(n):
        for s in range(n-i-1):
            print('  ',end='')
        for p in range(2*i+1):
            if p == 0 or p == 2*i:
                print('* ',end='')
            else:
                print('  ',end='')
        print()
        
    for j in range(n-1):
        for s in range(j+1):
            print('  ',end='')
        for p in range(2*(n - j - 1) - 1):
            if p==0 or p==2*(n - j - 1) - 2:
                print('* ',end='')
            else:
                print('  ',end='')
        print()
     
        
        
pattern(5)


#output

'''
        * 
      *   * 
    *       * 
  *           * 
*               * 
  *           * 
    *       * 
      *   * 
        * 

'''