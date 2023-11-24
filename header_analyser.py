import pandas as pd

def get_header_type(dataset):

    headers_list = ["corruption", "human_trafficking"]

    df = pd.read_csv(dataset)
    headers = df.columns.tolist()
    for header in headers:
        if header in headers_list:
            return header

print(get_header_type("human_tr.csv"))
