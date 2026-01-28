import pandas as pd
from delphi_epidata import Epidata

res = Epidata.fluview(["nat","hhs1","hhs2","hhs3","hhs4","hhs5","hhs6","hhs7","hhs8","hhs9","hhs10"], [201501, Epidata.range(201502, 202552)])

d = pd.DataFrame(res["epidata"])
d.to_csv("ili_data.csv",index=False)