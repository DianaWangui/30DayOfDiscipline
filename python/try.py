def magic_string():
    return ', '.join(['BestSchool' * (i + 1) + '$' for i in range(10)])



for i in range(10):
    print(magic_string())