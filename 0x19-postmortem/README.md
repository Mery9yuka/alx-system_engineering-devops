Issue:
Duration of Outage:

Start Time: June 1, 2024, 09:00 AM (UTC)
End Time: June 1, 2024, 11:30 AM (UTC)
Impact:

Service Affected: User Authentication Service
User Experience: Users were unable to log in or register on our platform.
Percentage of Users Affected: 100%
Root Cause:

A misconfiguration in the authentication microservice deployment caused the service to crash under high load, leading to a complete outage.
Timeline
09:00 AM: Issue detected via monitoring alert indicating high error rates in the authentication service.
09:05 AM: Incident escalated to the on-call engineer.
09:10 AM: On-call engineer began investigating the authentication service logs.
09:20 AM: Initial assumption was a bug in the recent deployment; rollback initiated.
09:40 AM: Rollback completed, but the issue persisted.
09:50 AM: Further investigation revealed configuration errors in the deployment settings.
10:00 AM: Misleading path: checked database for possible issues with user data, no issues found.
10:30 AM: Escalated to the DevOps team to review deployment configurations.
11:00 AM: DevOps team identified and corrected the configuration errors.
11:15 AM: Redeployment initiated with correct settings.
11:30 AM: Service restored, users able to log in and register again.
Root Cause and Resolution

Root Cause:
The root cause was a misconfiguration in the deployment settings of the authentication microservice. The configuration did not properly handle high load scenarios, causing the service to crash when the number of concurrent login attempts spiked.

Resolution:
The issue was resolved by: Me( Maryem )

Identifying the incorrect settings in the deployment configuration.
Correcting the settings to ensure the service could handle high loads.
Redeploying the authentication service with the updated configuration.
Corrective and Preventative Measures
Improvements/Fixes:

Deployment Configuration Review: Implement a more thorough review process for deployment configurations to catch potential issues before they go live.
Load Testing: Introduce regular load testing for all critical services to ensure they can handle high traffic scenarios.
Monitoring Enhancements: Enhance monitoring to include more detailed metrics and alerts specifically for configuration issues.
Tasks to Address the Issue:

 Conduct a full review of the authentication service deployment process.
 Implement automated configuration validation checks.
 Schedule regular load testing for the authentication service.
 Update monitoring systems to include alerts for configuration discrepancies.
 Train the engineering team on best practices for deployment configurations.

By addressing these areas, we can minimize the risk of similar outages in the future and improve the overall reliability of our services.