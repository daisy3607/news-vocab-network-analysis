import matplotlib.pyplot as plt
import pandas as pd
import math

# load freq & cofreq data
df_node = pd.read_csv('UDN_0203/freq_aboriginal.csv', encoding='big5')
df_line = pd.read_csv('UDN_0203/cofreq_aboriginal.csv', encoding='big5', header=None)
df_line = df_line[0:][1:]

# preprocessing
### if numbers with comma
freq_cnt= list(df_node.ix[:,1])
freq_cnt = [int(freq.replace(',', '')) for freq in freq_cnt]
symbol_size_value = [int(i/50) for i in freq_cnt] # set values

# represent as json
json_node = [{'id': i, 'name': df_node.ix[i,0], 'symbolSize': symbol_size_value[i]} for i in range(len(df_node))]

# build dictionary
node_dict = {v: i for i, v in enumerate(list(df_node.ix[:,0]))}

# create links
value = list(map(float, df_line.ix[:,3].values))
value = list(map(int, value))
links = list(zip(list(df_line.ix[:,1].values), list(df_line.ix[:, 2].values), value))

# set link rules
link = list(filter(lambda x: x[0] != x[1] and x[2] > 4, links))

# json links
json_links = [{'source': node_dict[n1], 'target': node_dict[n2], 
               'lineStyle': {'normal': {'width': int(value/3)}}} for n1, n2, value in link]
