# 🕵️‍♂️ yt-detective — Your YouTube Watch History Analyzer

Uncover your YouTube watching habits using Pandas and your own data. With `yt-detective`, you can analyze who you watch the most, what hours you’re most active, and more — all from your personal YouTube history.

---

## 🔍 What This Project Does

This tool:
- Loads your **YouTube watch-history JSON** file from Google Takeout
- Cleans and normalizes the data
- Gives insights like:
  - Top YouTubers you watch
  - Most active hours and days
  - Most rewatched videos
  - Weekday–YouTuber viewing combinations
- Plots a simple bar chart of your hourly viewing patterns

---

## 📁 Folder Structure

```
yt-detective/
├── data/
│   └── watch-history.json       # Exported from Google Takeout
├── cleaned_watch_history.csv    # (Optional) Cleaned CSV file
├── src/
│   └── main.py                  # Main analysis script
├── README.md
└── requirements.txt
```

---

## 📦 Installation

Make sure you’re using **Python 3.7+**.

Install dependencies with:
```bash
pip install -r requirements.txt
```

---

## ▶️ How to Use

1. **Download Your YouTube Data**
   - Visit [Google Takeout](https://takeout.google.com/)
   - Select only **YouTube and YouTube Music**
   - Export your data, unzip it
   - Move `watch-history.json` to the `data/` folder

2. **Run the Detective**
   ```bash
   python src/main.py
   ```

3. **View Your Results**
   - Clean summary printed to terminal
   - Chart showing your hourly activity
   - (Optional) A cleaned CSV file saved for deeper analysis

---

## 📊 Insights You’ll See

- 🧑‍💻 Top YouTubers you watch most
- 🕒 What hours you're active on YouTube
- 📅 Which days you binge certain creators
- 🎥 Most rewatched video titles

---

## 🧠 Why Use yt-detective?

Because it’s **your own data**, you’ll be more engaged — making it the perfect way to learn:
- Real-life Pandas usage
- Data cleaning and structuring
- Grouping, filtering, and aggregation
- Plotting insights with Matplotlib

This project teaches you **Pandas the fun way** — through your own watch history.

---

## 🛠 Tech Stack

- **Python**
- **Pandas** — Data wrangling
- **Matplotlib** — Data visualization
- **JSON** — For parsing exported data

---

## 📌 Stretch Ideas

- Heatmap of watch activity by weekday/hour
- Visualize trends month-over-month
- Turn into a full dashboard with Streamlit

---

## 🔒 Privacy Note

This project is 100% offline. Your data stays on your device, always.

---

## 🧵 Made with curiosity, Python, and late-night YouTube sessions.
