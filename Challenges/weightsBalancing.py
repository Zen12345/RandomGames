def ScaleBalancing(strArr): 
    balance = strArr[0][1:-1].split(',')
    balance = [int(x) for x in balance]
    weights = strArr[1][1:-1].split(',')
    weights = [int(x) for x in weights]
    print(weights)
    for weight_pos , weight in enumerate(weights):
        lighter_weight = min(balance)
        heavier_weight = max(balance)
        lighter_weight += weight
        if lighter_weight == heavier_weight:
            return weight
        weights_left = weights[:]
        weights_left.pop(weight_pos)
        temp_light_weight = lighter_weight
        for second_weight in weights_left:
            heavier_weight = max(balance)
            lighter_weight = temp_light_weight
            if lighter_weight > heavier_weight:
                heavier_weight += second_weight
            else:
                lighter_weight += second_weight
            print(lighter_weight)
            print(heavier_weight)
            print('\n')
            if lighter_weight == heavier_weight:
                return f"{weight},{second_weight}"
    return 'not possible'
    # code goes here 
    return strArr
    
# keep this function call here  
print(ScaleBalancing(["[13, 4]", "[1, 2, 3, 6, 14]"]))
