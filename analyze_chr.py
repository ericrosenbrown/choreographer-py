import json
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
from matplotlib.pyplot import figure
import pdb
  
# Opening JSON file
file_name_right = "in_her_prime_right"
f_right = open(file_name_right+".json")
  
# returns JSON object as 
# a dictionary
data_right = json.load(f_right)
f_right.close()

# Opening JSON file
file_name_left = "in_her_prime_left"
f_left = open(file_name_left+".json")
  
# returns JSON object as 
# a dictionary
data_left = json.load(f_left)
f_left.close()

ignore_moves = ['set_color']
arm_moves = ['arm_move','stow','figure8_move']
body_moves = ['stand_up', 'crawl', 'body_hold','goto','random_rotate','body_const','animation','butt_circle','pace','sit']

#Histogram of move types used
move_types_count = defaultdict(lambda : 0)
#Number of move slices per move
move_types_slices = defaultdict(lambda : [])
#Number of move types used for movement
arm_body_count = {"arm":0, "body": 0}

#Plot 2D position of where robot was
#When robot was synchronized or not based on start/end slices

for key in data_right['choreography_sequence']:
    if "moves" in key:
        move_entry = data_right['choreography_sequence'][key]
        if  move_entry['type'] not in ignore_moves:
            move_types_count[move_entry['type']] += 1
            move_types_slices[move_entry['type']].append(float(move_entry['requested_slices'].strip()))
            if move_entry['type'] in arm_moves:
                arm_body_count['arm'] += 1
            elif move_entry['type'] in body_moves:
                arm_body_count['body'] += 1


#Histogram of move types used
figure(figsize = (25, 6), dpi = 100)
plt.bar(move_types_count.keys(), move_types_count.values(), color ='maroon',
        width = 0.4)
 
plt.xlabel("Move Types")
plt.ylabel("No. times used")
plt.title("How Often Move Types Were Used")
plt.savefig('move_type_counts.pdf')
plt.show()

#Number of move slices per move
#Compute averages for each
av_move_types_slices = {}
std_move_types_slices = {}
for key in move_types_slices.keys():
    print(move_types_slices[key])
    av = np.average(move_types_slices[key])
    std = np.std(move_types_slices[key])
    av_move_types_slices[key] = av
    std_move_types_slices[key] = std

figure(figsize = (25, 6), dpi = 100)
# plt.bar(av_move_types_slices.keys(), av_move_types_slices.values(), color ='maroon',
#         width = 0.4, yerr=std_move_types_slices.values())

plt.bar(av_move_types_slices.keys(), av_move_types_slices.values(), color ='maroon',
        width = 0.4)

plt.xlabel("Move Types")
plt.ylabel("Average No. of time slices")
plt.title("How Long Move Types Were Used")
plt.savefig('move_type_times.pdf')
plt.show()

#Histogram of arm/moves usage

plt.bar(arm_body_count.keys(), arm_body_count.values(), color ='maroon',
        width = 0.4)

plt.xlabel("Number of arm vs. body moves")
plt.ylabel("No. times used")
plt.title("How Often Arm/Body Types Were Used")
plt.savefig('arm_body_counts.pdf')
plt.show()