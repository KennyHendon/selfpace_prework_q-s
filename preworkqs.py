#question 1
#write a function that prints "Hello_USERNAME!"   USERNAME is the input




def hello_name(user_name):


   print("Hello_"+ user_name + "!")

hello_name('USERNAME')

#question 2
#write a function that prints the odd numbers, from 1-100
def first_odds():
   for n in range(1,101):
      if n%2 == 0:
       continue
      else:
         print(n)
first_odds()

#question 3
#write a function that prints the max number of any given list

def max_num_of_list(a_list):

   my_list = list(a_list)
   print(max(my_list))

max_num_of_list('123435')

#question 4
#write a functiojn to return if any given year is a leapyear

def is_a_leap_year(year):

   if int(year)%4 == 0 and int(year)%100 != 0:
      print(year + " is/was/will be a leapyear!")
   else:
      print(year + " is/was NOT (or won't be) a leapyear")

is_a_leap_year('2024')

#question 5
#write a function to see if all numbers in a list are consecutive
def is_consecutive(a_list):


   a_list = list(a_list)
   a_list.sort()
   n = int(max(a_list))
   test_numbers = []
   numbers = []
   for value in range(1,n+1):
      test_numbers.append(value)

   print(test_numbers)
   for walue in a_list:
      numbers.append(int(walue))
   print(numbers)

   if test_numbers == numbers:
      print('consec!')
   else:
      print('nope!')
   
is_consecutive('1234567')
is_consecutive('1908547')

   


   
