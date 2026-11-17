\# Cynbit Technologies – Backend Architecture \& Security Audit



Assessment: Backend Developer Intern Technical Assessment  

Date: November 17, 2026



\## Overview



This repository contains a passive backend architecture and security assessment of Cynbit Technologies' publicly accessible website and the publicly available SprintPulse Fullstack Lab repository.



The assessment identifies observable architectural patterns, potential backend improvement areas, security considerations, and practical recommendations.



\## Scope and Limitations



\- Reviewed publicly accessible website behavior and response headers.

\- Reviewed the publicly available SprintPulse Fullstack Lab source code.

\- Documented observations, risks, and recommendations.

\- Built an independent FastAPI authentication prototype to demonstrate selected backend security practices.



Important: The SprintPulse Fullstack Lab is not confirmed to be Cynbit's production backend. The authentication prototype is an independent demonstration, not a modification or deployment of Cynbit's production systems. Findings are limited to the reviewed public evidence.



\## Repository Structure



| Path | Description |

|---|---|

| `reports/backend\_audit\_report.md` | Main audit report |

| `reports/prototype\_validation.md` | Prototype implementation and test results |

| `evidence/website\_network\_observations.md` | Public website observations |

| `architecture/backend\_architecture.md` | Current and proposed architecture diagrams |

| `improvements/backend\_recommendations.md` | Prioritized technical recommendations |

| `app/` | Independent FastAPI authentication prototype |

| `tests/test\_auth.py` | Authentication prototype tests |



\## Authentication Prototype



The independent prototype demonstrates:



\- Password hashing using Argon2 through pwdlib.

\- JWT-based authentication with short-lived access tokens.

\- Environment-based secret configuration.

\- Request validation using Pydantic.

\- Duplicate registration handling.

\- Generic invalid-credential responses.

\- Protected user profile endpoint.

\- Basic rate limiting and security headers.



The prototype uses an in-memory user store and is intended for demonstration, not production deployment.



\## Run the Tests



Activate the virtual environment and install dependencies from `requirements.txt` if needed.



powershell

python -m pytest -v





\\Latest validation:\\ 7 tests passed, with 1 dependency deprecation warning.



\## Assessment Ethics



The website review was passive. No unauthorized access, exploitation, destructive testing, or service-disruption activity was performed.



\## Author



Errabelli Sathvik

