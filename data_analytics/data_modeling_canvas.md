Pre-inspection
    Check feature identifiers/names
    .describe() / .info() / .head()

Lables Preparation
    Correct or remove samples with missing or incorrect label-values
    Not part of the pipeline

Split dataset
    Test
        Typically 20% Test-dataset
        Use seed value or indexes, to have always the same values for validation and test, even when further values are added to the original dataset
        Use stratified split methods, to ensure equal feature distribution in train and test dataset.
    Validation
        For hyperparameter optimization
        Alternatively use CrossValidation on training data
    Training
        This is the rest of the data. If it is too big for efficient exploratory analysis, create an subset for EDA.
        Separate labels from features

Exploratory Data Analysis / Feature selection
    Correlations to Label
    Correlation between features / redundant features
    Also check for non-linear correlations
    Generating additional features
        Variations from single feature (^^2, ^^3, sqrt)
        Aggregation or combination of similar/connected features, eg:
        - Count of daily logins instead of all events
        - count_of_houses / count_of_rooms = avg_rooms_per_house
        Decompose existing features, eg:
        - split datetime to date and time, or use the hour only, whatever seems suitable for the problem
    
Feature preparation (of selected features)
    Datatype modification where necessary
    missing values (univariate or multivariate imputation / row removal / >.15 feature removal)
    Numerical features
        Untrue values
            Value-encoded errors (-1, 999, 0, ...)
            Capped values
        Outliers
            Find/Remove by (histogram/scatter) plot / by standardized aproach
        Distribution
            Log-transformation (log1p?) against positive skew (skew>.75)
        Normalization / Standardization
    Categorical features
        one-hot-encoding

Create pipeline

Modeling
    Split train and test datasets into features and labels (X, y)
    Evaluate different models (algos, architectures, further hyperparameters) with cross-validation on training data
    Score final model against test data



Todo:
Impalanced class representations (regression?)
Collinearity
Pipeline
Normalization / Standardization
