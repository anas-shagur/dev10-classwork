# import numpy as np
import scipy.stats as stats


def print_describe(title, describe_result):
    _, (min, max), mean, var, skew, kurt = describe_result
    print(title)
    print(
        f"min: {min:.4f}, max: {max:.4f}, mean: {mean:.4f}, variance: {var:.4f}, skewness: {skew:.4f}, kurtosis: {kurt:.4f}"
    )


def confirm_null_hypothesis():
    # `loc` is the mean of the distribution
    # `scale` is the standard deviation of the distribution
    # `size` is the number of samples
    q1_2023_sales = stats.norm.rvs(loc=1000, scale=100, size=91)
    q1_2024_sales = stats.norm.rvs(loc=1000, scale=100, size=91)

    print_describe("Q1 2023 Sales", stats.describe(q1_2023_sales))
    print_describe("Q1 2024 Sales", stats.describe(q1_2024_sales))

    # `ttest_ind` performs a t-test on two independent samples.
    # It does the calculation for us!
    t_test, p_value = stats.ttest_ind(q1_2023_sales, q1_2024_sales)
    print(f"t-test: {t_test}, p-value: {p_value}")
    print(f"p-value > 0.05: {p_value > 0.05}")


def confirm_alternative_hypothesis():
    q1_2023_sales = stats.norm.rvs(loc=1000, scale=100, size=91)
    # The mean of the distribution is increased by 100
    q1_2024_sales_with_advertising = stats.norm.rvs(loc=1100, scale=100, size=91)

    print_describe("Q1 2023 Sales", stats.describe(q1_2023_sales))
    print_describe(
        "Q1 2024 Sales w/ Advertising", stats.describe(q1_2024_sales_with_advertising)
    )

    t_test, p_value = stats.ttest_ind(q1_2023_sales, q1_2024_sales_with_advertising)
    print(f"t-test: {t_test}, p-value: {p_value}")
    print(f"p-value > 0.05: {p_value > 0.05}")


def confirm_neither_hypothesis():
    q1_2023_sales = stats.norm.rvs(loc=1000, scale=100, size=91)
    # The mean of the distribution is increased by 100
    q1_2024_sales = stats.norm.rvs(loc=1100, scale=100, size=91)

    print_describe("Q1 2023 Sales", stats.describe(q1_2023_sales))
    print_describe(r"Q1 2024 Sales? ¯\_(ツ)_/¯", stats.describe(q1_2024_sales))

    t_test, p_value = stats.ttest_ind(q1_2023_sales, q1_2024_sales)
    print(f"t-test: {t_test}, p-value: {p_value}")
    print(f"p-value > 0.05: {p_value > 0.05}")


def pearson_correlation():
    # Example data for hours of exercise and hours on social media
    hours_of_exercise = [1.0, 2.0, 1.5, 3.0, 2.5, 0.5, 4.0, 3.5, 1.0, 2.0]
    hours_on_social_media = [4.0, 3.0, 3.5, 2.0, 2.5, 5.0, 1.5, 2.0, 4.5, 3.0]

    pearson_coefficient, p_value = stats.pearsonr(
        hours_of_exercise, hours_on_social_media
    )

    # The Pearson coefficient is -0.97, which is a strong negative linear relationship.
    print(f"Pearson Coefficient: {pearson_coefficient}, p-value: {p_value}")

    # Example data for hours of exercise and protein increase
    grams_of_protein = [
        0,
        40,
        30,
        60,
        50,
        8,
        80,
        70,
        -5,
        15,
    ]

    # The Pearson coefficient is 0.944, which is a strong positive linear relationship.
    pearson_coefficient, p_value = stats.pearsonr(hours_of_exercise, grams_of_protein)
    print(f"Pearson Coefficient: {pearson_coefficient}, p-value: {p_value}")

    # Example data for hours of exercise and time spent with clowns
    time_spent_with_clowns = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    pearson_coefficient, p_value = stats.pearsonr(
        hours_of_exercise, time_spent_with_clowns
    )

    # The Pearson coefficient is 0.275, which is a weak positive linear relationship.
    print(f"Pearson Coefficient: {pearson_coefficient}, p-value: {p_value}")


def spearman_correlation():
    # Example data for hours of exercise and hours on social media
    hours_of_exercise = [1.0, 2.0, 1.5, 3.0, 2.5, 0.5, 4.0, 3.5, 1.0, 2.0]
    hours_on_social_media = [4.0, 3.0, 3.5, 2.0, 2.5, 5.0, 1.5, 2.0, 4.5, 3.0]

    spearman_coefficient, p_value = stats.spearmanr(
        hours_of_exercise, hours_on_social_media
    )

    # The Spearman coefficient is -0.99, which is a strong negative monotonic relationship.
    print(f"Spearman Coefficient: {spearman_coefficient}, p-value: {p_value}")

    # Example data for hours of exercise and protein increase
    grams_of_protein = [
        0,
        40,
        30,
        60,
        50,
        8,
        80,
        70,
        -5,
        15,
    ]

    # The Spearman coefficient is 0.939, which is a strong positive monotonic relationship.
    spearman_coefficient, p_value = stats.spearmanr(hours_of_exercise, grams_of_protein)
    print(f"Spearman Coefficient: {spearman_coefficient}, p-value: {p_value}")

    # Example data for hours of exercise and time spent with clowns
    time_spent_with_clowns = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    spearman_coefficient, p_value = stats.spearmanr(
        hours_of_exercise, time_spent_with_clowns
    )

    # The Spearman coefficient is 0.292, which is a weak positive monotonic relationship.
    print(f"Spearman Coefficient: {spearman_coefficient}, p-value: {p_value}")


def main():
    while True:
        print("0. Exit")
        print("1. Confirm Null Hypothesis")
        print("2. Confirm Alternative Hypothesis")
        print("3. Confirm Neither Hypothesis")
        print("4. Pearson Correlation")
        print("5. Spearman Correlation")

        option = input("Select [0-5]: ")
        if option == "0":
            break
        elif option == "1":
            confirm_null_hypothesis()
        elif option == "2":
            confirm_alternative_hypothesis()
        elif option == "3":
            confirm_neither_hypothesis()
        elif option == "4":
            pearson_correlation()
        elif option == "5":
            spearman_correlation()


if __name__ == "__main__":
    main()
