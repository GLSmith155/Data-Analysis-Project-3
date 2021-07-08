import pandas as pd
import numpy as np
import time

start = time.time()

file_name = 'step 7 example data.csv'
lib_name = 'tech_tagsnewer.csv'

df = pd.read_csv(file_name, engine = 'python', error_bad_lines = False)
#df1 = pd.read_csv(file_name, engine = 'python', error_bad_lines = False)
df.fillna(0, inplace = True)
#df['Match 1'] = None

lib = pd.read_csv(lib_name).dropna(subset=['Tech Tags'])
updated_file_name = file_name[:-4] + '_matched.csv'

listname = lib['Tech Tags'].tolist()

match_list = ['Match 1', 'Match 2', 'Match 3', 'Match 4', 'Match 5', 'Match 6', 'Match 7', 'Match 8', 'Match 9', 'Match 10', 'Match 11', 'Match 12', 'Match 13', 'Match 14', 'Match 15', 'Match 16', 'Match 17', 'Match 18', 'Match 19', 'Match 20', 'Match 21', 'Match 22']
current_match = 0
global x
x = -1

#df2[match_list[current_match]][df2['Tech Tags'].str.contains(fr'\b{listname[x]}\b')] = listname[x]
#Number of Rows = 
for loop in range(3761):
    e = loop + 1
    df['Match ' + str(e)] = None 
    x += 1
    #Use new column for .contains
    df['Match ' + str(e)][df['Description'].str.contains(fr'\b{listname[x]}\b')] = listname[x]
    print(listname[x])
    #Move all empty cells to the right
    df = df.apply(lambda x: sorted(x, key=pd.isnull), 0)
    
    #Delete empty columns in Match 30 on after moving all data to the left...
    df = df.dropna(axis = 1, how = 'all')

    #Delete 'Match ' + str(e)
    
    #Iterates up tag list
    
    
df.to_csv(updated_file_name, index = False)



end = time.time()
process_time = end - start
print('\nTime it took for script to run : {0}'.format(process_time))  
print('done')
