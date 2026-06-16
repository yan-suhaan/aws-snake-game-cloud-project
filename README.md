AWS Snake Game Cloud Project

Project Overview

This project demonstrates the deployment of a cloud-native Snake Game application on Amazon Web Services (AWS). The application was developed using Python Flask and integrated with Amazon RDS (MariaDB) for persistent score storage.

The project was designed to demonstrate practical cloud engineering skills including networking, compute, databases, monitoring, load balancing, scaling, and backup strategies.

---

Technologies Used

Application Layer

- Python
- Flask
- PyMySQL
- HTML
- CSS
- JavaScript

AWS Services

- Amazon VPC
- Public and Private Subnets
- Internet Gateway
- Route Tables
- Network ACLs
- Security Groups
- Amazon EC2
- Amazon RDS (MariaDB)
- Amazon S3
- Amazon CloudWatch
- Application Load Balancer (ALB)
- Auto Scaling Group (ASG)
- IAM Roles

---

Architecture

Users access the application through an Application Load Balancer.

The ALB routes traffic to EC2 instances running the Flask-based Snake Game.

The application stores leaderboard information in Amazon RDS (MariaDB).

Amazon CloudWatch is used for monitoring and logging.

Amazon S3 is used for database backup storage.

---

Architecture Diagram

Users
↓
Application Load Balancer
↓
Target Group
↓
Auto Scaling Group
↓
EC2 Instances (Flask Application)
↓
Amazon RDS (MariaDB)

CloudWatch → Monitoring

Amazon S3 → Database Backups

---

Features

- Snake Game
- Score Tracking
- Leaderboard Storage
- Database Integration
- Cloud Monitoring
- Load Balancing
- Auto Scaling
- Backup Storage
- High Availability Architecture

---

Infrastructure Components

Networking

- Custom VPC
- Public Subnets
- Private Subnets
- Internet Gateway
- Route Tables
- Network ACLs

Security

- Security Groups
- IAM Roles
- Private Database Access

Compute

- Amazon EC2
- Flask Application Server

Database

- Amazon RDS MariaDB
- Leaderboard Storage

Monitoring

- CloudWatch Agent
- CloudWatch Metrics
- CloudWatch Logs

Scalability

- Application Load Balancer
- Auto Scaling Group

Storage

- Amazon S3 Backup Storage

---

Challenges Solved

ALB Health Check Failure

Problem:
Target group instances became unhealthy.

Solution:
Verified Flask application status, corrected application startup process, and validated health check configuration.

RDS Connectivity

Problem:
Application could not communicate with the database.

Solution:
Configured security group rules to allow MySQL traffic from EC2 to RDS.

CloudWatch Monitoring

Problem:
Metrics and logs were not available.

Solution:
Installed and configured Amazon CloudWatch Agent and validated agent operation.

---

Skills Demonstrated

- AWS Infrastructure Deployment
- Linux Administration
- Python Development
- Database Integration
- Networking Concepts
- Cloud Monitoring
- Troubleshooting
- Security Configuration
- High Availability Design

---

Author

Suhaan S Safaliga

Bachelor of Computer Applications (BCA)

AWS Cloud Engineering Project
