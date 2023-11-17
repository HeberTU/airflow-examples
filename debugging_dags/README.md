## Usage

To get started wit debugging locally, you have to:


1. install al dependencies with poetry:
```bash
poetry install
```

2. Activate the environment: 
```bash
source .venv/bin/activate
```

3. Set the `AIRFLOW_HOME` to the project path 
```bash
export AIRFLOW_HOME=/path/to/your/project
```

4. Initialize the airflow db 
```bash
airflow db migrate
```

5. Check that the db is initialized 
```bash
airflow db check
```

6. For Pycharm, add `AIRFLOW_HOME` to environmental debugging variables.