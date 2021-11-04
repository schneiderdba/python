# https://jigarius.com/blog/shopify-software-developer-interview
fname = input("Enter your first name: ").upper()
lname = input("Enter your last name: ").upper()
idcode = input("Enter your ID Code (example: CAJI202002196): ").upper()
numeric_id_no_id_code = int(idcode[4:12])
first_2_chars_fname = fname[0:2].upper()
first_2_chars_lname = lname[0:2].upper()
lname_fname_chars = first_2_chars_lname + first_2_chars_fname
idcode_fist_4 = idcode[0:5].upper()
cnt_letters = len(lname_fname_chars)
err_cnt = 0

if idcode_fist_4 != idcode_fist_4:
    print("First 4 chars are not ok") 
    err_cnt +=1
for char in lname_fname_chars:
    if not char.isalpha():
        print("Invalid ID at first 4 characters")
        err_cnt += 1
        break
if cnt_letters != 4:
    print("First 4 characters are not correct")
    err_cnt += 1
if len(str(numeric_id_no_id_code)) < 8:
    print("Length of digits is not correct")
    err_cnt += 1
if err_cnt >= 1:
    print(exit)
    exit()
else:
    #print(numeric_id_no_id_code)
    res = [int(x) for x in str(numeric_id_no_id_code)]
    print(str(res))
    odd_numbers = [y for x,y in enumerate(res) if x%2 != 0]
    even_numbers = [y for x,y in enumerate(res) if x%2 == 0]
    odd_num_sum = sum(odd_numbers)
    even_num_sum = sum(even_numbers)
    #print(odd_numbers)
    #print(even_numbers)
    #print(odd_num_sum)
    #print(even_num_sum)
    diff = even_num_sum - odd_num_sum
    if diff > 0:
        print("Positive number")
    elif diff == 0:
        print("Zero")
    else:
        diff = abs(diff)
    if diff > 9:
        remainder = diff % 10
    print(diff) 