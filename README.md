# 🚗 Travel Matrix Access Visualization API

This API allows uploading `.txt` travel time matrix files (e.g. from Helsinki Region Travel Time Matrix), processes them by spatially joining them with a zone grid, and generates **PNG heatmaps** of car travel times.

---

## 🧠 What It Does

1. Accepts one or more matrix files (`.txt`) with travel time values.
2. Extracts the destination zone (`YKR_ID`) from the filename.
3. Joins each matrix with a Helsinki grid shapefile (`MetropAccess_YKR_grid_EurefFIN.shp`).
4. Exports the result as a `.gpkg` file (GeoPackage).
5. Plots a map of car travel times and saves it as a `.png`.

---

## 🚀 Endpoint

### `POST /AccessViz`

Upload one or more `.txt` travel matrix files.

#### 📥 Request Parameters

- **`matrix_files`**: list of uploaded `.txt` files (multipart/form-data)

Each file must be named like: `travel_matrix_<ykr_id>.txt`  
Example: `travel_matrix_5975371.txt`

#### 🧾 Expected File Format (`;`-delimited)

#### ✅ Response

Returns simple text confirmation:

```json
"All is good"

