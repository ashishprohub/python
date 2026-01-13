'''Write a program to find out whether a student has passed or failed if it requires a 
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
take marks as an input from the user.'''

sub1 = int(input("Enter marks obtained in sub1:"))
max1 = int(input("Enter maximum marks of sub1:"))
sub2 = int(input("Enter marks obtained in sub2:"))
max2 = int(input("Enter maximum marks of sub2:"))
sub3 = int(input("Enter marks obtained in sub3:"))
max3 = int(input("Enter maximum marks of sub3:"))
total_obtained = sub1 + sub2 + sub3
total_maxm = max1 + max2 + max3
if(sub1/max1 >= 0.33 and sub2/max2 >= 0.33 and sub3/max3 >=0.33 and total_obtained/total_maxm >= 0.4):
    print("You're passed in exam")
else:
    print("You're failed in exam")