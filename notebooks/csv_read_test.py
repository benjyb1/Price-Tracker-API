import pandas as pd


def compare_timestamps_with_new_row_pandas(csv_filepath, timestamp_column_name="timestamp", new_row_dict):
    """
    Opens a CSV file using pandas, extracts the latest timestamp, 
    and compares it with a new row's timestamp.

    Args:
        csv_filepath (str): The path to the CSV file.
        timestamp_column_name (str): The name of the timestamp column in the CSV.
        new_row_dict (dict): A dictionary representing the new row, with a 'timestamp' key.

    Returns:
        tuple: 
            - bool: True if the new row's timestamp is newer than or equal to the latest CSV timestamp, False otherwise.
            - pd.Timestamp or None: The latest timestamp found in the CSV, or None if the CSV is empty or doesn't contain the timestamp column.
            - pd.Timestamp: The timestamp from the new row dictionary.
    """

    latest_csv_timestamp = None

    try:
        # Read the CSV into a Pandas DataFrame
        df = pd.read_csv(csv_filepath, parse_dates=[timestamp_column_name])  # Automatically parse dates

        # Check if the timestamp column exists
        if timestamp_column_name not in df.columns:
            print(f"Error: CSV does not have a column named '{timestamp_column_name}'.")
            return False, None, pd.to_datetime(new_row_dict['timestamp'])

        # Find the latest timestamp using .max()
        latest_csv_timestamp = df[timestamp_column_name].max()

    except FileNotFoundError:
        print(f"Error: CSV file not found at '{csv_filepath}'")
        return False, None, pd.to_datetime(new_row_dict['timestamp'])

    # Convert the new row's timestamp to a Pandas Timestamp object
    new_row_timestamp = pd.to_datetime(new_row_dict['timestamp'])

    # Compare the timestamps
    is_new_row_newer = False
    if latest_csv_timestamp is pd.NaT:  # pd.NaT for Not a Time, equivalent to None for datetime objects in pandas
        is_new_row_newer = True
    elif new_row_timestamp >= latest_csv_timestamp:
        is_new_row_newer = True

    return is_new_row_newer, latest_csv_timestamp, new_row_timestamp