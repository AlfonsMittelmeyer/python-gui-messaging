config(**{'grid_cols': '(4, 75, 0, 0)', 'grid_multi_cols': '[4, (0, 11, 0, 0), (1, 67, 0, 0), (3, 10, 0, 0)]', 'grid_multi_rows': '[8, (0, 10, 0, 0), (5, 30, 0, 0), (7, 7, 0, 0)]', 'grid_rows': '(8, 25, 0, 0)'})

Label('Label',**{'text': 'PanedWindow', 'font': 'TkDefaultFont 12 bold', 'fg': 'blue'}).grid(**{'column': '1', 'sticky': 'w', 'row': '1'})
Message('Message',**{'text': "PanedWindows have a sash with a handle and the sash with the handle may be moved. But for doing such layouts the full functionality of the GuiDesigner is needed.\n\nMaybe you remember the photo image of the GuiDesigner in the beginning?\n\nThere are two very important menu entries in the GuiDesigner: 'Config ON' and 'Layout ON', which were not discussed yet.", 'pady': '10', 'padx': '10', 'width': '600', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'ew', 'columnspan': '2', 'row': '3'})
Message('Message2',**{'text': 'So, it would say: explore self', 'font': 'TkDefaultFont 9 bold', 'width': '600', 'bg': 'white'}).grid(**{'column': '1', 'sticky': 'ew', 'columnspan': '2', 'row': '5'})
PanedWindow('PanedWindow',**{'bd': '5', 'sashrelief': 'raised', 'bg': '#76a9d9', 'sashwidth': '8', 'handlesize': '20', 'showhandle': '1', 'height': '100', 'width': '600'})
goIn()

Label('Pane 1',**{'text': 'Pane 1', 'bg': 'black', 'fg': 'white'})
Label('Pane 2',**{'text': 'Pane 2', 'bg': 'red'})
Label('Pane 3',**{'text': 'Pane 3', 'bg': 'gold'})

widget('Pane 1').pane()
widget('Pane 2').pane()
widget('Pane 3').pane()
container().trigger_sash_place(300,0,200,5)
container().trigger_sash_place(600,1,400,5)

goOut()
grid(**{'column': '1', 'columnspan': '2', 'pady': '5', 'row': '2'})
Label('designer_image').grid(**{'column': '1', 'columnspan': '2', 'pady': '7', 'row': '4'})
Label('gui_link',**{'text': 'PanedWindow once more', 'font': 'TkDefaultFont 12 bold underline', 'fg': 'blue'}).grid(**{'column': '2', 'sticky': 'e', 'row': '6'})

### CODE ===================================================
widget("designer_image").mydata = PhotoImage(file="introduction/start_image.gif")
widget("designer_image")['image'] = widget("designer_image").mydata

def start_gui(me):
    me.destroy()
    gotoTop()
    goto('Introduction')
    goIn()
    goto('Inside')
    here = this()
    widget("MouseMenu").destroy()
    widget(here,"designer_image").destroy() # could crash
    
    gui()
    gotoTop()
    goto('Introduction')
    goIn()
    goto('Inside')
    goIn()
    goto('PanedWindow')

widget('gui_link').do_event('<Button-1>',start_gui,wishWidget=True)
### ========================================================
