import multiprocessing as mp
import time
from functools import partial

data = (
	['a', '2'], ['b', '4'], ['c', '6'], ['d', '8'],
	['e', '1'], ['f', '3'], ['g', '5'], ['h', '7']
)

data2 = [1,2,3,4,5,6,7,8]

def mp_worker(const_input1, const_input2, data, data2):
	inputs, the_time = data
	print('Process number ' + str(data2))
	print(const_input2 + ' constant is ' + str(const_input1))
	print (" Processs %s Waiting %s seconds" % (inputs, the_time))
	time.sleep(int(the_time))
	print (" Process %s DONE" % inputs)
	return the_time

def mp_handler():
	pool = mp.Pool(mp.cpu_count())
	const_input1 = 4  # Constant input 1
	const_input2 = 'Haha'  # Constant input 2
	func = partial(mp_worker, const_input1, const_input2)  # Partial to include the function with constant inputs 
	performance = pool.starmap(func, zip(data, data2))  # Use map to wrap the function with input sets
	# performance = [item for item in performance]
	pool.close()
	pool.join()
	return performance

if __name__ == '__main__':
	tic = time.time()
	print('The number of cores of this computer is: '+ str(mp.cpu_count()))
	Final_res = mp_handler()
	print(Final_res)
	print('All done in: '+ str(time.time()-tic))