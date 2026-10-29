# Agent Catalog

Platform: AGENT-CORE-GW

Version: 1.0

Purpose:

This document defines all registered agents in the AI Enabler platform.

The catalog serves as the single source of truth for:

- Agent registration
- Agent governance
- Agent ownership
- Agent lifecycle management
- Gateway routing
- Future authorization policies

==================================================

ACTIVE AGENTS

==================================================

Agent ID: analyze_organization

Name:
Organization Analysis Agent

Status:
Active

Type:
Discovery Agent

Owner:
AI Discovery Platform

Purpose:
Create a structured organization profile from organization source documents.

Input:
Organization Source Document

Output:
organization_profile.json

--------------------------------------------------

Agent ID: function_analysis

Name:
Function Analysis Agent

Status:
Active

Type:
Analysis Agent

Owner:
AI Discovery Platform

Purpose:
Analyze business functions and identify:

- Purpose
- Pain Points
- Systems
- Information Flows
- KPIs

Input:
organization_profile.json

Output:
function_analysis.json

--------------------------------------------------

Agent ID: ai_opportunity

Name:
AI Opportunity Agent

Status:
Active

Type:
Opportunity Discovery Agent

Owner:
AI Discovery Platform

Purpose:
Identify and prioritize AI opportunities based on business analysis.

Input:
function_analysis.json

Output:
function_ai_opportunities.json

--------------------------------------------------

Agent ID: roadmap

Name:
Roadmap Agent

Status:
Active

Type:
Planning Agent

Owner:
AI Discovery Platform

Purpose:
Generate an enterprise AI roadmap based on identified AI opportunities.

Input:
function_ai_opportunities.json

Output:
ai_roadmap.json

--------------------------------------------------

Agent ID: executive_report

Name:
Executive Report Agent

Status:
Active

Type:
Reporting Agent

Owner:
AI Discovery Platform

Purpose:
Generate executive recommendations, business benefits, implementation guidance and next steps.

Input:
ai_roadmap.json

Output:
executive_report.json

==================================================

CURRENT PROCESSING FLOW

==================================================

Organization Source Document

↓

analyze_organization

↓

organization_profile.json

↓

function_analysis

↓

function_analysis.json

↓

ai_opportunity

↓

function_ai_opportunities.json

↓

roadmap

↓

ai_roadmap.json

↓

executive_report

↓

executive_report.json

==================================================

AGENT LIFECYCLE STATES

==================================================

- Draft
- Active
- Disabled
- Deprecated
- Retired

==================================================

NAMING CONVENTION

==================================================

All Agent IDs must use:

lower_snake_case

Examples:

- analyze_organization
- function_analysis
- ai_opportunity
- roadmap
- executive_report

==================================================

AGENT DEPENDENCY MATRIX

==================================================

Agent:
analyze_organization

Depends On:
None

Required Input:
Organization Source Document

Produces:
organization_profile.json

--------------------------------------------------

Agent:
function_analysis

Depends On:
analyze_organization

Required Input:
organization_profile.json

Produces:
function_analysis.json

--------------------------------------------------

Agent:
ai_opportunity

Depends On:
function_analysis

Required Input:
function_analysis.json

Produces:
function_ai_opportunities.json

--------------------------------------------------

Agent:
roadmap

Depends On:
ai_opportunity

Required Input:
function_ai_opportunities.json

Produces:
ai_roadmap.json

--------------------------------------------------

Agent:
executive_report

Depends On:
roadmap

Required Input:
ai_roadmap.json

Produces:
executive_report.json
==================================================

GOVERNANCE RULES

==================================================

Rule 1

Every agent must be registered in the Agent Catalog.

Rule 2

Every agent must define:

- Agent ID
- Name
- Purpose
- Input
- Output
- Status
- Type
- Owner

Rule 3

Every agent execution must pass through AGENT-CORE-GW.

Rule 4

Direct MCP access is prohibited.

Rule 5

All MCP communication must pass through AGENT-CORE-GW.

Rule 6

Only Active agents may be executed.

Rule 7

Any agent not registered in this catalog must be rejected by the Gateway.

==================================================

CURRENT PLATFORM SCOPE

==================================================

Registered Active Agents:

- analyze_organization
- function_analysis
- ai_opportunity
- roadmap
- executive_report

Total Active Agents: 5
