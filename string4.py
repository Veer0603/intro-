main_string=input("Enter string ")
sub_string=input("Enter string to remove")
if sub_string in main_string:
  result = main_string.replace(sub_string,"")
  print(f"NEW STRING : {result}")
else:
  print("NO SUBSTRING FOUND")
