import pandas as pd
import statistics as st
data = [453,45,6,452,675,9,7,64,5,3,435,3,67,3,3,7,3,4,5,6,8,90,7,5,2]
data.sort()
sum = sum(data)
length = len(data)
mean = sum/length
#print(mean)
if length/2==0:
    median = (length//2) + (length//2) + 1/2
else:
    median = (length+1)//2
#print(median)
from collections import Counter
  
# list of elements to calculate mode  
modeData = Counter(data)
get_mode = dict(modeData)
mode = [k for k, v in get_mode.items() if v == max(list(modeData.values()))]
  
if len(mode) == length:
    get_mode = "No mode found"
else:
    get_mode = "Mode is / are: " + ', '.join(map(str, mode))
      
#print(get_mode)


df = pd.read_csv(r"C:/Users/Admin/Downloads/Practice/SOCR-HeightWeight.csv")
ht = df["Height(Inches)"]
mean2 = st.mean(ht)
median2 = st.median(ht)
mode2 = st.mode(ht)
print(mode2)