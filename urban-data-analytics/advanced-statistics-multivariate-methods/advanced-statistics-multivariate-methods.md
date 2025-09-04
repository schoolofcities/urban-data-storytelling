---
title: "Advanced statistics and multivariate methods"
author: "Aniket Kali"
---

[📥 Click here to download this document and any associated data and images](/downloads/advanced-statistics-multivariate-methods.zip)

This section will cover:
 
- the utility and limitations of multivariate statistical models
- key statistical approaches including regression, clustering, and dimensionality reduction techniques
- a high-level introduction to advanced machine learning methods

In the previous section on statistical foundations, we provided a detailed overview with lots of practice. The content of this section is much more advanced; each subsection often ends up being weeks of university courses. In this chapter then, we'll just be providing an overview of different methods, intuition, applications, and resources for you to learn more and apply these methods yourself.

## Why use more advanced models?

In the previous section on statistical foundations, we learned how to describe, find relationships, and test hypotheses in the data. Much of the time, this will get you quite far. Sometimes, however, it won’t be enough: suppose you want to understand housing prices, where income, education, distance to downtown, and neighborhood crime, all interact. Or, perhaps you want to discern which neighborhoods are similar based on many demographic variables. These kinds of questions require us to go beyond the simple one variable methods we've seen.

Multivariate methods are tools for analyzing situations where many variables operate together. Cities are intrinsically multivariate systems: built environment, demographics, infrastructure, mobility patterns, environmental factors - these are all interdependent, and a single one rarely tells the full story.

In this chapter, we’ll introduce three major families of multivariate methods:

 - Regression and classification models, which explain or predict outcomes based on multiple predictors.
 - Clustering methods, which group similar observations without pre-defined categories.
 - Dimensionality reduction techniques, which simplify complex, high-dimensional data into a smaller set of underlying structures.

Each of these approaches has a trade-off between interpretability and predictive power. Regression, for example, allows us to easily observe the relationship between particular variables, but loses nuance. That nuance might be preserved in other methods, but at the loss of direct causal interpretation. The key to using these methods effectively is to know what it is you're trying to achieve, as that will tell you what is a priority in your analysis.

## Regression and classification models

In the previous chapter, we talked about simple linear regression. The goal was straightforward: figure out how one variable affects another. It isn't a big leap toward more advanced regression models. Instead of that one variable, now we ask questions like:

 - How do multiple variables affect another?
 - Is a certain outcome likelier because of multiple variables?
 - What is the role of distance and spatial relationships in predicting an outcome?

Below, you can see an overview of different methods and a link to libraries used to implement them.

### Classical regression

Classical regression models let us study how multiple predictors together influence an outcome. They're useful when we want to isolate the effect of individual factors - like income, education, or transit access - while holding others constant.

| Method | What it is / When to use | Example |
|--------|-------------------------|---------|
| [Linear regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html) | Models a continuous outcome predicted by one or more variables. Works best when relationships are roughly straight line. | Estimating how housing price varies with distance to city center, number of rooms, and neighborhood crime rate. |
| [Logistic regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) | Models the probability of a binary outcome (yes/no). Useful when the dependent variable has two categories. | Predicting whether or not a household owns a car based on income, household size, and transit accessibility. |
| [Multinomial regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) | Logistic regression but generalized to more than two, unordered categories | Predicting primary commuting mode choice (car, bus, subway, bike, walking) based on demographic and location variables. |
| [Ordinal regression](https://www.statsmodels.org/stable/examples/notebooks/generated/ordinal_regression.html) | Handles outcomes that are ordinal (ranked categories). Assumes the "distance" between categories may not be equal. | Modeling residents' reported satisfaction with local services (e.g., "poor," "fair," "good," "excellent"). |

### Spatial regression

Spatial regression is just an extension of the classical models. It recognizes that places are not just independent, and that in cities, what might happen in one neighborhood can spill over to another.

| Method | What it is / When to use | Example |
|--------|---------------------------|---------|
| [Spatial lag model](https://pysal.org/spreg/generated/spreg.ML_Lag.html) | Adds the influence of nearby areas’ outcomes into the model. Use when you think what happens in one place directly affects its neighbors. | Housing prices in one neighborhood tend to rise if surrounding neighborhoods also become more expensive. |
| [Spatial error model](https://pysal.org/spreg/generated/spreg.ML_Error.html) | Adjusts for unmeasured factors that are clustered in space. Use when missing variables or regional patterns cause neighboring areas to have similar errors. | Air pollution levels in adjacent districts may be correlated because of wind patterns or shared industrial sources, even after controlling for known predictors. |

## Cluster analysis

## Dimensionality reduction

## Advanced machine learning

## Choosing the right tool

