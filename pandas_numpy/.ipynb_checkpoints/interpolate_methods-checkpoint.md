	default 
		‘linear’
	
	‘linear’: 
		Ignore the index and treat the values as equally spaced. This is the only method supported on MultiIndexes.

	‘time’: 
		Works on daily and higher resolution data to interpolate given length of interval.

	‘index’, ‘values’: 
		use the actual numerical values of the index.

	‘pad’: 
		Fill in NaNs using existing values.

	‘nearest’, ‘zero’, ‘slinear’, ‘quadratic’, ‘cubic’, ‘barycentric’, ‘polynomial’: 
		Passed to scipy.interpolate.interp1d, whereas ‘spline’ is passed to scipy.interpolate.UnivariateSpline. These methods use the numerical values of the index. Both ‘polynomial’ and ‘spline’ require that you also specify an order (int), e.g. df.interpolate(method='polynomial', order=5). Note that, slinear method in Pandas refers to the Scipy first order spline instead of Pandas first order spline.

	‘krogh’, ‘piecewise_polynomial’, ‘spline’, ‘pchip’, ‘akima’, ‘cubicspline’: 
		Wrappers around the SciPy interpolation methods of similar names. See Notes.

	‘from_derivatives’: 
		Refers to scipy.interpolate.BPoly.from_derivatives.