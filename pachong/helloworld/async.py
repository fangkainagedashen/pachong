from threading import Thread
import multiprocessing
def async(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=())
        thr.start()
    return wrapper
def process(f):
	def wrapper(*args,**kwargs):
		pro = multiprocessing.Process(target=f,args=())
		pro.start()
	return wrapper
