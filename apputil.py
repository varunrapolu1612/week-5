
import pandas as pd
import plotly.express as px

# -------------------------------
# Exercise 1: Survival Patterns
# -------------------------------
def survival_demographics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Analyze survival patterns by class, sex, and age group.
    Returns a table with n_passengers, n_survivors, and survival_rate.
    """
    # Create Age Groups
    bins = [0, 12, 19, 59, 120]
    labels = ["Child", "Teen", "Adult", "Senior"]
    df["AgeGroup"] = pd.cut(df["Age"], bins=bins, labels=labels, right=True)

    # Group by Class, Sex, and Age Group
    grouped = (
        df.groupby(["Pclass", "Sex", "AgeGroup"])
        .agg(
            n_passengers=("PassengerId", "count"),
            n_survivors=("Survived", "sum")
        )
        .reset_index()
    )

    # Survival rate
    grouped["survival_rate"] = grouped["n_survivors"] / grouped["n_passengers"]

    # Order
    grouped["AgeGroup"] = pd.Categorical(grouped["AgeGroup"], categories=labels, ordered=True)
    grouped = grouped.sort_values(by=["Pclass", "Sex", "AgeGroup"]).reset_index(drop=True)

    return grouped


def visualize_demographic(df: pd.DataFrame):
    """
    Create a Plotly visualization for survival demographics.
    """
    fig = px.bar(
        df,
        x="AgeGroup",
        y="survival_rate",
        color="Sex",
        barmode="group",
        facet_col="Pclass",
        text="survival_rate",
        category_orders={"AgeGroup": ["Child", "Teen", "Adult", "Senior"]},
        labels={"survival_rate": "Survival Rate", "Pclass": "Passenger Class"},
        title="Survival Rates by Class, Sex, and Age Group"
    )
    fig.update_traces(texttemplate="%{text:.2f}", textposition="outside")
    fig.update_layout(yaxis=dict(tickformat=".0%"))

    return fig


# -------------------------------
# Exercise 2: Family Size & Wealth
# -------------------------------
def family_groups(df: pd.DataFrame) -> pd.DataFrame:
    """
    Analyze family size, passenger class, and ticket fare.
    """
    df["family_size"] = df["SibSp"] + df["Parch"] + 1

    grouped = (
        df.groupby(["family_size", "Pclass"])
        .agg(
            n_passengers=("PassengerId", "count"),
            avg_fare=("Fare", "mean"),
            min_fare=("Fare", "min"),
            max_fare=("Fare", "max")
        )
        .reset_index()
    )

    grouped = grouped.sort_values(by=["Pclass", "family_size"]).reset_index(drop=True)
    return grouped


def last_names(df: pd.DataFrame) -> pd.Series:
    """
    Extract last names and return their counts.
    """
    df["LastName"] = df["Name"].apply(lambda x: x.split(",")[0].strip())
    last_name_counts = df["LastName"].value_counts()
    return last_name_counts


def visualize_families(df: pd.DataFrame):
    """
    Plot family size vs average fare, split by class.
    """
    fig = px.line(
        df,
        x="family_size",
        y="avg_fare",
        color="Pclass",
        markers=True,
        labels={"avg_fare": "Average Fare", "family_size": "Family Size"},
        title="Average Fare by Family Size and Passenger Class"
    )
    return fig


# -------------------------------
# Exercise 3: Age Division (Bonus)
# -------------------------------
def determine_age_division(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add a new column 'older_passenger' that indicates whether a passenger
    is older than the median age of their passenger class.
    """
    # Compute median age per class
    medians = df.groupby("Pclass")["Age"].transform("median")
    
    # True if Age > median for that class
    df["older_passenger"] = df["Age"] > medians
    
    return df


def visualize_age_division(df: pd.DataFrame):
    """
    Visualize how survival relates to being older or younger than
    the class median age.
    """
    grouped = (
        df.groupby(["Pclass", "older_passenger"])
        .agg(
            n_passengers=("PassengerId", "count"),
            n_survivors=("Survived", "sum")
        )
        .reset_index()
    )
    grouped["survival_rate"] = grouped["n_survivors"] / grouped["n_passengers"]

    fig = px.bar(
        grouped,
        x="Pclass",
        y="survival_rate",
        color="older_passenger",
        barmode="group",
        text="survival_rate",
        labels={"survival_rate": "Survival Rate", "older_passenger": "Older than Class Median"},
        title="Survival Rate by Passenger Class and Age Division"
    )
    fig.update_traces(texttemplate="%{text:.2f}", textposition="outside")
    fig.update_layout(yaxis=dict(tickformat=".0%"))

    return fig




