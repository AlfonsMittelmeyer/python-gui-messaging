LabelFrame('PackLayout',link="guidesigner/PackLayout.py")
grid(sticky='ew',row='0')

LabelFrame('GridLayout',link="guidesigner/GridLayout.py")
grid(sticky='ew',row='1')

LabelFrame('PlaceLayout',link="guidesigner/PlaceLayout.py")
grid(sticky='ew',row='2')

LabelFrame('PaneLayout',link="guidesigner/PaneLayout.py")
grid(sticky='ew',row='3')

LabelFrame('ItemLayout',link="guidesigner/MenuItemLayout.py")
grid(sticky='ew',row='4')

LabelFrame('MenuLayout',link="guidesigner/MenuLayout.py")
grid(sticky='ew',row='5')


### CODE ===================================================

# A routine for the pack and he grid layout: pack and grid must not occur in the same parent. ------------------------------------
# This would cause a system hang up of TkInter. If the parent (container) contains already the other layout (pack or grid),
# the pack or grid portion will be hidden (unlayout)

def hide_pack_or_grid(packly=widget('PackLayout'),gridly=widget('GridLayout'),placely=widget('PlaceLayout'),panely=widget('PaneLayout'),itemly=widget('ItemLayout'),menuly=widget('MenuLayout')):

    if this().Layout != LAYOUTNEVER:

        if this().tkClass == StatTkInter.Menu:
            packly.unlayout()
            gridly.unlayout()
            placely.unlayout()
            itemly.unlayout()
            panely.unlayout()
            menuly.grid()
            send("ENABLE_SASH_LIST",False)

        elif container() != this() and container().tkClass == StatTkInter.PanedWindow:
            packly.unlayout()
            gridly.unlayout()
            placely.unlayout()
            itemly.unlayout()
            menuly.unlayout()
            panely.grid()
            send("ENABLE_SASH_LIST",True)

        elif container().Layout == MENULAYOUT or this().Layout == MENUITEMLAYOUT:
            packly.unlayout()
            gridly.unlayout()
            placely.unlayout()
            panely.unlayout()
            menuly.unlayout()
            itemly.grid()
            send("ENABLE_SASH_LIST",False)
        else:
            placely.grid()
            packly.grid()
            gridly.grid()
            panely.unlayout()
            menuly.unlayout()
            itemly.unlayout()
            send("ENABLE_SASH_LIST",False)
            cont = container()
            if container() == this() and container().master != None:
                cont = container().master
            cont_layouts = getContLayouts(cont)
            if cont_layouts & GRIDLAYOUT:
                if packly.Layout != NOLAYOUT: packly.unlayout()
            elif packly.Layout == NOLAYOUT: packly.grid()
            if cont_layouts & PACKLAYOUT:
                if gridly.Layout != NOLAYOUT: gridly.unlayout()
            elif gridly.Layout == NOLAYOUT: gridly.grid()

do_receive('BASE_LAYOUT_REFRESH', hide_pack_or_grid)

### ========================================================
