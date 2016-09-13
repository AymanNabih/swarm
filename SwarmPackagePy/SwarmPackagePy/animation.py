import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animat
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from numpy import linspace, meshgrid, array, ravel

def animation(agents, function, A, B, sr=False):

    side = linspace(A, B, (A - B)*5)
    X, Y = meshgrid(side, side)
    Z = array([array([function([X[i][j], Y[i][j]]) for j in range(len(X))]) for i in range(len(X[0]))])

    fig = plt.figure()
    ax = plt.axes(xlim=(A, B), ylim=(A, B))
    ax.pcolormesh(X, Y, Z, shading='gouraud')
    iter_text = plt.text(0.02, 0.95, '', transform=ax.transAxes)

    x = array([j[0] for j in agents[0]])
    y = array([j[1] for j in agents[0]])
    sc = plt.scatter(x, y, color='black')

    def init():
        iter_text.set_text('')

    def an(i):
        x = array([j[0] for j in agents[i]])
        y = array([j[1] for j in agents[i]])
        sc.set_offsets(list(zip(x, y)))
        iter_text.set_text('iteration = {}'.format(i))

    ani = animat.FuncAnimation(fig, an, frames=len(agents)-1, init_func=init)


    if sr:
        ani.save('result.gif', fps=30)

    plt.show()

def animation3D(agents, function, A, B, sr=False):

    side = linspace(A, B, 100)
    X, Y = meshgrid(side, side)
    zs = array([function([x, y]) for x, y in zip(ravel(X), ravel(Y))])
    Z = zs.reshape(X.shape)

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='jet',
    linewidth=0, antialiased=False)
    ax.set_xlim(A, B)
    ax.set_ylim(A, B)

    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    fig.colorbar(surf, shrink=0.5, aspect=5)

    ims = []
    im = []
    for i in agents:
        for j in i:
            im1 = ax.scatter(j[0], j[1], function([j[0], j[1]]), color='black')
            im.append(im1)
        ims.append(im)
        im = []
    ani = animat.ArtistAnimation(fig, ims)

    if sr:
        ani.save('result.gif', fps=30)

    plt.show()