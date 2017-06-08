Frame('paneaddframe',link='guidesigner/PaneAddFrame.py').grid(row=0)
Frame('paneindexframe',link='guidesigner/PaneIndexFrame.py').grid(row=1)
LabelFrame('sashframe',link='guidesigner/PaneLayoutSashes.py')

### CODE ===================================================


def refresh_layout(
    paneaddframe = widget('paneaddframe'),
    paneindexframe = widget('paneindexframe'),
    #sashframe = widget('sashframe')
    ):
    if this().Layout == NOLAYOUT:
        paneaddframe.grid()
        paneindexframe.unlayout()
        #sashframe.unlayout()
    elif this().Layout in (PANELAYOUT,TTKPANELAYOUT):
        paneaddframe.unlayout()
        paneindexframe.grid()

do_receive('BASE_LAYOUT_REFRESH',refresh_layout)

### ========================================================

