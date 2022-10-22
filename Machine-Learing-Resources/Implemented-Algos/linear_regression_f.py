import matplotlib.pyplot as plt

data = [
    [1,1],
    [2,2],
    [3,3],
    [4,4],
    [5,5],
    [6,6],
    [7,7],
    [8,8],
    [9,9],
    [10,10]
]

def gradient_descent(m_now, b_now, points, L):
    m_gradient = 0
    b_gradient = 0
    N = float(len(points))

    for i in range(0, len(points)):
        x = points[i][0]
        y = points[i][1]
        m_gradient += -(2/N) * (y - ((m_now * x) + b_now)) * x
        b_gradient += -(2/N) * (y - ((m_now * x) + b_now)) 

    m = m_now - (L * m_gradient)
    b = b_now - (L * b_gradient)

    return m,b

#MAIN PROGRAM
m = 0
b = 0
L = 0.000001

epochs = 100000

for i in range(epochs):
    #if i % 10 == 0:
        #print("Epoch: ", i)
    m, b = gradient_descent(m, b, data, L)

print(m,b)

number = 5

print(f'At {number} the value is: {m * number + b}')
print(f'Errore: {str(abs(m * number + b - number) / number * 100)[:3]}%')

plt.scatter([data[i][0] for i,_ in enumerate(data)] , [data[i][1] for i,_ in enumerate(data)])
plt.plot([data[i][0] for i,_ in enumerate(data)], [m * data[i][0] + b for i,_ in enumerate(data)])
plt.show()