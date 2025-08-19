import pandas as pd
from datetime import datetime, timezone
from API_call import fetch
import os

fetch1 = {'timestamp': "2025-08-18T23:59:59+00:00",'base': "USD",'rate':3333.5944648998,'inv':0.0002999765}

def fetch_csv(filepath='prices.csv'):
    """ Fetch the csv """
    df = pd.read_csv(filepath)
    print(df.iloc[-1,0])

df = pd.read_csv('prices.csv')
row = fetch1
print(row)


# def compare_rows():
# #     df.loc[-1]
#
# def dict_to_csv(data, filepath="prices.csv"):
#     # Convert timestamp to human-readable format
#     iso_time = datetime.fromtimestamp(data['timestamp'], timezone.utc).isoformat()
#
#     row = {
#         "timestamp": iso_time,
#         "base": data.get("base")
#     }
#     row.update(data.get("rates", {}))  # add rate columns dynamically
#
#     df = pd.DataFrame([row])
#
#     # Append to CSV or create new file with header
#
#     write_header = not os.path.exists(filepath)
#     df.to_csv(filepath, mode="a", header=write_header, index=False)
#     print(f"Saved to {filepath}")
#
#
# # Example usage:
# data = fetch(base="USD", currencies="XAU")
# dict_to_csv(data)
