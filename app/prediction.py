import pickle
import numpy as np
import pickle

# Load serialized objects from file
with open('package.pkl', 'rb') as f:
    serialized_objects = pickle.load(f)

# Access the objects
model = serialized_objects['model']
scaler = serialized_objects['scaler']
sEncoder=serialized_objects['sEncoder']
SmEncoder=serialized_objects['SmEncoder']
REncoder=serialized_objects['REncoder']

def make_predictions(arr):
    arr[1]=sEncoder.transform([arr[1]])[0]
    arr[4]=SmEncoder.transform([arr[4]])[0]
    arr[5]=REncoder.transform([arr[5]])[0]
    arr=scaler.transform([arr])
    arr1=np.array(arr).reshape(1,-1)
    results=model.predict(arr1)
    return results[0]
    
    
