from .transform import get_data, clean_aliases


def list_authors(by_languages=True, alias=True):
    """Return author aliases ordered from most to fewest translations."""
    merged_df = get_data()
    merged_df["author_alias"] = clean_aliases(merged_df["author_alias"])
    merged_df.dropna(subset=["author_alias"], inplace=True)

    if by_languages and alias:
      counts = merged_df.groupby("author_alias")["language"].agg(
          lambda s: len({lang for entry in s.astype(str) for lang in entry.split("/")})
      )
      return counts.sort_values(ascending=False).index.tolist()
    
    # if alias:
    #     counts = merged_df.groupby("author_alias")["gutenberg_id"].agg(
    #     lambda s: len({book for book in s})
    #     )
    #     return counts.sort_values(ascending=False).index.tolist()
