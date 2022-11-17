# Title of the program - 			Near Miss

# Name of the program - 			miss.py

# External files used in this program - 	NA 

# list of external files - 		NA

# Names of Programmers - 			Eshwar Chatelli, Neelima vuyyuru

# Email address of the Programmers - 	Eshwar Chatelli = eshwarchatelli@lewisu.edu , Neelima vuyyuru = neelimavuyyuru@lewisu.edu

# Course Number - 			CPSC 60500

# Section Number - 			5

# Date - 					11/11/2022

# Explanation - 				The fermat's last theorem is used in this program to calculate the "near miss" of the program using the formulas. the values of the n and k are 
# 					asked by the user to enter it and then it will calculate the near miss.
		
# 					Step 1:

# 						the user is asked to enter the values of n that will be between 2 to 12
# 						if the user enters more than 12 or less than 2 it will ask one more time to enter the values.

# 					Step 2:

# 						the next step is to enter the value of k and the value of k should be more than 10.
# 						if the user enters below 10 then the program ask one more time to enter the value.

# 					step 3:

# 						if the user enters greater values, then the program displays the error message like "Overflow!!!"

# 					Step 4:

# 						after these process, the program displays the values of x,y,z, miss and relative miss.


# Resources used to complete program - 	NA 


def main():
    # intialising the n value as 1
    n=1 
    while ((n <= 2) or (n >= 12)):
        n= int(input("Enter integer n such that 2 < n < 12 ===> ")) # placing the n value in between 2 and 12
    # intialising the k value as 1   
    k=1 
    # iterating the loop while k is less than 10
    while k <= 10: 
            k= int(input("Enter upper limit k for x and y (k > 10) ===> ")) 
            #if loop is used to set the error message for values 
            if n >= 10:
                print("OVERFLOW ERROR!!!! Choose lower values of n and k")
                #After error it will return to exit 
                return 
    # intialising the past miss is equal to None
    past_miss=None 
    # the x value is in the range of 10 to k+1
    for x in range(10, k+1): 
        # the y value is in the range of x value  to  k+1
        for y in range(x,k+1): 
            xysum_pow = pow(x, n) + pow(y, n)
            z = int(pow(xysum_pow, 1/n))
            z_pow = pow(z, n)
            z1_pow = pow(z+1, n)
            miss = min( xysum_pow - z_pow, z1_pow - xysum_pow)
            relative_miss_temp = miss / xysum_pow
            relative_miss = relative_miss_temp
            print("\nx = {}      y = {}      z = {}       Miss = {}      Relative Miss = {}%".format(x, y, z, miss, round(relative_miss*100,2)))
                    
if __name__ == '__main__':
    main()
