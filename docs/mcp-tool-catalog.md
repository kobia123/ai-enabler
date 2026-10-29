# MCP Tool Catalog

Platform: AI Enabler

Version: 1.0

Purpose:

Define all MCP tools available to AGENT-CORE-GW.

The catalog serves as the single source of truth for:

- MCP Registration
- MCP Governance
- Tool Authorization
- Tool Ownership
- Agent Tool Access
- Future AgentCore Gateway Integration

==================================================

MCP STRATEGY

==================================================

Current State:

Mock MCP Implementation

Purpose:

Validate architecture and workflows without requiring external systems.

--------------------------------------------------

Future State:

AWS AgentCore Gateway

Purpose:

Provide secure access to enterprise tools and services.

==================================================

ACTIVE MCP TOOLS

==================================================

Tool ID:
document_search

Status:
Active

Type:
Read Only

Implementation:
Mock

Purpose:

Search project documents and return matching content.

Used By:

- analyze_organization
- function_analysis
- ai_opportunity
- roadmap
- executive_report

Input:

Search Query

Output:

Matching Documents

--------------------------------------------------

Tool ID:
knowledge_lookup

Status:
Active

Type:
Read Only

Implementation:
Mock

Purpose:

Provide enterprise knowledge and technology definitions.

Examples:

- SAP
- Salesforce
- ServiceNow
- Azure
- AWS

Used By:

- function_analysis
- ai_opportunity
- roadmap

Input:

Knowledge Term

Output:

Knowledge Record

--------------------------------------------------

Tool ID:
organization_data

Status:
Active

Type:
Read Only

Implementation:
Mock

Purpose:

Provide structured organizational information.

Examples:

- Employee Count
- Business Units
- Application Count
- Region Count

Used By:

- analyze_organization
- function_analysis
- ai_opportunity

Input:

Organization Query

Output:

Organization Data

==================================================

AGENT TOOL MATRIX

==================================================

Agent:
analyze_organization

Allowed Tools:

- document_search
- organization_data

--------------------------------------------------

Agent:
function_analysis

Allowed Tools:

- document_search
- knowledge_lookup
- organization_data

--------------------------------------------------

Agent:
ai_opportunity

Allowed Tools:

- document_search
- knowledge_lookup
- organization_data

--------------------------------------------------

Agent:
roadmap

Allowed Tools:

- document_search
- knowledge_lookup

--------------------------------------------------

Agent:
executive_report

Allowed Tools:

- document_search

==================================================

ROLE TOOL MATRIX

==================================================

BusinessAnalyst

Allowed Tools:

- document_search
- knowledge_lookup
- organization_data

--------------------------------------------------

SolutionArchitect

Allowed Tools:

- document_search
- knowledge_lookup
- organization_data

--------------------------------------------------

Executive

Allowed Tools:

- document_search

--------------------------------------------------

PlatformAdmin

Allowed Tools:

- document_search
- knowledge_lookup
- organization_data

==================================================

TOOL ACCESS RULES

==================================================

Rule 1

All tool requests must pass through AGENT-CORE-GW.

--------------------------------------------------

Rule 2

Direct tool access is prohibited.

--------------------------------------------------

Rule 3

Both agent authorization and user authorization are required.

--------------------------------------------------

Rule 4

Tool access must be audited.

--------------------------------------------------

Rule 5

Unknown tools must be denied.

==================================================

AUTHORIZATION MODEL

==================================================

A tool request is approved only if:

User Permission

AND

Agent Permission

are both valid.

--------------------------------------------------

Example

User Role:

SolutionArchitect

Agent:

roadmap

Tool:

document_search

Result:

ALLOW

--------------------------------------------------

Example

User Role:

Executive

Agent:

executive_report

Tool:

organization_data

Result:

DENY

Reason:

Tool not authorized for role.

==================================================

AUDIT REQUIREMENTS

==================================================

Every MCP request must record:

- Timestamp
- User ID
- Role
- Agent ID
- Tool ID
- Request
- Result
- Duration
- Correlation ID

==================================================

LIFECYCLE STATES

==================================================

Draft

Active

Disabled

Deprecated

Retired

==================================================

FUTURE MCP TOOLS

==================================================

Planned:

SharePoint Search

Description:

Enterprise document search.

--------------------------------------------------

Planned:

Enterprise Knowledge Base

Description:

Organization knowledge retrieval.

--------------------------------------------------

Planned:

Confluence Search

Description:

Knowledge article retrieval.

--------------------------------------------------

Planned:

Application Inventory

Description:

Enterprise application catalog.

--------------------------------------------------

Planned:

Architecture Repository

Description:

Architecture document retrieval.

==================================================

AGENTCORE MAPPING

==================================================

Current:

Mock MCP Tools

↓

AGENT-CORE-GW

--------------------------------------------------

Future:

AWS AgentCore Gateway

↓

Enterprise MCP Servers

↓

Enterprise Tools

This migration should require no changes to business agents.

==================================================

CURRENT SCOPE

==================================================

Active Tools:

- document_search
- knowledge_lookup
- organization_data

Total Active Tools:

3