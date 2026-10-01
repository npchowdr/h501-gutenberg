from .transform import get_data, clean_aliases


def list_authors(by_languages=True, alias=True):
    """Return author aliases ordered from most to fewest translations."""
    authors = get_data(name="authors")[["gutenberg_author_id", "alias"]].copy()
    authors["alias"] = clean_aliases(authors["alias"])
    authors = authors.dropna(subset=["alias"])

    metadata = get_data(name="metadata")[["gutenberg_id", "gutenberg_author_id"]]
    languages = get_data(name="languages")[["gutenberg_id", "language"]]

    df = (
        metadata.dropna(subset=["gutenberg_author_id"])
        .merge(languages, on="gutenberg_id")
        .merge(authors, on="gutenberg_author_id")
        .drop_duplicates(subset=["gutenberg_id", "language", "gutenberg_author_id"])
    )

    counts = (
        df.groupby("alias")
        .size()
        .reset_index(name="translations")
        .sort_values(["translations", "alias"], ascending=[False, True])
    )
    return counts["alias"].tolist()