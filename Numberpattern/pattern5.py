def pattern(n):
    for row in range(n,0,-1):
        for j in range(1,n+1):
            print(f'{row} ',end = '')
        print('\n')
        
pattern(5)


#output

'''
5 5 5 5 5 

4 4 4 4 4 

3 3 3 3 3 

2 2 2 2 2 

1 1 1 1 1 

'''