def countMagicalRows(input1: int, input2: int, input3: [[int]]) -> int:
    magical_rows_count = 0
    
    for row in input3:
        odd_sum = 0
        even_sum = 0
        
        for num in row:
            if num % 2 == 0:
                even_sum += num
            else:
                odd_sum += num
        
        # Check if sum of odd numbers is greater than sum of even numbers
        if odd_sum > even_sum:
            magical_rows_count += 1
    
    return magical_rows_count

# Dynamic input handling
input1 = int(input("Enter the number of rows: "))  # Number of rows
input2 = int(input("Enter the number of columns: "))  # Number of columns

input3 = []
print("Enter the elements row by row:")
for i in range(input1):
    row = list(map(int, input().split()))  # Reading a row of space-separated integers
    input3.append(row)

# Output the number of magical rows
result = countMagicalRows(input1, input2, input3)
print(f"Number of magical rows: {result}")
