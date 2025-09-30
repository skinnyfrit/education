# Course Outcomes
TBA

## Table of contents  

0. [R, RStudio, Shortcuts and Dependency](#r-rstudio-shortcuts-and-dependency)
1. [Foundation of Data Analytics with R](#foundation-of-data-analytics-with-r)
2. [Exploring Data: Descriptive and Inferential Statistics in R](#exploring-data-descriptive-and-inferential-statistics-in-r)
3. [Understanding Distributions, Sampling, and Estimation](#understanding-distributions-sampling-and-estimation)
4. [Preparing and Comparing Data: t-tests, ANOVA, and Hypothesis Testing](#preparing-and-comparing-data-t-tests-anova-and-hypothesis-testing)
5. [Predictive Analytics I - Introduction to ML and LR](#predictive-analytics-i---introduction-to-ml-and-lr)
6. [Predictive Analytics II - MLR, Model complexity, Generalization, and Bias-Variance Tradeoff](#predictive-analytics-ii---mlr-model-complexity-generalization-and-bias-variance-tradeoff)
7. [Predictive Analytics III - Logistic Regression](#predictive-analytics-iii---logistic-regression)
8. [Predictive Analytics IV - Decision Trees](#predictive-analytics-iv---decision-trees)
9. [Advanced Topics in Predictive Modeling and Business Impact](#advanced-topics-in-predictive-modeling-and-business-impact)
10. [Prescriptive Analytics: Introduction to Optimization and Decision Models](#prescriptive-analytics-introduction-to-optimization-and-decision-models) 

# R, RStudio, Shortcuts and Dependency
## Working Directory
Check current working directory: ``getwd()``  
Set current working directory: ``setwd("C:/Users/YourName/Documents/R_Projects")``  
Show files in CWD: ``list.files()``

## Basic R Operations & Data Types  
> [!NOTE]
> Use snake_case for variable names.

Use `<-` for assignment *(preferred over =)*
Check data types: ``class()`` or ``typeof()`` 
* Data types:
    * Numeric
        * Double (internal storage type obtained using ``typeof()``)
        * Integer (internal storage type obtained using ``typeof()``)
    * Character (text)
    * Logical (boolean)

Creating vectors (collection of values): ``c()``  
* Some examples of built-in functions:
    * ``mean()``
    * `sum()`
    * `length()`
    * `rowSums()`
    * `colSums()`
    * `summary()`

> [!NOTE]
> R uses 1-based indexing (starts at 1, not 0)

Accessing items in a vector: ``vector[1]``
*similar to python*

## R Vector Type Coercion
https://github.com/skinnyfrit/education/blob/35ea162a365398e1090758504e18c791bf0c8a57/tcx2002.r#L1-L4  
Hierarchy for data type coercion: 
> Logical < Integer < Double (Numeric) < Complex (Imaginary value) < Character
- Logical being weakest and Character being strongest  

Fixing numeric vector that includes character type: ``as.numeric()``  
To be able to parse values after conversion, include na.rm = T :``mean(vector, na.rm = TRUE)`` 

## Matrices
Changing 1-D vector to 2-D matrix  
https://github.com/skinnyfrit/education/blob/5b741e74665d61ff0436dceaa15c6f6c39aa8a96/tcx2002.r#L6C1-L18C23  
Accessing items in a matrix: ``matrix[1,2]`` or ``matrix[row_name, col_name]``
*can use both indexing and row/col name*

> [!NOTE]
> Remember to follow the [row, col] format (e.g. matrix[, col_name] if you want all rows of a specified column)

## Factors (Categorical Data)
Levels/Priority of categories  
Example: 
```
product vector:
c("Electronics", "Clothing", "Electronics", "Books", "Clothing")

product categories: (no factor involvement, no proper levels set, thus they are set alphabetically)
Levels: Books Clothing Electronics
```
https://github.com/skinnyfrit/education/blob/5b741e74665d61ff0436dceaa15c6f6c39aa8a96/tcx2002.r#L20C1-L37C31  

## Data Frames (Tables)
https://github.com/skinnyfrit/education/blob/5b741e74665d61ff0436dceaa15c6f6c39aa8a96/tcx2002.r#L39C1-L57C32  
- Show first 6 rows: `head()`
- Show last 6 rows: `tail()`
- Inspect data frame structure: `str()` *shows col types and first few values*
- Accessing specific columns by name: `dataframe$column1`
- Selecting multiple columns by name (or index): `dataframe[c("column1","column2")]` (or `dataframe[c(1, 3)]`)
- Access data w/ multiple variables involved:
    - `dataframe[dataframe$column1 == "Value1" & dataframe$column2 > 10, ]`
    - `dataframe[dataframe$column1 %in% c("Value1", "Value2"), ]` *%in% means whether right in left column vs dplyr/tidyverse %>% means 'and then'/pipe*
- Accessing specific data:
    - `dataframe[dataframe$column1 == "Value1", ]`
    - `dataframe[grepl("^A", dataframe$column1),]` *finds all data in column1 starting with "A" (using grepl for pattern matching)*

## Special Values & Missing Data
NA  
is.na()  
sum(is.na()) # gives total number of NA values  


## Reading and Writing Data


# Foundation of Data Analytics with R
Check r script  
Tidyverse Packages  
Import/Exporting data  
Date/Time handling  
Data Joins

# Exploring Data: Descriptive and Inferential Statistics in R
Check r script (GGplot2)  

# Understanding Distributions, Sampling, and Estimation
- Probability
- Normal Distribution
- Sampling
- CLT, CI and Point Estimation

# Preparing and Comparing Data: t-tests, ANOVA, and Hypothesis Testing
- ANOVA

# Predictive Analytics I - Introduction to ML and LR 
## Machine Learning
traditional programming vs machine learning
rules + data -> ans
vs
data + ans -> rules (model)

Examples of machine learning applications in businesses
| Industry | ML Application | Business Value | Typical ROI (examples) |
|---|---|---|---|
| Retail | Demand forecasting | Optimal inventory levels | 15-20% cost reduction |
| Marketing | Customer segmentation | Targeted campaigns | 20-30% better conversion |
| Finance | Credit scoring | Risk assessment | 10-20% lower defaults |
| Operations | Predictive maintenance | Reduce downtime | 25-35% cost savings |
| HR | Employee retention | Reduce turnover | $15k+ per retained employee |

> [!IMPORTANT]
> Good input -> good output. ML requires good data to work.  
>   More data != better results. No correlation!  
>   Simple models often outperform complex ones!

### Types of Machine Learning
1. Supervised Learning: Use when labeled data is available and specific predictions are needed
2. Unsupervised Learning: Use when exploring unlabeled data to find hidden patterns
3. Reinforcement Learning: Use when learning through interaction and feedback is necessary

| Characteristics | Supervised | Unsupervised | Reinforcement |
|---|---|---|---|
| Learning Style | Learning with teacher, guided | Learning without teacher | Learning through trial & error |
| Primary Goal | Predict outcomes | Discover hidden patterns | Optimize actions |
| Example Use Cases | Predicting house prices | Customer segmentation | Game playing (optimise chess moves, etc.) |

### Supervised Learning 
Primary focus as it directly addresses most business prediction problems.  
- Shows the algorithm many examples of inputs and their correct outputs
- So that it can predict outputs for new inputs

Regression vs Classification problem  
|  | Regression | Classification |
|---|---|---|
| Goal | Predict a continuous number | Predict a category or class |
| Qn Type | "How much..?" or "How many..?" | "Which type..?" or "Will it happen..?" |
| Business examples | Sales forecasting, stock price prediction, customer lifetime value, etc. | Email spam detection, product recommendations, credit approval (yes/no), customer segmentation, fraud detection |

### CRISP-DM
Cross-Indsutry Standard Process for Data Mining (CRISP-DM)  
1. Business Understanding: 
2. Data Understanding: 
3. Data Preparation: 
4. Modeling: 
5. Evaluation: 
6. Deployment: 
7. Model Management: 

Best practices: 
- Start simple, then increase complexity
- Document everything for reproducibility
- 80/20 rule (80% data prep, 20% modeling)
- Validate business assumptions early
- Plan for ongoing maintenance and monitoring

Pitfalls to avoid:
- Skipping business understanding phase
- Poor data quality due to rushed exploration
- Model overfitting that doesn't generalize
- Ignoring deployment challenges
- No monitoring plan for production models

### Train-Test
70-30 Train-Test sample/split data  
purpose, data, process, outcome  
risks of overfitting

### Random vs Stratified Samples
random vs stratified  
how, best for?, risk/benefits, examples

### Matching Predictive Techniques to Data Types
||||

> [!CAUTION]
> Data Leakages

### Correlation
* Strong Positive: 0.7 - 1.0
* Moderate Positive: 0.3 - 0.7
* No Correlation: -0.3 - 0.3
* Moderate Negative: -0.7 - -0.3
* Strong Negative: -0.7 - -1.0

Pearson's Correlation Coefficient

Usefulness & limitations of correlation



# Predictive Analytics II - MLR, Model complexity, Generalization, and Bias-Variance Tradeoff
- Regression (continued)

# (Lab Test)

# Predictive Analytics III - Logistic Regression

# Predictive Analytics IV - Decision Trees

# --Break--

# Prescriptive Analytics: Introduction to Optimization and Decision Models I


# Prescriptive Analytics: Introduction to Optimization and Decision Models II
