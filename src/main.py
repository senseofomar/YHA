import pandas as pd
import json
import matplotlib.pyplot as plt
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


file_path = os.path.join(BASE_DIR, '../data/watch-history.json')

# --------------- LOAD AND CLEAN DATA ---------------

# Load your watch history JSON
with open('../data/watch-history.json', encoding='utf-8') as f:
    data = json.load(f)

# Flatten nested structure (YouTube history has nested fields)
df = pd.json_normalize(data)

# Extract YouTuber/channel name from subtitles
df['YouTuber'] = df['subtitles'].apply(
    lambda x: x[0]['name'] if isinstance(x, list) and len(x) > 0 and 'name' in x[0] else 'Unknown'
)

# Convert 'time' to datetime format safely
df['time'] = pd.to_datetime(df['time'], utc=True, errors='coerce')

# Extract hour and weekday
df['hour'] = df['time'].dt.hour
df['weekday'] = df['time'].dt.day_name()

# Quick null check
print("❌ Failed to convert time:", df['time'].isna().sum())

# Optional: Save cleaned data
df.to_csv('cleaned_watch_history.csv', index=False)

# --------------- INSPECT BASIC STRUCTURE ---------------

print("\n📊 Dataset Dimensions:", df.shape)
print("\n🧾 Columns:", df.columns.tolist())
print("\n🔍 Sample Entries:\n", df.head())
print("\nℹ️ Info:\n")
print(df.info())
print("\n📈 Summary Stats (numerical columns only):\n", df.describe())

# --------------- ANALYSIS SECTION ---------------

# Top YouTubers
print("\n🔝 Top 10 YouTubers by Videos Watched:")
top_youtubers = df['YouTuber'].value_counts().head(10).to_frame(name='Videos Watched')
top_youtubers.index.name = 'YouTuber'
print(top_youtubers)

# Hour-wise viewing pattern
print("\n🕒 Videos Watched by Hour:")
hourly = df['hour'].value_counts().sort_index().to_frame(name='Videos Watched')
hourly.index.name = 'Hour (0–23)'
print(hourly)

# Top (Weekday, YouTuber) combos
print("\n📅 Top 10 (Weekday, YouTuber) combinations:")
combo = df.groupby(['weekday', 'YouTuber']).size().sort_values(ascending=False).head(10).to_frame(name='Videos Watched')
print(combo)

# Most watched video titles
print("\n🎥 Most Watched Video Titles:")
top_videos = df['title'].value_counts().head(10).to_frame(name='Times Watched')
top_videos.index.name = 'Video Title'
print(top_videos)

# --------------- VISUALIZATION ---------------

plt.figure(figsize=(10, 4))
hourly['Videos Watched'].plot(kind='bar', color='skyblue')
plt.title("YouTube Viewing Pattern by Hour")
plt.xlabel("Hour of Day (0–23)")
plt.ylabel("Videos Watched")
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()