"""
Author: Darrien Guan
Date: November 1, 2023
Discription: Improved version of the bubble sort algorithm
with improved efficiency and execution time. (Classic leet code problem :) )
"""

def bubble_sort(num_list):
    '''Classic bubble sort algorithm, numbers are sorted in list smallest to greatest.'''
    
    # Number of iterations
    iterations = 0
    
    for pass_num in range(1, len(num_list)):

        # Boolean for whether list is already sorted.
        swap_stat = False
        
        for index in range(len(num_list)-1):
            iterations += 1
            if num_list[index] > num_list[index+1]:
                
                temp = num_list[index]
                num_list[index] = num_list[index+1]
                num_list[index+1] = temp
                swap_stat = True
        
        # Stops loop if already fully sorted.
        if not swap_stat:
            break
        
    return num_list, iterations

def main():
    '''main logic'''
    
    # Example list
    num_list = [23,4,73,4,8,24,1,2,3]
    
    # Call buble sort with num_list param. Display sorted result.
    sorted_list = bubble_sort(num_list)
    print(f"Sorted list: {sorted_list[0]}, Iterations: {sorted_list[1]}")
    
main()