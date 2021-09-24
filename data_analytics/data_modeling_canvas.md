Pre-inspection
    Check feature identifiers
    .describe() / .info() / .head()
    Check for duplicates

Feature selection
    Correlations to Label
    Correlation between features?
    Feature selection

Feature (and label) preparation, all features together
    Split numerical and categorical freatures

Feature (and label) preparation per feature
    Datatype modification where necessary
    Numerical features
        Outliers by plot / by standardized aproach
        Distribution
            Log-transformation (log1p?) against positive skew (skew>.75)
        missing values (imputation / row removal / >.15 feature removal)
        Normalization / Standardization
    Categorical features
        missing values (imputation / row removal / feature removal)
        one-hot-encoding

Generating additional features
    Variations from single feature (^^2, ^^3, sqrt)
    Combination of similar features

Split dataset
    Train / Validation / Test

Modeling

Evaluation



Todo:
Impalanced class representations (regression?)
Collinearity