"""Assignment for session 9 based on Decorators"""
import pandas as pd

class Users:
    """
    This class is to create a user,
    set the user password and s
    provide methods to get the password and privileges
    """
    def __init__(self, uid, password, privilege):
        """
        create user
        Inputs:
            uid: user id
            password: password for the user
            privileges: user privilege
        """
        self.user_id = uid
        self.password = password
        self.privilege = privilege # should be between 'high ->4', 'mid-3', 'low->2' or 'no->1'

    def get_password(self):
        """
        returns the user password
        """
        return self.password

    def get_privilege(self):
        """
        returns the user privilege
        """
        return self.privilege


# TODO: 1 Write a decorator that allows a function to run only on odd seconds
def run_at_odd(func):
    """
    function called to create a decorator. func is a non local variable
    for the inner function.
    Inputs:
        func: function name
    Returns:
        execute: function
    """
    from datetime import datetime
    from functools import wraps

    # Check for a valid  function is passed to create a decorator
    if not hasattr(func, '__call__'):
        raise NameError(f"{func} is not a valid function")

    @wraps(func)
    def execute(*args,**kwargs):
        """
        calls any function only if current time second's value is odd

        # Inputs:
            *args: expects input parameters a and b

        # Returns:
            Returns output of function func(*args,**kwargs) only if called at odd seconds

        # Functionality:
            Function check's current time to see if the current time's second's value is odd or not,
            if odd, then only function is executed otherwise not

        For eg: after decorating add function, if add is called at time secods value is 21 (odd), function will be
        executed while if second's value is 20(even) it will not executeoadd function with 1,2 as input for 1st time, the output
        will be: add has been called 1 times, Result: 1 + 2 = 3
        """
        second = datetime.now().second
        is_odd = second %2
        print(f"Current time second's value is: {second}",f",Function: {func.__name__} will run" if is_odd else f"Function: {func.__name__} didn't run" )
        if is_odd:
            return(func(*args,**kwargs))
    return(execute)

@run_at_odd
def add(*args):
    """add the input variables"""
    return(sum(args))

# TODO: 2 Write a decorator to add log to any function
func_log = [] # Global logger list to test the logging

def logged(func):
    """
    function called to create a decorator. func is a non local variable
    for the inner function.
    Inputs:
        func: function name
    Returns:
        logger: function
    """
    from datetime import datetime, timezone
    from functools import wraps
    from time import perf_counter

    count = 0
    @wraps(func)
    def logger(*args,**kwargs):
        """
        add log to any function call

        # Inputs:
            *args: positioned parameters
            **kwargs: named parameters
        # Returns:
            Returns output of function func(*args,**kwargs) only if called at odd seconds

        # Functionality:
            Print the log of function with details like function name,function documentation, execution time, count of
            times function is called and function call representation with arguments as string. Also, update the global
            func_log list which is be used to varify the logging functionality

        For eg: after decorating add function, if add(1,2) is called, apart from result, log will be showcased like-
        ---  Log for function: add  ---
        Function documentation: add the input variables
        Function called at: 2020-09-20 20:40:08.767335+00:00
        Total time to execute: 1.9999998812636477e-07
        Function called: 1 times
        Call function add(1,2)
        Result-
        3
        """
        # Check for a valid  function is passed to create a decorator
        if not hasattr(func, '__call__'):
            raise NameError(f"{func} is not a valid function")

        nonlocal count
        func_name = func.__name__
        func_doc = func.__doc__
        run_dt = datetime.now(timezone.utc)
        start = perf_counter()
        end = perf_counter()
        exec_time = end - start
        count +=1
        args_ = [str(a) for a in args]
        kwargs_ = ['{0}={1}'.format(k, v) for k, v in kwargs.items()]
        all_args = args_ + kwargs_
        args_str = ','.join(all_args)
        result = func(*args, **kwargs)

        log = f"""
        ---  Log for function: {func_name}  ---
        Function documentation: {func_doc}
        Function called at: {run_dt}
        Total time to execute: {exec_time}
        Function called: {count} times
        Call function {func_name}({args_str})
        Result-
        """
        func_log.insert(0,log)
        print(log)
        return(result)
    return(logger)

@logged
def add_logged(*args):
    """add the input variables"""
    return(sum(args))

@logged
def mul_logged(a,b,c=1):
    """Multiple the input variables"""
    return(a*b*c)


# TODO: 3  Write a decorator to add authentication to any function
def factory_authenticate(current_password, user_password):
    """
    Decorators factory to create a decorator. func is a non local variable
    for the inner function.
    Inputs:
        current_password: password of user
        user_password: password input by user
    Returns:
        authenticate: decorator
    """
    def authenticate(fn):
        """
        decorator for authenticating a function
        Inputs:
            func: function
        Returns:
            inner: function
        """
        cnt = 0
        def inner(*args, **kwargs):
            """
            function for authenticating a function
            # Inputs:
                *args: positioned parameters
                **kwargs: named parameters
            # Returns:
                Returns output of function func(*args,**kwargs) only if authenticated

            # Functionality:
                Call a function after it is authenticated. Otherwise display error

            For eg: on calling add function, if the user name is correct, then only function will result the output
            else it will show an error message
            """
            if not hasattr(fn, '__call__'):
                raise NameError(f"{func} is not a valid function")

            if user_password == current_password:
                print(f'{fn.__name__} was called {cnt} times')
                return fn(*args, **kwargs)
            else:
                raise ValueError(f'You are not authenticated to use {fn}')
        return inner
    return authenticate

user = Users('test1','password1','1')

@factory_authenticate(user.get_password(),'a1bc')
def add_auth_f(*args):
    """add the input variables"""
    return(sum(args))

@factory_authenticate(user.get_password(),'password1')
def add_auth_p(*args):
    """add the input variables"""
    return(sum(args))

# TODO 4: Decorator to add time to any function
def timer_factory(repeat):
    """
    decorator factory to create a decorator.
    Inputs:
        repaet: number of times the decorated function will be called
    Returns:
        time_it: decorator
    """
    def time_it(func):
        """
        decorator function called to decorate a function by timing it.
        Inputs:
            func: name of function which has to be timed ( will be free variable)
        Returns:
            time_it: function
        """
        from time import perf_counter
        from functools import wraps
        # Check for a valid  function is passed to create a decorator
        if not hasattr(func, '__call__'):
            raise NameError(f"{func} is not a valid function")

        @wraps(func)
        def timer(*args, **kwargs):
            """
            find average time to execute a function while running it for n times.
            # Inputs:
                *args: positioned parameters
                **kwargs: named parameters
            # Returns:
                Returns output of function func(*args,**kwargs)

            # Functionality:
                Function check's how much time it takes on an average for n runs to execute a function

            For eg: after decorating fact function for repeat = 100, we will get how much time it takes for
            fact function to run for any given inputs on an average for 100 runs. In this case we will get -
            fact(5)
            Function fact takes average run time of 2.3930000179461787e-06 for 100 iterations
            """
            total_elapsed = 0
            for i in range(repeat):
                start = perf_counter()
                result = func(*args, **kwargs)
                end = perf_counter()
                total_elapsed += (end - start)
            avg_run_time = total_elapsed / repeat
            print(f'Function {func.__name__} takes average run time of {avg_run_time} for {repeat} iterations')
            return result, avg_run_time
        return timer
    return time_it

@timer_factory(100)
def fact(n:int)->int:
    """Factorial of a numer"""
    from operator import mul
    from functools import reduce
    return reduce(mul, range(1, n+1))

# TODO: 5 Provides privilege access (has 4 parameters, based on privileges (high, mid, low, no), gives access to all 4, 3, 2 or 1 params)
# Health data of patients
data = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':[20, 21, 19, 18], 'Blood_Group':['O+','B+','A-','B-'],'Covid_Infected':['Y','N','N','Y']}

# Create DataFrame of data of patients
df = pd.DataFrame(data)

def prev_access(func):
    """
    Get the records of four columns of the
    df based on the user 4 level of access
    privilege for the user. If privilege is
    1, user can see only Name. if privilege
    is 2, user can see Name and age and like
    this if access if 4, user can see all
    four columns
    Inputs:
        func: function
    Returns:
        access_data: inner function
    """
    user_lvl = {'1':'accountant', '2':'nurse', '3':'Doctor','4':'HoD'}
    def access_data(user,df):
        """
        Provides the user data access
        based on its privilege
        """
        prev = user.get_privilege()
        print(f'user has previlage of {user_lvl[prev]}, can access only {prev} columns of records')
        return func(user,df.iloc[:,0:int(prev)])
    return access_data

@ prev_access
def access_records(user,df):
    """
    print and return records of dataframe
    Inputs:
        df: dataframe
    """
    print(df)
    return df

accountant = Users('abc1','password1','1')
acc_df = access_records(accountant,df)

doctor = Users('abc2','password2','3')
dr_df = access_records(doctor,df)


# TODO: 6 Htmlize code using inbuild singledispatch
from functools import singledispatch
from numbers import Integral
from collections.abc import Sequence
from decimal import Decimal

@singledispatch # Creates registry, register and dispatch function
def htmlize(a): # Decorater
    """ convert in html format for object type"""
    from html import escape
    return escape(str(a))

@htmlize.register(Integral) # int
def htmlize_integral_numbers(a):
    """ convert in html format for int type"""
    return f'{a}(<i>{str(hex(a))}</i>)'

@htmlize.register(float) # float
def htmlize_real(a):
    """ convert in html format for float type"""
    return f'{round(a, 2)}'

@htmlize.register(Decimal) # decimal
def htmlize_decimal(a):
    """ convert in html format for decimal type"""
    return f'{round(a, 2)}'

@htmlize.register(Sequence) # list and tuple
def htmlize_sequence(a):
    """ convert in html format for list anf tuple type"""
    items = (f'<li>{htmlize(item)}</li>' for item in a)
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

@htmlize.register(dict) # dict
def htmlize_dict(d):
    """ convert in html format for dict type"""
    items = (f'<li>{k}={v}</li>' for k, v in d.items())
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

@htmlize.register(str) # string
def htmlize_str(s):
    """ convert in html format for str type"""
    return htmlize(s).replace('\n', '<br/>\n')
