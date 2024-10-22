#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import necessary libraries
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt


# In[2]:


# Load the dataset
df = pd.read_csv('Downloads/bmi.csv')
df


# In[3]:


df.info()


# In[4]:


df.isna().sum()


# In[5]:


df.nunique()


# In[6]:


df['BmiClass'].unique()


# In[7]:


# Function to calculate basic statistics
def display_basic_statistics(dataframe):
    # Describe will give mean, std, min, 25%, 50%, 75%, max for numerical columns
    print("Descriptive Statistics (Basic):\n")
    print(dataframe.describe())

    # Median
    print("\nMedian values for numerical columns:")
    print(dataframe.median())

    # Skewness
    print("\nSkewness for numerical columns:")
    print(dataframe.skew())

    # Kurtosis
    print("\nKurtosis for numerical columns:")
    print(dataframe.kurt())

    # Correlation matrix
    print("\nCorrelation Matrix:")
    print(dataframe[['Age', 'Height', 'Weight', 'Bmi']].corr())

display_basic_statistics(df)


# In[8]:


# Function 1: Histogram for BMI Class distribution
def plot_bmi_class_distribution(dataframe):
    plt.figure(figsize=(8, 6))
    sns.countplot(x='BmiClass', data=dataframe, palette='Set2')
    plt.title('Distribution of BMI Classes')
    plt.xlabel('BMI Class')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

plot_bmi_class_distribution(df)


# In[9]:


# Function 2: Scatter plot of BMI vs Age
def plot_bmi_vs_age(dataframe):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='Age', y='Bmi', hue='BmiClass', data=dataframe, palette='Set1')
    plt.title('Scatter Plot of BMI vs Age')
    plt.xlabel('Age')
    plt.ylabel('BMI')
    plt.legend(title='BMI Class', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

plot_bmi_vs_age(df)


# In[10]:


# Function 3: Heatmap of correlations between Age, Height, Weight, and BMI
def plot_correlation_heatmap(dataframe):
    plt.figure(figsize=(8, 6))
    corr = dataframe[['Age', 'Height', 'Weight', 'Bmi']].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Heatmap')
    plt.tight_layout()
    plt.show()

plot_correlation_heatmap(df)


# In[ ]:





# In[ ]:




