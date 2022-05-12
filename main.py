# Imports
import numpy as np

# Global Variables
global needleman_wunsch_list_of_trace_back_strings
global smith_waterman_list_of_trace_back_strings
needleman_wunsch_list_of_trace_back_strings = []
smith_waterman_list_of_trace_back_strings = []

# Needleman-Wunsch Algorithm
def needleman_wunsch(str_one, str_two):
    
    # To Do: User Input Score & Penalties
    gap_penalty = -1
    mis_match_score=-1
    match_score=2
    
    # Initializing A Zero Matrix
    str_one_len = len(str_one)
    str_two_len= len(str_two)
    output_table=np.zeros((str_one_len+1, str_two_len+1), dtype=np.int64) # one more row and column
    trace_back_table=np.zeros((str_one_len+1, str_two_len+1), dtype=np.int64) # one more row and column
    
    # 1 -> diagonal match
    # -1 -> diagonal mismatch
    # 2 -> left gap
    # 3 -> upper gap
    # -12 -> either diagonal or left directions
    # -13 -> either diagonal or upper directions
    # 23 -> either left or upper directions
    
    # Filling First Row & Column
    for index in range(0,str_one_len+1,1):
        output_table[index][0] = index*gap_penalty
        trace_back_table[index][0] = 3
    
    for index in range(0,str_two_len+1,1):
        output_table[0][index] = index*gap_penalty
        trace_back_table[0][index] = 2
        
    trace_back_table[0][0] = 0
    
    #print(output_table)
    # Filling Rest Of The Table
    for i in range(1,str_one_len+1,1):
        for j in range(1,str_two_len+1,1):
            if str_one[i-1] == str_two[j-1]:
                output_table[i][j] = output_table[i-1][j-1] + match_score
                trace_back_table[i][j] = 1 
            else:
                max_value=output_table[i][j] = max(output_table[i-1][j-1] + mis_match_score, output_table[i][j-1]+gap_penalty, output_table[i-1][j]+gap_penalty)
                if max_value == output_table[i-1][j-1] + mis_match_score:
                    if max_value == output_table[i][j-1]+gap_penalty:
                        trace_back_table[i][j] = -12
                    elif max_value == output_table[i-1][j]+gap_penalty:
                        trace_back_table[i][j] = -13
                    else:
                        trace_back_table[i][j] = -1
                elif max_value == output_table[i][j-1]+gap_penalty:
                    if max_value == output_table[i-1][j]+gap_penalty:
                        trace_back_table[i][j] = 23
                    else:
                        trace_back_table[i][j] = 2
                elif max_value == output_table[i-1][j]+gap_penalty:
                    trace_back_table[i][j] = 3
                else:
                    raise ValueError("ValueError exception thrown")

#     print(trace_back_table)
    trace_back_indices=np.zeros((str_one_len+1, str_two_len+1), dtype=np.int64) # one more row and column
    trace_back_indices=trace_back_functionality_nw(trace_back_table,trace_back_indices, str_one, str_two, str_one_len, str_two_len)
    trace_back_indices[0][0] = 1
#     print(trace_back_indices)
    return output_table, trace_back_indices
    
    
    
    # Trace Back Functionality
def trace_back_functionality_nw(trace_back_table, trace_back_indices,str_one, str_two, i_index, j_index,  sequence_one_result = "", sequence_two_result = ""):
    
    while(i_index >= 0 or j_index >= 0):
        if trace_back_table[i_index][j_index] == 1:
            trace_back_indices[i_index][j_index] = 1
            sequence_one_result+=str_one[i_index-1]
            sequence_two_result+=str_two[j_index-1]
            i_index = i_index-1
            j_index = j_index-1
        elif trace_back_table[i_index][j_index] == -1:
            trace_back_indices[i_index][j_index] = 1
            sequence_one_result+=str_one[i_index-1]
            sequence_two_result+=str_two[j_index-1]
            i_index = i_index-1
            j_index = j_index-1
        elif trace_back_table[i_index][j_index] == 2:
            trace_back_indices[i_index][j_index] = 1
            sequence_one_result+="-"
            sequence_two_result+=str_two[j_index-1]
            i_index = i_index
            j_index = j_index-1
        elif trace_back_table[i_index][j_index] == 3:
            trace_back_indices[i_index][j_index] = 1
            sequence_one_result+=str_one[i_index-1]
            sequence_two_result+="-"
            i_index = i_index-1
            j_index = j_index
        elif trace_back_table[i_index][j_index] == -12:
            trace_back_indices[i_index][j_index] = 1
            sequence_one_to_send = sequence_one_result
            sequence_one_to_send += str_one[i_index-1]
            sequence_two_to_send = sequence_two_result
            sequence_two_to_send += str_two[j_index-1]
            trace_back_indices=trace_back_functionality_nw(trace_back_table, trace_back_indices, str_one, str_two, i_index-1, j_index-1, sequence_one_to_send, sequence_two_to_send)
            sequence_one_to_send = sequence_one_result
            sequence_one_to_send +="-"
            sequence_two_to_send = sequence_two_result
            sequence_two_to_send += str_two[j_index-1]
            trace_back_indices=trace_back_functionality_nw(trace_back_table, trace_back_indices, str_one, str_two, i_index, j_index-1, sequence_one_to_send, sequence_two_to_send)
            break
        elif trace_back_table[i_index][j_index] == -13:
            trace_back_indices[i_index][j_index] = 1
            sequence_one_to_send = sequence_one_result
            sequence_one_to_send += str_one[i_index-1]
            sequence_two_to_send = sequence_two_result
            sequence_two_to_send += str_two[j_index-1]
            trace_back_indices=trace_back_functionality_nw(trace_back_table, trace_back_indices, str_one, str_two, i_index-1, j_index-1, sequence_one_to_send, sequence_two_to_send)
            sequence_one_to_send = sequence_one_result
            sequence_one_to_send += str_one[i_index-1]
            sequence_two_to_send = sequence_two_result
            sequence_two_to_send += "-"
            trace_back_indices=trace_back_functionality_nw(trace_back_table, trace_back_indices, str_one, str_two, i_index-1, j_index, sequence_one_to_send, sequence_two_to_send)
            break
        elif trace_back_table[i_index][j_index] == 23:
            trace_back_indices[i_index][j_index] = 1
            sequence_one_to_send = sequence_one_result
            sequence_one_to_send +="-"
            sequence_two_to_send = sequence_two_result
            sequence_two_to_send += str_two[j_index-1]
            trace_back_indices=trace_back_functionality_nw(trace_back_table, trace_back_indices, str_one, str_two, i_index, j_index-1, sequence_one_to_send, sequence_two_to_send)
            sequence_one_to_send = sequence_one_result
            sequence_one_to_send += str_one[i_index-1]
            sequence_two_to_send = sequence_two_result
            sequence_two_to_send += "-"
            trace_back_indices=trace_back_functionality_nw(trace_back_table, trace_back_indices, str_one, str_two, i_index-1, j_index, sequence_one_to_send, sequence_two_to_send)
            break
        else:
#             print(sequence_one_result[::-1])
#             print(sequence_two_result[::-1])
            needleman_wunsch_list_of_trace_back_strings.append(sequence_one_result[::-1])
            needleman_wunsch_list_of_trace_back_strings.append(sequence_two_result[::-1])
            break
            
    return trace_back_indices


# Smith & Waterman Algorithm
def smith_waterman(str_one, str_two):
    
    # To Do: User Input Score & Penalties
    gap_penalty = -1
    mis_match_score=-1
    match_score=1
    
    # Initializing A Zero Matrix
    str_one_len = len(str_one)
    str_two_len= len(str_two)
    output_table=np.zeros((str_one_len+1, str_two_len+1), dtype=np.int64) # one more row and column
    trace_back_table=np.zeros((str_one_len+1, str_two_len+1), dtype=np.int64) # one more row and column
    # 1 -> diagonal
    # 2 -> left gap
    # 3 -> upper gap
    # 12 -> either diagonal or left directions
    # 13 -> either diagonal or upper directions
    # 23 -> either left or upper directions
    # Filling Rest Of The Table
    
    current_max_value = -1
    max_value = 0
    start_i_index = -1
    start_j_index = -1
    for i in range(1,str_one_len+1,1):
        for j in range(1,str_two_len+1,1):
            if str_one[i-1] == str_two[j-1]:
                max_value=output_table[i][j] = output_table[i-1][j-1] + match_score
                trace_back_table[i][j] = 1
            else:
                max_value=output_table[i][j] = max(output_table[i-1][j-1] + mis_match_score, output_table[i][j-1]+gap_penalty, output_table[i-1][j]+gap_penalty, 0)
                if max_value == output_table[i-1][j-1] + mis_match_score:
                    if max_value == output_table[i][j-1]+gap_penalty:
                        trace_back_table[i][j] = 12
                    elif max_value == output_table[i-1][j]+gap_penalty:
                        trace_back_table[i][j] = 13
                    else:
                        trace_back_table[i][j] = 1
                elif max_value == output_table[i][j-1]+gap_penalty:
                    if max_value == output_table[i-1][j]+gap_penalty:
                        trace_back_table[i][j] = 23
                    else:
                        trace_back_table[i][j] = 2
                elif max_value == output_table[i-1][j]+gap_penalty:
                    trace_back_table[i][j] = 3
                else:
                    trace_back_table[i][j] = 0
            if max_value > current_max_value:
                current_max_value = max_value
                start_i_index = i
                start_j_index = j
                
#     print(start_i_index,start_j_index)
#     print(output_table)
#     print(trace_back_table)
    trace_back_indices=np.zeros((str_one_len+1, str_two_len+1), dtype=np.int64) # one more row and column
    trace_back_indices=trace_back_functionality_sw(trace_back_table, trace_back_indices, str_one, str_two, start_i_index, start_j_index)
#     print(trace_back_indices)
    return output_table, trace_back_indices



# Trace Back Functionality
def trace_back_functionality_sw(trace_back_table, trace_back_indices, str_one, str_two, i_index, j_index,  sequence_one_result = "", sequence_two_result = ""):
    while(trace_back_table[i_index][j_index] != 0):
        if trace_back_table[i_index][j_index] == 1:
            trace_back_indices[i_index][j_index] = 1
            sequence_one_result+=str_one[i_index-1]
            sequence_two_result+=str_two[j_index-1]
            i_index = i_index-1
            j_index = j_index-1
        elif trace_back_table[i_index][j_index] == 2:
            trace_back_indices[i_index][j_index] = 1
            sequence_one_result+="-"
            sequence_two_result+=str_two[j_index-1]
            i_index = i_index
            j_index = j_index-1
        elif trace_back_table[i_index][j_index] == 3:
            trace_back_indices[i_index][j_index] = 1
            sequence_one_result+=str_one[i_index-1]
            sequence_two_result+="-"
            i_index = i_index-1
            j_index = j_index
        elif trace_back_table[i_index][j_index] == 12:
            trace_back_indices[i_index][j_index] = 1
            sequence_one_to_send = sequence_one_result
            sequence_one_to_send += str_one[i_index-1]
            sequence_two_to_send = sequence_two_result
            sequence_two_to_send += str_two[j_index-1]
            trace_back_indices=trace_back_functionality_sw(trace_back_table, trace_back_indices, str_one, str_two, i_index-1, j_index-1, sequence_one_to_send, sequence_two_to_send)
            sequence_one_to_send = sequence_one_result
            sequence_one_to_send +="-"
            sequence_two_to_send = sequence_two_result
            sequence_two_to_send += str_two[j_index-1]
            trace_back_indices=trace_back_functionality_sw(trace_back_table, trace_back_indices, str_one, str_two, i_index, j_index-1, sequence_one_to_send, sequence_two_to_send)
            break
        elif trace_back_table[i_index][j_index] == 13:
            trace_back_indices[i_index][j_index] = 1
            sequence_one_to_send = sequence_one_result
            sequence_one_to_send += str_one[i_index-1]
            sequence_two_to_send = sequence_two_result
            sequence_two_to_send += str_two[j_index-1]
            trace_back_indices=trace_back_functionality_sw(trace_back_table, trace_back_indices, str_one, str_two, i_index-1, j_index-1, sequence_one_to_send, sequence_two_to_send)
            sequence_one_to_send = sequence_one_result
            sequence_one_to_send += str_one[i_index-1]
            sequence_two_to_send = sequence_two_result
            sequence_two_to_send += "-"
            trace_back_indices=trace_back_functionality_sw(trace_back_table, trace_back_indices, str_one, str_two, i_index-1, j_index, sequence_one_to_send, sequence_two_to_send)
            break
        elif trace_back_table[i_index][j_index] == 23:
            trace_back_indices[i_index][j_index] = 1
            sequence_one_to_send = sequence_one_result
            sequence_one_to_send +="-"
            sequence_two_to_send = sequence_two_result
            sequence_two_to_send += str_two[j_index-1]
            trace_back_indices=trace_back_functionality_sw(trace_back_table, trace_back_indices, str_one, str_two, i_index, j_index-1, sequence_one_to_send, sequence_two_to_send)
            sequence_one_to_send = sequence_one_result
            sequence_one_to_send += str_one[i_index-1]
            sequence_two_to_send = sequence_two_result
            sequence_two_to_send += "-"
            trace_back_indices=trace_back_functionality_sw(trace_back_table, trace_back_indices, str_one, str_two, i_index-1, j_index, sequence_one_to_send, sequence_two_to_send)
            break
        else:
            break
    
#     print(sequence_one_result[::-1])
#     print(sequence_two_result[::-1])
    smith_waterman_list_of_trace_back_strings.append(sequence_one_result[::-1])
    smith_waterman_list_of_trace_back_strings.append(sequence_two_result[::-1])
    
    if(trace_back_table[i_index][j_index] == 0):
        trace_back_indices[i_index][j_index] = 1
    
    return trace_back_indices



x,y=needleman_wunsch("CATGT","ACGCTG")
x,y = smith_waterman("GCGATATA","AACCTATAGCT")
print(needleman_wunsch_list_of_trace_back_strings)
print(smith_waterman_list_of_trace_back_strings)