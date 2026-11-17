# Backend Architecture & Security Audit Report



**Assessment:** Backend Developer Intern Technical Assessment

**Organization:** Cynbit Technologies

**Assessment date:** November 17, 2026

**Repository reviewed:** [Cynbit Technologies – SprintPulse Fullstack Lab](https://github.com/Cynbit-Technologies/bitelevate-fullstack-lab)



---



## 1. Executive Summary



This assessment reviews publicly observable aspects of the Cynbit website and the publicly available SprintPulse Fullstack Lab repository.



The review covers frontend architecture indicators, HTTP response headers, privacy disclosures, API implementation, database models, validation, authentication, container configuration, dependencies, testing and repository security practices.



The most significant issues identified in the reviewed SprintPulse source code are:



1. Missing authentication and authorization dependencies on reviewed workspace, project and task endpoints.

2. Missing frontend-backend integration in the reviewed dashboard.

3. Non-persistent frontend task operations.

4. Hardcoded database credentials in Docker Compose.

5. Broad database port exposure in the supplied container configuration.

6. Unbounded database list operations.

7. Limited input validation and incomplete test coverage.



These findings apply to the public SprintPulse lab repository. Its relationship to Cynbit's production website backend has not been established. They must not be interpreted as confirmed production vulnerabilities.



## 2. Scope and Methodology



### Scope



- Public Cynbit website.

- Public privacy policy and contact page.

- Public SprintPulse GitHub repository.

- Backend API implementation.

- SQLAlchemy database models.

- Pydantic request and response schemas.

- Backend tests and dependencies.

- Docker Compose and environment configuration.

- Frontend application source.

- Public GitHub security documentation.



### Methodology



- Passive inspection of publicly accessible website pages.

- Browser Network panel inspection.

- Review of publicly accessible HTTP response headers.

- Static source-code review.

- Review of repository configuration and documentation.

- Local implementation of illustrative authentication controls and automated tests.



No exploitation, destructive testing, production API modification, credential testing or unauthorized access was performed.



## 3. Website Architecture Observations



The inspected website returned several indicators consistent with a Next.js application deployed on Vercel.



Observed indicators included:



- `server: Vercel`

- `content-type: text/x-component`

- `_rsc` request parameters.

- `x-nextjs-prerender: 1`

- `x-nextjs-stale-time: 300`



These observations are consistent with Next.js React Server Components and prerendering.



The exact framework version and production backend implementation were not established.



### HTTP response observations



The inspected contact response included:



- HTTP Strict Transport Security.

- Brotli content encoding.

- Vercel cache information.

- Next.js response metadata.



The main document response did not display all the commonly reviewed security headers in the supplied header listing. This is a limited observation, not proof that those headers are absent across the entire website.



## 4. Privacy and Contact Form Review



The public privacy policy states that the organization collects information such as names, email addresses and professional context.



It identifies Resend as an email delivery provider and Prisma as a database management provider.



### Documentation gaps



- Specific data-retention periods are not disclosed in the reviewed text.

- Encryption standards and key-management details are not specified.

- Newsletter collection and unsubscribe handling are not clearly addressed in the supplied policy text.

- No specific response timeframe for data-access or deletion requests is provided.



The contact page displays fields for name, email, company, industry and message.



No form submission was performed. Actual server-side validation, storage, spam prevention and retention behavior were not verified.



## 5. SprintPulse Backend Source Review



### 5.1 Authentication and authorization



**Finding: Missing authentication and authorization in reviewed endpoints.**



The reviewed workspace, project and task routes do not declare authentication or authorization dependencies.



Potential impact:

- Unauthorized access to workspace data.

- Unauthorized project or task modification.

- Cross-workspace data exposure if deployed with real multi-tenant data.



Recommendations:

- Implement authentication.

- Enforce workspace-level authorization.

- Verify resource ownership on every relevant operation.

- Add tests for unauthorized and cross-workspace requests.



### 5.2 Database models



The reviewed SQLAlchemy models include:



- UUID-based identifiers.

- Workspace, Project and Task relationships.

- Foreign key constraints.

- Task status enumeration.

- Cascading deletion relationships.



Improvement opportunities:

- Evaluate indexes on frequently filtered foreign-key columns.

- Enable and test SQLite foreign-key enforcement where SQLite is used.

- Add update timestamps and audit logging.

- Define backup and recovery procedures for destructive operations.



### 5.3 API implementation



The reviewed API exposes workspace, project and task operations.



Findings:



- List endpoints do not implement pagination.

- Workspace and project ownership checks are not visible.

- Database migration management is not demonstrated.

- Database commit failures are not explicitly handled in the reviewed routes.



Recommendations:

- Introduce pagination and maximum page sizes.

- Enforce ownership and tenant isolation.

- Use Alembic migrations.

- Handle database errors and transaction rollbacks consistently.



### 5.4 Request validation



The reviewed Pydantic schemas use basic types and optional fields.



Improvement opportunities:



- Add minimum and maximum string lengths.

- Validate workspace slug formats.

- Validate identifier formats.

- Limit description lengths.

- Define explicit PATCH behavior for omitted versus null fields.



### 5.5 Backend testing



The supplied test file covers:



- Health endpoint.

- Workspace creation.

- Project creation.

- Task creation.

- Task status update.



Missing test coverage includes:



- Authentication and authorization.

- Cross-workspace access.

- Invalid input.

- Missing resources.

- Duplicate workspace slugs.

- Database failures and rollback.

- Pagination.



Recommendation: introduce isolated test databases, reusable fixtures and negative security tests.



## 6. Frontend Review

**Reviewed file:** `frontend/src/app/page.tsx`

The inspected main frontend page uses Next.js, React and TypeScript. It stores sample tasks in local React component state.

### Findings

1. No backend API calls are visible in the inspected file.
2. Newly created tasks are stored only in component state.
3. Refreshing the page loses locally created tasks.
4. No authentication or session checks are visible in this file.
5. Kanban status columns do not provide task status-update functionality.
6. Loading and API error states are not implemented in this file.

The separate `frontend/src/app/dashboard/page.tsx` file was not independently reviewed. Therefore, these findings should not automatically be attributed to that page.

### Recommendations

- Connect frontend operations to backend APIs.
- Persist task changes in the database.
- Implement protected routes and appropriate session handling.
- Add loading, error and retry states.
- Implement task status updates through validated backend endpoints.


## 7. Docker and Configuration Review



The supplied Docker Compose configuration defines frontend, backend and PostgreSQL services.



Findings:



- Database credentials are hardcoded in the Compose file.

- PostgreSQL port 5432 is published to the host.

- No PostgreSQL health check is configured.

- Frontend API configuration uses localhost.

- No explicit non-root application user is visible in the supplied configuration.



Positive observation:



- PostgreSQL uses a named persistent volume.



Recommendations:



- Use environment variables or a secrets manager.

- Restrict database network exposure.

- Add health checks and readiness dependencies.

- Configure environment-specific API endpoints.

- Run application containers with least privilege.



The example environment file uses SQLite while Docker Compose configures PostgreSQL. Document and test the intended database configuration for each environment.



## 8. Dependency and Repository Security Review



### Dependency management



The supplied dependency manifests use version ranges.



Recommendations:



- Maintain committed lockfiles.

- Use reproducible dependency installation.

- Review dependency updates.

- Introduce automated dependency vulnerability scanning.



No specific vulnerable package version was established during this review.



### Repository security policy



The repository contains a SECURITY.md file directing security reports to `security@cynbit.com`.



The published policy does not specify response timelines or detailed coordinated disclosure guidance.



No published security advisories were displayed on the inspected GitHub security page.



### CI/CD visibility



The inspected `.github/workflows` path returned a 404.



This means no workflow files were found at that path. External CI/CD systems and other repository automation settings were not verified.



## 9. Recommended Remediation Priorities



| Priority | Recommendation |

|---|---|

| Critical | Implement authentication and workspace-level authorization before exposing the API to real users |

| High | Enforce resource ownership and tenant isolation |

| High | Remove hardcoded database credentials |

| High | Restrict PostgreSQL network exposure |

| High | Integrate frontend operations with persistent backend APIs |

| Medium | Add pagination and request validation |

| Medium | Introduce database migrations and transaction error handling |

| Medium | Expand automated security and integration tests |

| Medium | Add dependency scanning and CI checks |

| Low | Improve privacy documentation and security disclosure guidance |



Priorities represent recommended remediation order for the reviewed lab implementation, not confirmed production incident severity.



## 10. Conclusion



The public SprintPulse repository demonstrates a basic full-stack application structure using Next.js, FastAPI, SQLAlchemy and PostgreSQL.



However, the reviewed implementation has significant gaps in authentication, authorization, persistence, frontend-backend integration, deployment configuration and automated testing.



The highest-value improvements are to establish secure resource-level access control, connect the frontend to persistent backend operations, protect database credentials and introduce reliable automated testing.



All conclusions are limited to the publicly accessible materials and source files inspected during this assessment. The production backend architecture and its security controls remain unverified.
