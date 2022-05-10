# Imports
import numpy as np

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
    
    # Filling First Row & Column
    for index in range(0,str_one_len+1,1):
        output_table[index][0] = index*gap_penalty
        trace_back_table[index][0] = 3
    
    for index in range(0,str_two_len+1,1):
        output_table[0][index] = index*gap_penalty
        trace_back_table[0][index] = 2
    
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
                    trace_back_table[i][j] = -1
                elif max_value == output_table[i][j-1]+gap_penalty:
                    trace_back_table[i][j] = 2
                elif max_value == output_table[i-1][j]+gap_penalty:
                    trace_back_table[i][j] = 3
                else:
                    raise ValueError("ValueError exception thrown")
    return trace_back_table

    # Trace Back Functionality


# Smith & Waterman Algorithm
def smith_waterman(str_one, str_two):
    
    # To Do: User Input Score & Penalties
    gap_penalty = -6
    mis_match_score=-2
    match_score=5
    
    # Initializing A Zero Matrix
    str_one_len = len(str_one)
    str_two_len= len(str_two)
    output_table=np.zeros((str_one_len+1, str_two_len+1), dtype=np.int64) # one more row and column
    
    #print(output_table)
    # Filling Rest Of The Table
    for i in range(1,str_one_len+1,1):
        for j in range(1,str_two_len+1,1):
            if str_one[i-1] == str_two[j-1]:
                output_table[i][j] = output_table[i-1][j-1] + match_score
            else:
                output_table[i][j] = max(output_table[i-1][j-1] + mis_match_score, output_table[i][j-1]+gap_penalty, output_table[i-1][j]+gap_penalty, 0)
    return output_table


def global_alignment_with_affine_gap():
    pass

print(needleman_wunsch("CATGT","ACGCTG"))
# test push