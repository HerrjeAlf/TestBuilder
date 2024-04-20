import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as grid
from matplotlib.patches import Arc
from matplotlib.transforms import Bbox, IdentityTransform, TransformedBbox
from matplotlib.patches import Polygon
from sympy import *

a, b, c, d, e, f, g, x, y, z = symbols('a b c d e f g x y z')

class AngleAnnotation(Arc):
    """
    Draws an arc between two vectors which appears circular in display space.
    """
    def __init__(self, xy, p1, p2, size=75, unit="points", ax=None,
                 text="", textposition="inside", text_kw=None, **kwargs):
        """
        Parameters
        ----------
        xy, p1, p2 : tuple or array of two floats
            Center position and two points. Angle annotation is drawn between
            the two vectors connecting *p1* and *p2* with *xy*, respectively.
            Units are data coordinates.

        size : float
            Diameter of the angle annotation in units specified by *unit*.

        unit : str
            One of the following strings to specify the unit of *size*:

            * "pixels": pixels
            * "points": points, use points instead of pixels to not have a
              dependence on the DPI
            * "axes width", "axes height": relative units of Axes width, height
            * "axes min", "axes max": minimum or maximum of relative Axes
              width, height

        ax : `matplotlib.axes.Axes`
            The Axes to add the angle annotation to.

        text : str
            The text to mark the angle with.

        textposition : {"inside", "outside", "edge"}
            Whether to show the text in- or outside the arc. "edge" can be used
            for custom positions anchored at the arc's edge.

        text_kw : dict
            Dictionary of arguments passed to the Annotation.

        **kwargs
            Further parameters are passed to `matplotlib.patches.Arc`. Use this
            to specify, color, linewidth etc. of the arc.

        """
        self.ax = ax or plt.gca()
        self._xydata = xy  # in data coordinates
        self.vec1 = p1
        self.vec2 = p2
        self.size = size
        self.unit = unit
        self.textposition = textposition

        super().__init__(self._xydata, size, size, angle=0.0,
                         theta1=self.theta1, theta2=self.theta2, **kwargs)

        self.set_transform(IdentityTransform())
        self.ax.add_patch(self)

        self.kw = dict(ha="center", va="center",
                       xycoords=IdentityTransform(),
                       xytext=(0, 0), textcoords="offset points",
                       annotation_clip=True)
        self.kw.update(text_kw or {})
        self.text = ax.annotate(text, xy=self._center, **self.kw)

    def get_size(self):
        factor = 1
        if self.unit == "points":
            factor = self.ax.figure.dpi / 72.
        elif self.unit[:4] == "axes":
            b = TransformedBbox(Bbox.unit(), self.ax.transAxes)
            dic = {"max": max(b.width, b.height),
                   "min": min(b.width, b.height),
                   "width": b.width, "height": b.height}
            factor = dic[self.unit[5:]]
        return self.size * factor

    def set_size(self, size):
        self.size = size

    def get_center_in_pixels(self):
        """return center in pixels"""
        return self.ax.transData.transform(self._xydata)

    def set_center(self, xy):
        """set center in data coordinates"""
        self._xydata = xy

    def get_theta(self, vec):
        vec_in_pixels = self.ax.transData.transform(vec) - self._center
        return np.rad2deg(np.arctan2(vec_in_pixels[1], vec_in_pixels[0]))

    def get_theta1(self):
        return self.get_theta(self.vec1)

    def get_theta2(self):
        return self.get_theta(self.vec2)

    def set_theta(self, angle):
        pass

    # Redefine attributes of the Arc to always give values in pixel space
    _center = property(get_center_in_pixels, set_center)
    theta1 = property(get_theta1, set_theta)
    theta2 = property(get_theta2, set_theta)
    width = property(get_size, set_size)
    height = property(get_size, set_size)

    # The following two methods are needed to update the text position.
    def draw(self, renderer):
        self.update_text()
        super().draw(renderer)

    def update_text(self):
        c = self._center
        s = self.get_size()
        angle_span = (self.theta2 - self.theta1) % 360
        angle = np.deg2rad(self.theta1 + angle_span / 2)
        r = s / 2
        if self.textposition == "inside":
            r = s / np.interp(angle_span, [60, 90, 135, 180],
                                          [3.3, 3.5, 3.8, 4])
        self.text.xy = c + r * np.array([np.cos(angle), np.sin(angle)])
        if self.textposition == "outside":
            def R90(a, r, w, h):
                if a < np.arctan(h/2/(r+w/2)):
                    return np.sqrt((r+w/2)**2 + (np.tan(a)*(r+w/2))**2)
                else:
                    c = np.sqrt((w/2)**2+(h/2)**2)
                    T = np.arcsin(c * np.cos(np.pi/2 - a + np.arcsin(h/2/c))/r)
                    xy = r * np.array([np.cos(a + T), np.sin(a + T)])
                    xy += np.array([w/2, h/2])
                    return np.sqrt(np.sum(xy**2))

            def R(a, r, w, h):
                aa = (a % (np.pi/4))*((a % (np.pi/2)) <= np.pi/4) + \
                     (np.pi/4 - (a % (np.pi/4)))*((a % (np.pi/2)) >= np.pi/4)
                return R90(aa, r, *[w, h][::int(np.sign(np.cos(2*a)))])

            bbox = self.text.get_window_extent()
            X = R(angle, r, bbox.width, bbox.height)
            trans = self.ax.figure.dpi_scale_trans.inverted()
            offs = trans.transform(((X-s/2), 0))[0] * 72
            self.text.set_position([offs*np.cos(angle), offs*np.sin(angle)])

        # Erklärung nachzulesen bei https://matplotlib.org/stable/gallery/text_labels_and_annotations/angle_annotation.html

# Geometrie
def dreieck_zeichnen(pkt, pkt_bez, st, wk, name):
    fig, ax = plt.subplots()
    fig.canvas.draw()  # Need to draw the figure to define renderer
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.axis('off')
    ax.set_aspect(1)
    fig.tight_layout()
    grid.SubplotSpec(gridspec=0,num1=0,num2=0)
    # Plot two crossing lines and label each angle between them with the above
    # ``AngleAnnotation`` tool.
    l1 = [pkt[1],pkt[2]]
    l2 = [pkt[0],pkt[2]]
    l3 = [pkt[0],pkt[1]]

    name_pkt1 = ax.annotate(pkt_bez[0], xy=pkt[0], xycoords='data', xytext=(-10,0),  textcoords='offset points', fontsize=12)
    name_pkt2 = ax.annotate(pkt_bez[1], xy=pkt[1], xycoords='data', xytext=(+2,0),  textcoords='offset points', fontsize=12)
    name_pkt3 = ax.annotate(pkt_bez[2], xy=pkt[2], xycoords='data', xytext=(+2,+2),  textcoords='offset points', fontsize=12)

    line1, = ax.plot(*zip(*l1), 'k')
    name_line1 = ax.annotate(st[2], xy=((pkt[1][0]+pkt[0][0])/2,(pkt[1][1]+pkt[0][1])/2), xycoords='data',
                             xytext=(+8,+8),  textcoords='offset points', fontsize=12)
    line2, = ax.plot(*zip(*l2), 'k')
    name_line2 = ax.annotate(st[0], xy=((pkt[2][0]+pkt[1][0])/2,(pkt[2][1]+pkt[1][1])/2), xycoords='data',
                             xytext=(+4,+4),  textcoords='offset points', fontsize=12)
    line3 = ax.plot(*zip(*l3), 'k')
    name_line3 = ax.annotate(st[1], xy=((pkt[0][0]+pkt[2][0])/2,(pkt[0][1]+pkt[2][1])/2), xycoords='data',
                             xytext=(+4,+4),  textcoords='offset points', fontsize=12)

    # point, = ax.plot(*p1, marker="o")

    am1 = AngleAnnotation(pkt[0], l3[1], l2[1], ax=ax, size=500, text=r'$' + wk[0] + '$', textposition='inside', unit='pixels')
    am2 = AngleAnnotation(pkt[1], l1[1], l3[0], ax=ax, size=500, text=r'$' + wk[1] + '$', textposition='inside', unit='pixels')
    am3 = AngleAnnotation(pkt[2], l2[0], l1[0], ax=ax, size=500, text=r'$' + wk[2] + '$', textposition='inside', unit='pixels')
    # plt.show()
    return plt.savefig('img/temp' + name, bbox_inches= 'tight', pad_inches = 0, dpi = 300)

def dreieck_zeichnen_mit_hoehe(pkt, pkt_bez, st, wk, name):
    fig, ax = plt.subplots()
    fig.canvas.draw()  # Need to draw the figure to define renderer
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.axis('off')
    ax.set_aspect(1)
    fig.tight_layout()
    grid.SubplotSpec(gridspec=0,num1=0,num2=0)
    # Plot two crossing lines and label each angle between them with the above
    # ``AngleAnnotation`` tool.
    l1 = [pkt[1],pkt[2]]
    l2 = [pkt[0],pkt[2]]
    l3 = [pkt[0],pkt[1]]
    l4 = [pkt[2],pkt[3]]

    name_pkt1 = ax.annotate(pkt_bez[0], xy=pkt[0], xycoords='data', xytext=(-10,0),  textcoords='offset points', fontsize=10)
    name_pkt2 = ax.annotate(pkt_bez[1], xy=pkt[1], xycoords='data', xytext=(+10,0),  textcoords='offset points', fontsize=10)
    name_pkt3 = ax.annotate(pkt_bez[2], xy=pkt[2], xycoords='data', xytext=(0,+10),  textcoords='offset points', fontsize=10)
    name_pkt4 = ax.annotate(pkt_bez[3], xy=pkt[3], xycoords='data', xytext=(-10,+5),  textcoords='offset points', fontsize=10)

    line1, = ax.plot(*zip(*l1), 'k')
    name_line1 = ax.annotate(st[2], xy=((pkt[1][0]+pkt[0][0])*2/5,0), xycoords='data',
                             xytext=(0,-10),  textcoords='offset points', fontsize=12)
    line2, = ax.plot(*zip(*l2), 'k')
    name_line2 = ax.annotate(st[0], xy=((pkt[2][0]+pkt[1][0])/2,(pkt[2][1]+pkt[1][1])/2), xycoords='data',
                             xytext=(+4,+4),  textcoords='offset points', fontsize=12)
    line3 = ax.plot(*zip(*l3), 'k')
    name_line3 = ax.annotate(st[1], xy=((pkt[0][0]+pkt[2][0])/2,(pkt[0][1]+pkt[2][1])/2), xycoords='data',
                             xytext=(-10,+10),  textcoords='offset points', fontsize=12)
    line4 = ax.plot(*zip(*l4), 'k')
    name_line4 = ax.annotate(st[3], xy=((pkt[2][0]+pkt[3][0])/2,(pkt[2][1]+pkt[3][1])/2), xycoords='data',
                             xytext=(+4,0),  textcoords='offset points', fontsize=12)
    # point, = ax.plot(*p1, marker="o")

    am1 = AngleAnnotation(pkt[0], pkt[0], pkt[2], ax=ax, size=300, text=r'$' + wk[0] + '$', textposition='inside', unit='pixels')
    am2 = AngleAnnotation(pkt[1], pkt[2], pkt[0], ax=ax, size=300, text=r'$' + wk[1] + '$', textposition='inside', unit='pixels')
    am3 = AngleAnnotation(pkt[2], pkt[0], pkt[3], ax=ax, size=300, text=r'$' + wk[2] + '$', textposition='inside', unit='pixels')
    am4 = AngleAnnotation(pkt[3], pkt[1], pkt[2], ax=ax, size=100, text=r'$' + wk[3] + '$', textposition='inside', unit='pixels')
    # plt.show()
    return plt.savefig('img/temp/' + name, bbox_inches= 'tight', pad_inches = 0, dpi = 200)

# Analysis
def graph_xyfix(fkt, *funktionen, bezn='f', stl=-1, name='Graph'):
    # fig = plt.Figure()
    # ax = plt.gca()
    fig, ax = plt.subplots()
    fig.canvas.draw()
    fig.tight_layout()
    ax.set_aspect(1)
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))
    ax.set_xlabel('x', size=10, labelpad=-24, x=1.03)
    ax.set_ylabel('y', size=10, labelpad=-21, y=1.02, rotation=0)
    ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)
    arrow_fmt = dict(markersize=4, color='black', clip_on=False)
    ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
    ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)
    plt.annotate(bezn, xy=(stl, fkt.subs(x, stl)), xycoords='data',
                 xytext=(+5, +5), textcoords='offset points', fontsize=12)
    xwerte = np.arange(-6, 6, 0.01)
    ywerte = [fkt.subs(x, elements) for elements in xwerte]

    plt.grid(True)
    plt.xticks(np.linspace(-5, 5, 11, endpoint=True))
    plt.yticks(np.linspace(-5, 5, 11, endpoint=True))
    plt.axis([-6, 6, -6, 6])
    plt.plot(xwerte, ywerte)
    for fkt in funktionen:
        ywerte = [fkt[0].subs(x, elements) for elements in xwerte]
        plt.plot(xwerte, ywerte)
        plt.annotate(fkt[1], xy=(fkt[2], fkt[0].subs(x, fkt[2])), xycoords='data',
                     xytext=(+5, +5), textcoords='offset points', fontsize=12)
    # plt.show()
    return plt.savefig('img/temp/' + name, dpi=200, bbox_inches="tight", pad_inches=0.02)

def graph_xyfix_plus(a_1, b_1, xwert, fkt , titel, n, name, *lswerte):
    # lswerte sind für die Werte für die Lösungen
    fig, ax = plt.subplots()
    fig.canvas.draw()
    fig.tight_layout()
    ax.set_aspect(1)
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))
    ax.set_xlabel('x', size=10, labelpad=-21, x=1.02)
    ax.set_ylabel('y', size=10, labelpad=-21, y=1.02, rotation=0)
    ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)
    arrow_fmt = dict(markersize=4, color='black', clip_on=False)
    ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
    ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)
    plt.annotate(n, xy=(xwert, fkt.subs(x, xwert)), xycoords='data', xytext=(+5, +5), textcoords='offset points',
                 fontsize=12)
    plt.grid(True)
    plt.xticks(np.linspace(-5, 5, 11, endpoint=True))
    plt.yticks(np.linspace(-5, 5, 11, endpoint=True))
    plt.axis([-6, 6, -6, 6])
    plt.plot(a_1, b_1, linewidth=2)
    for i, werte in enumerate(lswerte):
        if i % 2 != 0:  # überspringt ungerade Zahlen für das elif weiter unten
            continue
        elif werte is not None and lswerte[i + 1] is not None:  # Überprüft, ob es den Wert oder den nächsten Wert gibt
            plt.plot(werte, lswerte[i + 1], linewidth=1)
    plt.suptitle(titel, usetex=True)
    return plt.savefig('img/temp/' + name, dpi=200, bbox_inches="tight", pad_inches=0.03)

def Graph(x_min, x_max, *funktionen, name='Graph'):
    fig, ax = plt.subplots()
    fig.canvas.draw()
    fig.tight_layout()
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))
    ax.set_xlabel('x', size=10, labelpad=-24, x=1.03)
    ax.set_ylabel('y', size=10, labelpad=-21, y=1.02, rotation=0)
    ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)
    arrow_fmt = dict(markersize=4, color='black', clip_on=False)
    ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
    ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)
    for fkt in funktionen:
        xwerte = np.arange(x_min, x_max, 0.01)
        ywerte = [fkt.subs(x, elements) for elements in xwerte]
        plt.plot(xwerte, ywerte, linewidth=2)
    plt.grid(True)
    # plt.show()
    return plt.savefig('img/temp/' + name, dpi=200, bbox_inches="tight", pad_inches=0.02)

# Wahrscheinlichkeit
def Baumdiagramm_zmZ(stf, wkt, name, bz='E', bz2= r'$ \overline{' + 'E' + '} $'):
    fig, ax = plt.subplots()
    fig.canvas.draw()  # Need to draw the figure to define renderer
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.axis('off')
    ax.set_aspect(1/stf)
    fig.tight_layout()
    grid.SubplotSpec(gridspec=0,num1=0,num2=0)
    ywerte_ende = [2**stf]
    k = 0
    for stufe in range(stf):
        xwerte = [k+ 2,k + 2**(1 + stf-stufe)]
        k += 2**(1 + stf-stufe)
        ywerte_start = ywerte_ende
        ywerte_ende = []
        for element in ywerte_start:
            ywerte_1 = [element,element + 2**(stf-stufe+1)]
            ywerte_2 = [element,element - 2**(stf-stufe+1)]
            ywerte_ende.extend((element + 2**(stf-stufe+1), element - + 2**(stf-stufe+1)))
            plt.annotate(str(wkt), xy=(xwerte[0]/2 + xwerte[1]/2, ywerte_1[0]/2 + ywerte_1[1]/2), xycoords='data',
                         xytext=(-3*stf,+20/stf), textcoords='offset points', fontsize=12-stufe)
            plt.annotate(bz, xy=(xwerte[1], ywerte_1[1]), xycoords='data',xytext=(+20/stf,-(stf-stufe)),
                         textcoords='offset points', fontsize=12-stufe)
            plt.annotate(str(1-wkt), xy=(xwerte[0]/2 + xwerte[1]/2, ywerte_2[0]/2 + ywerte_2[1]/2), xycoords='data',
                         xytext=(-3*stf,-50/stf), textcoords='offset points', fontsize=12-stufe)
            plt.annotate(bz2, xy=(xwerte[1], ywerte_2[1]), xycoords='data',xytext=(+20/stf,-(stf-stufe)),
                         textcoords='offset points', fontsize=12-stufe)
            plt.plot(xwerte, ywerte_1, 'k')
            plt.plot(xwerte, ywerte_2, 'k')
            print('Stufe: ' + str(stufe))
            print('xwerte: ' + str(xwerte))
            print('ywerte_1: ' + str(ywerte_1))
            print('ywerte_2: ' + str(ywerte_2))
    return plt.savefig('img/temp/' + name, dpi=200, bbox_inches="tight", pad_inches=0.02)

def Baumdiagramm_zoZ(stf, anzahl_1, anzahl_2, name, bz1='E', bz2= r'$ \overline{' + 'E' + '} $'):
    fig, ax = plt.subplots()
    fig.canvas.draw()  # Need to draw the figure to define renderer
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.axis('off')
    ax.set_aspect(1/stf)
    fig.tight_layout()
    grid.SubplotSpec(gridspec=0,num1=0,num2=0)
    ywerte_ende = [2**stf]
    k = 0
    wkt_liste_anzahl_1 = [anzahl_1]
    wkt_liste_anzahl_2 = [anzahl_2]
    for stufe in range(stf):
        xwerte = [k+ 2,k + 2**(1 + stf-stufe)]
        k += 2**(1 + stf-stufe)
        ywerte_start = ywerte_ende
        ywerte_ende = []
        i = 0
        wkt_liste_anzahl_1_neu = []
        wkt_liste_anzahl_2_neu = []
        for element in ywerte_start:
            ywerte_1 = [element,element + 2**(stf-stufe+1)]
            ywerte_2 = [element,element - 2**(stf-stufe+1)]
            ywerte_ende.extend((element + 2**(stf-stufe+1), element - + 2**(stf-stufe+1)))
            plt.annotate(r'$ \frac{' + latex(wkt_liste_anzahl_1[i]) + '}{' + latex(anzahl_1+anzahl_2-stufe) + '} $',
                         xy=(xwerte[0]/2 + xwerte[1]/2, ywerte_1[0]/2 + ywerte_1[1]/2), xycoords='data',
                         xytext=(-3*stf,+20/stf), textcoords='offset points', fontsize=12-stufe)
            plt.annotate(bz1, xy=(xwerte[1], ywerte_1[1]), xycoords='data',xytext=(+20/stf,-(stf-stufe)),
                         textcoords='offset points', fontsize=12-stufe)
            plt.annotate(r'$ \frac{' + latex(wkt_liste_anzahl_2[i]) + '}{' + latex(anzahl_1+anzahl_2-stufe) + '} $',
                         xy=(xwerte[0]/2 + xwerte[1]/2, ywerte_2[0]/2 + ywerte_2[1]/2), xycoords='data',
                         xytext=(-3*stf,-50/stf), textcoords='offset points', fontsize=12-stufe)
            plt.annotate(bz2, xy=(xwerte[1], ywerte_2[1]), xycoords='data',xytext=(+20/stf,-(stf-stufe)),
                         textcoords='offset points', fontsize=12-stufe)
            plt.plot(xwerte, ywerte_1, 'k')
            plt.plot(xwerte, ywerte_2, 'k')
            wkt_liste_anzahl_1_neu.append(wkt_liste_anzahl_1[i]-1)
            wkt_liste_anzahl_2_neu.append(wkt_liste_anzahl_2[-i]-1)
            # print('Stufe: ' + str(stufe)), print('xwerte: ' + str(xwerte)), print('ywerte_1: ' + str(ywerte_1)), print('ywerte_2: ' + str(ywerte_2)), print('ywerte_start: ' + str(ywerte_start)), print(wkt_liste_anzahl_1_neu), print(wkt_liste_anzahl_2_neu)
            i += 1
        # print(wkt_liste_anzahl_1_neu), print(wkt_liste_anzahl_2_neu), print(wkt_liste_anzahl_1), print(wkt_liste_anzahl_2)
        wkt_liste_anzahl_1_neu.extend(wkt_liste_anzahl_1)
        wkt_liste_anzahl_2.extend(wkt_liste_anzahl_2_neu)
        wkt_liste_anzahl_1 = wkt_liste_anzahl_1_neu
    return plt.savefig('img/temp/' + name, dpi=200, bbox_inches="tight", pad_inches=0.02)

def loeschen():
    plt.figure().clear()

# Baumdiagramm(2,0.3,'E')