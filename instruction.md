Your task is to analyze the Apache-style access log located at:
/app/access.log
Generate a JSON file named:
/app/report.json
The JSON object must contain exactly these fields:
1. total_requests
   - Total number of log entries.
2. unique_ips
   - Number of distinct client IP addresses.
3. top_path
   - The request path that appears most frequently.
Success Criteria
1. Create /app/report.json.
2. total_requests equals 6.
3. unique_ips equals 3.
4. top_path equals "/index.html".