import math
from sympy import symbols, diff, simplify
# delta -> known, epsilon->known
#STEP 1:
#alpha_0 equals delta value.
#alpha_n = alpha_(n-1) + delta x (1,618)^n
#calculate f(alpha_n's)
#f(alpha_(q-1)) < f(alpha_(q-2)) and f(alpha_(q-1)) < f(alpha_q) -> upper and lower bounds are found which is q-2 and q
#STEP2:
#calculate first interval (I) as upper - lower
#alpha_b = alpha_lower + 0,618 * I ; calculate f(alpha_b), alpha_a = alpha_lower + 0,382 * I; calculate f(alpha_a)
#STEP3:
#compare f(alpha_a) and f(alpha_b)

#----

def f(x):
    #y = 7*(x**2) - 20*x + 22 #example 10.17 from book
    #y = 2 - 4*x + ((math.e)**x) #example 10.13 from book
    #y = 8.5*(x**2) -13*x + 14.5 #homework, Section B-1st function
    y = 279*(x**2) -216*x + 69 #homework, Section B-2nd function
    #y = (2*(a+1)**2) + (3*(a+1)*(3*a+2)) + (2*(2+2*a)*(2+3*a))
    return simplify(y)

def goldenSectionSearch(delta, epsilon):
    #STEP1
    alph_q = 0
    alph_q1 = 0
    alph_q2 = 0
    j = 1;  # iteration count
    upper = 0
    lower = 0

    while True:
        for i in range(0, j):
            alph_q = delta*(pow(1.618, i))
            alph_q1 = alph_q + delta*(pow(1.618, i+1))
            alph_q2 = alph_q1 + delta*(pow(1.618, i+2))
        j += 1

        if (f(alph_q1) < f(alph_q)) and (f(alph_q1) < f(alph_q2)):
            upper = alph_q2
            lower = alph_q
            break
        else:
            continue

    while True:
        #STEP2
        intervalI = upper - lower
        alph_b = lower + (0.618*intervalI)
        alph_a = lower + (0.382*intervalI)

        #STEP3
        if f(alph_a) < f(alph_b):
            upper = alph_b
            alph_b = alph_a
            alph_a = lower + (0.382*intervalI)
            f(alph_a)
            #go to step 4
        elif f(alph_a) > f(alph_b):
            lower = alph_a
            alph_a = alph_b
            alph_b = lower + (0.618*intervalI)
            f(alph_b)
            #go to step 4
        else:
            lower = alph_a
            upper = alph_b
            continue

        #STEP4
        if upper - lower < epsilon:
            a_opt=(upper + lower)/2
            break

    return a_opt


def main():
    #print(goldenSectionSearch(0.5, 0.001, 0.01)) #example 10.13 from book
    #print(goldenSectionSearch(0.05, 0.005))  #example 10.17 from book
    print(goldenSectionSearch(0.05, 0.0001)) #homework, Section B

main()