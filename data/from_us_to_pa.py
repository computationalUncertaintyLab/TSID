import pandas as pd

if __name__ == "__main__":
    d1 = pd.read_csv("2020_US_Region_Mobility_Report.csv")
    d2 = pd.read_csv("2021_US_Region_Mobility_Report.csv")
    d3 = pd.read_csv("2022_US_Region_Mobility_Report.csv")

    def combine_covid(imput,output):
        d = pd.concat(imput)
        pa_covid = d.loc[d.sub_region_1 == "Pennsylvania"]
        pa_covid.to_csv(output, index = False)
    
    output = "pa_covid.csv"
    combine_covid([d1,d2,d3],output)