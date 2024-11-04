import sqlite3

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero is not allowed."
    return a / b

conn = sqlite3.connect('math_results.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS results
             (operation TEXT, num1 REAL, num2 REAL, result REAL)''')

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice(1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    result = add(num1, num2)
    operation = 'Add'
elif choice == '2':
    result = subtract(num1, num2)
    operation = 'Subtract'
elif choice == '3':
    result = multiply(num1, num2)
    operation = 'Multiply'
elif choice == '4':
    result = divide(num1, num2)
    operation = 'Divide'
else:
    print("Invalid input")
    result = None
    operation = None

if result is not None:
    print(f"The result is: {result}")
    c.execute("INSERT INTO results (operation, num1, num2, result) VALUES (?, ?, ?, ?)",
              (operation, num1, num2, result))
    conn.commit()

conn.close()
