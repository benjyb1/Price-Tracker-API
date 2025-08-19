import pandas as pd
from datetime import datetime, timezone
from API-call import fetch
import os


def dict_to_csv(data, filepath="prices.csv"):
    # Convert timestamp to human-readable format
    iso_time = datetime.fromtimestamp(data['timestamp'], timezone.utc).isoformat()

    row = {
        "timestamp": iso_time,
        "base": data.get("base")
    }
    row.update(data.get("rates", {}))  # add rate columns dynamically

    df = pd.DataFrame([row])

    # Append to CSV or create new file with header

    write_header = not os.path.exists(filepath)
    df.to_csv(filepath, mode="a", header=write_header, index=False)
    print(f"Saved to {filepath}")


# Example usage:
data = fetch(base="USD", currencies="XAU")
dict_to_csv(data)
