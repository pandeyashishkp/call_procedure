from google.cloud import bigquery
from flask import Flask
import os
from glob import glob


app = Flask(__name__)


client = bigquery.Client(project='ash11123')
fl = glob("templates/*.sql")
for fn in fl:
    scr_name = fn.split(".sql")[0].split("/")[-1]
    with open(fn) as f:
        sql_script = f.read()
        query = f"""
        CREATE OR REPLACE PROCEDURE tetramumbai.{scr_name}()
        BEGIN
            {sql_script}
        END
        """
        job_config = bigquery.job.QueryJobConfig(use_query_cache=False)
        results = client.query(query, job_config=job_config)
port = int(os.environ.get('PORT', 8080))
app.run(debug=True, host='0.0.0.0', port=port)
