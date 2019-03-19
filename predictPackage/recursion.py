def  sum_array(array):

     '''Return sum of all items in array'''

     if len(arr)== 1:
        return arr[0]
     else:
        return arr[0]+sum_array(arr[1:], N)

def Fibonacci(n):

        '''Return nth term in fibonacci sequence'''

        if n<0:
         print("Incorrect input")

        elif n==0:
           return 0
    # Second Fibonacci number is 1
        elif n==1:
            return 1
        else:
            return Fibonacci(n-1)+Fibonacci(n-2)



def factorial(n):

        if n <1:
            return 1
        else:
            return n * factorial( n - 1 )


def reverse(word):

    '''Return word in reverse'''

    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]
