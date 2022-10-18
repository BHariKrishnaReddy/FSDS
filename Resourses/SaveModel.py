import joblib

# Save the model as a pickle file
filename = './bike-share.pkl'
joblib.dump(model, filename)

'''
Now, we can load it whenever we need it, and use it to predict labels for new data. This is often called scoring or inferencing.
'''

# Load the model from the file
loaded_model = joblib.load(filename)

# Create a numpy array containing a new observation (for example tomorrow's seasonal and weather forecast information)
X_new = np.array([[1,1,0,3,1,1,0.226957,0.22927,0.436957,0.1869]]).astype('float64')
print ('New sample: {}'.format(list(X_new[0])))

# Use the model to predict tomorrow's rentals
result = loaded_model.predict(X_new)
print('Prediction: {:.0f} rentals'.format(np.round(result[0])))