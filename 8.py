#Výpočty funkcí
def forward_derivate(f, x0, h):
    return (f(x0+h) - f(x0))/h

def backward_derivate(f, x0, h):
    return (f(x0) - f(x0-h))/h

def central_derivate(f, x0, h):
    return (f(x0+h) - f(x0-h))/(2*h)

def forward_derivate_adaptive(f, x0, h_adaptive):
    return (f(x0+h_adaptive) - f(x0))/h_adaptive

def backward_derivate_adaptive(f, x0, h_adaptive):
    return (f(x0) - f(x0-h_adaptive))/h_adaptive

def central_derivate_adaptive(f, x0, h_adaptive):
    return (f(x0+h_adaptive) - f(x0-h_adaptive))/(2*h_adaptive)

#Funkce a adaptivní volba
f = lambda x: x**2 + 2
x0 = 2
h = 0.1
h_adaptive = float(input("Zadejte adaptive krok: "))

#Mezi výsledky 
fd = forward_derivate(f, x0, h)
bd = backward_derivate(f, x0, h)
cd = central_derivate(f, x0, h)
fda= forward_derivate_adaptive(f, x0, h_adaptive)
bda = backward_derivate_adaptive(f, x0, h_adaptive)
cda = central_derivate_adaptive(f, x0, h_adaptive)

#Výsledky
print(f"Bez daného kroku pro dopřednou: {fd}, s daným krokem pro dopřednou: {fda}")
print(f"Bez daného kroku pro zpětnou: {bd}, s daným krokem pro dopřednou: {bda}")
print(f"Bez daného kroku pro centrální: {cd}, s daným krokem pro dopřednou: {cda}")
