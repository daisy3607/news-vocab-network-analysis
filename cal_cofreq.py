'''
November 2017 by Daisy Tsai.
daisy3607@gmail.com

'''
import numpy as np
import pandas as pd
from parameter import Parameters as hp
from preprocessing import load_corpus

# load corpus
corpus = load_corpus(target_path)

# keywords setting
cur_keywords = medicine_keyword # target keyword
cur_corpus = All_corpus[0] # target corpus

# calculate freq
freq_list=[]
for co_keyword_idx in range(len(cur_keywords)):
    co_frequency = np.zeros(len(cur_keywords))
    co_keyword = cur_keywords[co_keyword_idx]
    #find all the occurrence of a keyword in the corpus
    for key_idx in range(len(cur_keywords)):
        key_count = [m.start() for m in re.finditer(cur_keywords[key_idx],cur_corpus)]
        keyword_length = len(cur_keywords[key_idx])-1
        #print("==========================================================================")
        for co_idx in range(len(key_count)):
            if(co_keyword == cur_keywords[key_idx]):
                co_frequency[key_idx] = 0
            else:
                target_str = cur_corpus[(key_count[co_idx]-window):(key_count[co_idx]+window+keyword_length)]
                co_iter = [m.start() for m in re.finditer(co_keyword,target_str)]
                co_frequency[key_idx] += len(co_iter)
                #print(target_str,"co-iter = ",len(co_iter)," total co-frequency =",co_frequency[key_idx])
    freq_list.append(co_frequency)

# saving as table
medicine_result1 = {
    '共詞關鍵詞':cur_keywords[0],
    '所有關鍵詞': cur_keywords,
    '共詞頻率':freq_list[0]}
result_df = pd.DataFrame(medicine_result1)

for combine_idx in range(1,len(cur_keywords)):
    co_keyword = cur_keywords[combine_idx]
    medicine_result1 = {
        '共詞關鍵詞':[co_keyword for i in range(len(cur_keywords))],
        '所有關鍵詞': cur_keywords,
        '共詞頻率':freq_list[combine_idx]}
    medicine_result1 = pd.DataFrame(medicine_result1)
    result_df = result_df.append(medicine_result1,ignore_index=True)
    
#rearrange
cols = result_df.columns.tolist()
cols = cols[-1:]+cols[0:1]+cols[1:2]
result_df[cols]

#rearrange
cols = result_df.columns.tolist()
cols = cols[-1:]+cols[0:1]+cols[1:2]
result_df[cols]

keyword_frame = pd.DataFrame(cur_keywords)
keyword_frame.to_csv(hp.output_cofreq_table, encoding='big5')