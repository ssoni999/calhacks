from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models

# Create tables
models.Base.metadata.create_all(bind=engine)

# Create session
db: Session = SessionLocal()

try:
    # Create sample recruiters
    recruiter1 = models.Recruiter(name="Sarah Johnson", email="sarah.j@company.com")
    recruiter2 = models.Recruiter(name="Michael Chen", email="michael.c@company.com")
    
    db.add(recruiter1)
    db.add(recruiter2)
    db.commit()
    
    # Get recruiters for foreign keys
    recruiters = db.query(models.Recruiter).all()
    
    # Sample candidates for recruiter 1
    sample_candidates = [
        {
            "name": "Emma Watson",
            "email": "emma.watson@email.com",
            "position": "Software Engineer",
            "resume_text": """
PROFESSIONAL SUMMARY
Experienced software engineer with 5 years of experience developing scalable web applications using Python, JavaScript, React, and Node.js. Proven track record of building robust backend systems and modern frontend interfaces at major tech companies. Expertise in API development, database design, and cloud infrastructure deployment. Strong problem-solving skills and passion for clean, maintainable code.

WORK EXPERIENCE

Software Engineer | Tech Solutions Inc | San Francisco, CA | 2019 - Present
- Designed and developed scalable web applications serving 500k+ daily active users using Python, JavaScript, and React
- Architected and implemented RESTful APIs with Django and Flask frameworks, improving API response time by 40%
- Led migration of legacy system from monolithic architecture to microservices, reducing deployment time by 60%
- Collaborated with cross-functional teams including product managers, designers, and QA engineers
- Built real-time features using WebSocket technology and Socket.io for live collaboration
- Implemented comprehensive testing suite achieving 85% code coverage
- Worked extensively with PostgreSQL, Redis, and MongoDB databases
- Deployed applications on AWS using EC2, S3, RDS, and Lambda services

Junior Software Engineer | StartupCo | Palo Alto, CA | 2017 - 2019
- Developed and maintained React-based frontend applications
- Worked with Node.js and Express to build backend services
- Implemented CI/CD pipelines using Jenkins and Docker
- Participated in code reviews and mentored intern developers
- Contributed to open-source projects

TECHNICAL SKILLS
Languages: Python, JavaScript (ES6+), TypeScript, Java, SQL
Frameworks: React, Node.js, Django, Flask, Express
Databases: PostgreSQL, MongoDB, Redis, MySQL
Cloud: AWS (EC2, S3, RDS, Lambda, CloudFront)
Tools: Docker, Kubernetes, Jenkins, Git, JIRA
Testing: Jest, Pytest, Cypress, Selenium

EDUCATION
Bachelor of Science in Computer Science | Stanford University | 2013 - 2017
- Graduated Magna Cum Laude with GPA 3.8/4.0
- Relevant coursework: Data Structures, Algorithms, Database Systems, Software Engineering
- Senior project: Built a distributed task management system used by 100+ students

PROJECTS
- E-Commerce Platform: Full-stack application with Python/Django backend and React frontend
- Real-time Chat Application: Built with Node.js and Socket.io supporting thousands of concurrent users
- Portfolio Website: React/TypeScript application showcasing technical projects
            """,
            "stage": "Resume Review"
        },
        {
            "name": "James Rodriguez",
            "email": "james.r@email.com",
            "position": "Senior Software Engineer",
            "resume_text": """
PROFESSIONAL SUMMARY
Senior software engineer with 8 years of experience building distributed systems and cloud-native applications. Expert in designing and implementing scalable microservices architecture on AWS and GCP platforms. Led multiple engineering teams to deliver high-performance applications serving millions of users. Strong background in containerization, CI/CD pipelines, and infrastructure as code.

WORK EXPERIENCE

Senior Software Engineer | CloudScale Technologies | Seattle, WA | 2020 - Present
- Architected and built microservices-based platform handling 10M+ daily requests using Python, Java, and Go
- Led team of 5 engineers in designing distributed systems with Redis clustering and Kafka event streaming
- Implemented infrastructure as code using Terraform, reducing manual provisioning time by 80%
- Designed and deployed containerized applications using Docker and Kubernetes across multiple cloud regions
- Optimized database queries and caching strategies, reducing latency by 50% and cutting infrastructure costs by $200k annually
- Established CI/CD best practices and automated testing pipelines using Jenkins and GitLab CI
- Mentored junior engineers and conducted technical interviews for hiring
- Technologies: Python, Java, Go, AWS (ECS, EKS, S3, DynamoDB), GCP, Terraform, Kubernetes, Docker

Software Engineer | DataFlow Systems | San Jose, CA | 2016 - 2020
- Developed distributed data processing pipelines processing 1TB+ daily using Apache Spark
- Built RESTful APIs and GraphQL services serving real-time analytics to internal dashboards
- Implemented message queuing systems with RabbitMQ and Apache Kafka
- Containerized applications using Docker and orchestrated with Kubernetes
- Collaborated with data scientists to productionize machine learning models

Software Engineer | MobileApps Inc | Austin, TX | 2014 - 2016
- Built backend services for mobile applications using Node.js and Python
- Developed RESTful APIs with Django and Flask frameworks
- Worked with PostgreSQL, MongoDB, and Redis databases
- Implemented authentication and authorization systems using JWT tokens
- Deployed applications on AWS infrastructure

TECHNICAL SKILLS
Languages: Python, Java, Go, JavaScript, TypeScript, SQL
Frameworks: Django, Flask, Spring Boot, React, Node.js, Express
Cloud Platforms: AWS (extensive), GCP, Azure (basic)
Databases: PostgreSQL, MongoDB, Redis, DynamoDB, Cassandra
DevOps: Docker, Kubernetes, Terraform, Ansible, Jenkins, GitLab CI
Messaging: Apache Kafka, RabbitMQ, AWS SQS
Containers: Docker, Kubernetes, Docker Compose

EDUCATION
Master of Science in Computer Science | University of Texas at Austin | 2012 - 2014
- Specialization in Distributed Systems and Cloud Computing
- Thesis: "Optimizing Microservices Architecture for Low-Latency Applications"
- Relevant coursework: Advanced Algorithms, Distributed Systems, Cloud Computing

Bachelor of Science in Computer Science | Texas A&M University | 2008 - 2012
- Graduated Summa Cum Laude with GPA 3.9/4.0
            """,
            "stage": "Phone Screen"
        },
        {
            "name": "Sophia Lee",
            "email": "sophia.l@email.com",
            "position": "Full Stack Developer",
            "resume_text": """
PROFESSIONAL SUMMARY
Full stack developer with 3 years of experience developing end-to-end web applications. Proficient in building scalable SaaS products from scratch using modern JavaScript frameworks and Python. Strong understanding of modern development practices including Agile methodologies, test-driven development, and DevOps. Passionate about creating intuitive user experiences and clean, maintainable code.

WORK EXPERIENCE

Full Stack Developer | SaaS Innovations | Berkeley, CA | 2021 - Present
- Developed and launched 3 production SaaS products from ideation to deployment
- Built responsive frontend applications using React, TypeScript, and Tailwind CSS
- Designed and implemented RESTful APIs with Node.js, Express, and PostgreSQL
- Created comprehensive authentication systems with JWT tokens and OAuth 2.0
- Integrated third-party APIs (Stripe, SendGrid, Twilio) for payments and notifications
- Implemented real-time features using WebSockets and Socket.io
- Set up CI/CD pipelines with GitHub Actions and deployed to AWS
- Collaborated with product team to implement features based on user feedback
- Technologies: React, TypeScript, Node.js, Express, PostgreSQL, Redis, AWS, Docker

Software Developer Intern | TechStars Startup | San Francisco, CA | 2020 - 2021
- Developed features for a B2B SaaS platform using React and Python
- Worked with Django REST Framework to build API endpoints
- Created responsive UI components using React and Material-UI
- Participated in daily standups and sprint planning sessions
- Wrote unit tests using Jest and Pytest
- Implemented feature flags for gradual rollout of new features

PROJECTS
- Task Management SaaS: Full-stack application with React frontend and Node.js backend, 500+ active users
- E-commerce Platform: Built with Python/Django and React, integrated with Stripe for payments
- Social Networking App: Real-time chat and feed features using MERN stack
- Portfolio Website: Personal site showcasing projects, built with Next.js and deployed on Vercel

TECHNICAL SKILLS
Languages: JavaScript, TypeScript, Python, SQL, HTML, CSS
Frontend: React, Next.js, Vue.js, Redux, Tailwind CSS, Material-UI, Bootstrap
Backend: Node.js, Express, Django, Flask, REST APIs, GraphQL
Databases: PostgreSQL, MongoDB, Firebase, Redis
Cloud & DevOps: AWS, Heroku, Vercel, Docker, GitHub Actions
Testing: Jest, Pytest, Cypress, React Testing Library
Tools: Git, Webpack, Babel, ESLint, Prettier, Postman

EDUCATION
Bachelor of Science in Computer Science | UC Berkeley | 2017 - 2021
- Graduated with honors, GPA 3.7/4.0
- Relevant coursework: Web Development, Database Systems, Software Engineering, Distributed Systems
- Senior Capstone: Built a collaborative project management platform
- Member of Women in Computing student organization
            """,
            "stage": "Technical Interview"
        },
        {
            "name": "David Park",
            "email": "david.p@email.com",
            "position": "Backend Engineer",
            "resume_text": """
PROFESSIONAL SUMMARY
Backend engineer specialized in building high-performance RESTful APIs and microservices. Expertise in Python, database optimization, and cloud infrastructure. Worked on high-traffic applications serving millions of users. Strong background in distributed systems, caching strategies, and system architecture. Passionate about code quality, performance optimization, and scalable system design.

WORK EXPERIENCE

Backend Engineer | HighTraffic Systems | Los Angeles, CA | 2019 - Present
- Designed and developed RESTful APIs handling 50M+ requests daily using Python, Django, and Flask
- Optimized database queries and implemented Redis caching, improving API response time by 65%
- Built microservices architecture using Docker and Kubernetes, serving 10M+ concurrent users
- Implemented message queuing systems with RabbitMQ and Apache Kafka for async processing
- Designed and developed GraphQL APIs for flexible data querying
- Worked with PostgreSQL, MongoDB, and Elasticsearch for different use cases
- Deployed applications on AWS using EC2, RDS, S3, and Elastic Beanstalk
- Implemented comprehensive monitoring and logging using Datadog and ELK stack
- Collaborated with frontend team to design API contracts and data models
- Technologies: Python, Django, Flask, PostgreSQL, Redis, RabbitMQ, Docker, Kubernetes, AWS

Backend Developer | GrowthTech Startups | San Diego, CA | 2017 - 2019
- Developed RESTful APIs and background job processors using Python
- Worked with PostgreSQL and MongoDB databases for different data models
- Implemented authentication and authorization using JWT and OAuth
- Built data pipelines for processing and analyzing user behavior data
- Deployed applications on Heroku and AWS cloud infrastructure
- Participated in code reviews and maintained code quality standards

Junior Backend Developer | WebApps Solutions | Irvine, CA | 2016 - 2017
- Developed backend services using Python and Django framework
- Created RESTful APIs for mobile and web applications
- Worked with MySQL and PostgreSQL databases
- Implemented authentication systems and user management
- Wrote unit and integration tests using Pytest
- Deployed applications using Docker containers

TECHNICAL SKILLS
Languages: Python, SQL, Bash
Frameworks: Django, Flask, FastAPI, SQLAlchemy
Databases: PostgreSQL, MongoDB, Redis, MySQL, Elasticsearch
Message Queues: RabbitMQ, Apache Kafka, Celery
APIs: RESTful APIs, GraphQL, gRPC, SOAP
Cloud: AWS (EC2, S3, RDS, Lambda, ECS, EKS), Heroku
DevOps: Docker, Kubernetes, Jenkins, GitHub Actions
Monitoring: Datadog, ELK Stack, New Relic, Prometheus
Caching: Redis, Memcached
Testing: Pytest, unittest, Postman, pytest-django

EDUCATION
Bachelor of Science in Software Engineering | UC Irvine | 2012 - 2016
- Graduated with GPA 3.6/4.0
- Relevant coursework: Database Systems, Software Architecture, Distributed Computing, Algorithms
- Senior Project: Built a distributed task queue system using Python and Redis
            """,
            "stage": "Final Round"
        },
        {
            "name": "Isabella Martinez",
            "email": "isabella.m@email.com",
            "position": "Frontend Engineer",
            "resume_text": """
PROFESSIONAL SUMMARY
Frontend engineer with 4 years of experience building responsive, accessible, and performant user interfaces. Expert in React, Vue.js, TypeScript, and modern CSS. Passionate about creating exceptional user experiences and maintaining high code quality. Strong advocate for accessibility, responsive design, and progressive web applications. Active contributor to open source projects.

WORK EXPERIENCE

Frontend Engineer | DesignTech Solutions | San Francisco, CA | 2020 - Present
- Built responsive web applications using React, TypeScript, and styled-components serving 1M+ users
- Led migration of legacy jQuery codebase to modern React application, improving load time by 50%
- Implemented comprehensive design system with 50+ reusable components
- Developed mobile-first responsive designs ensuring 100% accessibility compliance (WCAG 2.1)
- Optimized bundle size and implemented code splitting, reducing initial load time by 40%
- Built real-time data visualization dashboards using D3.js and Recharts
- Implemented progressive web app (PWA) features for offline functionality
- Collaborated with UX designers to translate mockups into pixel-perfect interfaces
- Mentored junior developers and established frontend best practices
- Technologies: React, TypeScript, Next.js, Redux, Tailwind CSS, Storybook, Jest, Cypress

Frontend Developer | StartupHub | Mountain View, CA | 2018 - 2020
- Developed interactive single-page applications using React and Vue.js
- Built component libraries and UI kits for rapid prototyping
- Implemented state management using Redux and Vuex
- Created responsive layouts using Flexbox and CSS Grid
- Worked with designers to implement design systems
- Optimized application performance and implemented lazy loading
- Participated in design reviews and user testing sessions

Web Developer Intern | Digital Agency | Palo Alto, CA | 2017 - 2018
- Built responsive websites for clients using HTML, CSS, and JavaScript
- Worked with Bootstrap and custom CSS frameworks
- Implemented cross-browser compatibility and mobile responsiveness
- Collaborated with designers on multiple client projects

OPEN SOURCE CONTRIBUTIONS
- React DatePicker Component: 200+ stars on GitHub, actively maintained
- Vue Accessibility Plugin: Shared component library for accessible UI elements
- CSS Grid Layout System: Utility-first responsive layout system

TECHNICAL SKILLS
Languages: JavaScript (ES6+), TypeScript, HTML, CSS, SASS, SCSS
Frameworks/Libraries: React, Vue.js, Next.js, Redux, Vuex, React Query
Styling: Tailwind CSS, styled-components, CSS Modules, Bootstrap, Material-UI
Build Tools: Webpack, Vite, Babel, ESLint, Prettier
Testing: Jest, React Testing Library, Cypress, Playwright
Accessibility: WCAG 2.1 compliance, ARIA attributes, screen reader testing
Performance: Lighthouse optimization, bundle analysis, code splitting
Tools: Git, npm, yarn, Storybook, Chrome DevTools

EDUCATION
Bachelor of Science in Computer Science | UC Santa Barbara | 2013 - 2017
- Graduated Summa Cum Laude with GPA 3.9/4.0
- Relevant coursework: Human-Computer Interaction, User Interface Design, Web Development
- Senior Thesis: "Accessibility in Modern Web Development"
- President of Women in Tech student organization
            """,
            "stage": "Offer"
        },
        {
            "name": "Ryan Thompson",
            "email": "ryan.t@email.com",
            "position": "Software Engineer",
            "resume_text": """
PROFESSIONAL SUMMARY
Motivated software engineer with foundational experience in full-stack web development. Proficient in Python, JavaScript, and React. Eager to grow skills in software engineering and contribute to building modern web applications. Strong problem-solving abilities and commitment to learning industry best practices.

WORK EXPERIENCE

Software Engineering Intern | Local Web Agency | Sacramento, CA | 2022 - Present
- Developed web applications using Python and JavaScript
- Built responsive user interfaces using React and React Hooks
- Created RESTful API endpoints using Flask framework
- Worked with MySQL database for data persistence
- Implemented user authentication and session management
- Participated in agile development practices and daily standups
- Wrote unit tests using pytest and Jest
- Collaborated with senior developers on code reviews

PROJECTS
- Personal Portfolio Website: Built with React, featuring project showcases and blog
- Task Management App: Full-stack application using React frontend and Python backend
- Weather Dashboard: Real-time weather data visualization using React and weather APIs
- E-commerce Demo: Mock e-commerce site with React and integrated Stripe payment demo

TECHNICAL SKILLS
Languages: Python, JavaScript, HTML, CSS, SQL
Frameworks: React, Flask, Express
Databases: MySQL, PostgreSQL (beginner)
Version Control: Git, GitHub
Other: RESTful APIs, JSON, HTTP/HTTPS
Learning: Node.js, TypeScript, AWS basics

EDUCATION
Bachelor of Science in Computer Science | UC Davis | 2018 - 2022
- Graduated with GPA 3.5/4.0
- Relevant coursework: Web Development, Data Structures, Algorithms, Software Engineering
- Capstone project: Built a collaborative task management application
            """,
            "stage": "Resume Review"
        },
    ]
    
    for candidate_data in sample_candidates:
        candidate_data["recruiter_id"] = recruiters[0].id
        candidate = models.Candidate(**candidate_data)
        db.add(candidate)
    
    # Add some candidates for recruiter 2
    sample_candidates_r2 = [
        {
            "name": "Alex Turner",
            "email": "alex.t@email.com",
            "position": "DevOps Engineer",
            "resume_text": """
PROFESSIONAL SUMMARY
DevOps engineer with 6 years of experience automating deployments, managing cloud infrastructure, and building scalable CI/CD pipelines. Expert in AWS, Terraform, Jenkins, Docker, and Kubernetes. Proven track record of implementing infrastructure as code, reducing operational overhead, and ensuring high availability of production systems. Passionate about automation, monitoring, and cloud-native technologies.

WORK EXPERIENCE

Senior DevOps Engineer | CloudOps Solutions | Portland, OR | 2020 - Present
- Architected and implemented infrastructure as code using Terraform, managing 200+ AWS resources across multiple environments
- Designed and deployed containerized applications using Docker and Kubernetes, serving 50M+ requests daily
- Built comprehensive CI/CD pipelines using Jenkins and GitLab CI, reducing deployment time from 2 hours to 15 minutes
- Implemented automated monitoring and alerting using Prometheus, Grafana, and PagerDuty
- Migrated legacy applications from on-premises to AWS, reducing infrastructure costs by 60%
- Managed Kubernetes clusters with 500+ pods across staging and production environments
- Automated infrastructure provisioning using Terraform and Ansible
- Led incident response and troubleshooting for production outages
- Technologies: AWS, Terraform, Kubernetes, Docker, Jenkins, Python, Bash, Helm, Ansible

DevOps Engineer | TechCorp Systems | San Jose, CA | 2017 - 2020
- Automated application deployments using Jenkins and GitLab CI/CD pipelines
- Managed AWS infrastructure including EC2, ECS, S3, RDS, and VPC configurations
- Implemented infrastructure monitoring using CloudWatch, DataDog, and ELK stack
- Containerized legacy applications using Docker and orchestrated with Docker Swarm
- Wrote infrastructure automation scripts using Python, Bash, and Terraform
- Performed security hardening and compliance audits
- Collaborated with development teams to improve deployment processes

Junior DevOps Engineer | StartupX | Oakland, CA | 2016 - 2017
- Managed AWS cloud infrastructure for multiple projects
- Built and maintained CI/CD pipelines for web applications
- Automated server provisioning using Ansible playbooks
- Monitored application performance and availability
- Assisted in security audits and compliance checks

TECHNICAL SKILLS
Cloud Platforms: AWS (EC2, ECS, EKS, S3, RDS, Lambda, CloudFormation), GCP, Azure
Containerization: Docker, Kubernetes, Docker Swarm
Infrastructure as Code: Terraform, CloudFormation, Ansible
CI/CD: Jenkins, GitLab CI, GitHub Actions, CircleCI, Travis CI
Monitoring: Prometheus, Grafana, DataDog, CloudWatch, ELK Stack
Scripting: Python, Bash, Shell scripting
Version Control: Git, GitHub, GitLab
Configuration Management: Ansible, Puppet, Chef
Tools: Helm, kubectl, AWS CLI, Terraform CLI, Docker Compose
OS: Linux (Ubuntu, CentOS, Amazon Linux)

EDUCATION
Bachelor of Science in Computer Engineering | UC Berkeley | 2012 - 2016
- Graduated with GPA 3.7/4.0
- Relevant coursework: Operating Systems, Computer Networks, Cloud Computing, Distributed Systems
- Senior Project: Built automated infrastructure deployment pipeline
            """,
            "stage": "Technical Interview"
        },
        {
            "name": "Olivia Brown",
            "email": "olivia.b@email.com",
            "position": "Data Engineer",
            "resume_text": """
PROFESSIONAL SUMMARY
Data engineer specializing in building scalable data pipelines, ETL processes, and real-time data processing systems. Strong expertise in Python, SQL, Apache Spark, and cloud data warehouses. Experience designing and implementing data architectures that process terabytes of data daily. Passionate about data quality, scalability, and enabling data-driven decision making.

WORK EXPERIENCE

Senior Data Engineer | DataFlow Analytics | Boston, MA | 2020 - Present
- Designed and implemented real-time data pipelines processing 1TB+ daily using Apache Spark and Kafka
- Built data lake architecture on AWS S3 using Parquet format, reducing storage costs by 40%
- Developed ETL pipelines using Python, Spark, and Airflow for batch processing
- Optimized Spark jobs and SQL queries, reducing processing time by 60%
- Implemented data quality checks and monitoring using Great Expectations and DataDog
- Worked with data warehouses including Redshift, Snowflake, and BigQuery
- Designed and built real-time analytics dashboards for business stakeholders
- Collaborated with data scientists to productionize machine learning models
- Technologies: Python, Spark, SQL, Kafka, Airflow, AWS (S3, Redshift, EMR), Snowflake, Airflow

Data Engineer | Analytics Corp | Cambridge, MA | 2018 - 2020
- Built and maintained ETL pipelines using Python, pandas, and SQL
- Developed data processing workflows processing millions of records daily
- Worked with PostgreSQL, MongoDB, and Elasticsearch databases
- Implemented data validation and quality checks
- Created data pipelines for business intelligence and reporting
- Optimized database queries and indexes for better performance
- Automated data collection and processing tasks

Junior Data Engineer | TechStart Data | Boston, MA | 2016 - 2018
- Developed Python scripts for data extraction and transformation
- Worked with SQL databases for data analysis and reporting
- Built automated data pipelines for daily data updates
- Performed data cleaning and validation
- Created data visualizations and reports using Tableau
- Assisted in building data infrastructure

TECHNICAL SKILLS
Programming: Python, SQL, Scala, Java
Big Data: Apache Spark, Hadoop, Kafka, Airflow, Beam
Databases: PostgreSQL, MySQL, MongoDB, Redis, Elasticsearch
Cloud: AWS (S3, Redshift, EMR, Glue), GCP (BigQuery, Dataflow), Snowflake
Data Warehouses: Redshift, BigQuery, Snowflake, Azure Synapse
ETL Tools: Airflow, Luigi, Prefect, AWS Glue
Data Formats: Parquet, ORC, Avro, JSON, CSV
Data Quality: Great Expectations, dbt, Deequ
ML/Analytics: Scikit-learn, Pandas, NumPy, Jupyter
Visualization: Tableau, Looker, Metabase

EDUCATION
Master of Science in Data Science | Massachusetts Institute of Technology | 2014 - 2016
- Specialization in Machine Learning and Big Data
- Thesis: "Scalable Data Processing for Real-Time Analytics"
- Relevant coursework: Data Mining, Machine Learning, Distributed Systems, Database Systems
- TA for Introduction to Data Science course

Bachelor of Science in Computer Science | Stanford University | 2010 - 2014
- Graduated Cum Laude with GPA 3.8/4.0
- Relevant coursework: Data Structures, Algorithms, Database Systems, Statistics
            """,
            "stage": "Final Round"
        },
    ]
    
    for candidate_data in sample_candidates_r2:
        candidate_data["recruiter_id"] = recruiters[1].id
        candidate = models.Candidate(**candidate_data)
        db.add(candidate)
    
    db.commit()
    print("Database initialized with sample data!")
    print(f"Created {len(recruiters)} recruiters and {len(sample_candidates) + len(sample_candidates_r2)} candidates")
    
except Exception as e:
    db.rollback()
    print(f"Error: {e}")
    raise
finally:
    db.close()

