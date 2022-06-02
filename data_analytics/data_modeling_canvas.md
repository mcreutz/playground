This worksfow is ordered from the computational point of view. The workflow may be in a slightly different order.

Pre-inspection
    Check feature identifiers (what is this?)
    .describe() / .info() / .head()
    Check for duplicates

Split dataset
    Test
        Typically 20% Test-dataset
        Use seed value or indexes, to have always the same values for validation and test, even when further values are added to the original dataset
        Use stratified split methods, to ensure equal feature distribution in train and test dataset.
    Validation
    Test
        This is the rest of the data. If it is too big for efficient exploratory analysis, create an subset for EDA.
        Separate labels from features

Feature selection
    Generating additional features
        Variations from single feature (^^2, ^^3, sqrt)
        Aggregation or combination of similar/connected features, eg:
        - Count of daily logins instead of all events
        - count_of_houses / count_of_rooms = avg_rooms_per_house
        Decompose existing features, eg:
        - split datetime to date and time, or use the hour only, whatever seems suitable for the problem
    Correlations to Label
    Correlation between features / redundant features
    Also check for non-linear correlations
    
Feature preparation
    Datatype modification where necessary
    missing values (univariate or multivariate imputation / row removal / >.15 feature removal)
    Split numerical and categorical freatures
    Numerical features
        Untrue values
            Value-encoded errors (-1, 999, 0, ...)
            Capped values
        Outliers
            Find by (histogram/scatter) plot / by standardized aproach (what does this mean?)
            Remove by ...
        Distribution
            Log-transformation (log1p?) against positive skew (skew>.75)
        Normalization / Standardization
    Categorical features
        one-hot-encoding
    Lables
        Remove samples with missing label-values?

Modeling

Evaluation



Todo:
Impalanced class representations (regression?)
Collinearity