# Backend Code Improvement \& Remediation Guide



**Assessment:** Cynbit Technologies Backend Developer Intern

**Date:** November 17, 2026



**Scope:** Proposed improvements based on the public SprintPulse lab repository review. These examples are recommendations, not verified production fixes.



\---



## 1. Authentication and Authorization



### Problem



The reviewed workspace, project and task routes do not declare authentication or authorization dependencies.



### Recommendation



Require an authenticated user and verify that the user has permission to access the requested workspace or resource.



Illustrative FastAPI pattern:



```python

from fastapi import Depends, HTTPException, status



def require_workspace_access(

&#x20;   workspace_id: str,

&#x20;   current_user = Depends(get_current_user),

&#x20;   db: Session = Depends(get_db),

):

&#x20;   membership = db.query(WorkspaceMember).filter(

&#x20;       WorkspaceMember.workspace_id == workspace_id,

&#x20;       WorkspaceMember.user_id == current_user.id,

&#x20;   ).first()



&#x20;   if membership is None:

&#x20;       raise HTTPException(

&#x20;           status_code=status.HTTP_403_FORBIDDEN,

&#x20;           detail="Workspace access denied",

&#x20;       )



&#x20;   return membership

```



Example endpoint:



```python

@app.get("/api/v1/workspaces/{workspace_id}/projects")

def list_projects(

&#x20;   workspace_id: str,

&#x20;   membership = Depends(require_workspace_access),

&#x20;   db: Session = Depends(get_db),

):

&#x20;   return db.query(Project).filter(

&#x20;       Project.workspace_id == workspace_id

&#x20;   ).all()

```



**Implementation note:** `WorkspaceMember` and `get_current_user` are illustrative dependencies. They must be implemented using the actual user and membership models. Authorization must also be enforced on individual project and task operations.



\---



## 2. Pagination



### Problem



The reviewed list endpoints return all matching records without pagination.



### Recommendation



Use bounded pagination.



```python

from fastapi import Query



@app.get("/api/v1/tasks")

def list_tasks(

&#x20;   project_id: str | None = None,

&#x20;   skip: int = Query(0, ge=0),

&#x20;   limit: int = Query(20, ge=1, le=100),

&#x20;   db: Session = Depends(get_db),

):

&#x20;   query = db.query(Task)



&#x20;   if project_id:

&#x20;       query = query.filter(Task.project_id == project_id)



&#x20;   return query.offset(skip).limit(limit).all()

```



Benefits:



\- Prevents unnecessarily large database responses.

\- Reduces memory and network usage.

\- Makes large task lists easier to handle.



\---



## 3. Input Validation



### Problem



The supplied Pydantic schemas do not define meaningful string-length constraints for several fields.



### Recommendation



Use Pydantic field validation.



```python

from pydantic import BaseModel, Field



class TaskCreate(BaseModel):

&#x20;   title: str = Field(

&#x20;       min_length=1,

&#x20;       max_length=255,

&#x20;   )



&#x20;   description: str | None = Field(

&#x20;       default=None,

&#x20;       max_length=2000,

&#x20;   )

```



Additional validation should cover workspace slugs, identifiers and allowed state transitions.



Server-side validation is mandatory. Frontend validation alone is not a security control.



\---



## 4. Secure CORS Configuration



### Problem



The supplied Docker-independent backend configuration uses:



```python

allow_origins=["*"]

allow_credentials=True

allow_methods=["*"]

allow_headers=["*"]

```



This is unnecessarily broad. Wildcard origins and credentialed browser requests also have important browser and framework restrictions.



### Recommendation



Configure an explicit origin allowlist.



```python

app.add_middleware(

&#x20;   CORSMiddleware,

&#x20;   allow_origins=[

&#x20;       "https://app.example.com",

&#x20;       "https://staging.example.com",

&#x20;   ],

&#x20;   allow_credentials=True,

&#x20;   allow_methods=["GET", "POST", "PATCH", "DELETE"],

&#x20;   allow_headers=["Authorization", "Content-Type"],

)

```



The example domains must be replaced with actual trusted deployment origins.



\---



## 5. Secure Environment Configuration



### Problem



The supplied Docker Compose file contains hardcoded database credentials.



### Recommendation



Read credentials from environment configuration or a secrets manager.



```yaml

services:

&#x20; db:

&#x20;   image: postgres:15-alpine

&#x20;   environment:

&#x20;     POSTGRES_USER: ${POSTGRES_USER}

&#x20;     POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}

&#x20;     POSTGRES_DB: ${POSTGRES_DB}

&#x20;   volumes:

&#x20;     - postgres_data:/var/lib/postgresql/data

```



Keep the database port private in production unless external access is explicitly required and restricted.



Never commit actual secrets to Git.



\---



## 6. Database Migrations



### Problem



The reviewed backend calls:



```python

Base.metadata.create_all(bind=engine)

```



This creates missing tables but does not replace a proper schema migration workflow.



### Recommendation



Use Alembic to manage database schema changes.



Example commands:



```powershell

alembic revision --autogenerate -m "add workspace membership"

alembic upgrade head

```



Benefits:



\- Version-controlled schema changes.

\- Repeatable deployment upgrades.

\- Better coordination across development and production databases.



\---



## 7. Database Transaction Error Handling



### Problem



The reviewed route handlers commit database changes without explicit rollback handling.



### Recommendation



Use transaction-safe error handling.



```python

try:

&#x20;   db.add(task)

&#x20;   db.commit()

&#x20;   db.refresh(task)

except Exception:

&#x20;   db.rollback()

&#x20;   raise

```



In production, catch and translate known database exceptions into appropriate API responses. Do not expose raw database error messages to clients.



\---



## 8. Automated Testing



### Problem



The supplied tests focus primarily on a successful workspace-project-task workflow.



### Recommendation



Expand testing to cover both successful and unsuccessful scenarios.



Examples:



1\. An unauthenticated user attempting to access a protected endpoint should receive an authentication error.

2\. A user from Workspace A attempting to update a task belonging to Workspace B should be denied.



Additional test categories:



\- Invalid request data.

\- Missing resources.

\- Duplicate records.

\- Database transaction failures.

\- Pagination limits.

\- Authentication token expiry.

\- Workspace ownership and membership.



Use a dedicated test database and fixtures to isolate test data.



\---



## 9. Frontend-Backend Integration



### Problem



The reviewed dashboard uses local React state rather than backend API operations.



### Recommendation



Connect task creation to the backend.



Illustrative TypeScript example:



```typescript

const response = await fetch(

&#x20; `${process.env.NEXT_PUBLIC_API_URL}/tasks`,

&#x20; {

&#x20;   method: "POST",

&#x20;   headers: {

&#x20;     "Content-Type": "application/json",

&#x20;     "Authorization": `Bearer ${accessToken}`,

&#x20;   },

&#x20;   body: JSON.stringify({

&#x20;     title: newTaskTitle,

&#x20;     status: "TODO",

&#x20;     project_id: projectId,

&#x20;   }),

&#x20; }

);



if (!response.ok) {

&#x20; throw new Error("Unable to create task");

}



const createdTask = await response.json();

```



The application should also:



\- Display loading states.

\- Handle network and server errors.

\- Update the interface after successful API responses.

\- Persist task changes in the database.

\- Avoid exposing authentication secrets in browser-visible configuration.



Token storage and session management require a separate security design; this example is not a complete authentication implementation.



\---



## 10. Implementation Priority



| Priority | Improvement |

|---|---|

| Critical | Authentication and resource-level authorization |

| High | Tenant isolation |

| High | Remove hardcoded credentials |

| High | Frontend-backend integration |

| High | Restrict database exposure |

| Medium | Pagination |

| Medium | Request validation |

| Medium | Database migrations |

| Medium | Transaction error handling |

| Medium | Automated security tests |

| Medium | Dependency scanning |



## Final Note



These recommendations are proposed engineering improvements derived from the inspected public repository. They have not been applied to or tested against Cynbit's production infrastructure.
