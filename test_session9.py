import pytest
import random
import string
import session9
import os
import inspect
import re
from functools import reduce
from functools import singledispatch
from numbers import Integral
from collections.abc import Sequence
from decimal import Decimal
import pandas as pd

README_CONTENT_CHECK_FOR = [ # not needed to check as these are not required to be named similar
    '@timer_factory',
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    """get file content"""
    readme = open("README.md", "r", encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session9)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session9, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


############################## session9 Validations#############################

# TODO: 1 Test the function to run only on odd seconds
def test_add_is_decorator():
    """
    Test to check the add has closure attribute which is required to get Decorator
    """
    assert hasattr(session9.add, '__closure__'), "add is not a valid closure"

def test_decorator_has_called_func_docstring():
    """
    Test to check the decorator has doc string
    """
    assert session9.__doc__, "Decorator is missing original function documentation"

def test_decorator_called_at_odd_sec():
    """
    Test to check the decorator changed function to be called at odd seconds only
    """
    for _ in range(1000):
     result = session9.add(1)

    assert result != 1000, "add is not only called at odd seconds"

# TODO: 2 Test Decorator to add log to any function
def test_add_logged_is_decorator():
    """
    Test to check the add has closure attribute which is required to get Decorator
    """
    assert hasattr(session9.add_logged, '__closure__'), "add_logged is not a valid decorator"

def test_add_logged():
    """
    Test to check the add_logged is working and its logs are generated
    we are also inserting the logs in global log list(func_log) to check whether the
    count for log is increasing when the function is called
    """
    for _ in range(5):
        session9.add_logged(1,2)

    assert len(session9.func_log)==5, "add_logged is not generating logs as expected"


# TODO: 3 Test decorator to add authentication to any function.
def test_authenticate():
    """
    check the decorator @authenticate is validating user credentials before
    calling a function
    """
# We will use class named users to generate a user object with previlage and password.
    user = session9.Users('test1','password1','1')
    # we have created two users objects and used their correct and incorrect
    # credentials to create to decorated functions named
    @session9.factory_authenticate(user.get_password(),'a1bc')
    def add_auth_f(*args):
        """add the input variables"""
        return(sum(args))
    @session9.factory_authenticate(user.get_password(),'password1')
    def add_auth_p(*args):
        """add the input variables"""
        return(sum(args))

    # incorrect user password
    with pytest.raises(ValueError, match=r".*are not authenticated to use'*"):
        result1 = add_auth_f(1,2)

    # correct user password
    result2 = add_auth_p(1,2)
    assert result2 == 3, "Decorater to add authentication is not working as expected"

# TODO: 4 Test decorator to add timer to any function.
def test_timer():
    """
    Create a decorator, which when added to any function can execute it given number
    of times and return the results and gives back the average runtime based for given
    number of runs
    """
    n = random.randint(1,10)
    @session9.timer_factory(n)
    def fact(n:int)->int:
        """Factorial of a numer"""
        from operator import mul
        from functools import reduce
        return reduce(mul, range(1, n+1))

    result, avg_time = fact(5)
    assert avg_time != 0 and result == 120, "Decorater to add timer function is not working as expected"


# TODO: 5 Test decorator to Provides privilege access (has 4 parameters, based on privileges (high, mid, low, no), gives access to all 4, 3, 2 or 1 params)
def test_privilege_access():
    """
    Create a decorator, which when added to any function allows to let the user access
    a database based on the previlege user has got.
    To demonstarate the functionality, we have used a user class to create 4 different
    users with different privileges, 1 being lowest and 4 being highest.

    We have created a pandas dataframe to store data of four patients with details of
    name, age, bood_group and Covid_Infected.
    Rules ->
    The user named HOD, created with previlage 4 should be able to access all 4 columns
    The user named Doctor, created with previlage 3 should be able to access first 3 columns as we don't want doctor to be baised against covid patients
    The user named nurse, created with previlage 2 should be able to access first 2 columns only
    The user named accountant, created with previlage 1 should be able to access first column to get the patients id for billing purpose

    we have access_records which is decorated with privilege access and it returns only the data based on users privilege
    """
    # Health data of patients
    data = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':[20, 21, 19, 18], 'Blood_Group':['O+','B+','A-','B-'],'Covid_Infected':['Y','N','N','Y']}
    # Create DataFrame of data of patients
    df = pd.DataFrame(data)

    # Create decorated function
    @session9.prev_access
    def access_records(user,df):
        """
        print and return records of dataframe
        Inputs:
            df: dataframe
        """
        print(df)
        return df

    # Correct credentials
    accountant = session9.Users('abc1','password1','1')
    acc_df = access_records(accountant,df)
    assert acc_df.shape[1] == 1, "Decorater to add previlage function is not working as expected"

    nurse = session9.Users('abc2','password2','2')
    acc_df1 = access_records(nurse,df)
    assert acc_df1.shape[1] == 2, "Decorater to add previlage function is not working as expected"

    doctor = session9.Users('abc3','password3','3')
    acc_df2 = access_records(doctor,df)
    assert acc_df2.shape[1] == 3, "Decorater to add previlage function is not working as expected"

    hod = session9.Users('abc3','password4','4')
    acc_df3 = access_records(hod,df)
    assert acc_df3.shape[1] == 4, "Decorater to add previlage function is not working as expected"

    # Incorrect credentials
    acc_fraud = session9.Users('abc5','password101','1')
    acc_df_fraud = access_records(acc_fraud,df)
    assert acc_df_fraud.shape[1] != 2, "Decorater to add previlage function is not working as expected"


# TODO: 5 Test singledispatch to htmlize the code
def test_singledispatch():
    """
    singledispatch creates three things, a registry, a register and a dispatch fucntion.
    We have used the singledispatch from functools to create htmlizer. We will test the
    htmlizer is converting the code properly or not
    """

    # for int
    assert session9.htmlize(1) == '1(<i>0x1</i>)', 'singledispatch to htmlize is not working as expected for Integral'
    # for float
    assert session9.htmlize(1.1) == '1.1', 'singledispatch to htmlize is not working as expected for float types'
    # for list  and tuple
    assert session9.htmlize((1,2)) == '<ul>\n<li>1(<i>0x1</i>)</li>\n<li>2(<i>0x2</i>)</li>\n</ul>', 'singledispatch to htmlize is not working as expected for list and tuple'
    # for Decimal
    a = Decimal('1.4535')
    assert session9.htmlize(1.4535) == '1.45', 'singledispatch to htmlize is not working as expected for decimal type'
    # for dict
    assert session9.htmlize({'a':1,'b':2}) == '<ul>\n<li>a=1</li>\n<li>b=2</li>\n</ul>', 'singledispatch to htmlize is not working as expected for dic types'
