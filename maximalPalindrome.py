# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 13:14:38 2020

@author: Rokas
"""

import numpy as np
import math

# SPAUSDINIMUS REIKIA UZKOMENTUOTI, NES SULETINA IR 30 TESTU NEPRAEINA, O TIK 26

def maximalPalindrome(s):
    
    s_list = list(s)
    #print(s_list)
    
    s_list.sort()
    #print('>', s_list)
    
    unique_list = list(set(s_list))
    unique_list.sort()
    #print('>>', unique_list)
    
    odd_letter = []
    letter_times = []
    half_pol_left = []
    
    s_arr = np.array(s_list)
    #print(s_arr)
    
    for unique in unique_list:
        ind_letter = np.where(s_arr == unique)
        times = len(ind_letter[0])
        
        if times%2 == 1:
            odd_letter.append(unique)
        letter_times.append(unique)
        
        if times > 1:
            half_pol_left.extend(list(unique * (times//2))) # 3//2=1
    
    half_pol_right = sorted(half_pol_left, reverse = True)
    
    if len(odd_letter) > 0:
        palindrome = half_pol_left + list(odd_letter[0]) + half_pol_right
    else:
        palindrome = half_pol_left + half_pol_right

    palindrome_last = "".join(palindrome)    
    #print(palindrome_last)
    
    return palindrome_last

        