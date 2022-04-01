# a-z , alphabet in small case
# 0-9, 
#(.)(_), occure in one time
# (@) , occure in one time
# (.), in 2nd or 3rd position from right to left

import re # importing regex 
email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w +[.]\w{2,3}$"
# for start (^), (+) for merging condition,(\)for searching, (?)True(0) or False(1), 
# \w for searching special character within string, {} for searching in particular postion, ($) for searching from right to left.  
user_email=input('Enter your mail:')
if re.search(email_condition, user_email):
 print(" Right Email")
else:
 print("Wrong Email")