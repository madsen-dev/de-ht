# Data Platform Solution: Invoices & Countries

## Task

Make the _Invoices_ and _Countries_ tables available for consumption through the company’s data platform.

---

## Basic Idea (Medallion Architecture)

1. **Bronze (raw):** Ingest raw data into the lakehouse in an open format (e.g., Delta/Parquet).
2. **Silver (processed):** Clean and standardize data, apply incremental updates, and optimize with partitioning.
3. **Gold (transformed):** Create business-ready models (denormalized, aggregated, and joined with dimensions).
4. **Consumption:** BI tools connect to the gold layer for analysis.
5. **Orchestration:** An orchestration tool coordinates the entire flow end-to-end.

---

## Proposed Solution

### 1. Extraction (Batch, Bronze)

- **dlt (data load tool)** ingests the _Invoices_ and _Countries_ tables from the source systems into the lakehouse.
- Data is stored in the **Databricks Lakehouse (Delta/Parquet format)** as the raw bronze layer.

**Alternative Ingestion Solutions:**

- **Azure Data Factory**
- **Airbyte**
- **Fivetran**
- **Apache Kafka** - event-based streaming for near real-time ingestion instead of batch processing

### 2. Processing (Silver)

- **Azure Databricks (Spark)** processes the bronze data.
- Steps include cleaning, deduplication, incremental loading, and partitioning (important for the large _Invoices_ table).

### 3. Transformation (Gold)

- **dbt** runs on top of Databricks to model the data.
- It builds reusable, documented tables such as:
  - `dim_countries` (dimension)
  - `fct_invoices` (fact table, aggregated and joined with countries).
- dbt also provides **tests and lineage tracking** for quality assurance.

### 4. Visualization & Consumption

- **Power BI** connects directly to the gold layer in Databricks (via SQL endpoints).
- Analysts can explore invoices by country, trends, and drill down to individual invoices.

**Alternative Visualization Tools:**

- **Steep**
- **Evidence.dev**

### 5. Orchestration

- **Airflow DAGs** orchestrate the pipeline end-to-end:

  - Trigger dlt ingestion.
  - Run Databricks Spark jobs for processing.
  - Execute dbt transformations.
  - Refresh Power BI (or other BI tool) datasets if needed.

- **Airflow Setup**:
  - **Error handling & retry logic** to make the pipeline resilient to temporary failures.
  - **Scheduled automatic updates** to ensure data is always fresh and up to date.
  - **Alerting & monitoring** for pipeline failures, enabling quick response and minimizing downtime.

---

## End-to-End Flow

The pipeline is orchestrated by **Airflow**, which triggers and manages all steps:

**Source → Bronze Layer (dlt) → Silver Layer (Databricks Spark) → Gold Layer (dbt) → BI Tools (Power BI, Steep, Evidence.dev)**

Airflow handles scheduling, retries, and alerting across all layers, ensuring a reliable and automated data flow.
