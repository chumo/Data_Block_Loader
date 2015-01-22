def Data_Block_Loader(fname,keytext,instance=1,skip=0):
    '''Loads a block of data from a file and returns a list of tuples,
    with each tuple corresponding to one column of the data block.
    
    Parameters
    ----------
    fname : a string representing the filename 
            (including a full path if the file is not in the working directory).

    keytext : any identification text at the head of the data block that is to be loaded.
    
    instance : (optional) If keytext appears in more than one data block header, 
                load the block in the position indicated by instance.

    skip : (optional) The number of lines to skip just after the header of the data block
            before starting loading data.    
    '''
    
    #- Read the list of file lines.
    f = open(fname)
    lines = f.readlines()
    f.close()

    #- Eliminate newline and return characters, if any.    
    numlines = len(lines)
    lines = [lines[i].replace('\n','').replace('\r','') for i in range(numlines)]
    
    #- Loop until keytext is found, and load data line by line as long as the line text is not empty and can be casted to float.
    rows = []
    inst = 1
    
    for i in range(numlines):
        if keytext in lines[i] and inst == instance:
            for j in range(i+1+skip,numlines):
                try:
                    #- Split the line text. Replace commas (if any) because split() won't interpret them as separators.
                    splitted_list = lines[j].replace(',',' ').split() 
                    if len(splitted_list) == 0:
                        raise ValueError
                    rowdata = [float(splitted_list[i]) for i in range(len(splitted_list))]
                    rows.append(rowdata)
                except ValueError: #- The data block has finished because the line text cannot be casted to float.
                    break
            break
        elif keytext in lines[i]:
            inst += 1

    #- Ensure that all rows have the same number of points. If not, fill with nan (not a number)
    if len(rows) > 0:
        rows_lengths = [len(rows[i]) for i in range(len(rows))]
        max_length = max(rows_lengths)
    
        for i in range(len(rows)):
            for j in range(max_length-rows_lengths[i]):
                rows[i].append(float('nan'))
    
    #- Transpose the data so that every tuple is a column of the data block.
    block = list(zip(*rows)) #The function list() was added to make it Python 3 compatible.
    
    #- Inform and return.
    if len(block) > 0:
        print('{0} columns were loaded, each with {1} rows.'.format(len(block),len(block[0])))
        return block
    else:
        print('The block was not found or is empty.')
        return None