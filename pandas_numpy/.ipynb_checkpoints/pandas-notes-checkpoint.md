
# Series

# Data frame
Create
	.DataFrame()
	1. Map
		{ 'col1':[val1,val2,val3],,
		  'col2':[val1,val2,val3]
		}
	2. 
Methods
	.head(int)
	.tail(int)
	.set_index('col1')
	.reset_index(inplace=True)
	
Access
	df['column_name']
	df[['col1','col2']]
	df[start:stop:step]

	loc->
	df.loc[1]
	df.loc['<<index_values>>']

	Conditions
	df[<<condition>>]
	df['col1'] =? 
	df['col1'] > < >= <= !=

Variables
	.shape
	.columns
	.<<column_names>> to print values of that column
	.index
# Cleansing

	.fillna(any_value)
	.fillna({'col1':v1,
			 'col2':v2,
			 'col3':v3
			 })
	.fillna(method='ffill/bfill', axis="columns",limit)
	.interpolate(method=linear/time)
	.dropna(how="all/",thresh=1)
	.date_range()
	.DatatimeIndex(dt)
	.reindex
	.replace([from_values],to_value)
	.replace({'col1':values,
			  'col2':values
			  },to_value)
	.replace({'old_v1':new_v1,
			  'old_v2':new_v2
			  })
	.replace(regexp=True)
	.replace(list<f_values>,list<n_values>)
# Analysis methods
	.describe()
	.count()
	.min()
	.max()
	.mean()
	.mode()
	.median()
	.std()

	[25%/50%75%]
# Exploratory Analysis
	.groupby()
		.get_group('g_value1')
		.plot()
		.apply()
		.agg()
		.aggregate()
		.transform()
		.pipe()
		.filter()

		.all()
		.any()
		.bfill()

