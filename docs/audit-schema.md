# Audit Schema

Platform: AGENT-CORE-GW

Version: 1.0

Purpose:

Define the audit structure used by AGENT-CORE-GW.

All gateway requests, authorization decisions, agent executions and MCP calls must be auditable.

==================================================

AUDIT OBJECTIVE

==================================================

The audit system must answer:

- Who performed an action?
- When was the action performed?
- Which agent was executed?
- Which MCP tool was accessed?
- Was access approved or denied?
- What was the execution outcome?
- How many tokens were consumed?
- What was the execution cost?

==================================================

AUDIT EVENT TYPES

==================================================

AUTHENTICATION

User authentication events.

Examples:

- Login success
- Login failure
- Token validation

--------------------------------------------------

AUTHORIZATION

Gateway authorization decisions.

Examples:

- Agent execution approved
- Agent execution denied
- MCP access approved
- MCP access denied

--------------------------------------------------

AGENT_EXECUTION

Agent runtime events.

Examples:

- Agent started
- Agent completed
- Agent failed

--------------------------------------------------

MCP_ACCESS

Tool execution events.

Examples:

- SharePoint Search
- SQL Read
- Document Search
- Knowledge Search

--------------------------------------------------

SYSTEM_EVENT

Platform management events.

Examples:

- Agent registration
- Agent update
- Gateway configuration change

==================================================

COMMON AUDIT FIELDS

==================================================

Audit ID

Unique audit event identifier.

Example:

AUD-000001

--------------------------------------------------

Timestamp UTC

UTC event timestamp.

Example:

2026-10-18T10:15:00Z

--------------------------------------------------

Correlation ID

Unique ID used to track an entire request flow.

Example:

CORR-8fa9d2

--------------------------------------------------

Request ID

Unique request identifier.

Example:

REQ-10231

--------------------------------------------------

Session ID

User session identifier.

Example:

SES-55443

--------------------------------------------------

User ID

Authenticated user identifier.

Example:

kobi

--------------------------------------------------

User Role

Example:

BusinessAnalyst

SolutionArchitect

Executive

PlatformAdmin

--------------------------------------------------

Source System

Originating application.

Example:

AI-Enabler

==================================================

AUTHORIZATION AUDIT FIELDS

==================================================

Agent Name

Example:

roadmap

--------------------------------------------------

Authorization Result

Values:

ALLOW

DENY

--------------------------------------------------

Reason

Explanation for the authorization decision.

Example:

Role not authorized.

--------------------------------------------------

Policy Version

Authorization policy version used.

Example:

1.0

==================================================

AGENT EXECUTION AUDIT FIELDS

==================================================

Agent Name

Example:

executive_report

--------------------------------------------------

Agent Version

Example:

1.0

--------------------------------------------------

Execution Status

Values:

Started

Completed

Failed

--------------------------------------------------

Execution Duration Seconds

Example:

18.54

--------------------------------------------------

Input Artifact

Example:

ai_roadmap.json

--------------------------------------------------

Output Artifact

Example:

executive_report.json

==================================================

LLM USAGE FIELDS

==================================================

Model Name

Example:

gpt-6.1-sol

--------------------------------------------------

Input Tokens

Example:

1259

--------------------------------------------------

Output Tokens

Example:

606

--------------------------------------------------

Total Tokens

Example:

1865

--------------------------------------------------

Estimated Cost

Example:

0.12

==================================================

MCP AUDIT FIELDS

==================================================

MCP Server

Example:

sharepoint

--------------------------------------------------

Tool Name

Example:

document_search

--------------------------------------------------

Action

Values:

Read

Write

Execute

--------------------------------------------------

Execution Result

Values:

Success

Failed

Denied

--------------------------------------------------

Execution Duration Milliseconds

Example:

850

==================================================

SECURITY FIELDS

==================================================

Authentication Status

Values:

Success

Failed

--------------------------------------------------

Authentication Provider

Example:

Cognito

Future Example:

EntraID

--------------------------------------------------

Risk Level

Values:

Low

Medium

High

--------------------------------------------------

Approval Required

Values:

True

False

==================================================

AUDIT RETENTION POLICY

==================================================

Authentication Events

365 Days

--------------------------------------------------

Authorization Events

365 Days

--------------------------------------------------

Agent Executions

365 Days

--------------------------------------------------

MCP Access Events

365 Days

--------------------------------------------------

System Events

365 Days

==================================================

MINIMUM REQUIRED AUDIT RECORD

==================================================

Every audit record must contain:

- Audit ID
- Timestamp
- Correlation ID
- User ID
- Role
- Event Type
- Event Result

Records missing any of these fields are invalid.

==================================================

DEFAULT AUDIT POLICY

==================================================

Audit Mode:

Always On

Audit cannot be disabled for:

- Authentication
- Authorization
- Agent Execution
- MCP Access

==================================================

SAMPLE AUDIT RECORD

==================================================

Audit ID:
AUD-000001

Timestamp:
2026-10-18T10:15:00Z

Correlation ID:
CORR-12345

User ID:
kobi

Role:
SolutionArchitect

Event Type:
AGENT_EXECUTION

Agent:
roadmap

Execution Status:
Completed

Duration:
24.7

Model:
gpt-6.1-sol

Input Tokens:
1049

Output Tokens:
1038

Total Tokens:
2087

Authorization Result:
ALLOW