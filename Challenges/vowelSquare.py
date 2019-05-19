def VowelSquare(strArr): 
    vowels = 'aeiou'
    check = []
    matrix = [[1, 0], [0, 1], [1, 1]]
    for y_coord, y_data in enumerate(strArr):
        
        if y_coord == len(strArr) - 1:
            continue
        
        for x_coord, x_data in enumerate(y_data):
            print(x_coord)
            print(x_data)
            print('test')
            if x_coord == len(x_data) - 1 or x_data not in vowels:
                continue
            
            check = []
            for coords in matrix:
                letter = strArr[y_coord + coords[1]][x_coord + coords[0]]
                print(letter)
                if letter not in vowels:
                    break
            else:
                print('help')
                return f"{y_coord}-{x_coord}"
    return 'not found'
    # code goes here 
    
    
# keep this function call here  
print(VowelSquare(["gg", "ff"]))
