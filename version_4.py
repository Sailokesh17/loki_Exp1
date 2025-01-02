import matplotlib.pyplot as plt

x_values = []
y_values = []

# Correct the file path using a raw string or forward slashes
file_path = r'C:\Users\Sai Lokesh\OneDrive\Desktop\SW Lab\Exp_1\data2.txt'

with open(file_path, 'r') as file:
    for _ in range(40):
        try:
            # Read and process each line
            a = float(file.readline().strip().split('=')[1])
            b = float(file.readline().strip().split('=')[1])
            c = float(file.readline().strip().split('=')[1])
            x = float(file.readline().strip().split('=')[1])
            
            # Calculate y and append to lists
            y = a * x * x + b * x + c
            x_values.append(x)
            y_values.append(y)
        except (IndexError, ValueError) as e:
            print(f"Error reading or processing a line: {e}")
            continue  # Skip the problematic entry and move to the next

# Plot the data
plt.plot(x_values, y_values, marker='o', linestyle='-', color='b')
plt.title('Graph of y = ax^2 + bx + c')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
