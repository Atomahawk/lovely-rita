import pandas as pd
import re

#ADDRESS CLEANER
block_variations = ['bll', 'bllk','bk', 'blck' , 'bl0ck', 'bkl', 'block', 'bfk']
error_lst = []

def devoid_col(column):
    new_column = [item  for item in column if 'void' not in item]
    return new_column

def address_cleaner(text):
    try:
        #find index of first digit
        d1_index = re.search("\d", text).start()
        #find index of first non-digit
        non_d_index = re.search("\D", text[d1_index:]).start()
        #Street number lies within these two points. Limited to 4 digits to correct for data entry.
        street_num = text[d1_index:][:non_d_index][:4]
        #Assuming Street name starts with character A-Z (not true for numeric street numbers, eg 66th St)
        street_name_start_index = re.search("[a-zA-Z]", text[(d1_index + non_d_index):]).start()
        ad_rest = text[(d1_index + non_d_index+street_name_start_index):]
        address = street_num + " " + ad_rest
        #taking block codes out of address
        for var in block_variations:
            address = address.replace(var, '')
        return address
    except:
        error_lst.append(text)
        return text

## Usage Example
# devoid_ad_lst = devoid_col(pandas_column.values)
# cleaned_list = [address_cleaner(address_string) for address_string in devoid_ad_lst]
##List of errors and number or errors, usually due to no digits in address line (expect ~6%)
# print((error_lst))
# print(len(error_lst))
