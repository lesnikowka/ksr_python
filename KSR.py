import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D

#Функция фи, первый слой
def Phi(x):
    return 1 - x ** 2


#Вычислние первого слоя
def calculateFirstLayer(x0, n, h, phi):
    v0 = []
    xi = x0
    for i in range(n + 1):
        vi0 = phi(xi)
        v0.append(vi0)
        xi += h
    return v0
    

#Вычисление коэфициентов матрицы на j-ом слое
def initCoeff(n, h, tau, j, prevLayer):
    Ai = [9 * tau / h ** 2] * (n + 1)
    Bi = [9 * tau / h ** 2] * (n + 1)
    Ci = [1 + 18 * tau / h ** 2] * (n + 1)
    kapa1 = 1
    kapa2 = 1 / (1 + 7 * h)
    mu1 = 0
    mu2 = 2 * h / (1 + 7 * h)
    phi = [0] * (n + 1)
    Const = 5 * tau * np.sin(tau * j)
    for i in range(1, n):   
        phi[i] =  prevLayer[i] + Const
    coeffs = [kapa1, kapa2, mu1, mu2, phi, Ai, Bi, Ci]
    return coeffs
    

#Прогонка-вычисления j-го слоя
def runTrough(coeffs, n):
    v = [0] * (n + 1)
    kapa1 = coeffs[0]
    kapa2 = coeffs[1]
    mu1 = coeffs[2]
    mu2 = coeffs[3]
    phi = coeffs[4]
    Ai = coeffs[5]
    Bi = coeffs[6]
    Ci = coeffs[7]
    
    #Прямой ход
    alpha = [0] * (n + 1)
    betta = [0] * (n + 1)
    alpha[1] = kapa1 
    betta[1] = mu1
    for i in range(2, n + 1):
        alpha[i] = Bi[i - 1] / (Ci[i - 1] - Ai[i - 1] * alpha[i - 1])
        betta[i] = (phi[i - 1]  + Ai[i - 1] * betta[i - 1]) / (Ci[i - 1] - Ai[i - 1] * alpha[i - 1])
    
    #Обратный ход
    v[n] = (-kapa2 * betta[n] - mu2) / (kapa2 * alpha[n] - 1)
    for i in range(n - 1, -1, -1):
        v[i] = alpha[i + 1] * v[i + 1] + betta[i + 1]
    return v


#Основная функция численного решения
def solution(x0, t0, n, m, h, tau):
    V = [[0] * (n + 1) for i in range(m + 1)]
    prevLayer = calculateFirstLayer(x0, n, h, Phi)
    V[0] = prevLayer
    coeffs = []
    for j in range(1, m + 1):
        coeffs = initCoeff(n, h, tau, j, prevLayer)
        prevLayer = runTrough(coeffs, n)
        V[j] = prevLayer
    return V
    

#Функция для задачи интервалов t и x, размеров сетки m, n
def start(n, m, x0, xn, t0, tm):
    h = (xn - x0) / n
    tau = (tm - t0) / m
    result = solution(x0, t0, n, m, h, tau)
    x = np.linspace(x0, xn, n + 1)
    t = np.linspace(t0, tm, m + 1)
    return result, x, t


#Функция для рисования 3d графиков
def drawPlots3d(v, x, t):
    v = np.array(v)
    fig = plt.figure(figsize=(20, 20))
    ax3d = fig.add_subplot(projection='3d')
    xgrid, tgrid = np.meshgrid(x, t)
    ax3d.plot_surface(xgrid, tgrid, v)
    #plt.show()
    return 0


#Функция для рисования графиков проекций на оси xOv, tOv
def drawPlots2d(v, x, t):
    fig = plt.figure(figsize=(15, 15))
    ax1 = fig.add_subplot(1, 2, 1)
    for i in range(int(len(v))):
        tlay = [t[i]] * len(x)
        ax1.plot(tlay, v[i], 'green')
    ax2 = fig.add_subplot(1, 2, 2)
    for i in range(len(v)):
        ax2.plot(x, v[i], 'blue')
    return 0

def draw2dplot1(v, x, t):
    for i in range(int(len(v))):
        tlay = [t[i]] * len(x)
        plt.plot(tlay, v[i], 'green')
    plt.savefig("first2d.png")
    plt.clf()

def draw2dplot2(v, x, t):
    for i in range(len(v)):
        plt.plot(x, v[i], 'blue')
    plt.savefig("second2d.png")
    plt.clf()

def draw3d(v, x, t):
    v = np.array(v)
    fig = plt.figure()
    ax3d = fig.add_subplot(projection='3d')
    xgrid, tgrid = np.meshgrid(x, t)
    ax3d.plot_surface(xgrid, tgrid, v)
    plt.savefig("3d.png")
    plt.clf()




def calculate(n, m, tbound):
    v, x, t = start(n, m, 0, 1, 0, tbound)
    v2, x2, t2 = start(n * 2 + 1, m * 2 + 1, 0, 1, 0, tbound)

    v2 = [v2[2 * i] for i in range(len(v))]
    for i in range(len(v2)):
        v2[i] = [v2[i][2 * j] for j in range(len(v[i]))]

    t2 = [t2[2 * i] for i in range(len(t))]
    x2 = [x2[2 * i] for i in range(len(x))]

    diff = []
    difflay = []
    for i in range(len(v)):
        for j in range(len(v[i])):
            difflay.append(abs(v2[i][j] - v[i][j]))
        diff.append(max(difflay))

    draw2dplot1(v, x, t)
    draw2dplot2(v, x, t)
    draw3d(v, x, t)

    return v, x, t, v2, x2, t2











