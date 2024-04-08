# Relabeling
Each set of labels for a metric creates an individual time series. Having many timeseries can be expensive in terms of storage and query performance, so it is important to keep the cardinality of the labels low. Otherwise, do not reduce the cardinality too much, as you might lose important information. Balance is key.

## There are 4 areas where labels are used and relabeling can be applied
#### Scraping targets
- are being attatched to all metrics from that target
- target list before relabeling is at webui - status - service discovery
- target list after relabeling is at webui - status - targets

Docs: https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config

#### Scraped metrics
#### Alerting rules
#### Recording rules


## Meta labels
- name starts with "__" 
- used to store metadata about the target
- are being removed after relabeling
- K8s meta labels see: https://prometheus.io/docs/prometheus/latest/configuration/configuration/#kubernetes_sd_config


## Actions
- `replace`: Replace the value in matching labels. If no match, add new label
- `keep`: Keep only matching objects. Non-matching objects are removed.
- `drop`: Drop matching objects. 
- `labeldrop`: Drop matching labels.
- `labelkeep`: Keep only matching labels.
- `labelmap`: Matches existing labels and creates new ones of them. Eg. useful for keeping meta labels.

See documentation for more details: https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config

### Important
If all labels from an object are removed, the whole object is ignored!


## Sythetic metrics for scrape targets
These metrics are not exposed by the target itself, but are created by Prometheus to provide additional information about the scrape target. They are useful for monitoring the health of the scrape target and the scrape process itself.

- `up{job="<job-name>", instance="<instance-id>"}`: 1 if the instance is healthy, i.e. reachable, or 0 if the scrape failed.
- `scrape_duration_seconds{job="<job-name>", instance="<instance-id>"}`: duration of the scrape.
- `scrape_samples_post_metric_relabeling{job="<job-name>", instance="<instance-id>"}`: the number of samples remaining after metric relabeling was applied.
- `scrape_samples_scraped{job="<job-name>", instance="<instance-id>"}`: the number of samples the target exposed.
- `scrape_series_added{job="<job-name>", instance="<instance-id>"}`: the approximate number of new series in this scrape. New in v2.10

Documentation: https://prometheus.io/docs/concepts/jobs_instances/#automatically-generated-labels-and-time-series

## Relabeling tool  
https://relabeler.promlabs.com/

