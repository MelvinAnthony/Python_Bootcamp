def fun_1(n):
    return [int(num) for num in range(n)]
print(fun_1(10))

def fun_2(n):
    return list(map(int,range(n)))
print(fun_2(10))


#calculte the time for excution speed fun_1
import time

# #current time
# start_time = time.time()
# #run code
# result = fun_1(100000)
# #current time ater excution
# end_time = time.time()
# #calculate the time
# calculate_time = end_time - start_time
# #display the time
# print("fun_1 calulate time: ",calculate_time)


#calculte the time for excution speed fun_2

# #current time
# start_time = time.time()
# #run code
# result = fun_2(100000)
# #current time ater excution
# end_time = time.time()
# #calculate the time
# calculate_time = end_time - start_time
# #display the time
# print("fun_2 calulate time: ",calculate_time)


#using timelit
import timeit

#for fun_1
stmt = '''
fun_1(10)
'''
setup = '''
def fun_1(n):
    return [int(num) for num in range(n)]
'''

result = timeit.timeit(stmt,setup,number = 100000)
print(result)

#for fun_2
stmt_2 = '''
fun_2(10)
'''
setup_2 = '''
def fun_2(n):
    return [int(num) for num in range(n)]
'''

result_2 = timeit.timeit(stmt_2,setup_2,number = 100000)
print(result_2)

