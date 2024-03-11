# Ternary operators are just like if else but they are written in one line or it's just a shortcut
# ternary operators are also called as conditional expressions

# consider an example of facebook feature your friends can only message you
is_friend = True
# can_message = "true_logic_block" if "true_condition" else "false_logic_block"
can_message = "Message allowed" if is_friend else "Not allowed"
print(can_message)
