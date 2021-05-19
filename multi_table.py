def multi_table(number):
    sentence = [f"{i} * {number} = {i*number}" for i in range(1,11)]
    return '\n'.join(sentence))
    # good luck

print(multi_table(5) )   