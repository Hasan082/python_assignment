
# Read the from the input file and return as dictionary
def read_dictionary(input_file):
    dictionary = {}
    with open(input_file, 'r') as file:
        for singleline in file:
            try:
                parts = singleline.strip().split(':')
                key = parts[0].strip()
                value = ':'.join(parts[1:]).strip()
                dictionary[key] = value
            except Exception as e:
                return f"There is an error reading the input file {e}"
    return dictionary

# Reverse the dictionary
def reverse_dictionary(input_dict):
    reversed_dict = {}
    for key, value in input_dict.items():
        if isinstance(value, list):
            for item in value:
                if item not in reversed_dict:
                    reversed_dict[item] = key
                elif key not in reversed_dict[item]:
                    reversed_dict[item] += ", " + key
        else:
            if value not in reversed_dict:
                reversed_dict[value] = key
            elif key not in reversed_dict[value]:
                reversed_dict[value] += ", " + key
    return reversed_dict

# Write from the reversed dictionary to the output file
def write_dictionary(reversed_dict, output_file):
    with open(output_file, 'w') as file:
        for key, value in reversed_dict.items():
            if isinstance(value, list):
                file.write(f"{key}: {' '.join(value)}\n")
            else:
                file.write(f"{key}: {value}\n")


# Specify input and output file names
input_file = "input_dict.txt"
output_file = "output_dict.txt"

# Read the original dictionary from the input file
original_dictionary = read_dictionary(input_file)

# Reverse the original dictionary
reversed_dict = reverse_dictionary(original_dictionary)

# Write the reversed dictionary to the output file
write_dictionary(reversed_dict, output_file)

# Print the reversed dictionary to see the output
print(reversed_dict)
