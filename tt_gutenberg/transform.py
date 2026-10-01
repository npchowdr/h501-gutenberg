import pandas as pd

DATA = {
    "gutenberg_authors":  "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv",
    "gutenberg_languages": "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_languages.csv",
}

def base_url():
    return (
        "https://raw.githubusercontent.com/rfordatascience/tidytuesday/"
        "main/data/2025/2025-06-03/"
    )

def get_data(name):
    """Load one of the gutenberg_*.csv tables, e.g. 'authors' or 'languages'."""
    return pd.read_csv(f"{base_url()}gutenberg_{name}.csv")


def clean_aliases(series):
    """Trim aliases and replace blank or letterless values with NA."""
    cleaned = series.astype("string").str.strip()
    return cleaned.where(cleaned.str.contains(r"[A-Za-z]", na=False))