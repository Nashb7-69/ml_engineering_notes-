# Reference: DataFrame Creation Methods

## From Python Objects

### Dict of Lists/Arrays (Column-Oriented) — Most Common
```python
pd.DataFrame({
    "feature_1": [1.2, 3.4, 2.1],
    "feature_2": [0, 1, 0],
    "target":    [10, 20, 15]
})
# All lists must be same length
```

### Dict of Series (Column-Oriented, Explicit Index)
```python
pd.DataFrame({
    "a": pd.Series([1, 2, 3], index=["x", "y", "z"]),
    "b": pd.Series([4, 5, 6], index=["x", "y", "z"])
})
# Index alignment is automatic
```

### List of Dicts (Row-Oriented)
```python
pd.DataFrame([
    {"feature_1": 1.2, "feature_2": 0, "target": 10},
    {"feature_1": 3.4, "feature_2": 1, "target": 20},
])
# Missing keys become NaN
```

### List of Lists/Tuples (Matrix-Style)
```python
pd.DataFrame(
    [[1.2, 0, 10], [3.4, 1, 20]],
    columns=["feat_1", "feat_2", "target"],
    index=["row1", "row2"]  # optional
)
```

## From NumPy / Array-Like

### 2D Array + Column Names
```python
X = np.array([[1.2, 0], [3.4, 1], [2.1, 0]])
df = pd.DataFrame(X, columns=["feat_1", "feat_2"])
```

### Structured/Record Array
```python
dt = np.dtype([("x", float), ("y", float), ("label", int)])
arr = np.array([(1.2, 0, 10), (3.4, 1, 20)], dtype=dt)
df = pd.DataFrame(arr)
```

## From Files (IO) — ML Workhorse

| Format | Read Function | Key Parameters |
|--------|---------------|----------------|
| CSV | `pd.read_csv()` | `sep`, `encoding`, `dtype`, `parse_dates`, `na_values`, `chunksize` |
| Parquet | `pd.read_parquet()` | `columns`, `filters` (partition pruning) |
| Excel | `pd.read_excel()` | `sheet_name`, `header`, `engine="openpyxl"` |
| SQL | `pd.read_sql()` | `con` (SQLAlchemy engine), `params` |
| JSON | `pd.read_json()` | `orient`, `lines=True` for JSONL |
| Feather | `pd.read_feather()` | Fast, preserves dtypes |
| HDF5 | `pd.read_hdf()` | `key`, `mode` |

### CSV Best Practices for ML
```python
df = pd.read_csv(
    "data.csv",
    dtype={"id": "int32", "category": "category"},  # Specify dtypes upfront
    parse_dates=["timestamp"],                       # Parse dates on load
    na_values=["NA", "N/A", "missing", ""],         # Custom missing markers
    low_memory=False                                 # Avoid mixed-type inference
)
```

## From Other Pandas Objects

### From Series
```python
s = pd.Series([1, 2, 3], name="values")
df = s.to_frame()           # Single-column DataFrame
df = pd.DataFrame({"col": s})  # Explicit column name
```

### From Another DataFrame
```python
df2 = df.copy()             # Deep copy
df2 = df[["a", "b"]].copy() # Subset + copy (avoid SettingWithCopyWarning)
df2 = df.assign(new_col=df["a"] * 2)  # Add column, returns new DF
```

## Special Constructors

### Empty DataFrame with Schema
```python
df = pd.DataFrame(columns=["feat_1", "feat_2", "target"])
df = pd.DataFrame({"feat_1": pd.array([], dtype="float64"),
                   "feat_2": pd.array([], dtype="int32"),
                   "target": pd.array([], dtype="float64")})
```

### From Dictionary with `orient`
```python
# orient="index": keys become row index
pd.DataFrame.from_dict({"row1": {"a": 1}, "row2": {"a": 2}}, orient="index")

# orient="columns": keys become columns (default)
pd.DataFrame.from_dict({"a": [1, 2], "b": [3, 4]}, orient="columns")
```

### `pd.concat` / `pd.merge` / `pd.join`
```python
pd.concat([df1, df2], axis=0)  # Stack rows
pd.concat([df1, df2], axis=1)  # Join columns (align on index)
pd.merge(df1, df2, on="key")   # SQL-style join
df1.join(df2, on="key")        # Join on index/key
```

## ML-Specific Patterns

### Feature Matrix + Target from Arrays
```python
X = np.random.randn(100, 5)
y = np.random.randint(0, 2, 100)

df = pd.DataFrame(X, columns=[f"feat_{i}" for i in range(5)])
df["target"] = y
```

### Train/Test Split with Indices Preserved
```python
from sklearn.model_selection import train_test_split

train_df, test_df = train_test_split(df, test_size=0.2, random_state=42, stratify=df["target"])
# Both keep original index — reset if needed:
train_df = train_df.reset_index(drop=True)
```

### Synthetic Data for Testing
```python
# Classification
from sklearn.datasets import make_classification
X, y = make_classification(n_samples=1000, n_features=10, random_state=42)
df = pd.DataFrame(X, columns=[f"f{i}" for i in range(10)])
df["y"] = y

# Regression
from sklearn.datasets import make_regression
X, y = make_regression(n_samples=500, n_features=5, noise=0.1)
df = pd.DataFrame(X, columns=[f"f{i}" for i in range(5)])
df["target"] = y
```

## Common Pitfalls

| Pitfall | Symptom | Fix |
|---------|---------|-----|
| Lists of different lengths | `ValueError: arrays must all be same length` | Check lengths; pad with `NaN` |
| Mutable default argument | Shared state across calls | Use `None` default, create inside |
| Column order from dict | Random order (Py<3.7) or insertion order | Pass `columns=[...]` explicitly |
| `df.values` with mixed dtypes | Returns `object` array, slow | Use `df.to_numpy(dtype=...)` or select cols |
| Forgetting `copy()` | SettingWithCopyWarning | Use `.copy()` when subsetting for mutation |

## Quick Reference: Choosing a Method

| Situation | Recommended |
|-----------|-------------|
| Known columns, building row by row | List of dicts → `pd.DataFrame(records)` |
| Columnar data (dict of arrays) | `pd.DataFrame(dict_of_lists)` |
| NumPy matrix → labeled DF | `pd.DataFrame(X, columns=names)` |
| Loading training data | `pd.read_parquet()` or `pd.read_csv()` |
| Appending rows in loop | **Don't**. Collect list of dicts, create once. |
| Empty DF with known schema | `pd.DataFrame(columns=...)` + `df.astype(dtypes)` |

## Related References
- [DataFrame Anatomy](./01-dataframe-anatomy.md)
- [IO Tools Deep Dive](./05-io-tools.md)
- [Dtypes & Conversion](./04-dtypes-conversion.md)