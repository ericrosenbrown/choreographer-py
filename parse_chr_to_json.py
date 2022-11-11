#To turn into JSON
# : before {
# surround in ""X"" for everything before { and :
# add , after } unless next line is }

#if next thing is }, no comma. else, comma

file_name = "in_her_prime_left"
#file_name = "simple"

file1 = open(file_name + ".chr", 'r')
Lines = file1.readlines()

json_lines = "{\n"
  
count = 0
num_moves = 0
for idx, line in enumerate(Lines):
    clean_line = line.strip()
    if ":" in clean_line: 
        split_line = clean_line .split(":")
        if '"' in split_line[1]: #don't add more
            split_val_one = split_line[1]
        else:
            split_val_one = '"' + split_line[1] + '"'
        json_line = '"' + split_line[0] + '"' + ':' + split_val_one
        try:
            if Lines[idx+1].strip() != "}":
                json_line += ","
        except:
            pass
        json_lines += json_line + "\n"
    elif "{" in clean_line :
        split_line = clean_line .split(" ")
        if "moves" in split_line[0]: #moves are not unique, and need to be given unique identifier 
            split_line_zero = split_line[0]+str(num_moves)
            num_moves += 1
        else:
            split_line_zero = split_line[0]
        json_line = '"' + split_line_zero + '"' + ': {'
        json_lines += json_line + "\n"
    elif "}" in clean_line: 
        json_line = "}"
        try:
            if Lines[idx+1].strip() != "}":
                json_line += ","
        except:
            pass
        json_lines += json_line + "\n"

json_lines += "}"
#print(json_lines)

# writing to file
text_file = open(file_name+".json", "w")
text_file.write(json_lines)