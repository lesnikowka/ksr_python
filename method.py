import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import integrate


a = 0 #граничные условия
b = 1 #граничные условия
eps = 0.5e-6 #погрешность
n = 1000 #число разбиений


#Тестовая Задача
def k1test(x):
    return 4 / 9 #Обратная функция

def k2test(x):
    return 4 #Обратная функция

def q1test(x):
    return 1
    
def q2test(x):
    return 1

def f1test(x):
    return 0
    
def f2test(x):
    return 1


#Основная Задача 
#Функции для интегрирования
def k1(x):
    return 1 / ((x + 1) ** 2) #Обратная функция

def k2(x):
    return 1 / (x ** 2) #Обратная функция

def q1(x):
    return (np.exp(-x) * (np.exp(1) ** 0.5))
    
def q2(x):
    return (np.exp(x) / (np.exp(1) ** 0.5))

def f1(x):
    return (np.cos(np.pi * x))
    
def f2(x):
    return 1


#Интегрирование
def integrateFunction(f, a, b):
    result, error = integrate.quad(f, a, b)
    return result


#Коэфициент ai(ai + 1)
def aiInit(ksi, xi, xmi, h, k1, k2):
    if xi <= ksi:
        coef = h / (integrateFunction(k1, xmi, xi))
    elif ksi > xmi and ksi < xi:
        coef = h / (integrateFunction(k1, xmi, ksi) + integrateFunction(k2, ksi, xi))
    elif ksi <= xmi:
        coef = h / (integrateFunction(k2, xmi, xi))
    return coef


#Коэфициент di
def diInit(ksi, xi, xmi, h, q1, q2):
    if xi <= ksi:
        coef = (1 / h * (integrateFunction(q1, xmi, xi)))
    elif ksi > xmi and ksi < xi:
        coef = (1 / h * (integrateFunction(q1, xmi, ksi) + integrateFunction(q2, ksi, xi)))
    elif ksi <= xmi: 
        coef = (1 / h * (integrateFunction(q2, xmi, xi)))
    return coef


#Коэфициент phi
def phiInit(ksi, xi, xmi, h, f1, f2):
    if xi <= ksi:
        coef = (1 / h * (integrateFunction(f1, xmi, xi)))
    elif ksi > xmi and ksi < xi:
        coef = (1 / h * (integrateFunction(f1, xmi, ksi) + integrateFunction(f2, ksi, xi)))
    elif ksi <= xmi:
        coef = (1 / h * (integrateFunction(f2, xmi, xi)))
    return coef


#Создание трёхдиагональной матрицы
def matrixInit(k1, k2, q1, q2, f1, f2, mu1, mu2, ksi, n, a, b):
    h = (b - a) / n
    A = [[0] * (n + 1) for i in range(n + 1)]
    Ai = [0] * (n) #Массивы коэфициентов для прогонки
    Bi = [0] * (n)
    Ci = [0] * (n)
    b = [0] * (n + 1)
    A[0][0] = 1
    A[n][n] = 1
    b[0] = mu1
    b[n] = mu2
    xi = 0
    for i in range(1, n):
        xi += h #xi
        xi1 = xi + h #xi+1
        xi2 = xi + h / 2 #xi+0.5
        xmi = xi - h #xi-1
        xmi2 = xi - h / 2 #xi-0.5
        b[i] = -phiInit(ksi, xi2, xmi2, h, f1, f2) #Столбец
        for j in range(0, n + 1):
            if i - j == 1:
                A[i][j] = aiInit(ksi, xi, xmi, h, k1, k2) / h ** 2
                Ai[i] = A[i][j]
            if i == j:
                A[i][j] = -((aiInit(ksi, xi, xmi, h, k1, k2) + aiInit(ksi, xi1, xi, h, k1, k2)) / h ** 2 + diInit(ksi, xi2, xmi2, h, q1, q2))
                Ci[i] = -A[i][j]
            if j - i == 1:
                A[i][j] = aiInit(ksi, xi1, xi, h, k1, k2) / h ** 2
                Bi[i] = A[i][j]
    return A, b, Ai, Bi, Ci


def progonka(matrix, b, Ai, Bi, Ci):
    v = [0] * (n + 1)
    #прямой ход
    alpha = [0] * (n + 1)
    betta = [0] * (n + 1)
    alpha[1] = matrix[0][1]
    betta[1] = b[0]
    for i in range(2, n + 1):
        alpha[i] = Bi[i - 1] / (Ci[i - 1] - Ai[i - 1] * alpha[i - 1])
        betta[i] = (-b[i - 1]  + Ai[i - 1] * betta[i - 1]) / (Ci[i - 1] - Ai[i - 1] * alpha[i - 1])
    #обратный ход
    v[n] = (-matrix[n][n - 1] * betta[n] - b[n]) / (matrix[n][n - 1] * alpha[n] - 1)
    for i in range(n - 1, -1, -1):
        v[i] = alpha[i + 1] * v[i + 1] + betta[i + 1]
    return v

#Тестовая задача ответ
A, bs, Ai, Bi, Ci = matrixInit(k1test, k2test, q1test, q2test, f1test, f2test, 0, 0, 0.5, n, a, b)
otvet = progonka(A, bs, Ai, Bi, Ci)
#print(otvet)

#Аналитическое решение тестовой
def u(x):
    if x >= 0 and x <= 0.5: 
        return 0.289601 * np.exp(2 * x / 3) - 0.289601 * np.exp(-(2 * x / 3))
    elif x > 0.5 and x <= 1:
        return -0.110262 * np.exp(2 * x) - 1.36897 * np.exp(-(2 * x)) + 1

xx = np.linspace(0, 1, n + 1)
x = np.linspace(0, 1, n + 1)
plt.plot(xx, otvet)
uarray = []

for i in range(n + 1):
    uarray.append(u(x[i]))
plt.plot(x, uarray)
#print(uarray)

#Основная задача
A, bs, Ai, Bi, Ci = matrixInit(k1, k2, q1, q2, f1, f2, 0, 0, 0.5, n, a, b)

#for row in A:
#    print(row)
#print()

otvet = progonka(A, bs, Ai, Bi, Ci)
print(otvet)
xx = np.linspace(0, 1, n + 1)
plt.plot(xx, otvet)

A, bs, Ai, Bi, Ci = matrixInit(k1, k2, q1, q2, f1, f2, 0, 0, 0.5, n, a, b)
otvet = progonka(A, bs, Ai, Bi, Ci)
print(otvet)
xx = np.linspace(0, 1, n + 1)
#plt.plot(xx, otvet)

plt.show()