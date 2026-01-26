import pandas as pd

if __name__ == "__main__":
    from delphi_epidata import Epidata

    res = Epidata.fluview(['nat'], [201440, Epidata.range(201501, 201510)])
    print(res['result'], res['message'], len(res['epidata']))

