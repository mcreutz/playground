# PromQL querying

## Metric types
There are 4 types of metrics: 

#### Gauges
- standard time series
- floating point number

#### Counters
- integer
- can only only increase
- are reset to 0 when the emitting process is restarted, but rate-functions compensate for that
- counter values itself are mostly not useful to visualize, usually you use the rate function to make use of them

#### Histograms
- tbd

#### Summaries
- tbd

## Querying
- Evaulation timestamp is the time we are querying for

### Instant vector selector: `my_metric_name`
- Will return the last value for all metrics with that name 
- Usually only the last value of a series is returned. if there is no value in the system default lookback window of 5 minutes, the series is not returned at all.
- The returned values timestamp is set to the evaluation timestamp
under certain conditions, the series is marked as stale in the db and then no values are returned if the seiries matches the query

### Label filter: `my_metric_name{label="value"}`
- `{label="value"}` - will return metrics that have the given label and value
- `{label!="value"}` - will return all metrics that do *not* have the given label and value
- `{label=~"buffers|cache"}` - will return all metrics that have the given label with a value that matches the regex
- `{label!~".*some_regex.*"}` - will return all metrics that do *not* have the given label with a value that matches the regex
- `{label="value", label2="value2"}` - label filters can be combined with a comma, which is a logical AND

Best practice: Always use a label fileter, as different services might have the same metric names, but different labels.

### Range selector: `my_metric_name[5m]`
- Will return all metrics with that name and the given labels, but only the last 5 minutes from the evaluation timestamp
- Range values cannot be displayed in the graph view, only in the table view. to make them displayable, use the rate function.
- Staleness markers are ignored for range queries, so all values in the range are returned, even if they are stale

### Rate functions
- All rate functions need to find at least 2 data points in the given window to calculate the rate. Otherwise, the result is `NaN`.

#### Rate: `rate(my_metric_name[5m])`
- Will return the average rate of change per second of the metric over the last 5 minutes
use this one over 'irate' and 'increase', unless you have a good reason not to

#### Irate: `irate(my_metric_name[5m])`
- Actual counter difference per second, non-avaraged (instantaneously, using only the last data points of the time window)

#### Increase: `increase(counter_total[5m])`
- Absolute counter difference over the time window (range). Not per second as `rate` and `irate`.
- Scales the measured increase of the counter to the whole time window. This can lead to values higher than the actual increase.
- Has some more edge cases, handle with care.

### Offsets: `my_metric_name offset 5m`
- Will return the value of the metric 5 minutes before the evaluation timestamp
- Time values of the returned values are set to the evaluation timestamp, not the actual time of the value
- Do not use to actually evaluate past values, but use for comparison calculations

### Syntactic order
Example: `rate(metric name{label="value"}[10m]) offset 20m`
- Will return the rate per second of all metrics that match name and labels, averaged over the last 10 minutes, with an offset of 20 minutes