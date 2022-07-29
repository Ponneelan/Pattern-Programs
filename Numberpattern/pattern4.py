def pattern(n):
    for row in range(1,n+1):
        for j in range(n,0,-1):
            print(f'{j} ',end = '')
        print('\n')
        
pattern(5)

# Output

'''
5 4 3 2 1 

5 4 3 2 1 

5 4 3 2 1 

5 4 3 2 1 

5 4 3 2 1 

'''