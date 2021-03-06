### CODE ===================================================
import os

def test_syntax(me,textwidget):
    result = True
    selection = Selection()
    setWidgetSelection(me)
    goto("Syntax")
    try:
        compile(str(textwidget.get("1.0",'end-1c').encode('utf-8')),'<string>', 'exec')
        config(text="Syntax OK",fg="#006000")
        pack(side=LEFT)
    except SyntaxError as e:
        config(text="SyntaxError in line "+str(e.lineno),fg="red")
        pack(side=LEFT)
        traceback.print_exc()
        result = False
    setSelection(selection)
    return result

def execute_code(me,textwidget,current_selection,test_Syntax=test_syntax,os=os):
    result = False
    selection = Selection()
    if test_Syntax(me,textwidget):
        try:
            fh = open(os.path.join(os.getcwd(),'Testcode','tempcode.py'),"w",encoding="utf-8")
            is_open = True
        except:
            is_open = False
            setWidgetSelection(me)
            widget("Syntax").config(text="IOError: couldn't open file 'tempcode.py'",fg="red")
        if is_open:
            #fh.write(str(textwidget.get("1.0",'end-1c').encode('utf-8')))
            fh.write(textwidget.get("1.0",'end-1c'))
            fh.close()
            undo_receiveAll(current_selection._widget)
            setWidgetSelection(current_selection._widget)
            goIn()
            exec(compile(open('Testcode/tempcode.py', "r",encoding="utf-8").read(), 'Testcode/tempcode.py', 'exec'))
            #eval(compile(textwidget.get("1.0",'end-1c'),'<string>', 'exec'))
            setWidgetSelection(me)
            widget("Syntax").config(text="Code Run OK",fg="#006000")
            result = True
    setSelection(selection)
    return result

def do_OK(me,textwidget,current_selection,exec_code = execute_code):
    if exec_code(me,textwidget,current_selection):
        current_selection._widget.CODE = textwidget.get("1.0",'end-1c')
        me.myRoot().destroy()
        send('SHOW_SELECTION_UPDATE')

def create_LoadFrame():
    Frame('LoadFrame')
    goIn()
    Label('Label',text="File:").pack(side=LEFT)
    Entry('Entry',width=15).pack(side=LEFT)
    this().delete(0,END)
    this().insert(0,"tempcode.py")
    Button("Load",text="Load").pack(side=LEFT)
    Label("IOError")
    goOut()

def load_from_file(me,textwidget,os=os):
    selection = Selection()
    setWidgetSelection(me)
    widget('IOError').unlayout()
    try:
        fh = open(os.path.join(os.getcwd(),'Testcode',widget('Entry').get()),'r',encoding="utf-8")
        textwidget.delete(1.0, END)	
        textwidget.insert(END,fh.read())
        fh.close()
    except:
        widget('IOError').config(text="IOError: couldn't open file '"+widget('Entry').get()+"'",fg="red")
        widget('IOError').pack(side=LEFT)
    setSelection(selection)

def create_toplevel(message,ok_command = do_OK,load_frame=create_LoadFrame,load_execute = load_from_file,run_code=execute_code,do_test=test_syntax):

    current_selection = Selection()
    code = this().CODE
    cdApp()
    Toplevel("ToplevelCodeEdit",title = "Code Edit for "+ message)
    Text('CodeText',width=120,font=('Courier New',11)).insert(END,code)
    textwidget = widget('CodeText')

    Frame('Frame')
    goIn()
    Button('OK',text='OK',bg="lightgreen",width=6).pack(side=RIGHT)
    do_command(ok_command,(textwidget,current_selection),True)
    load_frame()
    pack(side=LEFT)
    goIn()
    widget("Load").do_command(load_execute,textwidget,True)
    widget("Entry").do_event('<Return>',load_execute,textwidget,True)
    goOut()
    Button('Cancel',text='Cancel',bg="#ff7040").pack(side=RIGHT)
    do_command(lambda this=this(): this.myRoot().destroy())
    Button('RunCode',text='Run Code').pack(side=RIGHT)
    do_command(run_code,(textwidget,current_selection),True)
    Label('Syntax',text="Syntax OK",fg="#006000",padx=5)
    Button('Test',text='Test Syntax').pack(side=RIGHT)
    do_command(do_test,textwidget,True)
    goOut()
    widget('CodeText').pack()
    widget('Frame').pack(anchor='e')
    setSelection(current_selection)
    goIn()
    send('SELECTION_CHANGED',this())


do_receive('EDIT_CODE',create_toplevel,wishMessage=True)


### ========================================================
