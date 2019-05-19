
def CorrectPath(string): 
    matrix = [[0 for _ in range(5)] for _ in range(5)]
    position = {'x': 0, 'y' : 0}
    matrix[position['y']][position['x']] = 1
    movement = {'r': [1, 0], 'l': [-1, 0], 'u': [0, -1], 'd' : [0, 1]}
    list_movement = list(string)
    movement_answer = list(string)
    for pos, letter in enumerate(list_movement):
        if letter == '?':
            x_move = movement_answer.count('r') - movement_answer.count('l')
            y_move = movement_answer.count('d') - movement_answer.count('u')
            if x_move < 4 and matrix[position['y']][position['x'] + 1] != 1 :
                movement_answer[pos] = 'r'
            elif y_move < 4 and matrix[position['y'] + 1][position['x']] != 1:
                movement_answer[pos] = 'd'
            elif x_move > -4 and matrix[position['y']][position['x'] - 1] != 1:
                movement_answer[pos] = 'l'
            elif y_move > -4 and matrix[position['y'] - 1][position['x']] != 1:
                movement_answer[pos] = 'u'
        position['x'] += movement[movement_answer[pos]][0]
        position['y'] += movement[movement_answer[pos]][1]
        matrix[position['y']][position['x']] = 1
    final_string = ''.join(movement_answer)
    return final_string
    # code goes here 
    return string
# keep this function call here  
print(CorrectPath("???rrurdr?"))
print(CorrectPath("drdr??rrddd?"))


  