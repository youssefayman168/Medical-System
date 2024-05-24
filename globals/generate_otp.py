import random
def generate_otp():
    number_list = [x for x in range(10)]
    code_items = []

    for i in range(4):
        num = random.choice(number_list)
        code_items.append(num)

    code_string = "".join(str(item) for item in code_items)
    return code_string
