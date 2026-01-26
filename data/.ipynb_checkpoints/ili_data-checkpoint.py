import pandas as pd
from delphi_epidata import Epidata

res = Epidata.fluview(["nat"], [201440, Epidata.range(201501, 201510)])

d = pd.DataFrame(res["epidata"])
d.to_csv("ili_data.csv",index=False)