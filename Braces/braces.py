#!/python3/bin/python3


## Function: check_braces
#  Description: Figure out if the list elements have a good matching braces
#  Parameters: expressions
#     expressions: list of strings with braces
def check_braces(expressions):
    # we need to iterate trough all elements of the list
    for expression in expressions:
        # we are going to use a list as a queue
        braces_stack = []
        # flag to help us and stop iterating when find a miss match
        result = True
        braces_len = len(expression)
        brace_index = 0
        while(brace_index < braces_len and result):
            brace = expression[brace_index]
            # if it is an opening brace we add it to the queue, otherwise we
            # remove the last element of the queue and compare if it is the
            # corresponding match
            if(brace in ['(', '[', '{']):
                braces_stack.append(brace)
            elif(len(braces_stack) > 0):
                last_brace_stack = braces_stack.pop()
                if(brace == ')'):
                    if(not '(' == last_brace_stack):
                        result = False
                elif(brace == ']'):
                    if(not '[' == last_brace_stack):
                        result = False
                else:
                    if(not '{' == last_brace_stack):
                        result = False
            else:
                result = False
            brace_index += 1

        # print the result
        if(result and len(braces_stack) == 0):
            print(1)
        else:
            print(0)


if(__name__ == '__main__'):
    expression = ['([][]{', '()()(){((()[]))}', '()()(){((()[])){}']
    # check if expressions are ok
    check_braces(expression)