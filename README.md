# Toil Reduction Automation

This project focuses on reducing toil by automating repetitive tasks encountered during on-call shifts and release management. The aim is to save time, minimize errors, and enhance efficiency. The project includes two automated solutions implemented with pseudocode: **Log Management Automation** and **DNS Failover Automation**.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Toil Reduction Plan](#toil-reduction-plan)
3. [Automated Solutions](#automated-solutions)
    - [Log Management Automation](#log-management-automation)
    - [DNS Failover Automation](#dns-failover-automation)
4. [Release Scenario](#release-scenario)
5. [On-Call Scenario](#on-call-scenario)
6. [How to Use](#how-to-use)
7. [Future Improvements](#future-improvements)
8. [License](#license)

---

## Introduction

Toil refers to repetitive, manual work that does not scale and provides limited enduring value. This project identifies four toil items, chooses two to automate, and provides pseudocode for the automation.

### Goals:
- Reduce repetitive workload.
- Automate log management to prevent storage overflow.
- Automate DNS failover for high availability and service reliability.

---

## Toil Reduction Plan

| Toil Item             | Why it is Considered Toil       | Benefits of Automation                                |
|-----------------------|---------------------------------|-----------------------------------------------------|
| Log Management        | Manual log rotation is time-consuming and error-prone. | Automating ensures storage optimization and saves time. |
| DNS Failover          | Requires manual intervention during outages. | Reduces downtime with instant failover mechanisms. |
| Releasing Updates     | Manually verifying release health is repetitive. | Automation ensures consistency and faster checks. |
| Incident Reporting    | Writing reports manually takes time. | Automated reporting standardizes and saves effort. |

---

## Automated Solutions

### 1. Log Management Automation

This script automates log rotation and archiving when disk usage exceeds a predefined threshold.

#### How It Works:
1. Checks disk usage of the log directory.
2. Compresses logs into a zip file and saves them in an archive directory.
3. Deletes original logs after successful archiving.

#### When to Use:
- Use this script as part of a daily cron job to prevent storage overflow.

---

### 2. DNS Failover Automation

This script monitors the primary DNS server and initiates a failover to a secondary DNS server if the primary becomes unreachable.

#### How It Works:
1. Pings the primary DNS server periodically to check availability.
2. If unavailable, redirects traffic to the secondary server automatically.

#### When to Use:
- Run as a daemon or background service to ensure high availability.

---

## Release Scenario

### As-Built Document

#### Stakeholders
- Development Team
- Operations Team
- Product Owners
- End Users

#### Application Changes
1. **Data Model Changes**: Added new fields to support feature X, optimized table Y for faster queries.
2. **System Changes**: Upgraded server infrastructure to handle increased traffic.
3. **Code Changes**: Refactored module Z to support new features and improve maintainability.

#### Design Decisions and Testing Highlights
- Modular architecture chosen for scalability.
- Load testing confirmed the system can handle 150% of projected traffic.
- Security tests ensured no vulnerabilities introduced.

#### Deployment Process Changes
- Automated deployment pipeline for faster release.
- Added rollback procedures for fail-safe deployments.

#### Capacity Planning
The deployment file for Release 2 has been updated to:
- Increase server resources by 25% to accommodate feature requirements.
- Add auto-scaling rules to manage sudden traffic spikes.

---

## On-Call Scenario

### On-Call Summary Log
- **Issue 1**: High disk usage on server A.
    - **Resolution**: Cleared temporary files and added a monitoring rule.
- **Issue 2**: DNS outage impacting service B.
    - **Resolution**: Manually updated DNS records to a secondary server.
- **Issue 3**: Unexpected API latency in module C.
    - **Resolution**: Rebooted services and identified root cause (misconfigured timeout).

### Blameless Post-Mortem

#### What Caused the Outage:
- Primary DNS server failure due to expired certificates.

#### Why It Occurred:
- Monitoring did not alert on impending certificate expiry.

#### What the Response Was:
- DNS traffic rerouted manually to the secondary server.
- Certificates renewed immediately.

#### How to Prevent It Going Forward:
- Implement monitoring for certificate expiry.
- Automate DNS failover to reduce manual intervention.

#### Future Reliability Concerns:
- Lack of centralized log management may delay troubleshooting.
- Limited monitoring coverage for edge cases like certificate expiry.

---

## How to Use

### Prerequisites:
1. **Python 3.x** installed on the system.
2. Necessary permissions for accessing log files and DNS tools.

### Instructions:
1. Clone the repository:
   ```bash
   git clone https://github.com/phan-van-thuy/sre-project04.git
