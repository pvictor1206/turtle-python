# Capítulo 4: Estudo de caso: projeto de interface
import turtle

programa = turtle.Turtle()
#programa = turtle.Screen()
#programa.mainloop()

#print(programa)
for c in range(50):
    programa.fd(100) #Move para frente
    programa.lt(90) #Virar a esquerda (angulo?)
    #programa.fd(100) #Move para frente

for c in range(50):
    programa.fd(20) #Move para frente
    programa.rt(20) #Virar a direita

for c in range(50):
    programa.fd(20)
    programa.bk(20)


# q1: Escreva uma função chamada square que receba um parâmetro chamado t, que é um turtle. Ela deve usar o turtle para desenhar um quadrado.
# q2: Fazer um poligono de "n" lados (360/n)
# q3: Desenhe um circulo 

def squart(t):
    for c in range(30):
        t.fd(200)
        t.lt(90)
    for p in range(30):
        t.fd(100)
        t.lt(36)

# Forma um circulo
def circle(t): 
    for c in range(50):
        t.fd(10)
        t.lt(10)

t = turtle.Turtle()
squart(t)
circle(t)


turtle.mainloop() #A janela fica aberta
