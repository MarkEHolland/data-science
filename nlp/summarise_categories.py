import torch

import pandas as pd

pd.set_option('display.max_columns', None)

from transformers import AutoTokenizer, pipeline, AutoModelForSeq2SeqLM

import re

from tqdm import tqdm

from IPython.display import display, HTML

 

 

#Provide the path to the Your Say Survey data

ys_data_path = 'C:\\Users\\614246757\OneDrive - BT Plc\\Documents\\HR Analytics\\yoursay_02_2022.csv'

 

## Load the fine-tuned model from the model hub

model_name = "arinze/t5_finetuned_xsum_hr"

#model_name = "facebook/bart-large-cnn"

model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

tokenizer = AutoTokenizer.from_pretrained(model_name)

summarizer = pipeline('summarization', model_name, framework="pt",tokenizer = tokenizer)

 

 

def clean_text(text):

   

    # lowercase

    #text=text.lower()

   

    #remove tags

    text=re.sub("</?.*?>"," <> ",text)

    # Only keep:

    # Letters a-z, A-Z

    # Dots (.)

    # Numbers (\d)

    # Non white space (\s)

 

    text = re.sub('[^a-zA-Z.\d\s]', '', text)

    text = re.sub("\n", '', text) # remove new line character

 

   

    return text

 

def chunks_joined(lst, n):

    """

    Divide a list of sentences into chunks of concatenated n sentences

    """

    all_chunks = []

    for i in range(0, len(lst), n):

        joined_sentences =  lst[i:i + n]

        joined_sentences = ' '.join(str(e) for e in joined_sentences)

        all_chunks.append(joined_sentences)

    return all_chunks

 

 

 

def summarise_categories(ys_data_path = ys_data_path):

    """

    Summary of Comments from YS survey using a fine-tuned summarisation model.

 

    Parameter: CSV file of YS survey

 

    Returns: Individual dataframes of respondents' comments and their corresponding summaries

    as individual files per category

   

    """

 

    ys_data = pd.read_csv(ys_data_path)

    ys_data.drop([0], inplace=True)

    ys_categories = list(ys_data['Q30'].unique())

    ys_categories = [x for x in ys_categories if str(x) != 'nan'] #remove nan from the list

 

    print("Model Max Length: ", tokenizer.model_max_length)

    for category in ys_categories:

        ys_category = ys_data[ys_data['Q30'] == category]

        ys_category = ys_category[~ys_category['Q31'].isnull()]

        ys_category['Q31_cleaned'] = ys_category['Q31'].apply(lambda x:clean_text(x))

        ys_category_corpus = list(ys_category['Q31_cleaned'])

        ys_category_test_chunks  = chunks_joined(ys_category_corpus, 10)

 

        all_category_summaries = []

        print("Summarising ",category, "category...")

        for i in tqdm(range(len(ys_category_test_chunks))):

            token_max_len = len(tokenizer(ys_category_test_chunks[i])['input_ids']) + 2 # Plus 2 factors in the the start of sequence [CLS] and separator [SEP] tokens.

            #print("Token Max length: ", token_max_len)

            # ignore warning message about token indices sequence length (if it occurs once or twice) as this is internally truncated by the model.

            # See issue:

            # https://github.com/explosion/spaCy/discussions/9277#discussioncomment-1374226

           

            if token_max_len > tokenizer.model_max_length:

                category_summary = summarizer(ys_category_test_chunks[i],  min_length = 10,max_length=tokenizer.model_max_length, truncation=True) #min_length of 10 to take care of very short comments

            else:

                category_summary = summarizer(ys_category_test_chunks[i], min_length = 10, max_length=token_max_len, truncation=True)

 

            all_category_summaries.append(category_summary)

 

               

            

        all_category_summaries_cleaned = []

        ## remove the "summary_text" prefix and convert the resulting list of dictionaries to strings

        for text in range(len(all_category_summaries)):

            cleaned_summaries = [d['summary_text'] for d in all_category_summaries[text]]

            all_category_summaries_cleaned.append(" ".join(str(x) for x in cleaned_summaries))

 

        ys_category_summary = pd.DataFrame({'YS_' + category + '_Comment':ys_category_test_chunks, 'Summary': all_category_summaries_cleaned})

        ys_category_summary.to_csv('Summary_for_Comments_in_YS_' + category + '_Category.csv', index=False)

 

 

if __name__ == '__main__':

    summarise_categories()

 