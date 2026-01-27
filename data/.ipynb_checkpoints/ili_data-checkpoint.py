import pandas as pd
from delphi_epidata import Epidata

res = Epidata.fluview(["nat"], [201501, Epidata.range(201502, 202552)])

d = pd.DataFrame(res["epidata"])
d.to_csv("ili_data.csv",index=False)