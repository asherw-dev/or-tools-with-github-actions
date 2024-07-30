# Graph Topological Sort Project

## Overview

This project provides a Python implementation for validating and finding topological sorts of directed acyclic graphs (DAGs) using OR-Tools. It also includes a GitHub Actions workflow for automated testing.

## Requirements

- Python 3.x
- Git

## Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/asherw-dev/or-tools-with-github-actions.git
   cd or-tools-with-github-actions
   ```

2. **Install Dependencies**

   Ensure you have Python 3.x installed. Then, install the required Python libraries:

   ```bash
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

## Running the Code

The `src` directory contains a default `graph_data.txt` file with graph data in the format:

```
source->target;source2->target2
```

To run the topological sort test, use:

```bash
python src/test_graph.py --file src/graph_data.txt
```

## GitHub Actions

The project is integrated with GitHub Actions to automate testing. The workflow triggers on push events and can also be manually triggered.

### Workflow Details

- **Trigger**: On push events or manually via `workflow_dispatch`
- **Steps**:
  1. Checkout the repository
  2. Set up Python and install dependencies
  3. Run the topological sort test

### Manual Trigger

To manually trigger the workflow:
1. Go to the Actions tab on GitHub.
2. Select the `Test topologic sort for graph` workflow.
3. Provide the graph in the format:
   ```
   source->target;source2->target2
   ```
   as input to test with a custom graph string.

## PyCharm Configuration

The project includes configuration files for PyCharm. Opening the project in PyCharm will benefit from the pre-configured settings, including:

- Run/Debug configurations with the graph file as an argument
- Dependency installation from `requirements.txt`

## Documentation

For more details on OR-Tools and graph handling, refer to the [OR-Tools documentation](https://developers.google.com/optimization).
