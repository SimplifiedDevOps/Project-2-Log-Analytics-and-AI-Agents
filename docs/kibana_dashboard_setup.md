# Kibana Dashboard Setup for Log Analysis

This document outlines the steps to create a Kibana dashboard for monitoring logs from the Java application.

## Step 1: Save Searches
1. Go to the *Discover* tab in Kibana.
2. Create a search for `log_level: ERROR` with a time filter for the last 24 hours. Save this as "Recent Errors."
3. Create a search for `error_code: 12345` to track logs with a specific error code. Save as "Error Code 12345 Logs."

## Step 2: Create Dashboard
1. Go to the *Dashboard* tab and create a new dashboard.
2. Add visualizations:
   - **Pie Chart** for Log Level Distribution
   - **Line Chart** for Error Code Frequency Over Time
   - **Table** for Recent Stack Traces
3. Add the saved searches ("Recent Errors", "Error Code 12345 Logs") to the dashboard.
4. Save the dashboard for quick monitoring of log patterns.
