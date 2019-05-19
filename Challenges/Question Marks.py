test_string1 = "arrb6???4xxbl5???eee5" 
test_string2 ="acc?7??sss?3rr1??????5" 
test_string3 ="5??aaaaaaaaaaaaaaaaaaa?5?5" 
test_string4 ="9???1???9???1???9"
test_string5 ="aa6?9" 
def questionMark(string):
    boolean = False
    number = []
    stored_question = []
    for letter in string:
        if number and letter == '?':
            stored_question.append(letter)
        if letter.isdigit():
            number.append(int(letter))
            if len(number) == 2:
                sum_of_numbers = sum(number)
                if sum_of_numbers == 10:
                    if len(stored_question) == 3:
                        boolean = True
                    else:
                        boolean = False
                        return boolean
                    stored_question = []
                    number.pop(0)
    return boolean
print(questionMark(test_string1))
print(questionMark(test_string2))
print(questionMark(test_string3))
print(questionMark(test_string4))
print(questionMark(test_string5))