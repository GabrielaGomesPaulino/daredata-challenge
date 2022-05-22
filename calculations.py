import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def run_calculate():
    # Create dataframe
    data= pd.read_csv("output.csv")

    # Average file size
    average_file_size= data['filesize'].mean()

    # Biggest file
    biggest_file_index= data['filesize'].idxmax()
    biggest_file = data['filename'][biggest_file_index]
    
    # Smallest file
    smallest_file_index = data['filesize'].idxmin()
    smallest_file = data['filename'][smallest_file_index]
    
    # Output to console
    print("The average file size is: ", average_file_size)
    print("The biggest file is: ", biggest_file)
    print("The smallest file is: ", smallest_file)
    
    data.hist(column='filesize')
    #plt.show() # Visual representation of the histogram

    # Values from the histogram
    count,filesize = np.histogram(data['filesize'])

    return {
        "average": average_file_size,
        "biggest_file": biggest_file,
        "smallest_file": smallest_file,
        "histogram":  {
            "count": count.tolist(),
            "filesize": filesize.tolist()
        }
    }
