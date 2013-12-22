D = 14**8
D3 = 3*D

a00,a11,a22 = 1,3,7

def A3(n):
    return (pow(2,(n+3),D3)-3)%D3

a4 = [13]
for n in range(8):
    a4.append(A3(a4[-1]))

print a4

print a4[4]

print((a00+a11+a22+A3(3)+a4[4]+2*a4[7])%D)
