UFC Fighters Data Analysis 

First, I show the data, the head, info and describe it using pandas
Next, data cleaning
1. Removing duplicates
2. Finding null values and replacing or removing according to importance of data (eg: name is crucial info so remove data with no name and dob isn't so putting null there)
3. Removing outliers using the IQR method

After which, feature engineering,
adding features for a more easier analysis model
Better in giving insights to the data 

Then, data visualization
using a white background for good visualizing
1. Distribution of Win Ratio
   Using a histplot to show if the win ratio is balanced records, shows outliers like those with better winning ratio as a better player and the other way round 

2. Height vs. Win Ratio Scatter Plot
   Using a scatter plot to visualize if there is a relation between players height and their winning ratio, scatter shows if there is a focus on a particular height giving insights for optimum player height

3. Correlation Heatmap of fighter stats
   GIves overall veiw of relationships between multiple values. Gives insights into exploring a particular relationship better

4. Wins vs. Losses Distribution
   Spotting good patterns, are they winning more or losing and how big is the difference

