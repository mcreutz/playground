# Alertmanager

## Core Concepts

### Silencing
- Temporarily suppress alerts based on matchers (labels)
- Typically used during maintenance windows or for known issues
- Can be created via UI or API with expiration time

### Muting
- Similar to silencing but typically refers to permanent suppression
- Typically used for known issues that are not expected to resolve themselves
- Configured through routing rules to send alerts to null receiver

### Inhibitions
- Suppress alerts when other alerts are already firing
- Prevents alert spam from cascading failures
- Example: Suppress instance-down alerts when entire cluster is down

### Groups
- Batch related alerts together to reduce notification noise
- Configured by grouping labels (e.g., cluster, service)
- Alerts in same group are sent in single notification

### Notifications
- Deliver alerts to various receivers (email, Slack, PagerDuty, etc.)
- Routing tree determines which alerts go to which receivers
- Support for templates to customize message format
