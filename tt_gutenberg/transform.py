import pandas as pd

from tt_gutenberg import authors

DATA = {
    "gutenberg_authors":  "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv",
    "gutenberg_metadata": "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_metadata.csv",
}

def get_data():
    """Load one of the gutenberg_*.csv tables, e.g. 'authors' or 'metadata'."""
    authors_df = pd.read_csv(DATA["gutenberg_authors"])
    metadata_df = pd.read_csv(DATA["gutenberg_metadata"])

    #join the two dataframes on the gutenberg_author_id column
    joined_df = metadata_df.merge(authors_df, on="gutenberg_author_id", how="left")

    #drop the duplicated author_y column and rename author_x to author
    joined_df.drop(columns=["author_y"], inplace=True)
    joined_df = joined_df.rename(columns={"author_x": "author"})
    joined_df["author_alias"] = joined_df["alias"]

    return joined_df


def clean_aliases(series):
    """Trim aliases and replace blank or letterless values with NA."""
    cleaned = series.astype("string").str.strip()
    return cleaned.where(cleaned.str.contains(r"[A-Za-z]", na=False))