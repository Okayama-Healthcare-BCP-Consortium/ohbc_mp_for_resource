import pandas as pd
from model import mp

if __name__ == "__main__":

    sheet2df = pd.read_excel('./data.xlsx', sheet_name=None)    
    
    problem2result = dict()
    
    for sheet, df in sheet2df.items():
        problem2result[sheet] = mp.resource_maximize(df, isBinary=False)

    print(problem2result)