import sys

#Check number of arguments
if (len(sys.argv) <= 2 ):
 print("Number of arguments are exactly two")
 exit(1)
if (len(sys.argv) > 3 ):
 print("Don't specify more than two argument")
 exit(1)
else:
 #print("We are good with number of params")
  pass
passed_obj=sys.argv[1]
passed_key=sys.argv[2]

#print('Passed Object is',passed_obj)
#print('Passed Key is',passed_key)

split_key = passed_key.split('/')
#print('Separated key is : ', split_key)


Formed_obj = "{"+split_key[0]+":{"+split_key[1]+":{"+split_key[2]+":"
#print('Partial formed object with provided key is : ', Formed_obj)

if Formed_obj in passed_obj:
    print('Found!')
    value_str = passed_obj.partition(Formed_obj)[2]   #Partition passed object and formed object (formed from provided key)
    #print('Value is in : ', value_str)
    value = value_str.split('}')[0]                   #Retrieve everything before first closing brace } from value string 
    print('Value of given object is',value)
	
else:
    print('Not found!')
