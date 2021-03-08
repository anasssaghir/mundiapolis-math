def add_arrays(arr1, arr2):
    if(np.shape(arr1) == np.shape(arr2) ):
        arr= np.add(arr1,arr2)
        return arr.tolist()
    else:  
        return "None"