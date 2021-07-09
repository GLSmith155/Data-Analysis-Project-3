import pandas as pd
import numpy as np
import time

start = time.time()

file_name = 'step 7 example data.csv'
lib_name = 'tech_tags_new.csv'

df = pd.read_csv(file_name, engine = 'python', error_bad_lines = False)

#df.drop(['Middle Name', 'Industry', 'Connections', 'Company2'], axis='columns', inplace = True)
df = df[['URL', 'Current Position', 'Job Title', 'Full Name', 'First Name', 'Surname', 'Company', 'Location', 'City', 'State', 'Country', 'Description']]

#Replace missing values with 0 to later shift cells left w/o losing order of original data
df.fillna('0', inplace = True)

selected_columns = df[["Description"]]

lib = pd.read_csv(lib_name).dropna(subset=['Tag Filter'])
updated_file_name = file_name[:-4] + '_matched.csv'

listname = lib['Tag Filter'].tolist()
altname = lib['Alt Name'].tolist()

df2 = selected_columns.copy()

match_list = ['Match 1', 'Match 2', 'Match 3', 'Match 4', 'Match 5', 'Match 6', 'Match 7', 'Match 8', 'Match 9', 'Match 10', 'Match 11', 'Match 12', 'Match 13', 'Match 14', 'Match 15', 'Match 16', 'Match 17', 'Match 18', 'Match 19', 'Match 20', 'Match 21', 'Match 22']
current_match = 0
global x
x = -1

#Number of Rows in library  = x then range(x) in loopy
for loop in range(3774):
    e = loop + 1
    df2['Match ' + str(e)] = None 
    x += 1
    #Find strings through three different search categories depending on location of tag in library.
    if loop < 3750:
        df2['Match ' + str(e)][df2['Description'].str.contains(fr'\b{listname[x]}\b')] = listname[x]
    elif loop < 3763:
        df2['Match ' + str(e)][df2['Description'].str.contains(str(listname[x]))] = altname[x]
    else:
        df2['Match ' + str(e)][df2['Description'].str.contains(str(listname[x]))] = listname[x]
    print(listname[x])
    
    #filtering works with lamda, but it is so slow.
    #df1 = df.apply(lambda x: pd.Series(x.dropna().values), axis=1).fillna('')
    #df1 = df1.reindex(columns=range(len(df.columns)))
    #df1.columns = df.columns
        
    #Move all empty cells to the right
    idx = pd.isnull(df2.values).argsort(axis=1)
    df2 = pd.DataFrame(
    df2.values[np.arange(df.shape[0])[:, None], idx],
    index=df2.index,
    columns=df2.columns,
    ).dropna(how="all", axis=1)
    
    #Delete empty columns in Match 30 on after moving all data to the left...
    df2 = df2.dropna(axis = 1, how = 'all')

col_index = []

#try except for renaming columns
try:
    num_col = len(df2.columns)
    
    for col_loop in range(num_col):
        #app_index = col_loop + 1
        col_index.append(col_loop)
        
    new_names  = ['Description', 'Match 1', 'Match 2', 'Match 3', 'Match 4', 'Match 5', 'Match 6', 'Match 7', 'Match 8', 'Match 9', 'Match 10', 'Match 11', 'Match 12', 'Match 13', 'Match 14', 'Match 15', 'Match 16', 'Match 17', 'Match 18', 'Match 19', 'Match 20', 'Match 21', 'Match 22']
    old_names = df2.columns[col_index]   
    df2.rename(columns = dict(zip(old_names, new_names)), inplace = True)
        
except:
    print('Renaming Issue Encountered')    
    
#Appending df2 to df
AppCol = df2.loc[:, 'Match 1':]
df = df.join(AppCol)

#try except for removing rows with zero matches to make file size smaller as we move to the bad filtering step.
try:
    # If all subsets listed are empty, drop the row.
    # The first column number equals match 1, the second is any remaining column w/ : as max column changes.
    ix = df.loc[:, 'Match 1':].dropna(how='all').index.tolist()
    df = df.loc[ix]
except:
    # The first column number equals match 1, the second number should surpass the total needed just in case.
    ix = df.loc[:, 'Description':].dropna(how='all').index.tolist()
    df = df.loc[ix]  

df.to_csv(updated_file_name, index = False)

end = time.time()
process_time = end - start
print('\nTime it took for script to run : {0}'.format(process_time))  
print('done')
