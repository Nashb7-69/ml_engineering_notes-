# Reference: DataFrame Anatomy

## Core Components

| Component | Accessor | Type | Description |
|-----------|----------|------|-------------|
| **Values** | `df.values` / `df.to_numpy()` | `np.ndarray` | Underlying data. 2D if single dtype; may return object array if mixed dtypes. |
| **Index** | `df.index` | `pd.Index` | Row labels. Default: `RangeIndex(0, n)`. Can be datetime, categorical, multi-level. |
| **Columns** | `df.columns` | `pd.Index` | Column labels. Always an Index object. |
| **Dtypes** | `df.dtypes` | `pd.Series` | Column → dtype mapping. One dtype per column. |
| **Shape** | `df.shape` | `tuple` | `(n_rows, n_cols)` |
| **Size** | `df.size` | `int` | Total elements = `n_rows * n_cols` |
| **Memory** | `df.memory_usage(deep=True)` | `pd.Series` | Bytes per column + index. Use `deep=True` for object columns. |

## Internal Structure (Mental Model)

```
DataFrame
├── BlockManager (internal)
│   ├── Block 1: float64  → columns ["age", "income"]  (shared array)
│   ├── Block 2: object   → columns ["city"]           (separate array)
│   └── Block 3: int32    → columns ["count"]          (separate array)
├── Index (rows)     → labels for axis 0
└── Columns (Index)  → labels for axis 1
```

- **Blocks**: Columns with same dtype are stored contiguously in a single NumPy array (a "block")
- **Consolidation**: `df._consolidate_inplace()` merges same-dtype blocks
- **Why it matters**: Operations on same-dtype columns are faster (cache locality, vectorization)

## Index Types

| Type | Use Case | Example |
|------|----------|---------|
| `RangeIndex` | Default, sequential | `0, 1, 2, ...` |
| `Int64Index` | Explicit integer labels | `[10, 20, 30]` |
| `DatetimeIndex` | Time series | `pd.date_range(...)` |
| `CategoricalIndex` | Low-cardinality labels | `pd.Categorical(["A","B","A"])` |
| `MultiIndex` | Hierarchical rows | `(year, month, day)` |

## Dtype System (pandas 2.0+)

| Category | Dtypes | Notes |
|----------|--------|-------|
| **Numeric** | `int8`–`int64`, `uint8`–`uint64`, `float16`–`float64` | Nullable: `Int64`, `Float64` (capital = nullable) |
| **String** | `string` (Arrow), `object` (Python) | Prefer `string` for missing-aware ops |
| **Boolean** | `bool`, `boolean` (nullable) | `boolean` supports `NA` |
| **Datetime** | `datetime64[ns]`, `datetime64[ns, tz]` | Timezone-aware supported |
| **Categorical** | `category` | Low memory, fast groupby |
| **Other** | `timedelta64[ns]`, `period`, `interval`, `sparse` | Specialized uses |

## Quick Inspection Commands

```python
df.info()                    # Full overview: dtypes, non-null, memory
df.info(verbose=True)        # Show all columns (even if > 20)
df.info(memory_usage="deep") # Accurate memory for object columns
df.describe()                # Numeric summary stats
df.describe(include="all")   # All columns
df.describe(include="object") # Only object/string
df.dtypes                    # Series: col → dtype
df.columns.tolist()          # Column names as list
df.index.tolist()            # Index values as list
```

## Conversion to NumPy (for ML)

| Method | Returns | Notes |
|--------|---------|-------|
| `df.to_numpy()` | `np.ndarray` | **Preferred**. Handles extension dtypes, lets you set `dtype=`, `na_value=`. |
| `df.values` | `np.ndarray` | Legacy. May return object array for mixed dtypes. Avoid in new code. |
| `df[cols].to_numpy()` | `np.ndarray` | Subset columns first for feature matrix `X`. |
| `df[col].to_numpy()` | 1D `np.ndarray` | Single column → 1D array (not 2D). |

## Related References
- [Creation Methods](./02-creation-methods.md)
- [Indexing & Selection](./03-indexing-selection.md)
- [Dtypes & Conversion](./04-dtypes-conversion.md)