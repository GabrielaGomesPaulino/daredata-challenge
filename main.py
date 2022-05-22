import pandas as pd
import matplotlib.pyplot as plt

data= pd.read_csv("output.csv")
average_file_size= data['filesize'].mean()
biggest_file_index= data['filesize'].idxmax()
smallest_file_index= data['filesize'].idxmin()
print("The average file size is: ",average_file_size)
print("The biggest file is: ",data['filename'][biggest_file_index])
print("The smallest file is: ",data['filename'][smallest_file_index])
data.hist(column='filesize')
plt.show()