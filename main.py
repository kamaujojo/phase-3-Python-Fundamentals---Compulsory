def add_numbers(num1, num2): ##adds two numbers and returns result
    return num1 + num2
print(add_numbers(1,2))


def is_even(number): #checks if a number is even 
    return number % 2 == 0 #returns true if a number is divisible by 2 without a reminder 
print(is_even(4))
print(is_even(9))
print(is_even(6))


def reverse_string(text): #reverses the given string 
    return text[::-1] #returns the string in reverse order
print(reverse_string("hello"))
print(reverse_string("first"))
print(reverse_string("last"))



def count_vowels(text): #counts the vowels of vowels
    vowels = 'aeiou'
    return sum(1 for char in text.lower() if char in vowels)
print(count_vowels(text='count'))


def calculate_factorial(n):  #Calculates the factorial of a number.
    if n == 0:    
        return 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i  # Multiply factorial by each number from 1 to n
    return factorial
print(calculate_factorial(5))


def apply_decorator(func):  
    def decorator_func(*args, **kwargs):
        print("Decorator Applied")  # Print message before executing the function
        return func(*args, **kwargs)
    return decorator_func
def greet():
    return "Hello!"
decorated_greet = apply_decorator(greet)
print(decorated_greet())


def sort_by_age(list_of_tuples):
    return sorted(list_of_tuples, key=lambda x: x[1])  # Sort the list by the second element of each tuple
people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
print(sort_by_age(people))


def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()  # Start with a copy of the first dictionary
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value # Sum values for overlapping keys
        else:
            merged_dict[key] = value
    return merged_dict
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
print(merge_dicts(dict1, dict2)) 


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Information: {self.year} {self.make} {self.model}") # Create an instance of the Car class and display its information
my_car = Car(make="Toyota", model="Corolla", year=2020)
my_car.display_info() 

 

