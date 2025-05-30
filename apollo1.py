# def find_max(numbers):
#     if not numbers:
#         return None
#     return max(numbers)
    
# print(find_max([1,3,2,16]))

def count_vowels(text):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count
print(count_vowels("Hello World!"))