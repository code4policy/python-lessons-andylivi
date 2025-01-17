
with open('name.txt') as f:
    my_name = f.read().strip()

with open('output/hello.txt', 'w') as f:
    f.write(f"Hello, my name is {my_name}.")

# Print the contents of output/hello.txt to verify
with open('output/hello.txt') as f:
    print(f.read())
print(my_name)