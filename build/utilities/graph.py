import matplotlib.pyplot as mp
import numpy as np
def graph2D(x_values,y_values, x_title, y_title, graph_title):
    mp.figure(figsize=(8, 5))
    mp.plot(x_values, y_values, color="b")

    # Añadir etiquetas y título
    mp.xlabel(x_title)
    mp.ylabel(y_title)
    mp.title(graph_title)

    # Mostrar la leyenda
    mp.legend()

    # Mostrar el gráfico
    mp.grid(True)
    mp.show()
def graph3D(x_values,y_values,z_values, x_title, y_title, z_title, graph_title):
    fig = mp.figure(figsize=(8, 5))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x_values, y_values, z_values, cmap='viridis')
    ax.set_xlabel(x_title)
    ax.set_ylabel(y_title)
    ax.set_zlabel(z_title)
    ax.set_title(graph_title)

    mp.show()

if __name__ == "__main__":
    x = [1,2,3,4,5]
    y = [1,2,3,4,5]
    #graph2D(x,y,"valor X", "valor Y", "Prueba")
    #graph2D(x,list(map(lambda x: x*2, y)),"valor X", "valor Y", "Prueba2")
    #graph3D(x,y,z,"Datos X", "Datos Y","Datos Z","Prueba")

    # Definir la función Z = f(X, Y)
    X,Y = np.meshgrid(x,y)
    Z = X + Y
    graph3D(X,Y,Z, "Datos X", "Datos Y", "Datos Z", "Prueba")