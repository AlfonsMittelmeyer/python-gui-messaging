Toplevel('Edit_Text',**{'title': 'Edit Text', 'grid_cols': '(9, 75, 0, 0)', 'bg': '#b9b9b9', 'grid_multi_cols': '[9, (0, 10, 0, 0), (8, 10, 0, 0)]', 'grid_multi_rows': '[5, (0, 10, 0, 0), (2, 5, 0, 0), (4, 5, 0, 0)]', 'grid_rows': '(5, 25, 0, 0)'})

Button('Cancel',**{'text': 'Cancel', 'bd': '3'}).grid(**{'column': '6', 'row': '3'})
Button('OK',**{'text': 'OK', 'width': '6', 'bd': '3'}).grid(**{'column': '7', 'sticky': 'e', 'row': '3'})
Text('Text',wrap ='word').grid(**{'column': '1', 'columnspan': '7', 'row': '1'})

### CODE ===================================================

def parent_destroy(parent=container()):
    selection_before = Selection()
    parent.destroy()
    if widget_exists(selection_before._widget): setSelection(selection_before)
    else: send("SELECTION_CHANGED")

widget('Cancel').do_command(parent_destroy)

def Access(widget_for_text):

    def store_text(text_field = widget('Text'),widget_for_text = widget_for_text):
        widget_for_text.setconfig('text',text_field.get("1.0",'end-1c'))
        selection_before = Selection()
        text_field.master.destroy()
        if widget_exists(selection_before._widget):
            setSelection(selection_before)
            send("SHOW_CONFIG",this()) # should see, that the text has changed
        else: send("SELECTION_CHANGED")
       
    widget('OK').do_command(store_text)

    widget('Text').delete(1.0, END)	
    widget('Text').insert(END,widget_for_text.getconfig('text'))

### ========================================================
