import pandas as py
import matplotlib.pyplot as plt

# Load the dataset
data = py.read_csv(r"C:\Users\sarth\OneDrive\Desktop\Sarthak a\Programming\GitHub\Basic-python\Project\matplotlib\netflix_sample.csv")
print(data.head())

# Drop rows with missing values (only for columns that exist)
#valid_cols = [col for col in ['type','release_year','country'] if col in data.columns]
data = data.dropna(subset=['type', 'release_year', 'country'])

# Count types
type_counts = data['type'].value_counts()



# # Plot
# plt.figure(figsize=(6,4))
# plt.bar(type_counts.index, type_counts.values, color=['skyblue', 'lightgreen'])
# plt.title('Distribution of Content Types on Netflix')
# plt.xlabel('Content Type')
# plt.ylabel('Count')
# plt.tight_layout()
# plt.savefig('movies_vs_tvshows.png')
# plt.show()



# rating_counts = data['rating'].value_counts().head(10)
# plt.figure(figsize=(10,6))
# plt.pie(rating_counts, labels=rating_counts.index,autopct='%1.1f%%',startangle=90)
# plt.title('Distribution of Content Types on Netflix')
# plt.xlabel('Content Type')
# plt.ylabel('Count')
# plt.tight_layout()
# plt.savefig('content_ratingpie.png')
# plt.show()



movie_df = data[data['type'] == 'Movie'].copy()
# movie_df['duration_int'] =movie_df['duration'].str.replace(' min', '').astype(int)
# plt.figure(figsize=(10,6))
# plt.hist(movie_df['duration_int'], bins=8, color='coral', edgecolor='black')
# # plt.hist(movie_df['duration_int'], bins=15, color='coral', edgecolor='black', alpha=0.8)

# plt.title('Distribution of Movie Durations on Netflix')
# plt.xlabel('Duration (minutes)')
# plt.ylabel('Number of Movies')
# plt.tight_layout()
# plt.savefig('movie_durationhistogram.png')
# plt.show()


relese_year_counts = data['release_year'].value_counts().sort_index()
plt.figure(figsize=(12,6))
# plt.plot(relese_year_counts.index, relese_year_counts.values, marker='o', linestyle='-', color='purple')
plt.scatter(relese_year_counts.index, relese_year_counts.values, color='purple')
plt.title('Number of Releases per Year on Netflix') 
plt.xlabel('Release Year')
plt.ylabel('Number of Releases')
plt.grid(True)
plt.tight_layout()
plt.savefig('releases_per_year.png')
plt.show()

country_counts = data['country'].value_counts().head(10)
plt.figure(figsize=(10,6))
plt.barh(country_counts.index, country_counts.values, color='teal')
plt.title('Top 10 Countries by Number of Titles on Netflix')
plt.xlabel('Number of Titles')
plt.ylabel('Country')
plt.tight_layout()
plt.savefig('top_countries_netflix.png')
plt.show()

content_by_year = data.groupby('release_year')['type'].size().unstack().fillna(0)   
fig, ax= plt.subplots(1,2, figsize=(14,6), sharey=True)
ax[0].plot(content_by_year.index, content_by_year['Movie'], marker='o', color='blue', label='Movies')
ax[0].set_title('Movies Released Over Years')
ax[0].set_xlabel('Release Year')
ax[0].set_ylabel('Number of Movies')
ax[0].grid(True)
ax[1].plot(content_by_year.index, content_by_year['TV Show'], marker='o', color='orange', label='TV Shows')
ax[1].set_title('TV Shows Released Over Years')
ax[1].set_xlabel('Release Year')
ax[1].grid(True)

plt.suptitle('Movies vs TV Shows Released Over Years on Netflix', fontsize=16, fontweight='bold', y=1.02)
#fig.subtitle('A Comparative Analysis', fontsize=12, y=0.95)
plt.tight_layout()
plt.savefig('movies_vs_tvshows_over_years.png')
plt.show()


#first subplot movies
# import matplotlib.pyplot as plt

# # Count types
# type_counts = data['type'].value_counts()

# # Create figure
# plt.figure(figsize=(10, 6))
# bars = plt.bar(type_counts.index, type_counts.values, color=['#4CAF50', '#2196F3', '#FFC107', '#E91E63'])

# # Add title and labels
# plt.title('Distribution of Types', fontsize=16, fontweight='bold', pad=15)
# plt.xlabel('Type', fontsize=12)
# plt.ylabel('Count', fontsize=12)

# # Add gridlines for clarity
# plt.grid(axis='y', linestyle='--', alpha=0.7)

# # Rotate x-axis labels
# plt.xticks(rotation=45, ha='right')

# # Add values on top of each bar
# for bar in bars:
#     height = bar.get_height()
#     plt.text(
#         bar.get_x() + bar.get_width()/2,
#         height + 0.5,
#         f'{int(height)}',
#         ha='center',
#         va='bottom',
#         fontsize=10,
#         fontweight='bold'
#     )

# # Adjust layout
# plt.tight_layout()

# # Show plot
# plt.show()
