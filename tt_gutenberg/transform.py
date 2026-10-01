import pandas as pd

DATA = {
    "gutenberg_authors":  "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv",
    "gutenberg_metadata": "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_metadata.csv",
}

def get_data():
    """Load one of the gutenberg_*.csv tables, e.g. 'authors' or 'metadata'."""
    authors_df = pd.read_csv(DATA["gutenberg_authors"])
    metadata_df = pd.read_csv(DATA["gutenberg_metadata"])
    return authors_df, metadata_df


# def clean_aliases(series):
#     """Trim aliases and replace blank or letterless values with NA."""
#     cleaned = series.astype("string").str.strip()
#     return cleaned.where(cleaned.str.contains(r"[A-Za-z]", na=False))