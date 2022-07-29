def pattern(n):
    for row in range(1,n+1):
        for j in range(1,n+1):
            print(f'{row} ',end = '')
        print('\n')
        
pattern(5)

#output

'''
1 1 1 1 1 

2 2 2 2 2 

3 3 3 3 3 

4 4 4 4 4 

5 5 5 5 5 

'''