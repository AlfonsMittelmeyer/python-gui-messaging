def grid_configure_multi(data):
    count = data[0]
    multi = []
    for i in range(count): multi.append([False,None])
    for i in range(len(data)):
        if i != 0:
            multi[data[i][0]] = [True,{'minsize':data[i][1],'pad':data[i][2],'weight':data[i][3]}]
    return multi

def grid_configure_cols(cont):

    cols = cont.grid_conf_cols[0]

    if len(cont.grid_multi_conf_cols) == 0:
        for i in range(cols): cont.grid_multi_conf_cols.append([False,None])

    to_insert =  {'minsize':cont.grid_conf_cols[1],'pad':cont.grid_conf_cols[2],'weight':cont.grid_conf_cols[3]}
    
    for col in range(cols):
        if cont.grid_multi_conf_cols[col][0] == False:
            cont.grid_multi_conf_cols[col][1] = dict(to_insert)

    for col in range(cols):
        cont.grid_columnconfigure(col,**(cont.grid_multi_conf_cols[col][1]))

def grid_configure_rows(cont):

    rows = cont.grid_conf_rows[0]

    if len(cont.grid_multi_conf_rows) == 0:
        for i in range(rows): cont.grid_multi_conf_rows.append([False,None])

    to_insert =  {'minsize':cont.grid_conf_rows[1],'pad':cont.grid_conf_rows[2],'weight':cont.grid_conf_rows[3]}
    
    for row in range(rows):
        if cont.grid_multi_conf_rows[row][0] == False: cont.grid_multi_conf_rows[row][1] = dict(to_insert)

    for row in range(rows):
        cont.grid_rowconfigure(row,**(cont.grid_multi_conf_rows[row][1]))

def clear_grid(cont):

    row_conf = cont.grid_conf_rows
    if row_conf != None:
        old_rows = row_conf[0]
        unconf_rows = old_rows
        if cont.grid_conf_individual_done:
            unconf_rows += 1
        for i in range(unconf_rows):
            cont.grid_rowconfigure(i,minsize = 0,pad=0,weight=0)

    col_conf = cont.grid_conf_cols
    if col_conf != None:
        old_cols = col_conf[0]
        unconf_cols = old_cols
        if cont.grid_conf_individual_done:
            unconf_cols += 1
        for i in range(unconf_cols):
            cont.grid_columnconfigure(i,minsize = 0,pad=0,weight=0)
    
    cont.reset_grid()

def grid_table(container,grid_rows = None, grid_cols = None, grid_multi_rows = None, grid_multi_cols = None):
    if grid_multi_rows != None:
        container.grid_conf_individual_has = True
        container.grid_multi_conf_rows = grid_configure_multi(eval(grid_multi_rows))

    if grid_multi_cols != None:
        container.grid_conf_individual_has = True
        container.grid_multi_conf_cols = grid_configure_multi(eval(grid_multi_cols))

    if grid_cols != None:
        container.grid_conf_cols = eval(grid_cols)
        grid_configure_cols(container)

    if grid_rows != None:
        container.grid_conf_rows = eval(grid_rows)
        grid_configure_rows(container)
