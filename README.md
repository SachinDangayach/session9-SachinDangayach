
# EPAI Session 9 Assignment by Sachin Dangayach

This assignment is based on the concepts of "Decorators". We have created different decorators for different tasks of the assignment.

# Below are key functions in session9.py file.

### A) Write a decorator that allows a function to run only on odd seconds

### 1. run_at_odd
function called to create a decorator. func is a non local variable.

### 2. execute
Function check's current time to see if the current time's second's value is odd or not, if odd, then only function is executed otherwise not For eg: after decorating add function, if add is called at time seconds value is 21 (odd), function will be executed while if second's value is 20(even) it will not execute add function with 1,2 as input for 1st time, the output will be: add has been called 1 times, Result: 1 + 2 = 3
### 3. @run_at_odd
Decorator to make a function run only on odd seconds

### B) Write a decorator to add log to any function
### 4. logged
function called to create a decorator. func is a non local variable for the inner function.
### 5. logger
Print the log of function with details like function name,function documentation, execution time, count of times function is called and function call representation with arguments as string. Also, update the global func_log list which is be used to verify the logging functionality For eg: after decorating add function, if add(1,2) is called, apart from result, log will be showcased like-
   ---  Log for function: add  ---
   Function documentation: add the input variables
   Function called at: 2020-09-20 20:40:08.767335+00:00
   Total time to execute: 1.9999998812636477e-07
   Function called: 1 times
   Call function add(1,2)
   Result-
   3
### 6 @logged
Decorator to make add log to a  function

### C) Write a decorator to add authentication to any function
### 7. factory_authenticate
Decorators factory to create a decorator. func is a non local variable for the inner function.
### 8. authenticate
Creates decorator through factory method for authenticating a function
### 9. inner
Call a function after it is authenticated. Otherwise display error For eg: on calling add function, if the user name is correct, then only function will result the output else it will show an error message
### 8. @factory_authenticate
Decorator to make add user authentication to a  function

### D) Decorator to add time to any function
### 10.     timer_factory
decorator factory to create a decorator.
### 11. op_countr
Calls function add, mul or div with input parameters and update a global dictionary "operation" having add, mul and div as its keys while calling the respective function. Function call updates the user specific dictionary and output the result showing how many times this function has been called.
It also calls respective function(non local variable fn) with given input and returns the output string.
For eg: on calling closure for add function with 1,2 as input for 1st time, the output will be: add has been called 1 times, Result: 1 + 2 = 3
### 12. time_it
Function to create a decorator called to decorate a function by timing it.
### 13. timer
Function check's how much time it takes on an average for n runs to execute a function. For eg: after decorating fact function for repeat = 100, we will get how much time it takes for fact function to run for any given inputs on an average for 100 runs. In this case we will get -  fact(5)
Function fact takes average run time of 2.3930000179461787e-06 for 100 iterations
### 14. @timer_factory
Decorator to make add timer to a  function

### E) Decorator Provides privilege access (has 4 parameters, based on privileges (high, mid, low, no), gives access to all 4, 3, 2 or 1 params)

### 15. prev_access
Get the records of four columns of the df based on the user 4 level of access privilege for the user. If privilege is 1, user can see only Name. if privilege is 2, user can see Name and age and like this if access if 4, user can see all four columns
### 16. access_data
 Provides the user data access based on its privilege
### 17. @ prev_access
Decorator to make privilege based call for a function

### F) Htmlize code using inbuilt singledispatch
Singledispatch creates three things, a registry, a register and a dispatch function. We have used the singledispatch from functools to create htmlizer.
### 18. htmlize
convert in html format for object type
### 19. htmlize_integral_numbers
convert in html format for int type
### 20. htmlize_real
convert in html format for float type
### 21. htmlize_decimal
convert in html format for decimal type
### 22. htmlize_sequence
convert in html format for list anf tuple type
### 23. htmlize_dict
convert in html format for dict type
### 24. htmlize_str
 convert in html format for str type
# Below are test cases functions in test_session9.py file.

### 25. test_add_is_decorator :
Test for readme exists

### 26. test_readme_contents :
Test for readme contents are more than 500 words

### 27. test_readme_proper_description :
Test for all important functions/class described well in your README.md file

### 28. test_readme_file_for_formatting :
Test for readme formatting

### 29. test_indentations :
Test for source code formatting. No tabs but four spaces are used for indentation

### 30. test_function_name_had_cap_letters :
Test for no function is with capitals in source code

### 31. test_add_is_decorator:
Test to check the docstr_len_check is a closure

### 32. test_decorator_has_called_func_docstring :
Test to check the decorator has doc string

### 33.test_decorator_called_at_odd_sec:
Test to check the decorator changed function to be called at odd seconds only

### 34. test_add_logged_is_decorator :
Test to check the add has closure attribute which is required to get Decorator

### 35. test_add_logged :
Test to check the add_logged is working and its logs are generated we are also inserting the logs in global log list(func_log) to check whether the count for log is increasing when the function is called

### 36. test_authenticate :
check the decorator @authenticate is validating user credentials before calling a function

### 37. test_timer :
Create a decorator, which when added to any function can execute it given number of times and return the results and gives back the average runtime based for given number of runs

### 38. test_privilege_access :
Create a decorator, which when added to any function allows to let the user access a database based on the privilege user has got. To demonstrate the functionality, we have used a user class to create 4 different users with different privileges, 1 being lowest and 4 being highest. We have created a pandas dataframe to store data of four patients with details of  name, age, bood_group and Covid_Infected.
Rules ->
    The user named HOD, created with privilege 4 should be able to access all 4 columns
    The user named Doctor, created with privilege 3 should be able to access first 3 columns as we don't want doctor to be biased against covid patients
    The user named nurse, created with privilege 2 should be able to access first 2 columns only
    The user named accountant, created with privilege 1 should be able to access first column to get the patients id for billing purpose
    we have access_records which is decorated with privilege access and it returns only the data based on users privilege

### 39. test_singledispatch :
singledispatch creates three things, a registry, a register and a dispatch function. We have used the singledispatch from functools to create htmlizer. We will test the htmlizer is converting the code properly or not.
to check the valid update for counters in user specific dictionary for alternative approach
