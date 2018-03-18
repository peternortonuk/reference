'''
import rpy2:
https://github.com/ContinuumIO/anaconda-issues/issues/1527

plot pairs
https://stackoverflow.com/questions/7941207/is-there-a-function-to-make-scatterplot-matrices-in-matplotlib
'''

import rpy2.robjects as robjects
import numpy as np

def main():
    np.random.seed(1977)
    numvars, numdata = 4, 10
    data = 10 * np.random.random((numvars, numdata))
    mpg = data[0,:]
    disp = data[1,:]
    drat = data[2,:]
    wt = data[3,:]
    robjects.set_default_mode(robjects.NO_CONVERSION)

    R_data = robjects.r.data_frame(mpg=mpg,disp=disp,drat=drat,wt=wt)

    # Figure saved as eps
    robjects.r.postscript('pairsPlot.eps')
    robjects.r.pairs(R_data,
       main="Simple Scatterplot Matrix Via rpy2")
    rpy2.r.dev_off()

    # Figure saved as png
    robjects.r.png('pairsPlot.png')
    robjects.r.pairs(R_data,
       main="Simple Scatterplot Matrix Via rpy2")
    robjects.r.dev_off()

    robjects.set_default_mode(robjects.BASIC_CONVERSION)


if __name__ == '__main__':
    main()