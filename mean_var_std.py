import numpy as np

def calculate(list):
    calculations = {'mean' : '', 'variance' : '', 'standard deviation' : '', 'max' : '', 'min' : '', 'sum' : ''}
    if len(list) <9:
        raise ValueError('List must contain nine numbers.')
    else:        
        arr_test = np.array(list).reshape((3, 3))
        #print(arr_test.mean())
        #'measure': [axis1, axis2, flattened],
        arr_mean = [ arr_test.mean(0).tolist(), arr_test.mean(1).tolist(), arr_test.mean().tolist() ]
        arr_var = [ arr_test.var(0).tolist(), arr_test.var(1).tolist(), arr_test.var().tolist() ]
        arr_std = [ arr_test.std(0).tolist(), arr_test.std(1).tolist(), arr_test.std().tolist() ]
        arr_max = [ arr_test.max(0).tolist(), arr_test.max(1).tolist(), arr_test.max().tolist() ]
        arr_min = [ arr_test.min(0).tolist(), arr_test.min(1).tolist(), arr_test.min().tolist() ]
        arr_sum = [ arr_test.sum(0).tolist(), arr_test.sum(1).tolist(), arr_test.sum().tolist() ]        
       
        calculations.update({
            'mean' : arr_mean, 
            'variance' : arr_var, 
            'standard deviation' : arr_std, 
            'max' : arr_max, 
            'min' : arr_min, 
            'sum' : arr_sum
        })
    return calculations