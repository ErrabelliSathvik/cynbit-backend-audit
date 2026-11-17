
# Cynbit Website Network Observations

Target: https://cynbit.in
Inspection type: Passive browser inspection
Date: 17 November 2026

## Page inspected
- Page URL: https://cynbit.in

## Network requests

| Request path | Method | Status | Approx. size | Duration | Observation |
|---|---|---:|---:|---:|---|
| careers?_rsc=SCJVgjZa56qhWaZb | Fetch | 200 | 0.2 kB | 297 ms | Successful response |
| story?_rsc=SCJVgjZa56qhWaZb | Fetch | 304 | 0.1 kB | 104 ms | Cached response |
| team?_rsc=SCJVgjZa56qhWaZb | Fetch | 304 | 0.1 kB | 57 ms | Cached response |
| impact?_rsc=SCJVgjZa56qhWaZb | Fetch | 304 | 0.1 kB | 87 ms | Cached response |
| services?_rsc=SCJVgjZa56qhWaZb | Fetch | 304 | 0.1 kB | 85 ms | Cached response |
| case-studies?_rsc=SCJVgjZa56qhWaZb | Fetch | 200 | 0.2 kB | 324 ms | Successful response |
| ai-agents-business-operations?_rsc=SCJVgjZa56qhWaZb | Fetch | 200 | 0.3 kB | 278 ms | Successful response |
| products?_rsc=SCJVgjZa56qhWaZb | Fetch | 304 | 0.1 kB | 92 ms | Cached response |
| contact?_rsc=SCJVgjZa56qhWaZb | Fetch | 200 | 2.6 kB | 60 ms | Successful response |
| bitelevate?_rsc=SCJVgjZa56qhWaZb | Fetch | 304 | 0.1 kB | 51 ms | Cached response |

## Notes
- Ten Fetch/XHR requests observed during homepage inspection.
- Requests contain the `_rsc` query parameter, consistent with Next.js React Server Components navigation.
- Both 200 and 304 responses were observed.
- No security vulnerability is established by these observations alone.
- Response headers and payloads require further inspection.


## Response Header Inspection

Request inspected: /contact?_rsc=...
Matched path: /contact.rsc
Server: Vercel
Response Content-Type: text/x-component

| Header | Observed value | Assessment |
|---|---|---|
| age | 81001 | Cached response age; investigate cache behavior in context |
| cache-control | public, max-age=0, must-revalidate | Requires revalidation before reuse |
| content-encoding | br | Brotli compression enabled |
| content-type | text/x-component | Consistent with Next.js RSC |
| server | Vercel | Hosting platform disclosed |
| strict-transport-security | max-age=63072000 | HSTS enabled |
| vary | rsc, next-router-state-tree, next-router-prefetch, next-router-segment-prefetch | Cache variation for Next.js request context |
| x-nextjs-prerender | 1 | Prerender metadata present |
| x-nextjs-stale-time | 300 | Next.js stale-time metadata |
| x-vercel-cache | HIT | Vercel cache hit |

### Initial assessment
- HSTS is present.
- Brotli compression is enabled.
- Vercel reports a cache hit.
- Server platform information is exposed.
- No confirmed vulnerability established from these headers alone.
- x-content-type-options was not present in the supplied response headers; verify on the main HTML document.


## Main HTML Document Response Headers

| Header | Observed value |
|---|---|
| cache-control | public, max-age=0, must-revalidate |
| date | Tue, 17 Nov 2026 09:05:05 GMT |
| server | Vercel |
| x-vercel-cache | HIT |

Assessment:
- Vercel cache hit observed.
- Browser cache revalidation is required.
- No confirmed security issue established from these headers alone.


## Main Document Security Header Assessment

Inspection scope: Main HTML document response only.

Observed response headers:
- cache-control
- date
- server
- x-vercel-cache
- x-vercel-id

The following headers were not observed in this response:
- Content-Security-Policy
- Strict-Transport-Security
- X-Content-Type-Options
- X-Frame-Options
- Referrer-Policy
- Permissions-Policy

Important qualification:
Strict-Transport-Security was observed on the separate
/contact.rsc response. Therefore, its absence from the
main document response does not establish site-wide absence.

Initial recommendation:
Review the security-header configuration and apply
appropriate headers consistently to relevant responses.
Validate compatibility before enforcing Content-Security-Policy.

Evidence limitation:
This observation is based on one main document response
during a single browser inspection.


## Contact Page Inspection

Page: https://cynbit.in/contact

### Visible form fields
- Full Name
- Email Address
- Company (Optional)
- Industry (Optional)
- Your Message

### Form action
- Button: Send Inquiry

### Additional observations
- Website displays a 24-hour response-time statement.
- Privacy Policy link is visible in the footer.
- Public email addresses and telephone numbers are displayed.
- No form submission was performed.
- Backend validation, storage, spam protection and retention behavior have not been verified.

### Recommended backend controls
- Server-side input validation
- Request-size limits
- Rate limiting and spam protection
- Secure handling of personal information
- Restricted access to inquiry records
- Defined data-retention policy


## Privacy Policy Inspection

Page: https://cynbit.in/privacy-policy
Last updated: 20 May 2026

### Policy statements
- Collects name, email and professional context.
- Uses inquiry and application information to respond to requests.
- States that personal data is not sold, rented or traded for marketing.
- Claims industry-standard encryption.
- Identifies Resend for email delivery.
- Identifies Prisma for database management.
- Provides access and permanent-deletion request rights.
- Provides opportunities@cynbit.in as the contact address.

### Documentation gaps
1. Encryption standards and key-management practices are not specified.
2. No personal-data retention period is stated.
3. Backup deletion and permanent-erasure procedures are not explained.
4. No deletion-request completion timeline is specified.
5. Details about third-party data processing and retention are limited.

### Evidence limitations
These are observations of published policy statements.
Technical implementation has not been independently verified.


## Privacy Policy Inspection

Page: https://cynbit.in/privacy-policy
Policy last updated: May 20, 2026

### Disclosed information
- The policy describes collecting names, email addresses, and professional context.
- Inquiry-form and BitElevate application information is stated to be used for communication.
- The policy states that personal data is not sold, rented, or traded for marketing.
- Resend is identified as an email delivery provider.
- Prisma is identified as a database management provider.
- Users may request access to or deletion of their data through opportunities@cynbit.in.

### Security statements
- The policy claims industry-standard encryption.
- It does not specify encryption algorithms, key-management practices, or whether encryption at rest is used.
- The phrase "optimistic architecture patterns" is not a sufficiently precise description of a security control.

### Documentation gaps
- No specific data-retention periods are disclosed.
- Newsletter email collection is visible on the website, but is not explicitly addressed in the supplied policy text.
- No unsubscribe process is explained in the supplied policy text.
- No response timeline or identity-verification process is specified for data-access and deletion requests.
- No details about third-party data-processing locations or international transfers are provided.

### Limitations
- These are observations about publicly available policy text.
- Actual database controls, encryption, retention, and third-party configurations were not verified.
- No forms were submitted and no backend systems were accessed.

## Newsletter Popup Inspection

### Visible elements
- Newsletter title: The Architect's Digest
- Description: Weekly insights on neural infrastructure and digital growth.
- Email field: Business Email
- Button: Subscribe Now
- Frequency statement: One editorial briefing per week.
- Privacy statement: Secure & Private.

### Observations
- No consent checkbox was visible in the inspected popup.
- No explicit consent statement was visible beside the email field.
- No Privacy Policy link was visible within the popup content.
- No unsubscribe instructions were visible.
- The website displays a weekly newsletter frequency statement.

### Limitations
- No email address was submitted.
- Subscription behavior and consent handling were not tested.
- Unsubscribe functionality was not verified.

## Frontend Architecture Indicators

### Observed evidence
- Hosting server header: Vercel
- Next.js prerender header: x-nextjs-prerender: 1
- Next.js stale-time header: x-nextjs-stale-time: 300
- Response content type: text/x-component
- Network requests included the _rsc query parameter.
- Response paths included .rsc resources.

### Assessment
These observations are consistent with a Next.js application using React Server Components and Vercel hosting.

### Limitations
- The exact Next.js version was not identified.
- The production backend framework was not verified.
- The production database was not verified.
- Frontend observations do not establish the internal backend architecture.

## Publicly Disclosed Technology Stack

Source: https://github.com/Cynbit-Technologies/.github

### Technologies listed by Cynbit
- Frontend: React, Next.js
- Backend: FastAPI, Django, Node.js, NestJS
- Databases: PostgreSQL, MongoDB, Redis, Supabase, Neo4j
- Infrastructure: AWS, Azure, Docker, Kubernetes

### Assessment
The public organization profile documents multiple backend frameworks and database technologies.

### Limitations
- These are company-level technology disclosures.
- The actual production backend framework was not independently verified.
- The database used by the public website was not identified.
- No public API documentation was identified in the searches performed.

## Public Full-Stack Project: SprintPulse SaaS

Source:
https://github.com/Cynbit-Technologies/bitelevate-fullstack-lab

### Documented architecture
- Frontend: Next.js 15, React 19, TypeScript, Tailwind CSS.
- Backend: FastAPI with Python 3.11+.
- ORM: SQLAlchemy 2.0.
- Databases: PostgreSQL / SQLite.
- Containerization: Docker and Docker Compose.
- Backend testing: Pytest.
- Local API documentation: /docs.

### Architecture observations
- The project separates frontend and backend directories.
- The backend uses an ORM for database interaction.
- Docker Compose is documented for local orchestration.
- Environment variables are used for API URL and database configuration.
- Backend tests are documented as part of the development workflow.

### Audit limitations
- SprintPulse is a separate public lab project.
- Its architecture does not establish the production architecture of cynbit.in.
- No production database, API implementation, or authentication configuration was verified.

## Public Security Policy Inspection

Source:
https://github.com/Cynbit-Technologies/bitelevate-fullstack-lab/blob/main/SECURITY.md

### Observed information
- Security reports should be sent to security@cynbit.com.
- Security vulnerabilities should not be reported through public GitHub issues.

### Positive observations
- A dedicated security reporting email address is documented.
- The policy discourages public disclosure of vulnerabilities.

### Documentation improvement opportunities
- Define a vulnerability acknowledgement timeframe.
- Explain the responsible disclosure process.
- Provide coordinated disclosure expectations.
- Clarify supported vulnerability report details.
- Document scope and exclusions.

### Limitations
- This is the security policy of the public SprintPulse repository.
- It does not establish the security practices of Cynbit's production website.

## Public Backend Repository Structure

Source:
https://github.com/Cynbit-Technologies/bitelevate-fullstack-lab

### Observed structure
- backend/app/
- backend/tests/
- backend/requirements.txt
- frontend/
- docker-compose.yml
- .env.example
- .gitignore
- SECURITY.md
- CONTRIBUTING.md

### Testing evidence
- One test file is visible: backend/tests/test_fullstack_api.py.
- README documents Pytest for backend testing.

### Repository metadata
- One public contributor listed.
- One pull request listed.
- One fork listed.

### Limitations
- Repository metadata does not establish code quality.
- Test coverage cannot be assessed from filenames alone.
- SprintPulse is not confirmed to be the production backend of cynbit.in.

## SprintPulse Backend Source-Code Review: main.py

Source:
https://github.com/Cynbit-Technologies/bitelevate-fullstack-lab/blob/main/backend/app/main.py

### Observed implementation
- FastAPI application.
- SQLAlchemy database engine and session management.
- SQLite default database URL.
- Workspace, project and task CRUD-related endpoints.
- Health endpoint at /health.
- CORS middleware configured with wildcard origins, methods and headers.
- Database tables created using Base.metadata.create_all().
- OpenAPI JSON configured at /api/v1/openapi.json.

### Findings

1. Missing authentication and authorization
- No authentication dependency is applied to workspace, project or task endpoints.
- Task updates do not verify user or workspace ownership.
- Recommendation: implement authenticated access and resource-level authorization.

2. Permissive CORS
- CORS allows all origins, methods and headers.
- Credentials are enabled.
- Recommendation: configure an explicit trusted-origin allowlist and restrict methods and headers.

3. Missing pagination
- List endpoints return all matching records.
- No limit, offset or cursor pagination is implemented.
- Recommendation: introduce pagination and maximum page sizes.

4. Missing tenant-level authorization
- Project filtering accepts a workspace_id supplied by the caller.
- No authenticated tenant context or ownership check is visible.
- Recommendation: enforce workspace membership and ownership on every resource operation.

5. Database migration management
- Tables are created during application initialization using create_all().
- No migration workflow is visible in this file.
- Recommendation: use version-controlled database migrations.

6. Database error handling
- Database commits do not have explicit rollback or integrity-error handling.
- Recommendation: handle transaction failures and return appropriate API errors.

### Scope limitation
These findings concern the publicly available SprintPulse lab source code only. They do not establish vulnerabilities in Cynbit's production website.

## SprintPulse Database Model Review: models.py

Source:
https://github.com/Cynbit-Technologies/bitelevate-fullstack-lab/blob/main/backend/app/models.py

### Positive observations
- UUID-based primary keys are generated for workspaces, projects and tasks.
- Workspace slugs have a unique constraint.
- Required fields use nullable=False.
- Projects reference workspaces through foreign keys.
- Tasks reference projects through foreign keys.
- Task statuses use a defined enumeration.
- SQLAlchemy relationships define cascading deletion behavior.

### Findings and recommendations

1. Cascading deletion
- Workspace deletion can cascade to associated projects and tasks through ORM relationships.
- Recommendation: protect destructive operations with authorization, confirmation and recovery safeguards.

2. SQLite foreign-key enforcement
- Foreign keys specify ondelete=CASCADE.
- SQLite foreign-key enforcement should be explicitly enabled and verified.
- Recommendation: configure and test SQLite foreign-key enforcement.

3. Query indexing
- No explicit indexes are defined for workspace_id and project_id.
- Recommendation: evaluate indexes for frequently filtered foreign-key columns.

4. Auditability
- Models expose created_at but no updated_at or change-history fields.
- Recommendation: add update timestamps and audit logging for important changes.

5. Data recovery
- No soft-delete or recovery mechanism is visible in these models.
- Recommendation: define backup, restore and deletion-recovery procedures.

### Scope limitation
These observations concern the SprintPulse public lab database models, not Cynbit's verified production database.

## SprintPulse Request Schema Review: schemas.py

Source:
https://github.com/Cynbit-Technologies/bitelevate-fullstack-lab/blob/main/backend/app/schemas.py

### Positive observations
- Separate request and response schemas are defined.
- Response schemas use ConfigDict(from_attributes=True).
- Task status uses a defined enumeration.
- Optional descriptions are supported.

### Findings and recommendations

1. Insufficient string constraints
- Workspace names, slugs, project names and task titles have no explicit length constraints.
- Recommendation: add minimum and maximum lengths and reject whitespace-only values.

2. Missing slug format validation
- Workspace slug accepts a plain string.
- Recommendation: validate an agreed slug format.

3. Missing identifier format validation
- workspace_id and project_id are plain strings.
- Recommendation: validate UUID format consistently.

4. Unbounded descriptions
- Project and task descriptions have no explicit maximum length.
- Recommendation: enforce reasonable maximum lengths.

5. PATCH null-handling ambiguity
- TaskUpdate fields are Optional and default to None.
- The current update implementation cannot distinguish an omitted field from an explicitly supplied null.
- Recommendation: use model_fields_set to distinguish omitted fields and define explicit null-handling behavior.

### Scope limitation
These findings concern the SprintPulse public lab source code, not the production Cynbit website.

## SprintPulse Backend Test Review: test_fullstack_api.py

Source:
https://github.com/Cynbit-Technologies/bitelevate-fullstack-lab/blob/main/backend/tests/test_fullstack_api.py

### Existing tests
- Health endpoint returns HTTP 200.
- Workspace creation succeeds.
- Project creation succeeds.
- Task creation succeeds.
- Task status update succeeds.

### Testing gaps

1. Invalid input testing
- No tests for missing fields, invalid values or oversized input.
- Recommendation: add positive and negative schema validation tests.

2. Authorization testing
- No tests for unauthenticated requests or unauthorized resource access.
- Recommendation: test authentication and resource-level authorization.

3. Tenant isolation testing
- No tests verify that one workspace cannot access another workspace's projects or tasks.
- Recommendation: add cross-workspace access tests.

4. Error handling
- No tests cover missing resources, duplicate slugs or database integrity errors.
- Recommendation: test expected error status codes and response bodies.

5. Pagination testing
- No tests verify maximum page sizes or pagination behavior.
- Recommendation: add pagination boundary tests after implementing pagination.

6. Test isolation
- The test file imports the application directly and does not visibly configure an isolated test database.
- Recommendation: use a dedicated test database and fixtures to isolate test cases.

### Scope limitation
This assessment covers the supplied public test file only. Other test files or automated checks may exist elsewhere in the repository.

## SprintPulse Dependency Review: requirements.txt

Source:
https://github.com/Cynbit-Technologies/bitelevate-fullstack-lab/blob/main/backend/requirements.txt

### Observed dependencies
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic
- Pydantic Settings
- python-jose
- passlib with bcrypt
- python-multipart
- Pytest
- HTTPX
- email-validator

### Findings and recommendations

1. Dependency versions are not fully pinned
- Requirements use minimum version constraints.
- Different installations may resolve to different versions.
- Recommendation: maintain a reproducible dependency lockfile and update dependencies through reviewed changes.

2. Dependency security monitoring
- No automated dependency scanning configuration was verified during this review.
- Recommendation: introduce automated vulnerability scanning and scheduled dependency updates.

3. Authentication dependency usage
- JWT and password-hashing libraries are listed.
- The inspected main.py does not apply authentication to its API endpoints.
- Recommendation: verify that authentication is implemented and enforced consistently across protected routes.

### Limitations
- No resolved package versions were inspected.
- No vulnerability scan was performed.
- No claim is made that a listed package has a known vulnerability.

## SprintPulse Docker Compose Review

Source:
https://github.com/Cynbit-Technologies/bitelevate-fullstack-lab/blob/main/docker-compose.yml

### Observed configuration
- Three services: backend, frontend and PostgreSQL database.
- Backend port 8000 is published.
- Frontend port 3000 is published.
- PostgreSQL port 5432 is published.
- PostgreSQL 15 Alpine image is used.
- A named volume persists PostgreSQL data.
- Backend receives DATABASE_URL through environment configuration.
- Frontend receives NEXT_PUBLIC_API_URL through environment configuration.

### Findings and recommendations

1. Hardcoded database credentials
- Database username and password are embedded in Docker Compose.
- Recommendation: use environment variables or a secrets manager and rotate exposed credentials before production deployment.

2. Database port exposure
- PostgreSQL port 5432 is published to the host.
- Recommendation: avoid publishing the database port in production unless operationally necessary and properly restricted.

3. Database readiness
- Backend depends_on references the database service.
- No database health check is configured.
- Recommendation: configure health checks and readiness-based startup dependencies.

4. Environment-specific frontend configuration
- Frontend API URL uses localhost.
- Recommendation: provide separate development and production configuration.

5. Container privileges
- No explicit non-root user configuration is visible in this file.
- Recommendation: run application containers with least privilege.

### Positive observation
- PostgreSQL uses a named persistent volume.

### Scope limitation
- This review covers the public SprintPulse Docker Compose configuration, not Cynbit's production deployment.

## SprintPulse Environment Configuration Review

Source:
https://github.com/Cynbit-Technologies/bitelevate-fullstack-lab/blob/main/.env.example

### Observed configuration
- NEXT_PUBLIC_API_URL points to localhost:8000/api/v1.
- DATABASE_URL uses a local SQLite database.
- Docker Compose separately configures PostgreSQL.

### Findings

1. Database environment inconsistency
- The example environment uses SQLite, while Docker Compose uses PostgreSQL.
- Recommendation: document development and deployment database configurations and test against the intended production database engine.

2. Frontend API configuration
- The frontend API URL points to localhost.
- Recommendation: configure the correct HTTPS API endpoint for production.
- NEXT_PUBLIC variables are browser-visible and must not contain secrets.

### Scope limitation
- This review covers public example configuration files.
- The actual production environment variables and deployment configuration were not verified.

## SprintPulse Backend Authentication Review

Source:
https://github.com/Cynbit-Technologies/bitelevate-fullstack-lab/tree/main/backend/app

### Observed evidence
- The backend application directory contains main.py, models.py and schemas.py.
- No separate auth.py or security.py module is present.
- No dedicated authentication directory is visible.
- Previously reviewed workspace, project and task endpoints do not declare authentication or authorization dependencies.

### Finding: Missing authentication and authorization in reviewed API endpoints

The reviewed API endpoints allow workspace, project and task operations without visible authentication or authorization dependencies.

Potential impact:
- Unauthorized users could access application data if the API is deployed in this configuration.
- Users could potentially access or modify records belonging to other workspaces.

Recommendations:
- Implement authentication using a suitable token or session mechanism.
- Enforce workspace-level authorization on every relevant operation.
- Verify ownership before retrieving, updating or deleting projects and tasks.
- Add tests for unauthorized requests and cross-workspace access.

### Scope limitation
This finding applies only to the reviewed public SprintPulse repository.
It does not establish that Cynbit's production website has the same issue.

## SprintPulse CI/CD Configuration Review

Source:
https://github.com/Cynbit-Technologies/bitelevate-fullstack-lab/tree/main/.github/workflows

### Observed evidence
- GitHub returned a 404 for the .github/workflows directory on the main branch.
- No GitHub Actions workflow files were visible at this path.

### Recommendation
- Introduce automated CI workflows for backend tests, frontend checks and code quality.
- Add dependency vulnerability scanning.
- Require successful checks before merging pull requests.
- Protect the main branch against unreviewed changes.

### Scope limitation
- No GitHub Actions workflow configuration was found at the inspected path.
- External CI/CD platforms and repository-level automation settings were not inspected.

## SprintPulse GitHub Security Configuration Review

Source:
https://github.com/Cynbit-Technologies/bitelevate-fullstack-lab/security

### Observed evidence
- A SECURITY.md policy is published.
- Security reports are directed to security@cynbit.com.
- The policy discourages reporting vulnerabilities through public GitHub issues.
- GitHub displays no published security advisories.

### Findings and recommendations

1. Limited vulnerability disclosure guidance
- The policy provides a reporting email but no response timeframe.
- Recommendation: document acknowledgement targets, severity handling and coordinated disclosure expectations.

2. Security monitoring visibility
- The inspected page does not establish whether Dependabot alerts, code scanning or secret scanning are enabled.
- Recommendation: enable and periodically review appropriate repository security controls.

3. Advisory visibility
- No published security advisories were displayed.
- This does not establish that the repository has no vulnerabilities.

### Scope limitation
- This is a review of publicly visible GitHub security information.
- Private alerts, repository settings and actual security monitoring configurations were not verified.
- This repository is the public SprintPulse lab project, not confirmed production infrastructure.

## SprintPulse Frontend Dependency Review

Source:
https://github.com/Cynbit-Technologies/bitelevate-fullstack-lab/blob/main/frontend/package.json

### Observed dependencies
- Next.js: ^15.1.0
- React: ^19.0.0
- React DOM: ^19.0.0
- TypeScript: ^5.7.2
- Tailwind CSS: ^3.4.16
- Lucide React: ^0.468.0

### Observed scripts
- dev: next dev
- build: next build
- start: next start

### Findings and recommendations

1. Dependency version reproducibility
- Dependencies use version ranges rather than exact versions.
- Recommendation: commit and maintain a lockfile and use reproducible dependency installation.

2. Frontend testing visibility
- No test or lint scripts are defined in the supplied package.json.
- Recommendation: add automated component or integration tests and lint/type-check commands.

3. Authentication and API client visibility
- No dedicated authentication or HTTP client library is declared.
- The frontend may still implement authentication and API calls using custom code or native fetch().
- Source inspection is required before drawing conclusions.

### Positive observation
- A production build script is defined.

### Scope limitation
- This review is limited to the supplied package.json.
- Resolved dependency versions and actual frontend implementation were not inspected.

## SprintPulse Main Frontend Page Review

Source:
https://github.com/Cynbit-Technologies/bitelevate-fullstack-lab/blob/main/frontend/src/app/page.tsx

### Observed implementation
- The main page is a client-side React component.
- Three sample tasks are hardcoded.
- Task creation modifies local React state.
- No backend API requests are implemented.
- Workspace name is hardcoded as Acme Global Workspace.
- Task status columns are display-only.
- No task status update operation is implemented.
- Input validation only checks whether the task title is empty.
- Next.js Link is imported but unused.

### Findings

1. Frontend-backend integration gap
- The UI describes itself as connecting Next.js to FastAPI, but the reviewed page does not make API requests.
- Recommendation: connect task operations to the backend API.

2. Non-persistent task operations
- Tasks are maintained in local component state.
- Recommendation: persist tasks through backend endpoints and PostgreSQL.

3. Incomplete Kanban functionality
- Tasks are displayed by status, but no status-update functionality is implemented.
- Recommendation: implement validated task status transitions through the backend.

4. Limited input validation
- Empty task titles are rejected, but no maximum length or other meaningful validation is visible.
- Recommendation: apply consistent client-side and server-side validation.

### Scope limitation
- This finding applies to the inspected main page.
- The public SprintPulse lab repository is not confirmed to represent Cynbit's production website or backend.