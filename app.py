'''
import streamlit as st
import pandas as pd
from apputil import (
    survival_demographics,
    visualize_demographic,
    family_groups,
    last_names,
    visualize_families,
    determine_age_division,
    visualize_age_division,
)

# -------------------------------
# Load dataset
# -------------------------------
df = pd.read_csv("train.csv")

# -------------------------------
# Streamlit Layout
# -------------------------------
st.title("🚢 Titanic Data Analysis")

# Sidebar menu to switch between exercises
option = st.sidebar.radio(
    "Choose an Exercise:",
    (
        "Exercise 1: Survival Patterns",
        "Exercise 2: Family Size and Wealth",
        "Exercise 3: Age Division (Bonus)"
    )
)

# -------------------------------
# Exercise 1
# -------------------------------
if option == "Exercise 1: Survival Patterns":
    st.header("Exercise 1: Survival Patterns")

    # Run demographics analysis
    results = survival_demographics(df)

    st.subheader("Demographic Survival Table")
    st.dataframe(results)

    # Pose a question
    st.write("❓ Did women in first class have a higher survival rate than men in other classes?")

    # Visualization
    fig = visualize_demographic(results)
    st.plotly_chart(fig)


# -------------------------------
# Exercise 2
# -------------------------------
elif option == "Exercise 2: Family Size and Wealth":
    st.header("Exercise 2: Family Size and Wealth")

    # Family size and wealth analysis
    family_results = family_groups(df)
    st.subheader("Family Groups Table")
    st.dataframe(family_results)

    # Last name frequency analysis
    last_name_counts = last_names(df)
    st.subheader("Most Common Last Names")
    st.write(last_name_counts.head(10))  # show top 10 for clarity

    # Pose a question
    st.write("❓ Did larger families in higher classes pay significantly more for their tickets?")

    # Visualization
    fig2 = visualize_families(family_results)
    st.plotly_chart(fig2)


# -------------------------------
# Exercise 3 (Bonus)
# -------------------------------
elif option == "Exercise 3: Age Division (Bonus)":
    st.header("Exercise 3: Age Division (Bonus Question)")

    # Apply function
    updated_df = determine_age_division(df)

    st.subheader("Dataset with 'older_passenger' column")
    st.dataframe(updated_df[["PassengerId", "Pclass", "Age", "older_passenger"]].head(15))

    # Pose a question
    st.write("❓ Did being older than the median age of your class affect your survival chances?")

    # Visualization
    fig3 = visualize_age_division(updated_df)
    st.plotly_chart(fig3)
'''



import streamlit as st
import pandas as pd

from apputil import *

# Load Titanic dataset

df = pd.read_csv('https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv')

st.set_page_config(page_title="Titanic Explorations", layout="wide")

st.title("Titanic Analysis Exercises")


# Exercise 1: Survival Patterns

st.subheader("Exercise 1: Survival Patterns")

st.write(
    "**Question:** Within each passenger class, how do survival rates compare between women and men across age groups?"
)

# Compute and display the result table
demo_tbl = survival_demographics(df)
st.subheader("Results Table: Survival by Class, Sex, and Age Group")
st.dataframe(demo_tbl)

fig1 = visualize_demographic(df)
st.plotly_chart(fig1, use_container_width=True)


# Exercise 2: Family Size and Wealth

st.subheader("Exercise 2: Family Size and Wealth")


st.write(
    "**Question:** How does average fare change with family size across passenger classes, and where are the largest groups by count?"
)

fam_tbl = family_groups(df)
st.subheader("Results Table: Family Size & Fare by Class")
st.dataframe(fam_tbl)

fig2 = visualize_families(df)
st.plotly_chart(fig2, use_container_width=True)

# Last names frequency analysis
st.subheader("Last Names (Counts)")
ln_series = last_names(df)
st.write(
    "**Last Name Analysis:** Below is the frequency of last names in the dataset. Compare large-family clusters in the table above with common surnames:"
    "An alternative approach is to count passengers with the same last name. However, these methods can differ. "
    "The `family_size` method is more precise for nuclear families, while counting last names might group "
    "extended family or unrelated individuals, and could miss family members with different last names."
)
st.dataframe(ln_series.rename("count").to_frame())

# Bonus: Age Division vs Outcomes

st.subheader("Bonus: Above-Median Age Within Class")

st.write(
    "**Question:** Within each class, how does survival rate differ for older vs. not-older passengers, and does this vary by sex?"
)

df_with_div = determine_age_division(df)
st.subheader("Sample of the New Column `older_passenger`")
st.dataframe(df_with_div[["Pclass", "Sex", "Age", "older_passenger"]].head(12))

fig3 = visualize_age_division(df)
st.plotly_chart(fig3, use_container_width=True)






