import pandas as pd

from tt_gutenberg import DATA


# def base_url():
#     return (
#         "https://raw.githubusercontent.com/rfordatascience/tidytuesday/"
#         "main/data/2025/2025-06-03/"
#     )


def get_data(name):
    """Load one of the gutenberg_*.csv tables, e.g. 'authors' or 'languages'."""
    if name not in DATA:
        raise ValueError(f"Unknown data name: {name}")
    return pd.read_csv(DATA[name])
    #return pd.read_csv(f"{base_url()}gutenberg_{name}.csv")


def clean_aliases(series):
    """Trim aliases and replace blank or letterless values with NA."""
    cleaned = series.astype("string").str.strip()
    return cleaned.where(cleaned.str.contains(r"[A-Za-z]", na=False))