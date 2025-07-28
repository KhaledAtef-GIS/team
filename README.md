# 🚗 Travel Matrix API for Geospatial Analysis

This API accepts `.txt` travel matrix files (e.g., from Helsinki region or similar sources), performs basic geospatial analysis, and generates a PNG plot visualizing **car travel times in minutes**.

---

## 📥 Input

- **Accepted file format:** `.txt`
- **Expected columns** (tab-delimited or CSV format):

| Column    | Description                         |
|-----------|-------------------------------------|
| `from_id` | Origin zone ID                      |
| `to_id`   | Destination zone ID                 |
| `car_r_t` | Car travel time in seconds or mins  |

**Example (`matrix.txt`):**
