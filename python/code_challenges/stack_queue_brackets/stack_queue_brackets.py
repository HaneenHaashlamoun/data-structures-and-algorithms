def validate_brackets(input):
    parentheses_open = input.count('(')
    parentheses_close = input.count(')')
    curly_open = input.count('{')
    curly_close = input.count('}')
    square_open = input.count('[')
    square_close = input.count(']')
    List=[]

    if parentheses_open == parentheses_close and curly_open == curly_close and square_open == square_close:
        for char in input:
            if char == '{' or char == '(' or char == '[':
                List.append(char) 
            elif char == '}' or char == ')' or char == ']':
                print(List)
                element = List.pop() 
                print(List)
                if not Compareing(element, char):
                    return False
        return True
    else:
        return False


def Compareing(opening, closing):
    if opening == '(' and closing == ')':
        return True
    if opening == '[' and closing == ']':
        return True
    if opening == '{' and closing == '}':
        return True  
    return False


if __name__=='__main__':

    print(validate_brackets('{}(){}'))
    print(validate_brackets('()[[Extra Characters]]'))
    print(validate_brackets('[({[({})]})]'))
    print(validate_brackets('{(})'))