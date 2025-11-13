import numpy
from matplotlib import pylab

data = numpy.transpose(numpy.loadtxt(r"C:\Users\44784\Desktop\Py_txt\sunspots.txt"))

def average(llist):
    final = sum(llist)/len(llist)
    return final

def running_average(llist):
    working_list = [0,0,0,0,0,0,0,0,0,0]
    results      = []
    for i in llist:
        working_list.append(i)
        working_list.remove(working_list[0])
        results.append(average(working_list))
    return results

ave_data = running_average(data[1][:1000])
                           
pylab.xlabel("Time / Months")
pylab.ylabel("Number")
pylab.title("Sunspots per month")
pylab.xlim(0,1100)
pylab.ylim(0,300)
pylab.plot(data[0][:1000],data[1][:1000], label = 'Monthly Sunspots')
pylab.plot(data[0][:1000],ave_data, label = 'Running Average')
pylab.legend()
pylab.show()
    
