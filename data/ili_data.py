import pandas as pd
from delphi_epidata import Epidata

res = Epidata.fluview(["nat"], [201901, Epidata.range(201902, 202350)])

d = pd.DataFrame(res["epidata"])
d.to_csv("ili_data.csv",index=False)