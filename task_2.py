# Step 1: Write to the file
text_to_write = input("Enter text to write to the file: ")
with open("output.txt", "w") as f:
    f.write(text_to_write + "\n")
print("Data successfully written to output.txt.")

# Step 2: Append to the file
text_to_append = input("Enter additional text to append: ")
with open("output.txt", "a") as f:
    f.write(text_to_append + "\n")
print("Data successfully appended.")

# Step 3: Read and display final content
print("\nFinal content of output.txt:")
with open("output.txt", "r") as f:
    content = f.read()
    print(content)
# Step 4: Read and display the first line