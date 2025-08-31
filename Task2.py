import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Copy pasting jupyter code in python cause this is my first time using jupyter, a bit confused so prefer to use direct python... Better for comments too

# 1. Loading the dataset
df = pd.read_csv("ufc_fighters.csv")

# 2. Basic description of the data set 
print(df.head())
print(df.info())
print(df.describe())

# 3.  missing values
df = df.drop_duplicates()
df = df.dropna(subset=["Name"])  # Name is critical
df.fillna({"Stance": "Unknown"}, inplace=True)  # Replace missing stance with Unknown

# 4. Fixing possible data type issues

def height_to_cm(height_str):
    try:
        feet, inches = height_str.split("'")
        feet = int(feet)
        inches = int(inches.replace('"','').strip())
        return round(feet*30.48 + inches*2.54, 1)
    except:
        return np.nan

df["Height_cm"] = df["Height"].apply(height_to_cm)

# Convert inch to cm
df["Reach_cm"] = df["Reach"].apply(lambda x: round(float(x)*2.54, 1) if pd.notnull(x) else np.nan)

def remove_outliers_iqr(df, column):
    """
    Removes outliers from a given column of a DataFrame using the IQR method.
    """
    Q1 = df[column].quantile(0.25)   
    Q3 = df[column].quantile(0.75)   
    IQR = Q3 - Q1                   

    lower_bound = Q1 - 1.5 * IQR    
    upper_bound = Q3 + 1.5 * IQR     

  
    df_cleaned = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    return df_cleaned

# Removing outliers
df = remove_outliers_iqr(df, 'Height')
df = remove_outliers_iqr(df, 'Weight')
df = remove_outliers_iqr(df, 'Reach')


# 5. Feature Engineering
df["Total_Fights"] = df["Wins"] + df["Losses"] + df["Draws"]
df["Win_Ratio"] = df["Wins"] / df["Total_Fights"]

# 6. Visualization
sns.set(style="whitegrid")

# Win Ratio distribution
plt.figure(figsize=(8,5))
sns.histplot(df["Win_Ratio"].dropna(), bins=20, kde=True)
plt.title("Distribution of Fighters' Win Ratio")
plt.xlabel("Win Ratio")
plt.ylabel("Count")
plt.show()

# Height vs Win Ratio
plt.figure(figsize=(8,5))
sns.scatterplot(x="Height_cm", y="Win_Ratio", data=df, alpha=0.6)
plt.title("Height vs Win Ratio")
plt.xlabel("Height (cm)")
plt.ylabel("Win Ratio")
plt.show()

# Stance vs Win Ratio
plt.figure(figsize=(10,6))
sns.boxplot(x="Stance", y="Win_Ratio", data=df)
plt.xticks(rotation=45)
plt.title("Fighting Stance vs Win Ratio")
plt.show()

# Correlation Heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df[["Wins","Losses","Total_Fights","Height_cm","Reach_cm","Win_Ratio"]].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap of UFC Fighter Stats")
plt.show()