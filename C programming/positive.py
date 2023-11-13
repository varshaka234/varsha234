input_numbers=input("Enter a list of numbers separated by spaces:")
numbers=input_numbers.split(',')
numbers = [int(num) for num in numbers]
even_numbers=[num for num in numbers if num % 2==0]
print("Even numbers from the given list:",even_numbers)
