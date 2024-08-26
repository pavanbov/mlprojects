import random
import pandas as pd

rmin = 3.5
rmax = 5.5
wmin = 4.5
wmax = 11
pmin = 1.5
pmax = 4.2
cmin = 0.1
cmax = 1.1

rw = 0.27
ww = 0.27
pw = 0.23
cw = 0.23

num = 1000000

data = []

t = (rmax*rw + wmax*ww + pmax*pw + cmax*cw) * 0.7

for i in range(num):
    r = random.uniform(rmin, rmax)
    w = random.uniform(wmin, wmax)
    p = random.uniform(pmin, pmax)
    c = random.uniform(cmin, cmax)
    o = r*rw + w*ww + p*pw + c*cw
    if o <= t:
        cl = 0
    else:
        cl = 1
    d = [r, w, p, c, o, cl]
    data.append(d)

# Create a DataFrame
columns = ["RBC", "WBC", "PLATLETS", "CHOLESTROL", "BLOOD_HEALTH", "HEALTHY"]
df = pd.DataFrame(data, columns=columns)

# Save the DataFrame to a CSV file
df.to_csv("output_data.csv", index=False)