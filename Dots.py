import numpy as np
vectors=[]
L=int(input())
h=int(input())
a=int(input())
t=int(input())
A=np.array([0,0])
G=np.array([L,0])
n=2*t
r_vectors=[]
dots=[(0,0)]
r_dots=[]
R=np.array([-1,1])#отражающий вектор
B=np.array([0,h+(L/2)*np.sin(a*np.pi/180)])
def vectorall(L,h,a,t,A,B,G,dots):
    def vectoring(f,L,h,a,k,A,B,G,dots):
        for i in range(k+2):
            vk_x = np.array([L/f, 0])
            if i>=k+1:
                vk_y = np.array([0, h+(L/2)*np.sin(a*np.pi/180)])
                vk_rem = vk_y 
            else:
                if i==0:
                    vk_y = np.array([0, h])
                    vk_rem = vk_y
                elif i%2 == 0:
                    vk_y = np.array([0, h+(L/(f)*i)*np.sin(a*np.pi/180)])
                    vk_rem = vk_x + vk_y
                else:
                    vk_y = np.array([0, h+(L*(i-1)/f)*np.sin(a*np.pi/180)])
                    vk_rem = vk_x - vk_y
            vectors.append(vk_rem)
            r_vectors.append(vk_rem*R)
            A=A+vectors[i]
            dots.append((A[0],A[1]))
            G=G+r_vectors[i]
            r_dots.append((G[0],G[1]))
        r_dots.pop()
    if t%2==0:
        A=A+np.array([L/n,0])
        G=G-np.array([L/n,0])
        r_dots.append((L,0))
        k=t-1
        f=n-2 # f это костыль который помогает свзять четный и нечетный случаи
        L=L*(n-2)/n
        vectoring(f,L,h,a,k,A,B,G,dots)
    else:
        k=t
        f=n
        vectoring(f,L,h,a,k,A,B,G,dots)
     #все точки объеденены в один массив но идут не против часовой стрелки а в порядке отдаления точки начала координат по x координате, центральная нижняя точка повторяется дважды, но получается так, что все не четные точки нижние а четные верхние то есть массив легко отсортировать нужным образом  
vectorall(L,h,a,t,A,B,G,dots)
r_dots.reverse()
for i in range(len(r_dots)):
    dots.append(r_dots[i])
print(dots)
print(r_dots)
print(vectors)
print(r_vectors)
