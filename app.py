
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



