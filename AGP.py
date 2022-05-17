# Imports
import numpy as np

# Global Variables
global affine_gap_list_of_trace_back_strings
affine_gap_list_of_trace_back_strings = []

#### Global Alignment With Affine Gap Algorithm

def global_alignment_with_affine_gap(str_one, str_two, match_score, mis_match_score, gap_open_penalty, gap_extension_penalty):
    ### Assigning Variables
    str_one_len= len(str_one)
    str_two_len= len(str_two)
    match_score= match_score
    mis_match_score= mis_match_score
    gap_open_penalty= gap_open_penalty
    gap_extension_penalty= gap_extension_penalty
   
    ### Initializing A Zero Matrix
    str_one_len= len(str_one)
    str_two_len= len(str_two)
    m_output_table=np.zeros((str_one_len+1, str_two_len+1), dtype=np.int64) # one more row and column
    ix_output_table=np.zeros((str_one_len+1, str_two_len+1), dtype=np.int64) # one more row and column
    iy_output_table=np.zeros((str_one_len+1, str_two_len+1), dtype=np.int64) # one more row and column
    
    ### Trace Back Tables
    which_trace_back_table=np.zeros((str_one_len+1, str_two_len+1), dtype=np.int64) # one more row and column
    # 100 -> Go To M  Trace Back Table
    # 200 -> Go To Ix Trace Back Table
    # 300 -> Go To Iy Trace Back Table
    m_trace_back_table=np.zeros((str_one_len+1, str_two_len+1), dtype=np.int64) # one more row and column
    # 1 -> Match M   \\  -1 Mis Match M
    # 2 -> Match Ix  //  -2 Mis Match Ix
    # 3 -> Match Iy  \\  -3 Mis Match Iy
    # 12 -> Match M,Ix // -12 Mis Match M,Ix
    # 13 -> Match M,Iy \\ -13 Mis Match M,Iy
    # 23 -> Match Ix,Iy// -23 Mis Match Ix,Iy
    # 123 -> Match M,Ix,Iy \\ -123 Mis Match M,Ix,Iy
    # 77 -> Go Left
    # 88 -> Go Upward
    ix_trace_back_table=np.zeros((str_one_len+1, str_two_len+1), dtype=np.int64) # one more row and column
    # 1 -> Upper M
    # 2 -> Upper Ix
    # 12 -> M or Ix
    # 77 -> Go Left
    iy_trace_back_table=np.zeros((str_one_len+1, str_two_len+1), dtype=np.int64) # one more row and column
    # 1 -> Left M
    # 2 -> Left Iy
    # 12 -> M or Iy
    # 88 -> Go Upward
    ### Intializing First Row & Column
    
    m_output_table[0][0]= 0
    ix_output_table[0][0]= gap_open_penalty
    iy_output_table[0][0]= gap_open_penalty
    
    for index in range(1,str_one_len+1,1):
        m_output_table[index][0] = -999
        ix_output_table[index][0] = ix_output_table[index-1][0] + gap_extension_penalty
        iy_output_table[index][0] = -999
        
        # Trace Back Tables
        m_trace_back_table[index][0] = 88
        ix_trace_back_table[index][0] = 2
        iy_trace_back_table[index][0] = 88
    
    for index in range(1,str_two_len+1,1):
        m_output_table[0][index] = -999
        ix_output_table[0][index] = -999
        iy_output_table[0][index] = iy_output_table[0][index-1] + gap_extension_penalty
        
        # Trace Back Tables
        m_trace_back_table[0][index] = 77
        ix_trace_back_table[0][index] = 77
        iy_trace_back_table[0][index] = 2
#     print(m_output_table)
#     print(ix_output_table)
#     print(iy_output_table)
    
    ### Filling Three Matrices
    for index_i in range(1, str_one_len+1, 1):
        for index_j in range(1, str_two_len+1, 1):
            
            # M Output Table
            if str_one[index_i-1] == str_two[index_j-1]:
                max_value=m_output_table[index_i][index_j] = max(m_output_table[index_i-1][index_j-1]+match_score,\
                                                      ix_output_table[index_i-1][index_j-1]+match_score,\
                                                      iy_output_table[index_i-1][index_j-1]+match_score)
                if(max_value == m_output_table[index_i-1][index_j-1]+match_score):
                    if(max_value == ix_output_table[index_i-1][index_j-1]+match_score):
                        m_trace_back_table[index_i][index_j] = 12
                    elif(max_value == iy_output_table[index_i-1][index_j-1]+match_score):
                         m_trace_back_table[index_i][index_j] = 13
                    elif(max_value == ix_output_table[index_i-1][index_j-1]+match_score == iy_output_table[index_i-1][index_j-1]+match_score):
                        m_trace_back_table[index_i][index_j] = 123
                    else:
                        m_trace_back_table[index_i][index_j] = 1
                elif(max_value == ix_output_table[index_i-1][index_j-1]+match_score):
                    if(max_value == iy_output_table[index_i-1][index_j-1]+match_score):
                         m_trace_back_table[index_i][index_j] = 23
                    else:
                        m_trace_back_table[index_i][index_j] = 2
                else:
                    m_trace_back_table[index_i][index_j] = 3
                
            else:
                max_value=m_output_table[index_i][index_j] = max(m_output_table[index_i-1][index_j-1]+mis_match_score,\
                                                      ix_output_table[index_i-1][index_j-1]+mis_match_score,\
                                                      iy_output_table[index_i-1][index_j-1]+mis_match_score)
                
                ## Handling Trace Back Matrix Values
                if(max_value == m_output_table[index_i-1][index_j-1]+mis_match_score):
                    if(max_value == ix_output_table[index_i-1][index_j-1]+mis_match_score):
                        m_trace_back_table[index_i][index_j] = -12
                    elif(max_value == iy_output_table[index_i-1][index_j-1]+mis_match_score):
                         m_trace_back_table[index_i][index_j] = -13
                    elif(max_value == ix_output_table[index_i-1][index_j-1]+mis_match_score == iy_output_table[index_i-1][index_j-1]+mis_match_score):
                        m_trace_back_table[index_i][index_j] = -123
                    else:
                        m_trace_back_table[index_i][index_j] = -1
                elif(max_value == ix_output_table[index_i-1][index_j-1]+mis_match_score):
                    if(max_value == iy_output_table[index_i-1][index_j-1]+mis_match_score):
                         m_trace_back_table[index_i][index_j] = -23
                    else:
                        m_trace_back_table[index_i][index_j] = -2
                else:
                    m_trace_back_table[index_i][index_j] = -3
                    
            # Ix Output Table
            max_value=ix_output_table[index_i][index_j] = max(ix_output_table[index_i-1][index_j]+gap_extension_penalty,\
                                                   m_output_table[index_i-1][index_j]+gap_open_penalty+gap_extension_penalty)
            
            ## Handling Trace Back Matrix Values
            if(max_value==m_output_table[index_i-1][index_j]+gap_open_penalty+gap_extension_penalty):
                if(max_value==ix_output_table[index_i-1][index_j]+gap_extension_penalty):
                    ix_trace_back_table[index_i][index_j] = 12
                else:
                    ix_trace_back_table[index_i][index_j] = 1
            else:
                ix_trace_back_table[index_i][index_j] = 2
    
            # Iy Output Table
            max_value=iy_output_table[index_i][index_j] = max(iy_output_table[index_i][index_j-1]+gap_extension_penalty,\
                                                   m_output_table[index_i][index_j-1]+gap_open_penalty+gap_extension_penalty)
            
            ## Handling Trace Back Matrix Values
            if(max_value==m_output_table[index_i][index_j-1]+gap_open_penalty+gap_extension_penalty):
                if(max_value==iy_output_table[index_i][index_j-1]+gap_extension_penalty):
                    iy_trace_back_table[index_i][index_j] = 12
                else:
                    iy_trace_back_table[index_i][index_j] = 1
            else:
                iy_trace_back_table[index_i][index_j] = 2
                
    # print(m_output_table)
    # print("\n")
    # print(ix_output_table)
    # print("\n")
    # print(iy_output_table)
    # print("\n")
    # print(m_trace_back_table)
    # print("\n")
    # print(ix_trace_back_table)
    # print("\n")
    # print(iy_trace_back_table)
    # print("\n")
    # print("I AM HERE I AM HERE I AM HERE!!!")
    
    if (m_output_table[str_one_len][str_two_len] > ix_output_table[str_one_len][str_two_len]):
        if (m_output_table[str_one_len][str_two_len] > iy_output_table[str_one_len][str_two_len]):
            print("I AM HERE I AM HERE I AM HERE!!!")
            which_trace_back_table[str_one_len][str_two_len] = 100
            which_trace_back_table=affine_gap_trace_back(m_trace_back_table, ix_trace_back_table, iy_trace_back_table, which_trace_back_table, str_one_len, str_two_len, str_one, str_two)
    elif(ix_output_table[str_one_len][str_two_len] > m_output_table[str_one_len][str_two_len]):
        if (ix_output_table[str_one_len][str_two_len] > iy_output_table[str_one_len][str_two_len]):
            which_trace_back_table[str_one_len][str_two_len] = 200
            which_trace_back_table=affine_gap_trace_back(m_trace_back_table, ix_trace_back_table, iy_trace_back_table, which_trace_back_table, str_one_len, str_two_len, str_one, str_two)
    elif(iy_output_table[str_one_len][str_two_len] > m_output_table[str_one_len][str_two_len]):
        if (iy_output_table[str_one_len][str_two_len] > ix_output_table[str_one_len][str_two_len]):
            which_trace_back_table[str_one_len][str_two_len] = 300
            which_trace_back_table=affine_gap_trace_back(m_trace_back_table, ix_trace_back_table, iy_trace_back_table, which_trace_back_table, str_one_len, str_two_len, str_one, str_two)
    elif(m_output_table[str_one_len][str_two_len] == ix_output_table[str_one_len][str_two_len]):
        if(m_output_table[str_one_len][str_two_len] > iy_output_table[str_one_len][str_two_len]):
            which_trace_back_table[str_one_len][str_two_len] = 100
            which_trace_back_table=affine_gap_trace_back(m_trace_back_table, ix_trace_back_table, iy_trace_back_table, which_trace_back_table, str_one_len, str_two_len, str_one, str_two)
            which_trace_back_table[str_one_len][str_two_len] = 200
            which_trace_back_table=affine_gap_trace_back(m_trace_back_table, ix_trace_back_table, iy_trace_back_table, which_trace_back_table, str_one_len, str_two_len, str_one, str_two)
    elif(m_output_table[str_one_len][str_two_len] == iy_output_table[str_one_len][str_two_len]):
        if(m_output_table[str_one_len][str_two_len] > ix_output_table[str_one_len][str_two_len]):
            which_trace_back_table[str_one_len][str_two_len] = 100
            which_trace_back_table=affine_gap_trace_back(m_trace_back_table, ix_trace_back_table, iy_trace_back_table, which_trace_back_table, str_one_len, str_two_len, str_one, str_two)
            which_trace_back_table[str_one_len][str_two_len] = 300
            which_trace_back_table=affine_gap_trace_back(m_trace_back_table, ix_trace_back_table, iy_trace_back_table, which_trace_back_table, str_one_len, str_two_len, str_one, str_two)
    elif(ix_output_table[str_one_len][str_two_len] == iy_output_table[str_one_len][str_two_len]):
        if(ix_output_table[str_one_len][str_two_len] > m_output_table[str_one_len][str_two_len]):
            which_trace_back_table[str_one_len][str_two_len] = 200
            which_trace_back_table=affine_gap_trace_back(m_trace_back_table, ix_trace_back_table, iy_trace_back_table, which_trace_back_table, str_one_len, str_two_len, str_one, str_two)
            which_trace_back_table[str_one_len][str_two_len] = 300
            which_trace_back_table=affine_gap_trace_back(m_trace_back_table, ix_trace_back_table, iy_trace_back_table, which_trace_back_table, str_one_len, str_two_len, str_one, str_two)
    else:
            which_trace_back_table[str_one_len][str_two_len] = 100
            which_trace_back_table=affine_gap_trace_back(m_trace_back_table, ix_trace_back_table, iy_trace_back_table, which_trace_back_table, str_one_len, str_two_len, str_one, str_two)
            which_trace_back_table[str_one_len][str_two_len] = 200
            which_trace_back_table=affine_gap_trace_back(m_trace_back_table, ix_trace_back_table, iy_trace_back_table, which_trace_back_table, str_one_len, str_two_len, str_one, str_two)
            which_trace_back_table[str_one_len][str_two_len] = 300
            which_trace_back_table=affine_gap_trace_back(m_trace_back_table, ix_trace_back_table, iy_trace_back_table, which_trace_back_table, str_one_len, str_two_len, str_one, str_two)
        
        
    return m_output_table, ix_output_table, iy_output_table, which_trace_back_table


#### Trace Back Functionality

def affine_gap_trace_back(m_trace_back_table, ix_trace_back_table, iy_trace_back_table, current_trace_back_table, index_i, index_j, str_one, str_two, sequence_one_result = "", sequence_two_result = ""):
    while(index_i >= 0 or index_j >= 0):
        print(index_i, index_j)
        print(current_trace_back_table)
        if(current_trace_back_table[index_i][index_j] == 100):
            if(m_trace_back_table[index_i][index_j] == 1 or m_trace_back_table[index_i][index_j] == -1):
                sequence_one_result+=str_one[index_i-1]
                sequence_two_result+=str_two[index_j-1]
                index_i = index_i-1
                index_j = index_j-1
                current_trace_back_table[index_i][index_j] = 100
            elif(m_trace_back_table[index_i][index_j] == 2 or m_trace_back_table[index_i][index_j] == -2):
                sequence_one_result+=str_one[index_i-1]
                sequence_two_result+=str_two[index_j-1]
                index_i = index_i-1
                index_j = index_j-1
                current_trace_back_table[index_i][index_j] = 200
            elif(m_trace_back_table[index_i][index_j] == 3 or m_trace_back_table[index_i][index_j] == -3):
                sequence_one_result+=str_one[index_i-1]
                sequence_two_result+=str_two[index_j-1]
                index_i = index_i-1
                index_j = index_j-1
                current_trace_back_table[index_i][index_j] = 300
            elif(m_trace_back_table[index_i][index_j] == 77):
                sequence_one_result+="-"
                sequence_two_result+=str_two[index_j-1]
                index_i = index_i
                index_j = index_j-1
                current_trace_back_table[index_i][index_j] = 100
            elif(m_trace_back_table[index_i][index_j] == 88):
                sequence_one_result+=str_one[index_i-1]
                sequence_two_result+="-"
                index_i = index_i-1
                index_j = index_j
                current_trace_back_table[index_i][index_j] = 100
            elif(m_trace_back_table[index_i][index_j] == 12 or m_trace_back_table[index_i][index_j] == -12):
                sequence_one_to_send = sequence_one_result
                sequence_one_to_send += str_one[index_i-1]
                sequence_two_to_send = sequence_two_result
                sequence_two_to_send += str_two[index_j-1]
                current_trace_back_table[index_i-1][index_j-1] = 100
                current_trace_back_table=affine_gap_trace_back(m_trace_back_table, ix_trace_back_table, iy_trace_back_table, current_trace_back_table, index_i-1, index_j-1, str_one, str_two, sequence_one_to_send, sequence_two_to_send)
                current_trace_back_table[index_i-1][index_j-1] = 200
                current_trace_back_table=affine_gap_trace_back(m_trace_back_table, ix_trace_back_table, iy_trace_back_table, current_trace_back_table,  index_i-1, index_j-1, str_one, str_two, sequence_one_to_send, sequence_two_to_send)
                break
            elif(m_trace_back_table[index_i][index_j] == 13 or m_trace_back_table[index_i][index_j] == -13):
                sequence_one_to_send = sequence_one_result
                sequence_one_to_send += str_one[index_i-1]
                sequence_two_to_send = sequence_two_result
                sequence_two_to_send += str_two[index_j-1]
                current_trace_back_table[index_i-1][index_j-1] = 100
                current_trace_back_table=affine_gap_trace_back(m_trace_back_table, ix_trace_back_table, iy_trace_back_table, current_trace_back_table,  index_i-1, index_j-1, str_one, str_two, sequence_one_to_send, sequence_two_to_send)
                current_trace_back_table[index_i-1][index_j-1] = 300
                current_trace_back_table=affine_gap_trace_back(m_trace_back_table, ix_trace_back_table, iy_trace_back_table, current_trace_back_table,  index_i-1, index_j-1, str_one, str_two, sequence_one_to_send, sequence_two_to_send)
                break
            elif(m_trace_back_table[index_i][index_j] == 23 or m_trace_back_table[index_i][index_j] == -23):
                sequence_one_to_send = sequence_one_result
                sequence_one_to_send += str_one[index_i-1]
                sequence_two_to_send = sequence_two_result
                sequence_two_to_send += str_two[index_j-1]
                current_trace_back_table[index_i-1][index_j-1] = 200
                current_trace_back_table=affine_gap_trace_back(m_trace_back_table, ix_trace_back_table, iy_trace_back_table, current_trace_back_table, index_i-1, index_j-1, str_one, str_two, sequence_one_to_send, sequence_two_to_send)
                current_trace_back_table[index_i-1][index_j-1] = 300
                current_trace_back_table= affine_gap_trace_back(m_trace_back_table, ix_trace_back_table, iy_trace_back_table, current_trace_back_table, index_i-1, index_j-1, str_one, str_two, sequence_one_to_send, sequence_two_to_send)
                break
            elif(m_trace_back_table[index_i][index_j] == 123 or m_trace_back_table[index_i][index_j] == -123):
                sequence_one_to_send = sequence_one_result
                sequence_one_to_send += str_one[index_i-1]
                sequence_two_to_send = sequence_two_result
                sequence_two_to_send += str_two[index_j-1]
                current_trace_back_table[index_i-1][index_j-1] = 100
                current_trace_back_table=affine_gap_trace_back(m_trace_back_table, ix_trace_back_table, iy_trace_back_table, current_trace_back_table, index_i-1, index_j-1, str_one, str_two, sequence_one_to_send, sequence_two_to_send)
                current_trace_back_table[index_i-1][index_j-1] = 200
                current_trace_back_table=affine_gap_trace_back(m_trace_back_table, ix_trace_back_table, iy_trace_back_table, current_trace_back_table, index_i-1, index_j-1, str_one, str_two, sequence_one_to_send, sequence_two_to_send)
                current_trace_back_table[index_i-1][index_j-1] = 300
                current_trace_back_table=affine_gap_trace_back(m_trace_back_table, ix_trace_back_table, iy_trace_back_table, current_trace_back_table, index_i-1, index_j-1, str_one, str_two, sequence_one_to_send, sequence_two_to_send)
                break
            else:
                affine_gap_list_of_trace_back_strings.append(sequence_two_result[::-1])
                affine_gap_list_of_trace_back_strings.append(sequence_one_result[::-1])
                break
        elif(current_trace_back_table[index_i][index_j] == 200):
            if(ix_trace_back_table[index_i][index_j] == 1):
                sequence_one_result+=str_one[index_i-1]
                sequence_two_result+="-"
                index_i = index_i-1
                index_j = index_j
                current_trace_back_table[index_i][index_j] = 100
            elif(ix_trace_back_table[index_i][index_j] == 2):
                sequence_one_result+=str_one[index_i-1]
                sequence_two_result+="-"
                index_i = index_i-1
                index_j = index_j
                current_trace_back_table[index_i][index_j] = 200
            elif(ix_trace_back_table[index_i][index_j] == 77):
                sequence_one_result+="-"
                sequence_two_result+=str_two[index_j-1]
                index_i = index_i
                index_j = index_j-1
                current_trace_back_table[index_i][index_j] = 200
            elif(ix_trace_back_table[index_i][index_j] == 12):
                sequence_one_to_send = sequence_one_result
                sequence_one_to_send += str_one[index_i-1]
                sequence_two_to_send = sequence_two_result
                sequence_two_to_send += "-"
                current_trace_back_table[index_i-1][index_j-1] = 100
                current_trace_back_table=affine_gap_trace_back(m_trace_back_table, ix_trace_back_table, iy_trace_back_table, current_trace_back_table, index_i-1, index_j, str_one, str_two, sequence_one_to_send, sequence_two_to_send)
                current_trace_back_table[index_i-1][index_j-1] = 200
                current_trace_back_table=affine_gap_trace_back(m_trace_back_table, ix_trace_back_table, iy_trace_back_table, current_trace_back_table, index_i-1, index_j, str_one, str_two, sequence_one_to_send, sequence_two_to_send)
                break
            else:
                affine_gap_list_of_trace_back_strings.append(sequence_two_result[::-1])
                affine_gap_list_of_trace_back_strings.append(sequence_one_result[::-1])
                break
        elif(current_trace_back_table[index_i][index_j] == 300):
            if(iy_trace_back_table[index_i][index_j] == 1):
                sequence_one_result+="-"
                sequence_two_result+=str_two[index_j-1]
                index_i = index_i
                index_j = index_j-1
                current_trace_back_table[index_i][index_j] = 100
            elif(iy_trace_back_table[index_i][index_j] == 2):
                sequence_one_result+="-"
                sequence_two_result+=str_two[index_j-1]
                index_i = index_i
                index_j = index_j-1
                current_trace_back_table[index_i][index_j] = 300
            elif(iy_trace_back_table[index_i][index_j] == 88):
                sequence_one_result+=str_one[index_i-1]
                sequence_two_result+="-"
                index_i = index_i-1
                index_j = index_j
                current_trace_back_table[index_i][index_j] = 300
            elif(iy_trace_back_table[index_i][index_j] == 12):
                sequence_one_to_send = sequence_one_result
                sequence_one_to_send +="-"
                sequence_two_to_send = sequence_two_result
                sequence_two_to_send += str_two[index_j-1]
                current_trace_back_table[index_i-1][index_j-1] = 100
                current_trace_back_table=affine_gap_trace_back(m_trace_back_table, ix_trace_back_table, iy_trace_back_table, current_trace_back_table, index_i, index_j-1, str_one, str_two, sequence_one_to_send, sequence_two_to_send)
                current_trace_back_table[index_i-1][index_j-1] = 300
                current_trace_back_table=affine_gap_trace_back(m_trace_back_table, ix_trace_back_table, iy_trace_back_table, current_trace_back_table, index_i, index_j-1, str_one, str_two, sequence_one_to_send, sequence_two_to_send)
                break
            else:
                affine_gap_list_of_trace_back_strings.append(sequence_two_result[::-1])
                affine_gap_list_of_trace_back_strings.append(sequence_one_result[::-1])
                break
        else:
            break
   
    return current_trace_back_table