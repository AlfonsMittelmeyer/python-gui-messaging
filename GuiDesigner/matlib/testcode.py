# -*- coding: utf-8 -*-

from functools import partial
from appimports import publish,subscribe,np


def TestGUI(self):

    def send_language(index):
        language_lists = (
            ( 'Sprache',('deutsch','german'),None,('englisch','english'),('französisch','french')),
            ( 'Language',('english','english'),None,('french','french'),('german','german'))
        )
        publish('MENU_LANGUAGE',language_lists[index])


    self.german['command'] = partial(send_language,0)
    self.english['command'] = partial(send_language,1)


    def test_plot():
        self.ax.imshow(np.random.normal(0.,1.,size=[1000,1000]),cmap="hot",aspect="auto")
        self.fig.canvas.draw()

    self.plot['command'] = test_plot

    def get_fig_ax(fig,ax):
        self.fig = fig
        self.ax = ax
        
    subscribe('FIG,AX',get_fig_ax)
    publish('REQUEST_FIG,AX')
