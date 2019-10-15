from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

# Plot average goals from 1930 to 2014

df = pd.read_csv('WorldCupMatches.csv')
print(df.head())
df['Total Goals'] = df['Home Team Goals'] + df['Away Team Goals']
print(df.head())
sns.set_style("whitegrid")
sns.set_context("notebook", font_scale=1.25)
f, ax = plt.subplots(figsize=(12, 7))
ax = sns.barplot(x=df['Year'], y=df['Total Goals'])
ax.set_title("Average Number Of Goals Scored In World Cup Matches By Year")
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
plt.show()
plt.savefig('average_goals.png')

# Plot the distribution of the goals data
df_goals = pd.read_csv('goals.csv')
print(df_goals.head())
f, ax2 = plt.subplots(figsize=(12, 7))
sns.boxplot(x='year', y='goals', data=df_goals, palette='Spectral')
ax2.set_title("Goals Visualization")
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45)
plt.show()
