'''
November 2017 by Daisy Tsai.
daisy3607@gmail.com

'''
import os
import docx
import re
import numpy as np
import pandas as pd

def load_docx(docx_file):
    fullText = ""
    doc = docx.Document(docx_file)
    for para in doc.paragraphs:
        fullText += para.text
    filtrate = re.compile(u'[^\u4E00-\u9FA5]') # only keep Chinese characters
    filtered_doc = filtrate.sub(r'', fullText)

    return filtered_doc

# for corpus of txt file
def load_txt(text_file):
    with open(text_file, 'rb') as corpus:
        raw_doc = corpus.read().decode('Big5')
        filtrate = re.compile(r'[^\u4E00-\u9FA5]')#非中文
        filtered_doc = filtrate.sub(r'', raw_doc)

    return filtered_doc

def load_txt_big5(text_file):
    with open(text_file, encoding='utf-8' ,errors='replace') as corpus:
        raw_doc = corpus.read()
        filtrate = re.compile(r'[^\u4E00-\u9FA5]')#非中文
        filtered_doc = filtrate.sub(r'', raw_doc)

    return filtered_doc

def load_corpus(target_dir):
    # find all path of doc
    for file in target_dir:
        path = os.path.join(root_dir, file)
        target_path.append(path)
    target_path = target_path[1:]

    # save all the corpus: aboriginal, country, medical_news, medical_policy
    All_corpus = []   
    for dir_path_name in target_path:
        class_corpus = ""
        for file in os.listdir(dir_path_name):
            target_filepath = os.path.join(dir_path_name, file)
            # load file text
            if(file.endswith('.docx')):
                doc = load_docx(target_filepath)
            if(file.endswith('.txt')):
                doc = load_txt_big5(target_filepath)
    #         # combine text to 
            class_corpus += doc
        All_corpus.append(class_corpus)
    
    return All_corpus


    