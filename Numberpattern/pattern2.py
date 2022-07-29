def pattern(n):
    for row in range(1,n+1):
        for j in range(1,n+1):
            print(f'{j} ',end = '')
        print('\n')
        
pattern(5)


# output

'''''
1 2 3 4 5 

1 2 3 4 5 

1 2 3 4 5 

1 2 3 4 5 

1 2 3 4 5 

'''''