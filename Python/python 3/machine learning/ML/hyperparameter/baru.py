import pandas as pd 

def outlier(data, parameter):
    q1 = data[parameter].quantile(0.25)
    q3 = data[parameter].quantile(0.75)
    iqr = q3 - q1 
    
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    
    clean = data[(data[parameter] >= lower) & (data[parameter] <= upper)]
    
    return clean