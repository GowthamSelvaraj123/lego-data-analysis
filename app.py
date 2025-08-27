# Day 74 - LEGO Data Analysis
# Complete code including merging and bar charts

import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# 1. Load Data
# -------------------------------
colors = pd.read_csv('colors.csv')
sets = pd.read_csv('sets.csv')
themes = pd.read_csv('themes.csv')

# -------------------------------
# 2. Sets Published Over Time
# -------------------------------
sets_by_year = sets.groupby('year').count()['set_num'][:-2]

plt.figure(figsize=(12,6))
plt.plot(sets_by_year.index, sets_by_year.values, color='blue', marker='o')
plt.title('Number of LEGO Sets Released Per Year')
plt.xlabel('Year')
plt.ylabel('Number of Sets')
plt.show()

# -------------------------------
# 3. Number of Themes Per Year
# -------------------------------
themes_by_year = sets.groupby('year').agg({'theme_id': pd.Series.nunique})
themes_by_year.rename(columns={'theme_id': 'nr_themes'}, inplace=True)
themes_by_year_full = themes_by_year[:-2]

plt.figure(figsize=(12,6))
plt.plot(themes_by_year_full.index, themes_by_year_full['nr_themes'], color='green', marker='o')
plt.title('Number of LEGO Themes Released Per Year')
plt.xlabel('Year')
plt.ylabel('Number of Themes')
plt.show()

# -------------------------------
# 4. Dual-axis chart: Sets vs Themes
# -------------------------------
fig, ax1 = plt.subplots(figsize=(12,6))
ax1.plot(sets_by_year.index, sets_by_year.values, color='blue', label='Number of Sets')
ax1.set_xlabel('Year')
ax1.set_ylabel('Number of Sets', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

ax2 = ax1.twinx()
ax2.plot(themes_by_year_full.index, themes_by_year_full['nr_themes'], color='green', label='Number of Themes')
ax2.set_ylabel('Number of Themes', color='green')
ax2.tick_params(axis='y', labelcolor='green')

plt.title('LEGO Sets vs Themes Over Time')
fig.tight_layout()
plt.show()

# -------------------------------
# 5. Average Number of Parts Per LEGO Set
# -------------------------------
parts_per_set = sets.groupby('year').agg({'num_parts': pd.Series.mean})[:-2]

plt.figure(figsize=(12,6))
plt.scatter(parts_per_set.index, parts_per_set['num_parts'], alpha=0.5)
plt.title('Average Number of Parts per LEGO Set Over Time')
plt.xlabel('Year')
plt.ylabel('Average Number of Parts')
plt.show()

# -------------------------------
# 6. Top 10 Themes by Number of Sets (Merged)
# -------------------------------
# Count number of sets per theme_id
set_theme_count = sets['theme_id'].value_counts().rename_axis('id').reset_index(name='set_count')

# Merge with themes DataFrame
merged_df = pd.merge(set_theme_count, themes, on='id')

# Plot top 10 themes
plt.figure(figsize=(14,8))
plt.bar(merged_df['name'][:10], merged_df['set_count'][:10], color='purple')
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)
plt.ylabel('Nr of Sets', fontsize=14)
plt.xlabel('Theme Name', fontsize=14)
plt.title('Top 10 LEGO Themes by Number of Sets', fontsize=16)
plt.show()

# -------------------------------
# 7. Exploring Star Wars Themes
# -------------------------------
star_wars_ids = themes[themes['name'] == 'Star Wars']['id']
star_wars_sets = sets[sets['theme_id'].isin(star_wars_ids)]
print("Star Wars LEGO sets:")
print(star_wars_sets[['name','set_num','year']])
