# AgentCore Mapping

Platform: AI Enabler

Version: 1.0

Purpose:

This document maps the AI Enabler architecture to AWS AgentCore services.

The objective is to avoid building components already provided by AWS AgentCore while maintaining ownership of business-specific logic.

==================================================

ARCHITECTURE STRATEGY

==================================================

Principle:

Build Business Logic.

Consume Infrastructure.

AI Enabler should focus on:

- Business workflows
- Agent definitions
- Agent governance
- Authorization policies
- Enterprise business rules

AWS AgentCore should provide:

- Agent runtime
- MCP routing
- Identity
- Observability
- Secure execution
- Agent hosting

==================================================

CURRENT AI ENABLER AGENTS

==================================================

analyze_organization

Purpose:

Create organization profile from source documentation.

Output:

organization_profile.json

--------------------------------------------------

function_analysis

Purpose:

Analyze business functions.

Output:

function_analysis.json

--------------------------------------------------

ai_opportunity

Purpose:

Discover AI opportunities.

Output:

function_ai_opportunities.json

--------------------------------------------------

roadmap

Purpose:

Generate AI roadmap.

Output:

ai_roadmap.json

--------------------------------------------------

executive_report

Purpose:

Generate executive recommendations.

Output:

executive_report.json

==================================================

MAPPING TO AGENTCORE

==================================================

AI Enabler Component:

analyze_organization

Ownership:

Custom

AgentCore Dependency:

Agent Runtime

Notes:

Business-specific logic remains within AI Enabler.

--------------------------------------------------

AI Enabler Component:

function_analysis

Ownership:

Custom

AgentCore Dependency:

Agent Runtime

Notes:

Business-specific logic remains within AI Enabler.

--------------------------------------------------

AI Enabler Component:

ai_opportunity

Ownership:

Custom

AgentCore Dependency:

Agent Runtime

Notes:

Business-specific logic remains within AI Enabler.

--------------------------------------------------

AI Enabler Component:

roadmap

Ownership:

Custom

AgentCore Dependency:

Agent Runtime

Notes:

Business-specific logic remains within AI Enabler.

--------------------------------------------------

AI Enabler Component:

executive_report

Ownership:

Custom

AgentCore Dependency:

Agent Runtime

Notes:

Business-specific logic remains within AI Enabler.

==================================================

IDENTITY MAPPING

==================================================

Current State

Authentication Provider:

Amazon Cognito

Responsibilities:

- Login
- JWT Token
- User Identity
- Group Membership

--------------------------------------------------

Future State

Authentication Provider:

Microsoft Entra ID

Federation Through:

Amazon Cognito

Responsibilities:

- Corporate Identity
- Corporate Groups
- Corporate Access Management

--------------------------------------------------

Gateway Impact

None

AGENT-CORE-GW must never depend on a specific identity provider.

==================================================

AUTHORIZATION MAPPING

==================================================

Current Authorization Source

authorization-matrix.md

Ownership

AI Enabler

Reason

AgentCore does not know enterprise-specific authorization rules.

Examples:

Who can execute roadmap?

Who can execute executive_report?

Which roles can run ai_opportunity?

These remain business decisions owned by AI Enabler.

==================================================

AGENT REGISTRY MAPPING

==================================================

Current Source

agent-catalog.md

Ownership

AI Enabler

Reason

Only AI Enabler knows which agents exist.

AgentCore executes agents but does not define enterprise business catalogs.

==================================================

MCP MAPPING

==================================================

Current Vision

Agent

↓

Gateway

↓

MCP

--------------------------------------------------

Target AgentCore Vision

Agent

↓

AgentCore Gateway

↓

MCP Server

↓

Tool

--------------------------------------------------

Ownership

AWS AgentCore

==================================================

MCP GOVERNANCE

==================================================

AI Enabler Owns:

- Business policy
- Tool usage policy
- Approval requirements

AWS Owns:

- Connectivity
- Discovery
- Secure transport
- Runtime integration

==================================================

AUDIT MAPPING

==================================================

Current Source

audit-schema.md

Business Ownership

AI Enabler

--------------------------------------------------

Infrastructure Ownership

AWS

Target Services

- CloudWatch
- Observability Services
- Agent Runtime Telemetry

==================================================

OBSERVABILITY MAPPING

==================================================

Metrics

Requests

Agent Executions

Authorization Decisions

Failures

Latency

Token Usage

--------------------------------------------------

Target AWS Services

CloudWatch

AgentCore Observability

Log Analytics

==================================================

TOKEN AND COST TRACKING

==================================================

Business Ownership

AI Enabler

Reason

Cost allocation is business dependent.

Examples

Which customer generated cost?

Which project generated cost?

Which agent generated cost?

--------------------------------------------------

Runtime Data

Provided by AWS Runtime and Model Providers.

==================================================

WHAT WE BUILD

==================================================

Agent Catalog

Authorization Matrix

Audit Schema

Business Policies

Agent Definitions

Business Workflows

Governance Rules

Approval Rules

==================================================

WHAT AWS BUILDS

==================================================

Runtime

Identity

Gateway

Tool Connectivity

MCP Connectivity

Hosting

Scaling

Observability

Execution Isolation

Security Controls

==================================================

WHAT WE SHOULD STOP BUILDING

==================================================

Custom Identity Platform

Custom JWT Framework

Custom Tool Gateway

Custom MCP Gateway

Custom Runtime Engine

Custom Hosting Platform

==================================================

WHAT WE SHOULD CONTINUE BUILDING

==================================================

analyze_organization

function_analysis

ai_opportunity

roadmap

executive_report

Authorization Policies

Governance Policies

Approval Policies

Cost Allocation Policies

Enterprise Workflows

==================================================

==================================================

AGENT EXECUTION STRATEGY

==================================================

Current State

AI Enabler agents execute as native Python applications.

The platform does not currently require AWS AgentCore Runtime.

The platform focuses on agent standardization, governance and business workflows.

Current Execution Model:

User

↓

Python Agent

↓

Artifacts

Examples:

analyze_organization

function_analysis

ai_opportunity

roadmap

executive_report

--------------------------------------------------

AgentCore Gateway Strategy

AgentCore Gateway adoption is strategic.

The platform should leverage AgentCore Gateway for:

- MCP Connectivity
- Tool Access
- Secure Routing
- Identity Integration
- Governance Enforcement

The Gateway should be adopted without requiring migration of existing agents to AgentCore Runtime.

--------------------------------------------------

Agent Runtime Strategy

AgentCore Runtime is optional.

The platform may continue executing agents using the existing Python implementation while consuming AgentCore Gateway services.

Migration to AgentCore Runtime should occur only when one or more of the following conditions are met:

- Multi-tenant deployment required
- Production scale requirements increase
- Managed runtime benefits exceed migration cost
- Advanced AgentCore capabilities are needed

--------------------------------------------------

Agent Standardization Requirement

All agents must expose a common execution contract.

Required Components:

- Agent Metadata
- Agent Dependencies
- Supported Tools
- Execute Method
- Execution Result

Example:

metadata

dependencies

tools

execute(context)

--------------------------------------------------

AgentCore Readiness Goal

All agents should become runtime-independent.

This enables future execution on:

- Local Python Runtime
- Container Runtime
- AWS AgentCore Runtime

without changing business logic.

--------------------------------------------------

Architecture Principle

Build agents once.

Run them anywhere.

Business logic remains owned by AI Enabler.

Infrastructure may evolve independently.

==================================================

TARGET END STATE

==================================================

User

↓

Microsoft Entra ID

↓

Amazon Cognito Federation

↓

AWS AgentCore Gateway

↓

AWS AgentCore Runtime

↓

analyze_organization

↓

function_analysis

↓

ai_opportunity

↓

roadmap

↓

executive_report

↓

MCP Tools

↓

Audit + Observability

==================================================

FINAL DECISION

==================================================

AI Enabler owns Business Logic.

AWS AgentCore owns Platform Infrastructure.

All future development should be evaluated using:

BUILD

BUY

INTEGRATE

before implementation.