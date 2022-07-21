# dictionary word lookup
import sys
phone_list = { str('John'):'212-321-2301',str('Kate'):'292-210-3941',str('Tony'):'391-310-2313'}
lookup = str(input("Lookup: "))
for keys in phone_list:
    if str(keys) in lookup:
        print(lookup+"'s phone number \n[", phone_list[lookup],"]")
        #this code basically tells program to exit after finding specific
        #not sure if it's the best
        sys.exit(0)
    '''    
    elif "Tony" in lookup:
        print("Welcome master.")
        print(lookup+"'s phone number:", phone_list[lookup])
        sys.exit(0)
    '''
try:
    print(lookup+"'s phone number:", phone_list[lookup])
except KeyError:
    print("Invalid ID")
        
   
