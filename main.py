from functools import wraps

# def upper_text(func):
#     @wraps(func)
#     def wrapper():
#         result = func()

#         return result.upper()
        
#     return wrapper

# @upper_text 
# def say_hi():
#     return 'всем привет'


# print(say_hi())



def change_number_to_sharp(func):
    
    @wraps(func)
    def wrapper():
        number = func()
        result = ''
        
        for _ in number [:-2]:
            result +='#'

        result += number[-2:]

        return result

    return wrapper

my_number ='+996700123456'

@change_number_to_sharp
def get_number(number):
    return number

print(get_number(my_number))