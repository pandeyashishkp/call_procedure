from google.cloud import bigquery
from flask import Flask
import os


app = Flask(__name__)


client = bigquery.Client(project='ash11123')
query = """
    CREATE OR REPLACE PROCEDURE tetramumbai.proc()
    BEGIN
        select year from tetramumbai.summer;
    END;
"""
job_config = bigquery.job.QueryJobConfig(use_query_cache=False)
results = client.query(query, job_config=job_config)
port = int(os.environ.get('PORT', 5000))
app.run(debug=True, host='0.0.0.0', port=port)
