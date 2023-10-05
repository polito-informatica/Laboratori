# Esercizio 10.1.2
# Dal fondo

#  Copy the lines from one file into another so that they are in reverse
#  order.

# Read the input file name from the command line and open the input file.
input_file = 'input.txt'
in_f = open(input_file, "r", encoding='utf-8')

# Read all the lines from the input file.
lines = in_f.readlines()

# Close the input file.
in_f.close()

# Read the output file name from the command line and open the output file.
output_file = 'output.txt'
out_f = open(output_file, "w", encoding='utf-8')

# Write the lines in reverse order.
for i in range(len(lines) - 1, -1, -1):
    out_f.write(lines[i])

# Close the output file.
out_f.close()
