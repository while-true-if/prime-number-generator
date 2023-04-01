def is_sosu(num: int):
        if type(num) != int:
                raise TypeError("The value is not an integer.")
        if num < 2:
                raise ValueError("The number is under 2")
        for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                        return False
        return True

def sosus(limit: int):
        array = []
        if type(limit) != int:
                raise TypeError("The value is not an integer.")
        if limit < 2:
                raise ValueError("The limit is under 2")
        for i in [2] + list(range(3, limit, 2)):
                if is_sosu(i):
                        array.append(i)
        return array

"""
while True:
        num = input()
        try:
                num = int(num)
        except:
                break
        print(is_sosu(num))
"""        

l = sosus(int(input()))
strings_of_numbers = ""
for i in l:
        strings_of_numbers += str(i) + " "
print(strings_of_numbers[:-1])
