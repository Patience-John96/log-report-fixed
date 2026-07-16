There is an Apache-style access log at /app/access.log. Parse it and write a JSON
summary report to /app/report.json with exactly these three keys:

- "total_requests": integer, the total number of log lines (requests) in the file.
- "unique_ips": integer, the count of distinct client IP addresses that made requests.
- "top_path": string, the request path (e.g. "/index.html") that appears most often
  across all requests. If there is a tie, use the path that appears first in the log.

You have 120 seconds to complete this task. Do not cheat by using online solutions or hints specific to this task.
