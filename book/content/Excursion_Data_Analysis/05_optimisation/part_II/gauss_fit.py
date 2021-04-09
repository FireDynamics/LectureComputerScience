import numpy as np
import pandas as pd
import scipy.optimize
import matplotlib.pyplot as plt

data = pd.read_csv('PMMA_kompakt_40K.csv', header=0)

x = data['# Temp_mean_R'].values[300:]
y = data[' reacr_mean'].values[300:] * 1e2

print(x)

# 1: x0
# 2: d
# 3: A
params = [3.5, 5., 1.,
          3., 10., 0.5,
          3.2, 5., 0.5,
          2.8, 1., 1.]

def function(x, p):
    # print(p)
    x0 = p[0] * 100
    d = p[1]
    A = p[2]
    return A*np.exp(-((x-x0)**2)/d**2)

def cost_function(p,x,y):
    delta = np.copy(y)
    for i in range(len(p)//3):
        delta -= function(x,p[3*i:3*i+3])
    l2 = np.sum(delta**2)
    print(l2)
    return l2

res = scipy.optimize.minimize(cost_function,
                              np.array(params),
                              method='BFGS',
                              args=(x,y),
                              options={'gtol':1e-7, 'maxiter':1000, 'eps':1e-8},
                              tol=1e-6)

print(res)

xdef = np.linspace(x[0], x[-1], 200)
print(params)

ydef = np.zeros_like(xdef)
print("gauss functions:")
for i in range(len(res.x)//3):
    print("id: {:02d}".format(i))
    loc_y = function(xdef, res.x[i*3:i*3+3])
    print("  integral: {}".format(np.trapz(loc_y, xdef)))
    ydef += loc_y
print("integral all gauss: {}".format(np.trapz(ydef, xdef)))

print("integral data: {}".format(np.trapz(y, x)))
plt.plot(x, y, label='data', linewidth=5)
plt.plot(xdef, ydef, label="fitted_total", linewidth=2)

for i in range(len(res.x)//3):
    plt.plot(xdef, function(xdef, res.x[i*3:i*3+3]),
             label="gauss_{:02d}".format(i), color='gray')


plt.legend()
plt.show()
