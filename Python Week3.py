# Dataframe

# 1. Function
## View Data
### view the top 5 rows of the dataset using the head() function
df.head()
### or
df.head(10)
### or
df.tail()

## Get basic information
df.info()

df.columns.values 
df.index.values

## view the dimensions of the dataframe
df.shape

# in pandas axis=0 represents rows (default) and axis=1 represents columns.
df.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)


# There are two ways to filter on a column name:
# Method 1: Quick and easy, but only works if the column name does NOT have spaces or special characters.

    df.column_name 
        #(returns series)
# Method 2: More robust, and can filter on multiple columns.
    df['column']  
        #(returns series)
    df[['column 1', 'column 2']] 
        #(returns dataframe)
      
      
# There are main 3 ways to select rows:
    df.loc[label]        
        #filters by the labels of the index/column
    df.iloc[index]       
        #filters by the positions of the index/column
