# pure function has two rules
# 1. It always return the same output for the same input.
# 2. It shouldn't produce any side effects.
# side effects are things that that function does which affects the outside of the function

def multiply_by_2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list  # if we use print with it it will not be following rule 02, it is producing side effects, which is interacting with screen

print(multiply_by_2([1, 2, 3])) # it implements rule 01 give same output for same input, also it follows rule 02, produces no side effects

# if local scope is interacting with global scope then it doesn't follows rule 02, because it is producing side effects