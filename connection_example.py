from neuron import h, gui
import numpy

# a - red
# b - blue
# c - green
# d - yellow
# e - black

# b(0)->a(1): blue->red
# c(1)->b(1): green->blue
# d(0)->b(1): yellow->blue
# e(0)->a(0): black->red

a, b, c, d, e = [h.Section(name=n) for n in ['a', 'b', 'c', 'd', 'e']]
b.connect(a)
c.connect(b(1), 1) # connect the 1 end of c to the 1 end of b
d.connect(b)
e.connect(a(0)) # connect the 0 end of e to the 0 end of a
for sec in h.allsec():
    sec.nseg = 20
    sec.L = 100
    for seg in sec:
        seg.diam = numpy.interp(seg.x, [0, 1], [10, 40])

s = h.Shape()
s.show(False)

s.color(2, sec=a)  # a - red
s.color(3, sec=b)  # b - blue
s.color(4, sec=c)  # c - green
s.color(5, sec=d)  # d - yellow
s.color(1, sec=e)  # e - black
h.topology()
h.finitialize()
for sec in h.allsec():
    print(sec)
    for i in range(sec.n3d()):
        print('%d: (%g, %g, %g; %g)' % (i, sec.x3d(i), sec.y3d(i), sec.z3d(i), sec.diam3d(i)))
