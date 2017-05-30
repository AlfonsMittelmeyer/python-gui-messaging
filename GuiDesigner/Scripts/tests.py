# -*- coding: utf-8 -*-
Button('english',text='english')
Button('german',text='german')
Button('plot',text='plot')

widget('german').pack(side='left')
widget('english').pack(side='left')
widget('plot').pack(side='left')

### CODE ===================================================

class TestApplication:

    def __init__(self,
                 german = widget('german'),
                 english = widget('english'),
                 plot = widget('plot')
                 ):

        german['command'] = partial(self.send_language,0)
        english['command'] = partial(self.send_language,1)
        plot['command'] = self.test_plot

        subscribe('FIG,AX',self.get_fig_ax)
        publish('REQUEST_FIG,AX')
        
    def get_fig_ax(self,fig,ax):
        self.fig = fig
        self.ax = ax
        
    def send_language(self,index):
        language_lists = (
            ( 'Sprache',('deutsch','german'),None,('englisch','english'),('französisch','french')),
            ( 'Language',('english','english'),None,('french','french'),('german','german'))
        )
        publish('MENU_LANGUAGE',language_lists[index])


    def test_plot(self):
        self.ax.imshow(np.random.normal(0.,1.,size=[1000,1000]),cmap="hot",aspect="auto")
        self.fig.canvas.draw()


TestApplication()
            
### ========================================================
