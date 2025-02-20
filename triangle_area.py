# FILE NAME - triangle_area.py
# DRG - Rerun for points 2025-02-18-2343
# NAME: Dan Stiglitz
# DATE: 2/19/25
# BRIEF DESCRIPTION:  Area of a Triangle Lab



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions below
# 4. The Sample Output has been included in this code for your convenience





########## ENTER YER CODE BELOW THIS LINE ##########
    
def triangle_area_bh(base, height):
  return (1/2) * base * height

height =float(input('Enter the height: '))
base = float(input('Enter the base: '))
area = triangle_area_bh(base, height)
print()
print(f'The area of the triangle is {area}')






    
    
    
    
    
    
########### END YER CODE ABOVE THIS LINE ###########





########################################
#          SAMPLE OUTPUT
########################################

'''

Enter the height: 1
Enter the base: 1

The area of the triangle is 0.5

'''



'''

Enter the height: 8
Enter the base: 4

The area of the triangle is 16.0

'''



########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is the flow of the program? Which line of code kicks off the process?

Creating the function sets the parameters for the script to calculate the area and then the user input calls that function



2. What was the hardest part of this lab?
figuring out the exact way for the output to show up, with the blank line in between it. I am definitely struggling with the exactness of these, 
I am used to having multiple ways to do things and being excited to see how my students have come up with alternatives, but it's the exactness that
helps to clarify how things work in here. 




'''
