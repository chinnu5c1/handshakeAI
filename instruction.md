Analyze the Apache-style access log located at:
/app/access.log
Generate a JSON report at:
/app/report.json
The JSON object must contain exactly the following fields:
1. total_requests
   - The total number of log entries.
2. unique_ips
   - The number of distinct client IP addresses.
3. top_path
   - The request path that appears most frequently.
Success Criteria
1. Create the file /app/report.json.
2. The value of total_requests must be 6.
3. The value of unique_ips must be 3.
4. The value of top_path must be "/index.html".
You have 120 seconds to complete this task. Do not cheat by using online solutions or hints specific to this task.