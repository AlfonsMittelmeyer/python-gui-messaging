Toplevel('toplevel',**{'grid_multi_cols': "[7, (0, 10, 0, 0, 'space'), (1, 200, 0, 0), (2, 10, 0, 0, 'space'), (4, 10, 0, 0, 'space'), (6, 10, 0, 0, 'space')]", 'grid_multi_rows': "[10, (0, 10, 0, 0, 'space'), (2, 10, 0, 0, 'space'), (4, 10, 0, 0), (5, 10, 0, 0, 'space'), (6, 63, 0, 0), (7, 10, 0, 0, 'space'), (9, 10, 0, 0, 'space')]", 'bd': 2, 'title': 'Select Font', 'grid_cols': '(7, 87, 0, 0)', 'relief': 'groove', 'grid_rows': '(10, 21, 0, 0)'})

ttk.Combobox('font',**{'fill by text': 'Helvetica\nTimes\nCourier\nTkDefaultFont\nTkTextFont\nTkFixedFont\nTkMenuFont\nTkHeadingFont\nTkCaptionFont\nTkSmallCaptionFont\nTkIconFont\nTkTooltipFont', 'width': 0, 'cursor': 'xterm'}).grid(column=1, sticky='new', row=3)
Label('l_font',**{'text': 'font family'}).grid(column=1, row=1)
Label('l_fontsize',**{'text': 'size'}).grid(column=3, row=1)
ttk.Combobox('fontsize',**{'fill by text': '', 'width': 0}).grid(column=3, sticky='new', row=3)
Label('lstyle',**{'text': 'style'}).grid(column=5, row=1)
Frame('styles')
goIn()

Checkbutton('bold',**{'font': 'TkDefaultFont 9 {bold }', 'offvalue': '', 'onvalue': 'bold ', 'text': ' bold', 'anchor': 'w'})
Checkbutton('italic',**{'font': 'TkDefaultFont 9 {italic }', 'offvalue': '', 'onvalue': 'italic ', 'text': ' italic', 'anchor': 'w'})
Checkbutton('underline',**{'font': 'TkDefaultFont 9 {underline }', 'offvalue': '', 'onvalue': 'underline ', 'text': ' underline', 'anchor': 'w'})
Checkbutton('overstrike',**{'font': 'TkDefaultFont 9 {overstrike }', 'offvalue': '', 'onvalue': 'overstrike ', 'text': ' overstrike', 'anchor': 'w'})

widget('bold').pack(fill='x')
widget('italic').pack(fill='x')
widget('underline').pack(fill='x')
widget('overstrike').pack(fill='x')

goOut()
grid(padx=6, column=5, sticky='nesw', row=3)
ttk.Separator('separator',**{'orient': 'vertical'}).grid(column=2, sticky='ns', row=0, rowspan=5)
ttk.Separator('separator',**{'orient': 'vertical'}).grid(column=4, sticky='ns', row=0, rowspan=5)
ttk.Separator('separator').grid(columnspan=7, sticky='ew', row=2)
Label('example',**{'text': 'Font Example', 'fg': 'black', 'bg': 'white'}).grid(column=1, columnspan=5, sticky='nesw', row=6)
ttk.Separator('separator').grid(columnspan=7, sticky='esw', row=4)
Button('quit',**{'text': 'quit'}).grid(column=5, sticky='nes', row=8)

### CODE ===================================================

def Access(font_widget,insert_entry):

    from tkinter import font

    widget('quit').do_command(lambda cont = container(): cont.destroy())

    values = list(widget('font')['values'])
    sorted_list = list(font.families())
    sorted_list.sort()
    for element in sorted_list:
        values.append(element)
    widget('font')['values'] = tuple(values)
    widget('font').delete(0,'end')
    widget('font').insert(0,'TkDefaultFont')

    widget('fontsize')['values'] = tuple([ x for x in range(4,73) ])


    example = widget('example')

    cbox_font = widget('font')
    cbox_size = widget('fontsize')
    

    w_bold = widget('.','styles','bold')
    v_bold = StringVar()
    w_bold['variable'] = v_bold
    w_bold.variable = v_bold

    w_italic = widget('.','styles','italic')
    v_italic = StringVar()
    w_italic['variable'] = v_italic
    w_italic.variable = v_italic

    w_underline = widget('.','styles','underline')
    v_underline = StringVar()
    w_underline['variable'] = v_underline
    w_underline.variable = v_underline


    w_overstrike = widget('.','styles','overstrike')
    v_overstrike = StringVar()
    w_overstrike['variable'] = v_overstrike
    w_overstrike.variable = v_overstrike


    def font_selected():
        try:
            size = int(cbox_size.get())
        except ValueError:
            size = 9

        style = v_bold.get()+v_italic.get()+v_underline.get()+v_overstrike.get()
        example['font'] = (cbox_font.get(),size,style)

        if widget_exists(font_widget):
            font_widget['font'] = (cbox_font.get(),size,style)

        if widget_exists(insert_entry):
            font = font_widget['font']
            insert_entry.delete(0,'end')
            insert_entry.insert(0,font)

    cbox_font.do_event('<<ComboboxSelected>>',font_selected)
    cbox_font.do_event('<Return>',font_selected)

    cbox_size.do_event('<<ComboboxSelected>>',font_selected)
    cbox_size.do_event('<Return>',font_selected)

    w_bold.do_command(font_selected)
    w_italic.do_command(font_selected)
    w_underline.do_command(font_selected)
    w_overstrike.do_command(font_selected)

    def analyze_font(font):
        font = str(font)
        font = font.strip()

        if font:
            if font[0] == '{':
                pos = font.find('}')
                font_family = font[1:pos].strip()
                font = font[pos+1:]
            else:
                pos = font.find(' ')
                if pos > 0:
                    font_family = font[:pos]
                    font = font[pos:]
                else:
                    font_family = font
                    font = ''
            font  = font.strip()

        else:
            font_family = font
            

        if font:
            pos = font.find(' ')
            if pos > 0:
                size = font[:pos]
                font = font[pos:]
            else:
                size = font
                font = ''
                    
        else:
            size = '9'

        cbox_font.delete(0,'end')
        cbox_font.insert(0,font_family)

        cbox_size.delete(0,'end')
        cbox_size.insert(0,size)

        if 'underline' in font:
            v_underline.set('underline ')

        if 'bold' in font:
            v_bold.set('bold ')
            
        if 'italic' in font:
            v_italic.set('italic ')

        if 'overstrike' in font:
            v_overstrike.set('overstrike ')

    widget('example').setconfig('font',font_widget['font'])
    analyze_font(font_widget['font'])
    container().after(100,lambda cont = container():cont.geometry(''))

    
### ========================================================

