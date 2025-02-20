def count_substring(string, sub_string):
    count = 0  # Initialize a counter to keep track of occurrences
    # Iterate through each starting position in the string
    for i in range(len(string)):
        # Check if the substring starts at index 'i'
        if string[i:].startswith(sub_string):
            count += 1  # If true, increment the counter
    
    return count  # Return the final count of occurrences

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)