import os
from datetime import datetime

from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig
from cosmos.profiles import SnowflakeUserPasswordProfileMapping

profile_config = ProfileConfig(
    profile_name='default',
    target_name='dev',
    profile_mapping=SnowflakeUserPasswordProfileMapping(
        conn_id='snowflake_conn',
        profile_args={'database':'dbt_db', 'schema':'dbt_schema'}
    )
)

execution_config = ExecutionConfig(
    dbt_executable_path='/usr/local/airflow/dbt_venv/bin/dbt'
)

dbt_snowflake_dag = DbtDag(
    project_config= ProjectConfig(dbt_project_path = '/usr/local/airflow/dags/dbt/dbt_pipeline'),
    operator_args={'install_deps':True},
    profile_config = profile_config,
    execution_config = execution_config,
    schedule_interval='@daily',
    start_date=datetime(2024,11,1),
    catchup=False,
    dag_id='dbt_dag'
)