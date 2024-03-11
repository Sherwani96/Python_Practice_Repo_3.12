# using operators between two conditions in if statement is called short circuiting

is_friend = True
is_user = True

# it takes only one true condition and it will execute, if there is no true condition otherwise it will fall in else block
if is_friend or is_user:
    print("Best friends forever")

# it takes both true conditions and it will execute it otherwise it will fall in else block
if is_friend or is_user:
    print("Best friends forever")

