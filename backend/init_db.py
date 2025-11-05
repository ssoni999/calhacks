from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models

# Create tables
models.Base.metadata.create_all(bind=engine)

# Create session
db: Session = SessionLocal()

def analyze_resume(resume_text: str, position: str) -> dict:
    """AI-powered resume analysis based on keywords"""
    experience_keywords = ["experience", "years", "worked", "developed", "implemented", "managed", "led", "built", "created", "designed", "architected"]
    skills_keywords = ["python", "javascript", "react", "sql", "api", "backend", "frontend", "cloud", "docker", "kubernetes", "aws", "node", "django", "flask", "typescript", "java", "go", "terraform", "spark", "kafka"]
    education_keywords = ["university", "degree", "bachelor", "master", "phd", "graduated", "college", "gpa", "summa", "magna", "cum laude"]

    text_lower = resume_text.lower()

    experience_score = min(100, len([kw for kw in experience_keywords if kw in text_lower]) * 8)
    skills_score = min(100, len([kw for kw in skills_keywords if kw in text_lower]) * 6)
    education_score = min(100, len([kw for kw in education_keywords if kw in text_lower]) * 15)

    # Ensure minimum scores based on resume length
    if len(resume_text) > 500:
        experience_score = max(experience_score, 30)
        skills_score = max(skills_score, 30)
        education_score = max(education_score, 30)

    overall_score = round(experience_score * 0.4 + skills_score * 0.4 + education_score * 0.2)

    notes = f"Analyzed for {position} position. Experience score based on relevant work history keywords, skills score based on technical keywords, education score based on academic credentials."

    return {
        "experience_score": round(experience_score),
        "skills_score": round(skills_score),
        "education_score": round(education_score),
        "overall_score": overall_score,
        "notes": notes
    }

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
        # Calculate scores for the candidate
        analysis = analyze_resume(candidate_data["resume_text"], candidate_data["position"])
        candidate_data["experience_score"] = analysis["experience_score"]
        candidate_data["skills_score"] = analysis["skills_score"]
        candidate_data["education_score"] = analysis["education_score"]
        candidate_data["overall_score"] = analysis["overall_score"]
        candidate_data["analysis_notes"] = analysis["notes"]
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
        # Calculate scores for the candidate
        analysis = analyze_resume(candidate_data["resume_text"], candidate_data["position"])
        candidate_data["experience_score"] = analysis["experience_score"]
        candidate_data["skills_score"] = analysis["skills_score"]
        candidate_data["education_score"] = analysis["education_score"]
        candidate_data["overall_score"] = analysis["overall_score"]
        candidate_data["analysis_notes"] = analysis["notes"]
        candidate = models.Candidate(**candidate_data)
        db.add(candidate)

    # Add 25 more candidates (5 per job category)
    additional_candidates = [
        # Software Engineers (5 candidates)
        {
            "name": "Nathan Chen",
            "email": "nathan.c@email.com",
            "position": "Software Engineer",
            "resume_text": """
PROFESSIONAL SUMMARY
Software engineer with 4 years of experience building scalable web applications using Python, JavaScript, React, and Node.js. Proven track record in developing RESTful APIs and full-stack applications. Strong background in agile development methodologies and cloud deployment.
WORK EXPERIENCE
Software Engineer | CloudTech Solutions | Austin, TX | 2020 - Present
- Developed microservices architecture using Node.js and Express, serving 100k+ users
- Built responsive React applications with TypeScript and Redux
- Implemented RESTful APIs with Python Flask and Django frameworks
- Worked with PostgreSQL and MongoDB for data storage
- Deployed applications on AWS using Docker containers
- Collaborated in agile environment with CI/CD pipelines
Junior Software Developer | Digital Innovations | Austin, TX | 2018 - 2020
- Built full-stack web applications using Python and JavaScript
- Developed frontend components with React and Vue.js
- Created REST APIs using Flask and Express
- Worked with MySQL and PostgreSQL databases
TECHNICAL SKILLS
Languages: Python, JavaScript, TypeScript, Java, SQL
Frameworks: React, Node.js, Django, Flask, Express
Databases: PostgreSQL, MongoDB, MySQL
Cloud: AWS (EC2, S3, RDS), Docker
Tools: Git, JIRA, Jenkins, Postman
EDUCATION
Bachelor of Science in Computer Science | University of Texas | 2014 - 2018
""",
            "stage": "Phone Screen"
        },
        {
            "name": "Rachel Green",
            "email": "rachel.g@email.com",
            "position": "Software Engineer",
            "resume_text": """
PROFESSIONAL SUMMARY
Full-stack software engineer with 3 years of experience in web development and cloud technologies. Expertise in building scalable applications using Python, JavaScript, and modern frameworks. Passionate about clean code and best practices.
WORK EXPERIENCE
Software Engineer | TechVentures Inc | San Jose, CA | 2021 - Present
- Developed and maintained React-based frontend applications
- Built backend services using Python Django and Node.js
- Implemented RESTful API endpoints with authentication
- Worked with PostgreSQL and Redis for data persistence
- Deployed applications using Docker and AWS ECS
- Participated in sprint planning and code reviews
Software Developer Intern | StartupHub | San Jose, CA | 2020 - 2021
- Developed features for SaaS platform using React and Python
- Created API endpoints using Django REST Framework
- Implemented responsive UI with Material-UI components
- Wrote unit tests using Jest and Pytest
TECHNICAL SKILLS
Languages: Python, JavaScript, TypeScript, HTML, CSS
Frontend: React, Vue.js, Redux, Tailwind CSS, Material-UI
Backend: Django, Flask, Node.js, Express
Databases: PostgreSQL, MongoDB, Redis
Cloud: AWS, Docker
EDUCATION
Bachelor of Science in Software Engineering | San Jose State University | 2017 - 2021
""",
            "stage": "Resume Review"
        },
        {
            "name": "Marcus Johnson",
            "email": "marcus.j@email.com",
            "position": "Software Engineer",
            "resume_text": """
PROFESSIONAL SUMMARY
Results-driven software engineer with 5 years of experience developing enterprise applications. Strong background in backend development, API design, and database optimization. Proven ability to deliver high-quality software in fast-paced environments.
WORK EXPERIENCE
Software Engineer | EnterpriseSoft | Chicago, IL | 2019 - Present
- Architected and implemented RESTful APIs handling 5M+ daily requests
- Developed backend services using Python Django and FastAPI
- Optimized database queries and implemented caching with Redis
- Built microservices using Docker containers orchestrated with Kubernetes
- Implemented CI/CD pipelines using Jenkins and GitHub Actions
- Collaborated with product team to define API specifications
Software Developer | WebApps Solutions | Chicago, IL | 2017 - 2019
- Developed full-stack applications using Python and JavaScript
- Built RESTful APIs with Django and Flask frameworks
- Created frontend interfaces with React and Bootstrap
- Worked with PostgreSQL and MySQL databases
TECHNICAL SKILLS
Languages: Python, JavaScript, SQL, Bash
Frameworks: Django, Flask, FastAPI, React
Databases: PostgreSQL, MySQL, Redis, MongoDB
Cloud: AWS, Docker, Kubernetes
Tools: Git, Jenkins, Postman, JIRA
EDUCATION
Bachelor of Science in Computer Science | University of Illinois | 2013 - 2017
""",
            "stage": "Resume Review"
        },
        {
            "name": "Priya Patel",
            "email": "priya.p@email.com",
            "position": "Software Engineer",
            "resume_text": """
PROFESSIONAL SUMMARY
Full-stack engineer with 3 years of experience building web applications and APIs. Expertise in Python, JavaScript, and cloud deployment. Strong problem-solving skills and passion for learning new technologies.
WORK EXPERIENCE
Software Engineer | SaaS Pro | Seattle, WA | 2021 - Present
- Built scalable web applications using Python, Django, and React
- Developed RESTful APIs serving internal tools and external integrations
- Implemented user authentication with JWT tokens and OAuth
- Created responsive UI components with React and CSS-in-JS
- Worked with PostgreSQL for data modeling and optimization
- Deployed applications on AWS using EC2, S3, and RDS
Software Development Intern | CloudStart | Seattle, WA | 2020 - 2021
- Developed features for B2B platform using Python and React
- Built API endpoints with Django REST Framework
- Created automated tests using Pytest and React Testing Library
- Participated in agile ceremonies and sprint retrospectives
TECHNICAL SKILLS
Languages: Python, JavaScript, TypeScript, SQL
Frameworks: Django, Flask, React, Express
Databases: PostgreSQL, SQLite
Cloud: AWS, Heroku
Testing: Pytest, Jest, React Testing Library
EDUCATION
Bachelor of Science in Computer Science | University of Washington | 2017 - 2021
""",
            "stage": "Technical Interview"
        },
        {
            "name": "Tyler Mitchell",
            "email": "tyler.m@email.com",
            "position": "Software Engineer",
            "resume_text": """
PROFESSIONAL SUMMARY
Full-stack developer specializing in modern JavaScript and Python development. 4 years of experience building responsive web applications and APIs. Strong advocate for test-driven development and code quality.
WORK EXPERIENCE
Software Engineer | DevStudio | Boulder, CO | 2020 - Present
- Developed full-stack applications using Node.js, Express, and React
- Built RESTful APIs with Python FastAPI framework
- Implemented real-time features using WebSockets and Socket.io
- Created comprehensive test suites using Jest and Pytest
- Worked with MongoDB and PostgreSQL databases
- Deployed applications using Docker and AWS
Software Developer | WebDev Agency | Denver, CO | 2018 - 2020
- Built responsive websites using HTML, CSS, and JavaScript
- Developed single-page applications using React and Vue.js
- Created backend services with Node.js and Express
- Implemented user authentication and authorization
TECHNICAL SKILLS
Languages: JavaScript, Python, TypeScript, SQL
Frontend: React, Vue.js, Redux, Tailwind CSS
Backend: Node.js, Express, FastAPI, Django
Databases: PostgreSQL, MongoDB
Cloud: AWS, Docker
Testing: Jest, Pytest, Cypress
EDUCATION
Bachelor of Science in Computer Science | University of Colorado | 2014 - 2018
""",
            "stage": "Final Round"
        },

        # Senior Software Engineers (5 candidates)
        {
            "name": "Jennifer Kim",
            "email": "jennifer.k@email.com",
            "position": "Senior Software Engineer",
            "resume_text": """
PROFESSIONAL SUMMARY
Senior software engineer with 10 years of experience architecting distributed systems and cloud-native applications. Expert in designing microservices, handling high-scale traffic, and leading engineering teams. Strong background in Python, Java, and AWS infrastructure.
WORK EXPERIENCE
Senior Software Engineer | CloudScale Systems | San Francisco, CA | 2021 - Present
- Architected distributed microservices platform handling 50M+ daily requests
- Led team of 6 engineers in building scalable backend services
- Implemented event-driven architecture using Kafka and RabbitMQ
- Designed data pipelines processing 10TB+ daily using Apache Spark
- Optimized services reducing latency by 50% and costs by $300k annually
- Established best practices for code quality and deployment pipelines
Software Architect | TechCorp Industries | San Francisco, CA | 2018 - 2021
- Designed microservices architecture for migration from monolith
- Built high-performance APIs using Go, Python, and Java
- Implemented caching strategies with Redis and Memcached
- Led technical decisions and architecture reviews
Staff Engineer | DataFlow Inc | Mountain View, CA | 2014 - 2018
- Developed distributed data processing systems
- Built RESTful APIs and GraphQL services
- Worked with large-scale databases and data warehouses
TECHNICAL SKILLS
Languages: Python, Java, Go, Scala, SQL
Frameworks: Django, Flask, Spring Boot, gRPC
Cloud: AWS (extensive), GCP, Kubernetes
Databases: PostgreSQL, MongoDB, Redis, Cassandra
Tools: Docker, Kubernetes, Terraform, Jenkins
EDUCATION
Master of Science in Computer Science | Stanford University | 2012 - 2014
Bachelor of Science in Computer Science | UC Berkeley | 2008 - 2012
""",
            "stage": "Offer"
        },
        {
            "name": "Robert Zhang",
            "email": "robert.z@email.com",
            "position": "Senior Software Engineer",
            "resume_text": """
PROFESSIONAL SUMMARY
Senior engineer with 9 years of experience in scalable backend systems and infrastructure. Expert in Python, distributed systems, and cloud architecture. Proven track record of leading projects from conception to production at scale.
WORK EXPERIENCE
Senior Software Engineer | ScaleTech Solutions | New York, NY | 2020 - Present
- Architected and built microservices handling 100M+ requests daily
- Led development of real-time analytics platform using Kafka and Flink
- Implemented infrastructure as code using Terraform for AWS resources
- Optimized database queries and caching, reducing response time by 60%
- Built comprehensive monitoring and alerting with Prometheus and Grafana
- Mentored team of 4 junior engineers
Software Engineer | FinTech Corp | New York, NY | 2016 - 2020
- Developed high-frequency trading systems with Python and C++
- Built distributed systems for financial data processing
- Implemented real-time risk calculation engines
- Worked with distributed databases and message queues
Software Engineer | WebServices Inc | Boston, MA | 2015 - 2016
- Developed backend services using Python and Node.js
- Built RESTful APIs and GraphQL endpoints
- Implemented authentication and authorization systems
TECHNICAL SKILLS
Languages: Python, Java, Go, C++, SQL
Frameworks: Django, Flask, FastAPI, Spring Boot
Cloud: AWS, GCP, Kubernetes, Docker
Databases: PostgreSQL, MongoDB, Redis, InfluxDB
Tools: Terraform, Ansible, Jenkins, GitLab CI
EDUCATION
Master of Science in Computer Science | MIT | 2013 - 2015
Bachelor of Science in Engineering | Carnegie Mellon | 2009 - 2013
""",
            "stage": "Final Round"
        },
        {
            "name": "Amanda Foster",
            "email": "amanda.f@email.com",
            "position": "Senior Software Engineer",
            "resume_text": """
PROFESSIONAL SUMMARY
Senior software engineer with 8 years of experience in enterprise software development. Expert in Python, microservices architecture, and cloud infrastructure. Strong background in leading technical initiatives and building scalable systems.
WORK EXPERIENCE
Senior Software Engineer | EnterpriseCloud | Atlanta, GA | 2019 - Present
- Designed and implemented microservices architecture serving 20M+ users
- Led migration of legacy systems to cloud-native architecture
- Built real-time data streaming using Apache Kafka and Storm
- Implemented containerization with Docker and orchestration with Kubernetes
- Optimized application performance reducing server costs by 40%
- Established CI/CD best practices and deployment pipelines
Software Engineer | SoftwareVentures | Austin, TX | 2015 - 2019
- Developed distributed backend services using Python and Go
- Built RESTful APIs and GraphQL services
- Implemented message queuing with RabbitMQ and Redis
- Worked with PostgreSQL, MongoDB, and Cassandra databases
- Deployed applications on AWS using Terraform
Software Developer | TechSolutions | Dallas, TX | 2013 - 2015
- Developed web applications using Python and Django
- Built REST APIs for mobile and web clients
- Worked with MySQL and PostgreSQL databases
TECHNICAL SKILLS
Languages: Python, Go, Java, SQL, JavaScript
Frameworks: Django, Flask, Gin, Express
Cloud: AWS, Azure, Kubernetes, Docker
Databases: PostgreSQL, MongoDB, Redis, Cassandra
Tools: Terraform, Ansible, Jenkins, GitLab
EDUCATION
Master of Science in Computer Science | Georgia Tech | 2011 - 2013
Bachelor of Science in Computer Science | UT Austin | 2007 - 2011
""",
            "stage": "Technical Interview"
        },
        {
            "name": "Kevin Liu",
            "email": "kevin.l@email.com",
            "position": "Senior Software Engineer",
            "resume_text": """
PROFESSIONAL SUMMARY
Senior engineer with 7 years of experience building high-performance distributed systems. Expert in Go, Python, and cloud-native development. Passionate about system architecture, performance optimization, and building reliable services.
WORK EXPERIENCE
Senior Software Engineer | CloudNative Inc | San Francisco, CA | 2020 - Present
- Architected and built microservices platform handling 80M+ daily requests
- Developed high-performance services using Go and Python
- Implemented event-driven architecture with Kafka and Redis
- Built infrastructure as code using Terraform and Ansible
- Optimized systems reducing latency by 55% and costs by $250k/year
- Led technical design reviews and architecture decisions
Software Engineer | Microservices Solutions | San Francisco, CA | 2017 - 2020
- Developed distributed microservices using Go and Python
- Built RESTful APIs and gRPC services
- Implemented caching strategies with Redis and Memcached
- Worked with container orchestration using Kubernetes
- Deployed applications on AWS and GCP platforms
Backend Developer | TechStartup | Palo Alto, CA | 2015 - 2017
- Built backend services using Python and Node.js
- Developed RESTful APIs with Django and Express
- Implemented real-time features using WebSockets
TECHNICAL SKILLS
Languages: Go, Python, Java, SQL
Frameworks: Django, Flask, Gin, Echo
Cloud: AWS, GCP, Kubernetes, Docker
Databases: PostgreSQL, MongoDB, Redis
Tools: Terraform, Ansible, Jenkins, GitLab CI
EDUCATION
Bachelor of Science in Computer Science | UC Berkeley | 2011 - 2015
""",
            "stage": "Phone Screen"
        },
        {
            "name": "Lisa Wang",
            "email": "lisa.w@email.com",
            "position": "Senior Software Engineer",
            "resume_text": """
PROFESSIONAL SUMMARY
Senior software engineer with 11 years of experience in building large-scale distributed systems and cloud infrastructure. Expert in Python, Java, and AWS. Proven track record of leading multi-team initiatives and delivering high-impact projects.
WORK EXPERIENCE
Senior Software Engineer | EnterpriseTech | Boston, MA | 2018 - Present
- Architected microservices platform processing 200M+ requests daily
- Led team of 8 engineers in building scalable backend services
- Implemented distributed caching and queue systems
- Designed and built data pipelines using Apache Spark and Airflow
- Reduced infrastructure costs by $500k through optimization and automation
- Established engineering standards and best practices across organization
Principal Engineer | CloudServices | Cambridge, MA | 2014 - 2018
- Designed and implemented distributed systems architecture
- Built high-performance APIs using Java and Python
- Led technical architecture for multiple product lines
- Mentored senior engineers and influenced technical roadmap
Software Engineer | DataSystems Inc | Boston, MA | 2012 - 2014
- Developed data processing pipelines
- Built RESTful APIs and backend services
- Worked with distributed databases and message queues
TECHNICAL SKILLS
Languages: Python, Java, Scala, SQL
Frameworks: Django, Flask, Spring Boot, Spark
Cloud: AWS, GCP, Kubernetes, Docker
Databases: PostgreSQL, MongoDB, Cassandra, Kafka
Tools: Terraform, Ansible, Jenkins, Airflow
EDUCATION
Master of Science in Computer Science | Harvard University | 2010 - 2012
Bachelor of Science in Computer Science | MIT | 2006 - 2010
""",
            "stage": "Resume Review"
        },

        # Frontend Engineers (5 candidates)
        {
            "name": "Michelle Kim",
            "email": "michelle.k@email.com",
            "position": "Frontend Engineer",
            "resume_text": """
PROFESSIONAL SUMMARY
Frontend engineer with 4 years of experience building modern, responsive web applications. Expert in React, TypeScript, and component design systems. Passionate about creating exceptional user experiences and writing maintainable code.
WORK EXPERIENCE
Frontend Engineer | DesignLab Solutions | Los Angeles, CA | 2020 - Present
- Built responsive web applications using React and TypeScript serving 500k+ users
- Developed comprehensive design system with 100+ reusable components
- Implemented state management using Redux and Context API
- Optimized application performance reducing bundle size by 35%
- Created accessible UI components following WCAG 2.1 guidelines
- Collaborated with UX designers on design system implementation
Frontend Developer | CreativeWeb Agency | Los Angeles, CA | 2018 - 2020
- Developed interactive single-page applications using React and Vue.js
- Built reusable component libraries using styled-components
- Implemented responsive designs using CSS Grid and Flexbox
- Worked with REST APIs and GraphQL endpoints
- Created animations and transitions using CSS and Framer Motion
TECHNICAL SKILLS
Languages: JavaScript, TypeScript, HTML, CSS, SASS
Frameworks: React, Vue.js, Next.js, Redux
Styling: Tailwind CSS, styled-components, CSS Modules
Build Tools: Webpack, Vite, Babel, ESLint
Testing: Jest, React Testing Library, Cypress
Accessibility: WCAG 2.1, ARIA attributes
EDUCATION
Bachelor of Science in Computer Science | UCLA | 2014 - 2018
""",
            "stage": "Technical Interview"
        },
        {
            "name": "Daniel Rodriguez",
            "email": "daniel.r@email.com",
            "position": "Frontend Engineer",
            "resume_text": """
PROFESSIONAL SUMMARY
Frontend developer with 5 years of experience creating beautiful, functional user interfaces. Expert in React, TypeScript, and modern CSS. Strong advocate for accessible design and progressive web applications.
WORK EXPERIENCE
Frontend Engineer | UserExperience Pro | Seattle, WA | 2019 - Present
- Built modern web applications using React, TypeScript, and Next.js
- Led migration of class components to functional components with hooks
- Created comprehensive design system with 80+ components
- Implemented progressive web app (PWA) features for offline capability
- Optimized performance achieving 95+ Lighthouse scores
- Mentored junior developers on React best practices
Frontend Developer | Interactive Solutions | Seattle, WA | 2017 - 2019
- Developed interactive dashboards using React and D3.js
- Built component libraries and UI kits
- Implemented state management with Redux and MobX
- Created data visualizations for business analytics
Web Developer | Digital Agency | Tacoma, WA | 2015 - 2017
- Built responsive websites for clients
- Worked with HTML, CSS, JavaScript
- Implemented cross-browser compatibility
TECHNICAL SKILLS
Languages: JavaScript, TypeScript, HTML, CSS
Frameworks: React, Next.js, Redux, MobX
Styling: CSS Modules, Tailwind CSS, styled-components
Tools: Webpack, Babel, ESLint, Prettier
Testing: Jest, Testing Library, Enzyme
EDUCATION
Bachelor of Science in Computer Science | University of Washington | 2011 - 2015
""",
            "stage": "Phone Screen"
        },
        {
            "name": "Sarah Thompson",
            "email": "sarah.t@email.com",
            "position": "Frontend Engineer",
            "resume_text": """
PROFESSIONAL SUMMARY
Frontend engineer with 3 years of experience building responsive web applications and design systems. Expert in React, TypeScript, and creating seamless user experiences. Passionate about clean code and accessibility.
WORK EXPERIENCE
Frontend Engineer | TechApp Inc | Austin, TX | 2021 - Present
- Developed responsive React applications with TypeScript
- Built reusable component library using styled-components
- Implemented state management using Redux Toolkit
- Created responsive layouts using CSS Grid and Flexbox
- Optimized application performance and bundle size
- Collaborated with backend team on API integration
Frontend Developer Intern | StartupStudio | Austin, TX | 2020 - 2021
- Built React applications using hooks and functional components
- Created responsive UI components with Material-UI
- Implemented form validation and error handling
- Worked with REST APIs and JSON data
TECHNICAL SKILLS
Languages: JavaScript, TypeScript, HTML, CSS
Frameworks: React, Redux, React Router
Styling: styled-components, Tailwind CSS, Material-UI
Build Tools: Webpack, Babel, Create React App
Testing: Jest, React Testing Library
EDUCATION
Bachelor of Science in Software Engineering | UT Austin | 2017 - 2021
""",
            "stage": "Resume Review"
        },
        {
            "name": "Jonathan Park",
            "email": "jonathan.p@email.com",
            "position": "Frontend Engineer",
            "resume_text": """
PROFESSIONAL SUMMARY
Frontend engineer with 6 years of experience creating pixel-perfect user interfaces. Expert in React, Vue.js, and building scalable frontend architectures. Strong background in animation, interaction design, and performance optimization.
WORK EXPERIENCE
Frontend Engineer | DesignFirst Studios | San Francisco, CA | 2018 - Present
- Built high-performance React applications with Next.js serving 2M+ users
- Developed comprehensive component library used across multiple products
- Implemented advanced animations using Framer Motion and GSAP
- Optimized applications achieving 98+ Lighthouse performance scores
- Created interactive data visualizations using D3.js and Recharts
- Led frontend architecture decisions and best practices
Frontend Developer | VisualTech Inc | San Francisco, CA | 2016 - 2018
- Developed Vue.js and React applications
- Built responsive designs for web and mobile
- Created complex UI components and layouts
- Implemented state management with Vuex and Redux
Web Designer | Creative Labs | Palo Alto, CA | 2014 - 2016
- Designed and developed websites
- Created user interfaces and prototypes
- Worked with HTML, CSS, JavaScript
TECHNICAL SKILLS
Languages: JavaScript, TypeScript, HTML, CSS, SASS
Frameworks: React, Vue.js, Next.js, Nuxt.js
Styling: CSS-in-JS, Tailwind CSS, styled-components
Animation: Framer Motion, GSAP, CSS animations
Testing: Jest, React Testing Library, Cypress
EDUCATION
Bachelor of Science in Computer Science | San Jose State University | 2010 - 2014
""",
            "stage": "Final Round"
        },
        {
            "name": "Emily Chen",
            "email": "emily.c@email.com",
            "position": "Frontend Engineer",
            "resume_text": """
PROFESSIONAL SUMMARY
Frontend developer with 2 years of experience building modern web applications. Proficient in React, TypeScript, and responsive design. Eager to grow skills in modern frontend technologies and best practices.
WORK EXPERIENCE
Frontend Engineer | ModernWeb Solutions | Portland, OR | 2022 - Present
- Built responsive React applications using React and TypeScript
- Created reusable UI components using styled-components
- Implemented state management with Redux and Context API
- Worked with REST APIs for data fetching and mutation
- Collaborated with designers on UI/UX implementation
- Participated in code reviews and agile ceremonies
Software Engineering Intern | TechVentures | Portland, OR | 2021 - 2022
- Developed React components and pages
- Built responsive layouts using CSS Grid and Flexbox
- Implemented user authentication and protected routes
- Created form components with validation
PROJECTS
- E-commerce Platform: Full-stack application with React frontend
- Task Management App: Real-time collaboration using WebSockets
- Portfolio Website: Personal site showcasing projects
TECHNICAL SKILLS
Languages: JavaScript, TypeScript, HTML, CSS
Frameworks: React, Redux, React Router
Styling: styled-components, CSS Modules, Tailwind CSS
Tools: Webpack, Babel, ESLint, Prettier
Testing: Jest, React Testing Library
EDUCATION
Bachelor of Science in Computer Science | Portland State University | 2018 - 2022
""",
            "stage": "Resume Review"
        },

        # DevOps Engineers (5 candidates)
        {
            "name": "Christopher Lee",
            "email": "christopher.l@email.com",
            "position": "DevOps Engineer",
            "resume_text": """
PROFESSIONAL SUMMARY
DevOps engineer with 5 years of experience automating deployments, managing cloud infrastructure, and building CI/CD pipelines. Expert in AWS, Terraform, Docker, and Kubernetes. Passionate about infrastructure as code and automation.
WORK EXPERIENCE
DevOps Engineer | CloudOps Solutions | Denver, CO | 2020 - Present
- Automated infrastructure provisioning using Terraform managing 300+ resources
- Built and maintained Kubernetes clusters with 200+ pods
- Implemented CI/CD pipelines using Jenkins and GitLab CI reducing deployment time by 70%
- Set up monitoring and alerting using Prometheus, Grafana, and DataDog
- Migrated applications from on-premises to AWS reducing costs by 50%
- Wrote infrastructure automation scripts using Python and Bash
DevOps Engineer | TechSystems Inc | Denver, CO | 2018 - 2020
- Managed AWS infrastructure including EC2, ECS, S3, and RDS
- Automated deployments using Jenkins and Docker containers
- Implemented infrastructure monitoring using CloudWatch and ELK stack
- Containerized applications using Docker and orchestrated with ECS
- Wrote automation scripts for server provisioning
TECHNICAL SKILLS
Cloud: AWS (EC2, ECS, S3, RDS, Lambda, CloudFormation), Docker, Kubernetes
Infrastructure: Terraform, Ansible, CloudFormation
CI/CD: Jenkins, GitLab CI, GitHub Actions
Monitoring: Prometheus, Grafana, DataDog, CloudWatch
Scripting: Python, Bash, Shell scripting
EDUCATION
Bachelor of Science in Computer Engineering | Colorado State University | 2014 - 2018
""",
            "stage": "Technical Interview"
        },
        {
            "name": "Jessica Martinez",
            "email": "jessica.m@email.com",
            "position": "DevOps Engineer",
            "resume_text": """
PROFESSIONAL SUMMARY
DevOps engineer specializing in cloud infrastructure and automation. 6 years of experience with AWS, Kubernetes, and infrastructure as code. Proven track record of improving system reliability and reducing operational overhead.
WORK EXPERIENCE
Senior DevOps Engineer | CloudScale Technologies | San Diego, CA | 2019 - Present
- Architected and implemented infrastructure as code using Terraform
- Managed Kubernetes clusters with 500+ pods across multiple environments
- Built comprehensive CI/CD pipelines reducing deployment time from 2hrs to 20min
- Implemented automated monitoring and alerting systems
- Led migration of 100+ servers from on-premises to AWS
- Reduced infrastructure costs by $400k through optimization
DevOps Engineer | EnterpriseOps | San Diego, CA | 2017 - 2019
- Managed cloud infrastructure on AWS and GCP
- Automated deployments using Jenkins and Docker
- Implemented infrastructure monitoring and logging
- Worked with Terraform and Ansible for automation
Junior DevOps Engineer | StartupCo | Irvine, CA | 2016 - 2017
- Managed AWS infrastructure for web applications
- Built CI/CD pipelines for automated deployments
- Automated server provisioning and configuration
TECHNICAL SKILLS
Cloud: AWS (extensive), GCP, Azure, Kubernetes, Docker
Infrastructure: Terraform, Ansible, CloudFormation
CI/CD: Jenkins, GitLab CI, GitHub Actions, CircleCI
Monitoring: Prometheus, Grafana, DataDog, ELK Stack
Scripting: Python, Bash, PowerShell
EDUCATION
Bachelor of Science in Computer Science | UC San Diego | 2012 - 2016
""",
            "stage": "Phone Screen"
        },
        {
            "name": "Thomas Anderson",
            "email": "thomas.a@email.com",
            "position": "DevOps Engineer",
            "resume_text": """
PROFESSIONAL SUMMARY
DevOps engineer with 4 years of experience in cloud infrastructure and automation. Expert in AWS, Docker, and Terraform. Strong background in CI/CD pipelines and infrastructure monitoring.
WORK EXPERIENCE
DevOps Engineer | CloudTech Systems | Atlanta, GA | 2021 - Present
- Managed cloud infrastructure using AWS including EC2, ECS, S3, RDS
- Automated infrastructure provisioning using Terraform
- Built CI/CD pipelines using Jenkins and GitLab CI
- Implemented containerization using Docker and Kubernetes
- Set up monitoring and alerting using Prometheus and Grafana
- Automated deployment processes reducing manual intervention
DevOps Engineer | TechVentures | Atlanta, GA | 2019 - 2021
- Managed AWS infrastructure for multiple projects
- Built deployment pipelines using Jenkins
- Automated server provisioning using Ansible
- Implemented infrastructure monitoring and logging
Systems Administrator | IT Solutions | Atlanta, GA | 2017 - 2019
- Managed Linux servers and network infrastructure
- Automated system administration tasks using scripts
- Implemented backup and disaster recovery procedures
TECHNICAL SKILLS
Cloud: AWS (EC2, ECS, S3, RDS, Lambda), Docker, Kubernetes
Infrastructure: Terraform, Ansible, CloudFormation
CI/CD: Jenkins, GitLab CI, GitHub Actions
Monitoring: Prometheus, Grafana, CloudWatch
Scripting: Python, Bash, PowerShell
EDUCATION
Bachelor of Science in Information Technology | Georgia Tech | 2013 - 2017
""",
            "stage": "Resume Review"
        },
        {
            "name": "Nicole Brown",
            "email": "nicole.b@email.com",
            "position": "DevOps Engineer",
            "resume_text": """
PROFESSIONAL SUMMARY
DevOps engineer with 7 years of experience managing cloud infrastructure and building scalable systems. Expert in AWS, Kubernetes, and infrastructure automation. Proven ability to improve system reliability and reduce costs.
WORK EXPERIENCE
Senior DevOps Engineer | CloudNative Solutions | Seattle, WA | 2018 - Present
- Architected infrastructure as code managing 400+ AWS resources
- Led migration to Kubernetes reducing deployment time by 65%
- Built comprehensive monitoring using Prometheus, Grafana, and DataDog
- Automated infrastructure provisioning using Terraform and Ansible
- Optimized cloud costs reducing annual spend by $600k
- Established best practices for CI/CD and deployment automation
DevOps Engineer | ScaleTech | Seattle, WA | 2015 - 2018
- Managed Kubernetes clusters with 1000+ pods
- Built CI/CD pipelines using Jenkins and GitLab
- Implemented infrastructure monitoring and alerting
- Containerized legacy applications using Docker
- Automated server provisioning and configuration
Systems Administrator | Enterprise Systems | Bellevue, WA | 2013 - 2015
- Managed Linux server infrastructure
- Automated system administration tasks
- Implemented backup and monitoring systems
TECHNICAL SKILLS
Cloud: AWS, GCP, Kubernetes, Docker
Infrastructure: Terraform, Ansible, CloudFormation, Puppet
CI/CD: Jenkins, GitLab CI, GitHub Actions, Travis CI
Monitoring: Prometheus, Grafana, DataDog, ELK Stack
Scripting: Python, Bash, Go, Shell scripting
EDUCATION
Master of Science in Computer Science | University of Washington | 2011 - 2013
Bachelor of Science in Computer Science | UW | 2007 - 2011
""",
            "stage": "Final Round"
        },
        {
            "name": "David Kim",
            "email": "david.k@email.com",
            "position": "DevOps Engineer",
            "resume_text": """
PROFESSIONAL SUMMARY
DevOps engineer with 3 years of experience in cloud infrastructure and automation. Proficient in AWS, Docker, and CI/CD pipelines. Passionate about infrastructure as code and improving system reliability.
WORK EXPERIENCE
DevOps Engineer | StartupCloud | Austin, TX | 2022 - Present
- Managed AWS infrastructure including EC2, ECS, S3, and RDS
- Automated deployments using Docker containers and ECS
- Built CI/CD pipelines using Jenkins and GitHub Actions
- Implemented infrastructure as code using Terraform
- Set up monitoring and alerting using CloudWatch and DataDog
DevOps Intern | TechStart Inc | Austin, TX | 2021 - 2022
- Assisted with AWS infrastructure management
- Automated deployments using Jenkins
- Wrote infrastructure automation scripts using Bash and Python
- Implemented monitoring and logging systems
PROJECTS
- Infrastructure as Code: Terraform modules for AWS resources
- CI/CD Pipeline: Automated deployment pipeline using Jenkins
- Monitoring Dashboard: Prometheus and Grafana setup
TECHNICAL SKILLS
Cloud: AWS, Docker, Kubernetes
Infrastructure: Terraform, Ansible
CI/CD: Jenkins, GitHub Actions
Monitoring: Prometheus, Grafana, CloudWatch
Scripting: Python, Bash
EDUCATION
Bachelor of Science in Computer Science | UT Austin | 2018 - 2022
""",
            "stage": "Resume Review"
        },

        # Data Engineers (5 candidates)
        {
            "name": "Jennifer Park",
            "email": "jennifer.p@email.com",
            "position": "Data Engineer",
            "resume_text": """
PROFESSIONAL SUMMARY
Data engineer with 5 years of experience building scalable data pipelines and ETL processes. Expert in Python, SQL, Apache Spark, and cloud data warehouses. Strong background in processing large-scale datasets and enabling data-driven decision making.
WORK EXPERIENCE
Senior Data Engineer | DataFlow Analytics | New York, NY | 2020 - Present
- Built data pipelines processing 5TB+ daily using Apache Spark and Airflow
- Designed data lake architecture on AWS S3 reducing storage costs by 45%
- Developed ETL pipelines using Python, Pandas, and SQL
- Optimized Spark jobs reducing processing time by 50%
- Implemented data quality checks using Great Expectations
- Worked with data warehouses including Redshift and Snowflake
Data Engineer | Analytics Solutions | New York, NY | 2018 - 2020
- Built ETL pipelines processing millions of records daily
- Developed data processing workflows using Python and Spark
- Worked with PostgreSQL, MongoDB, and Elasticsearch
- Implemented data validation and quality checks
- Created data pipelines for business intelligence
Junior Data Engineer | DataStart Inc | Brooklyn, NY | 2017 - 2018
- Developed Python scripts for data extraction and transformation
- Built automated data pipelines for daily updates
- Performed data cleaning and validation
- Created data visualizations using Tableau
TECHNICAL SKILLS
Programming: Python, SQL, Scala
Big Data: Apache Spark, Hadoop, Airflow
Databases: PostgreSQL, MongoDB, Elasticsearch, Redis
Cloud: AWS (S3, Redshift, EMR, Glue)
Data Warehouses: Redshift, Snowflake, BigQuery
Visualization: Tableau, Looker
EDUCATION
Master of Science in Data Science | Columbia University | 2015 - 2017
Bachelor of Science in Computer Science | NYU | 2011 - 2015
""",
            "stage": "Final Round"
        },
        {
            "name": "Michael Chang",
            "email": "michael.c@email.com",
            "position": "Data Engineer",
            "resume_text": """
PROFESSIONAL SUMMARY
Data engineer specializing in real-time data processing and big data technologies. 6 years of experience with Spark, Kafka, and cloud data platforms. Proven track record of building scalable data architectures.
WORK EXPERIENCE
Data Engineer | RealTime Analytics | San Francisco, CA | 2019 - Present
- Built real-time data pipelines processing 10TB+ daily using Spark and Kafka
- Designed streaming data architecture on AWS Kinesis and S3
- Developed batch processing pipelines using Airflow and Python
- Optimized data queries reducing processing time by 60%
- Implemented data quality monitoring using custom frameworks
- Worked with data warehouses including Snowflake and Redshift
Data Engineer | BigData Corp | San Francisco, CA | 2017 - 2019
- Developed ETL pipelines using Python and Apache Spark
- Worked with Kafka for real-time data streaming
- Built data processing workflows processing petabytes of data
- Implemented data validation and quality checks
Junior Data Engineer | AnalyticsTech | Mountain View, CA | 2016 - 2017
- Developed Python scripts for data processing
- Built automated ETL pipelines
- Worked with SQL databases for data analysis
TECHNICAL SKILLS
Programming: Python, SQL, Scala, Java
Big Data: Apache Spark, Kafka, Airflow, Hadoop
Databases: PostgreSQL, MongoDB, Redis
Cloud: AWS (S3, Kinesis, Redshift, EMR), GCP
Data Warehouses: Snowflake, Redshift, BigQuery
EDUCATION
Master of Science in Data Engineering | UC Berkeley | 2014 - 2016
Bachelor of Science in Computer Science | Stanford | 2010 - 2014
""",
            "stage": "Technical Interview"
        },
        {
            "name": "Stephanie Wu",
            "email": "stephanie.w@email.com",
            "position": "Data Engineer",
            "resume_text": """
PROFESSIONAL SUMMARY
Data engineer with 4 years of experience building data pipelines and ETL processes. Expert in Python, SQL, and cloud data technologies. Strong background in data quality and analytics infrastructure.
WORK EXPERIENCE
Data Engineer | Analytics Solutions | Chicago, IL | 2021 - Present
- Built data pipelines processing 2TB+ daily using Python and Airflow
- Developed ETL processes extracting data from multiple sources
- Implemented data quality checks and validation frameworks
- Worked with data warehouses including Snowflake and BigQuery
- Created data visualizations and reports for business stakeholders
- Optimized SQL queries improving performance by 40%
Data Engineer | DataTech Inc | Chicago, IL | 2019 - 2021
- Developed data processing pipelines using Python and pandas
- Built automated ETL workflows processing millions of records
- Worked with PostgreSQL, MongoDB, and Elasticsearch
- Implemented data validation and quality monitoring
- Created dashboards for data monitoring
TECHNICAL SKILLS
Programming: Python, SQL, R
Big Data: Spark, Airflow, Kafka
Databases: PostgreSQL, MongoDB, Elasticsearch, Redis
Cloud: AWS (S3, Redshift), GCP (BigQuery)
Data Warehouses: Snowflake, BigQuery
Visualization: Tableau, Looker, Metabase
EDUCATION
Bachelor of Science in Computer Science | Northwestern University | 2015 - 2019
""",
            "stage": "Phone Screen"
        },
        {
            "name": "Ryan Kim",
            "email": "ryan.k@email.com",
            "position": "Data Engineer",
            "resume_text": """
PROFESSIONAL SUMMARY
Data engineer with 7 years of experience in big data processing and analytics infrastructure. Expert in Spark, Kafka, and data warehousing solutions. Proven track record of building scalable data architectures.
WORK EXPERIENCE
Senior Data Engineer | BigData Systems | Seattle, WA | 2018 - Present
- Built distributed data pipelines processing 20TB+ daily using Spark and Kafka
- Designed data lake architecture on AWS S3 using Parquet format
- Implemented real-time streaming pipelines using Kafka and Flink
- Optimized Spark jobs reducing compute costs by 50%
- Built data quality framework using Great Expectations
- Worked extensively with Snowflake and Redshift
Data Engineer | DataFlow Inc | Seattle, WA | 2016 - 2018
- Developed ETL pipelines using Python and Spark
- Built batch processing workflows processing terabytes of data
- Implemented data validation and quality checks
- Worked with data warehouses and data lakes
Data Analyst | Analytics Firm | Bellevue, WA | 2015 - 2016
- Analyzed large datasets using Python and SQL
- Created data visualizations and reports
- Built data processing scripts
TECHNICAL SKILLS
Programming: Python, SQL, Scala, Java
Big Data: Apache Spark, Kafka, Flink, Airflow, Hadoop
Databases: PostgreSQL, MongoDB, Cassandra, Redis
Cloud: AWS (S3, Redshift, EMR, Kinesis), GCP
Data Warehouses: Snowflake, Redshift, BigQuery, Databricks
EDUCATION
Master of Science in Data Science | University of Washington | 2013 - 2015
Bachelor of Science in Computer Science | UW | 2009 - 2013
""",
            "stage": "Resume Review"
        },
        {
            "name": "Patricia Garcia",
            "email": "patricia.g@email.com",
            "position": "Data Engineer",
            "resume_text": """
PROFESSIONAL SUMMARY
Data engineer with 3 years of experience building data pipelines and ETL processes. Proficient in Python, SQL, and cloud data platforms. Passionate about data quality and building scalable analytics infrastructure.
WORK EXPERIENCE
Data Engineer | Analytics Start | Boston, MA | 2022 - Present
- Built data pipelines using Python, Airflow, and SQL
- Developed ETL processes extracting data from multiple APIs
- Implemented data quality checks and validation
- Worked with PostgreSQL and MongoDB databases
- Created dashboards for data monitoring and visualization
- Optimized database queries improving performance
Data Engineer Intern | DataTech Solutions | Boston, MA | 2021 - 2022
- Assisted with building ETL pipelines using Python
- Developed data processing scripts using pandas
- Worked with SQL databases for data analysis
- Created data visualizations using Tableau
PROJECTS
- ETL Pipeline: Automated data processing pipeline using Airflow
- Data Warehouse: Built data warehouse on Snowflake
- Analytics Dashboard: Created dashboards using Looker
TECHNICAL SKILLS
Programming: Python, SQL, R
Big Data: Spark, Airflow
Databases: PostgreSQL, MongoDB, Redis
Cloud: AWS (S3, Redshift)
Data Warehouses: Snowflake, BigQuery
Visualization: Tableau, Looker
EDUCATION
Bachelor of Science in Computer Science | Boston University | 2018 - 2022
""",
            "stage": "Resume Review"
        }
    ]

    # Add all additional candidates to recruiter 1
    for candidate_data in additional_candidates:
        candidate_data["recruiter_id"] = recruiters[0].id
        # Calculate scores for the candidate
        analysis = analyze_resume(candidate_data["resume_text"], candidate_data["position"])
        candidate_data["experience_score"] = analysis["experience_score"]
        candidate_data["skills_score"] = analysis["skills_score"]
        candidate_data["education_score"] = analysis["education_score"]
        candidate_data["overall_score"] = analysis["overall_score"]
        candidate_data["analysis_notes"] = analysis["notes"]
        candidate = models.Candidate(**candidate_data)
        db.add(candidate)

    db.commit()
    total_candidates = len(sample_candidates) + len(sample_candidates_r2) + len(additional_candidates)
    print("Database initialized with sample data!")
    print(f"Created {len(recruiters)} recruiters and {total_candidates} candidates")

except Exception as e:
    db.rollback()
    print(f"Error: {e}")
    raise
finally:
    db.close()

