"""
Optimized plotting module with memory management
"""
import os
import gc
from skripte.imports import get_matplotlib, get_numpy, cleanup_matplotlib

def create_plot_with_cleanup(plot_function):
    """Decorator to ensure matplotlib cleanup after plotting"""
    def wrapper(*args, **kwargs):
        try:
            result = plot_function(*args, **kwargs)
            return result
        finally:
            cleanup_matplotlib()
            gc.collect()
    return wrapper

@create_plot_with_cleanup
def dreieck_zeichnen(pkt, pkt_bez=False, st=False, wk=False, name='noName'):
    """Optimized triangle drawing function"""
    plt = get_matplotlib()
    np = get_numpy()
    
    fig, ax = plt.subplots()
    fig.canvas.draw()
    
    # Configure plot
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.axis('off')
    ax.set_aspect(1)
    fig.tight_layout()
    
    # Draw triangle lines
    l1 = [pkt[1], pkt[2]]
    l2 = [pkt[0], pkt[2]]
    l3 = [pkt[0], pkt[1]]
    
    if pkt_bez:
        ax.annotate(pkt_bez[0], xy=pkt[0], xycoords='data', xytext=(-18,0), textcoords='offset points', fontsize=18)
        ax.annotate(pkt_bez[1], xy=pkt[1], xycoords='data', xytext=(+2,0), textcoords='offset points', fontsize=18)
        ax.annotate(pkt_bez[2], xy=pkt[2], xycoords='data', xytext=(+2,+2), textcoords='offset points', fontsize=18)

    if st:
        ax.plot(*zip(*l1), 'k')
        ax.plot(*zip(*l2), 'k')
        ax.plot(*zip(*l3), 'k')
        
        # Add side labels
        ax.annotate(st[2], xy=((pkt[1][0]+pkt[0][0])/2,(pkt[1][1]+pkt[0][1])/2), 
                   xytext=(+8,+8), textcoords='offset points', fontsize=18)
        ax.annotate(st[0], xy=((pkt[2][0]+pkt[1][0])/2,(pkt[2][1]+pkt[1][1])/2), 
                   xytext=(+4,+4), textcoords='offset points', fontsize=18)
        ax.annotate(st[1], xy=((pkt[0][0]+pkt[2][0])/2,(pkt[0][1]+pkt[2][1])/2), 
                   xytext=(-4,+8), textcoords='offset points', fontsize=18)

    # Save and cleanup
    plt.savefig(f'img/temp/{name}', bbox_inches='tight', pad_inches=0, dpi=300)
    plt.close(fig)

@create_plot_with_cleanup  
def graph_xyfix(*funktionen, bezn=False, name='Graph'):
    """Optimized graph plotting function"""
    plt = get_matplotlib()
    np = get_numpy()
    
    # Get sympy only when needed
    sympy = get_sympy()
    x = sympy.symbols('x')
    
    if bezn == False:
        fkt_bez = ['f', 'g', 'h', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w']
    else:
        fkt_bez = bezn if len(funktionen) == len(bezn) else [f'f_{i+1}' for i in range(len(funktionen))]
    
    fig, ax = plt.subplots()
    fig.canvas.draw()
    fig.tight_layout()
    
    # Configure axes
    ax.set_aspect(1)
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))
    ax.set_xlabel('x', size=10, labelpad=-30, x=0.97)
    ax.set_ylabel('y', size=10, labelpad=-30, y=0.97, rotation=0)
    ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.3)
    
    # Add arrows
    arrow_fmt = dict(markersize=4, color='black', clip_on=False)
    ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
    ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)
    
    # Plot functions
    xwerte = np.arange(-5.5, 5.5, 0.05)
    plt.grid(True)
    plt.xticks(np.linspace(-5, 5, 11, endpoint=True))
    plt.yticks(np.linspace(-5, 5, 11, endpoint=True))
    plt.axis([-5.5, 5.5, -5.5, 5.5])
    
    for i, fkt in enumerate(funktionen):
        ywerte = [fkt.subs(x, element) for element in xwerte]
        plt.plot(xwerte, ywerte)
        
        # Add function label
        werte = [(element, fkt.subs(x, element)) for element in xwerte]
        valid_points = [element for element in werte if abs(element[1]) <= 5]
        if valid_points:
            xwert_ymax = valid_points[5][0] if len(valid_points) > 5 else valid_points[0][0]
            plt.annotate(fkt_bez[i], xy=(xwert_ymax, fkt.subs(x, xwert_ymax)), 
                        xytext=(+5, +5), textcoords='offset points', fontsize=12)
    
    plt.savefig(f'img/temp/{name}', dpi=200, bbox_inches='tight', pad_inches=0)
    plt.close(fig)