Frame('pageaddframe',link='guidesigner/PageAddFrame.py').grid(row=0)
Frame('pageindexframe',link='guidesigner/PageIndexFrame.py').grid(row=1)

### CODE ===================================================


def refresh_layout(
    pageaddframe = widget('pageaddframe'),
    pageindexframe = widget('pageindexframe')
    ):
    if this().Layout == NOLAYOUT:
        pageaddframe.grid()
        pageindexframe.unlayout()
    elif this().Layout == PAGELAYOUT:
        pageaddframe.unlayout()
        pageindexframe.grid()

do_receive('BASE_LAYOUT_REFRESH',refresh_layout)

### ========================================================

