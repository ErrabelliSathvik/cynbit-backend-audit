# Authentication Prototype — Implementation and Test Results



**Project:** Independent Backend Security Prototype

**Assessment:** Cynbit Technologies Backend Developer Intern

**Date:** November 17, 2026



## 1. Objective



Develop an illustrative FastAPI authentication implementation demonstrating secure password handling, JWT-based authentication, request validation and protected user endpoints.



This prototype is independent work. It is not part of Cynbit's production application and does not establish that the production application uses these controls.



## 2. Implemented Controls



| Control | Implementation |

|---|---|

| Password security | Password hashing using pwdlib |

| Authentication | JWT access tokens |

| Token expiration | 15-minute access-token lifetime |

| Secret management | JWT secret loaded from environment configuration |

| Registration validation | Pydantic request schemas |

| Duplicate registration | HTTP 409 response |

| Invalid credentials | Generic HTTP 401 response |

| Protected endpoint | Authenticated `/me` endpoint |

| Rate limiting | Registration and login limits |

| Security headers | Middleware adds selected HTTP security headers |

| User enumeration | Removed the public user-list endpoint |



## 3. Automated Test Results



Command:



```powershell

python -m pytest tests/test_auth.py -v

```



Result:



**7 passed, 0 failed, 1 warning**



Tests executed:



1\. Successful user registration.

2\. Duplicate registration rejection.

3\. Successful login.

4\. Incorrect password rejection.

5\. Profile access without a token rejected.

6\. Profile access with a valid token permitted.

7\. Invalid token rejected.



## 4. Environment and Secret Handling Verification



Checks performed:



\- `.env` is listed in `.gitignore`.

\- `git check-ignore -v .env` confirms the ignore rule.

\- `git ls-files .env` returned no tracked file.

\- JWT configuration check confirmed a configured secret with a length of 64 characters.



The actual secret value was not included in the assessment documentation.



## 5. Warning



The test run reported a Starlette deprecation warning regarding the use of `httpx` with `starlette.testclient`.



All seven tests passed. The warning should be reviewed during dependency maintenance.



## 6. Limitations



\- User records are stored in an in-memory store rather than a persistent production database.

\- The prototype is not deployed.

\- No production integration was performed.

\- The prototype has not undergone an independent security assessment.

\- Automated tests cover the listed authentication scenarios, not every possible attack or failure condition.



## 7. Conclusion



The prototype demonstrates practical implementation of several backend authentication and security controls. Its automated tests passed in the local development environment.



These results validate the prototype's tested behavior only. They must not be interpreted as evidence of the security posture of Cynbit's production systems.
