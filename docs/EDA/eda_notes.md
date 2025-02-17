
# Pandas
## load
    read_csv(file_path,na_values=[]/{c1:[],c2:[]})

##          Date Time
    to_datetime () - "%m-%d-%Y"
## Transformations
    apply(lambda x:x)
    astype(new_type)
    apply(float)==astype(float)
    replace([from_values],to_value)
    fillna( groubpy - transform(<function>))
    quantile(0.25/0.75)
## Cleaning
    drop_duplicates(keep="first")
    reset_index(drop=True)

## Analysis
    info()
    describe(include="all).T
    unique()  -> returns list (array of unique values)
    nunique() -> returns integer (no of unique values)
    isnull()/isna()
        .count() -- equals to total no of records
        .sum().  -- equals to total no of records with null value
        .value_count() - group by isnull
    corr()
## Others
    pd.cut(x,bins,labels,right) - to create bins
    
# Pandas.api
    from pandas.api.types import is_string_dtype
# ************************************
# Numpy

        np.nan (Not a Number)

# Transformation functions
    np.clip(Series,lower_whisker,higher_whisker)

