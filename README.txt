
NetPilot is a lightweight network infrastructure automation and monitoring platform designed to centralize basic administration, troubleshooting, and automation tasks for devices and servers.

The application allows users to register devices such as routers, switches, or servers by providing basic information including name, IP address, and device type. From a web dashboard, users can check the status of each device and run connectivity checks using tools such as ICMP, TCP connections, port validation, or HTTP requests.

The backend is developed in Python using FastAPI and exposes a REST API that connects the frontend with the database and automation services. PostgreSQL stores registered devices, connectivity check history, and the results of executed automations.

One of NetPilot's main features is its integration with Ansible. From the interface, users can select a device and run predefined playbooks to perform tasks such as retrieving the hostname, checking uptime, obtaining system information, or executing administrative operations. Each execution creates a job whose status, result, errors, and execution time are recorded on the platform.

The frontend, developed with React, presents this information through a simple dashboard that provides a quick overview of online devices, offline devices, recent errors, and automation jobs.

The entire system runs using Docker Compose, separating the frontend, backend, and database into independent containers. The project also includes automated tests with Pytest and a CI/CD pipeline that validates the code and automatically builds the containers.

The goal of NetPilot is not to replace an enterprise-grade Network Automation platform, but to directly demonstrate how software development, networking, automation, databases, testing, APIs, containers, and DevOps practices can be integrated into a small but functional solution.

Local backend setup
