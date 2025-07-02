# Youtube-etl-dashboard
End-to-End ETL (Extract, Transform, Load) that collects and analyzes video data from  public YouTube channel using the YouTube Data API v3. The processed data is stored in Google Cloud Storage and loaded into BigQuery for further analysis and dashboarding in Looker Studio.

This project is a complete **end-to-end data pipeline** for analyzing the YouTube channel **[Madras Samayal](https://www.youtube.com/@MadrasSamayal)**. The pipeline includes data extraction from the YouTube Data API, transformation with Python, loading into Google BigQuery, and dashboard visualization using Looker Studio.

## 📌 Project Objectives

- Retrieve video data from the YouTube API (titles, views, likes, etc.)
- Clean and transform the data (handle duration, newlines, tags, etc.)
- Load the cleansed data into BigQuery
- Build a Looker Studio dashboard for interactive analysis

## 🛠️ Tech Stack

| Component         | Tool/Tech                     |
|------------------|-------------------------------|
| Extraction        | Python, YouTube Data API v3   |
| Transformation    | Pandas, PySpark               |               |
| Storage & Query   | Google BigQuery               |
| Visualization     | Looker Studio (formerly GDS)  |



