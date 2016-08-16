import time

start = time.clock()
for i in range(50000000):
    pass
stop = time.clock()
print 'range ' + str(stop - start)

start = time.clock()
for i in xrange(50000000):
    pass
stop = time.clock()
print 'xrange ' + str(stop - start)

# eg.:
# range 4.751238
# xrange 1.960673
