# AGENTS.md

This file provides guidance to all ai coding agents when working with code in this repository.

## Repository Overview

This is a multi-purpose playground repository containing examples, reference code, and experimental projects across finance, data analytics, machine learning, DevOps, and software development.

## Development Environment

### Python Environment Management
- **Primary**: Root `pyproject.toml` contains comprehensive dependencies for data science, ML, and finance
- **Package Manager**: Uses `uv` for modern Python package management (see `software_dev/python/env_management/uv.md`)
- **Alternative**: Some projects use Poetry (see `poetry.lock` files in subdirectories)
- **Dependencies**: Includes data science stack (pandas, numpy, scikit-learn), finance libraries (zipline, yfinance, ib-insync), ML tools (mlflow, wandb), and web frameworks (fastapi, django)

### JavaScript/Node.js Projects
- Located in `software_dev/javascript/`
- React projects use `react-scripts` for build/test
- Vue.js projects use Vite for development and build
- Standard npm/yarn package management

## Common Development Commands

### Python Development
```bash
# Install dependencies (if using uv)
uv sync

# Code formatting and linting (dev dependencies)
black .
mypy .
pylint .

# Testing
pytest
```

### JavaScript Projects
```bash
# React projects
npm start          # Development server
npm test           # Run tests
npm run build      # Production build

# Vue.js projects
npm run dev        # Development server
npm run build      # Production build
```

### Jupyter Notebooks
- Extensive use of Jupyter notebooks for data analysis and experimentation
- Primary notebooks in: `finance/`, `data_analytics/`, `ml_ops/`
- Use `ipykernel` for Python notebook support

## Major Project Areas

### Finance (`/finance/`)
- **Backtesting**: Zipline and VectorBT for algorithmic trading strategies
- **Data Sources**: yfinance, CCXT (crypto), EOD Historical Data, Interactive Brokers API
- **Technologies**: Pandas for financial data manipulation, Jupyter for analysis

### Data Analytics (`/data_analytics/`)
- **Machine Learning**: scikit-learn with comprehensive classifier comparisons
- **Visualization**: Matplotlib, Plotly, Seaborn, Dash for interactive dashboards
- **Statistics**: statsmodels for time series and statistical analysis
- **Deep Learning**: TensorFlow/Keras examples and tutorials

### ML Ops (`/ml_ops/`)
- **Experiment Tracking**: MLflow (containerized deployment)
- **Pipelines**: Kubeflow Pipelines
- **Monitoring**: Weights & Biases (wandb) integration

### DevOps (`/dev_ops/`)
- **Container Orchestration**: Extensive Kubernetes configurations and Helm charts
- **CI/CD**: ArgoCD, multiple deployment strategies (Kustomize, Helmfile, Kluctl)
- **Infrastructure**: Terraform for AWS, Ansible for configuration management
- **Monitoring**: Prometheus/Grafana/Loki stack configurations
- **Cloud**: AWS Lambda, ECS, CloudWatch examples

### AI Tools (`/ai/`)
- **Platforms**: Ollama, LangFlow, OpenWebUI
- **Agents**: SmoLAgents (HuggingFace), K8sGPT
- **Deployment**: Kubernetes Helm charts for AI services

### Software Development (`/software_dev/`)
- **Languages**: Python, Go, JavaScript, Java, C++
- **Frameworks**: Django, FastAPI, React, Vue.js, Node.js
- **Design Patterns**: Comprehensive examples of SOLID principles, behavioral/structural/creational patterns
- **Testing**: pytest, unittest patterns with fixtures and mocking

## Architecture Patterns

### Containerization
- Docker-first approach with multi-service docker-compose configurations
- Kubernetes deployment preferences with Helm chart templating
- Service mesh configurations (Istio) for microservices

### Testing Strategies
- Python: Both pytest and unittest with comprehensive fixture patterns
- Go: Native testing framework with benchmark examples
- JavaScript: Jest/React Testing Library for React applications

### Configuration Management
- Infrastructure as Code: Terraform for cloud resources, Ansible for system configuration
- GitOps deployment patterns with ArgoCD
- Environment-specific configurations (dev/staging/prod)

## File Organization Conventions

- Each major area has its own dependency management (`pyproject.toml`, `package.json`)
- Reference documentation and READMEs in most subdirectories
- Jupyter notebooks for exploratory work and analysis
- Separate directories for different technologies and languages
- Examples follow language-specific project structure conventions

## Working with This Repository

When adding new code:
- Follow existing directory structure and naming conventions
- Use appropriate dependency management for the technology stack
- Include documentation for complex implementations
- Maintain separation between different project areas
- Consider containerization for deployable applications