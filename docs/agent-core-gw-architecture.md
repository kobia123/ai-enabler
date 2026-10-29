# AGENT-CORE-GW Architecture

Platform: AI Enabler

Component: AGENT-CORE-GW

Version: 2.0

Status: Target Architecture

Owner: AI Discovery Platform

==================================================

PURPOSE

==================================================

Architecture Decision

AGENT-CORE-GW is the logical governance layer of the AI Enabler platform.

AGENT-CORE-GW does not replace AWS AgentCore Gateway.

AGENT-CORE-GW defines:

- Business Governance
- Authorization Policies
- Agent Registry
- Workflow Rules
- Audit Rules
- Cost Governance
- Enterprise Policies

AWS AgentCore provides the infrastructure capabilities required to securely execute and connect agents.

AI Enabler owns business logic.

AWS owns infrastructure services.

==================================================

ARCHITECTURE RESPONSIBILITIES

==================================================

AI Enabler Responsibilities

- Agent Definitions
- Agent Catalog
- Agent Registry
- Authorization Matrix
- Workflow Definitions
- Business Policies
- MCP Governance
- Audit Schema
- Cost Governance

--------------------------------------------------

AWS AgentCore Responsibilities

- Gateway Infrastructure
- MCP Connectivity
- Secure Routing
- Identity Integration
- Runtime Hosting
- Tool Connectivity
- Observability
- Runtime Isolation
- Scalability

==================================================

ARCHITECTURAL PRINCIPLES

==================================================

Principle 1

Business Logic Ownership

AI Enabler owns all business workflows, agent definitions and governance decisions.

--------------------------------------------------

Principle 2

Infrastructure Reuse

Infrastructure capabilities should be consumed from AWS AgentCore whenever possible.

--------------------------------------------------

Principle 3

Default Deny

Any request not explicitly allowed must be denied.

--------------------------------------------------

Principle 4

Zero Direct MCP Access

Agents may not communicate directly with MCP servers.

All MCP communication must be mediated by approved infrastructure.

--------------------------------------------------

Principle 5

Full Auditability

All authorization decisions, agent executions and tool calls must be auditable.

--------------------------------------------------

Principle 6

Identity Provider Independence

The platform must support:

- Amazon Cognito
- Microsoft Entra ID
- Future Identity Providers

without changing business logic.

==================================================

HIGH LEVEL ARCHITECTURE

==================================================

User

↓

Microsoft Entra ID

↓

Amazon Cognito

↓

AWS AgentCore Gateway

↓

AGENT-CORE-GW Governance Layer

↓

Authorization Engine

↓

Agent Registry

↓

Python Agents

↓

MCP Services

↓

Audit + Observability

==================================================

CORE COMPONENTS

==================================================

AI Enabler Components

- Authorization Service
- Agent Registry
- Agent Catalog
- Workflow Orchestration
- Audit Schema
- Cost Tracking
- Governance Policies

--------------------------------------------------

AWS Components

- AgentCore Gateway
- AgentCore Identity
- MCP Connectivity
- Observability Services
- Runtime Services (Optional)

==================================================

AUTHORIZATION SERVICE

==================================================

Purpose

Determine whether a user may execute a specific agent.

Authorization Source

authorization-matrix.md

Examples

BusinessAnalyst

↓

roadmap

↓

DENY

--------------------------------------------------

SolutionArchitect

↓

roadmap

↓

ALLOW

==================================================

AGENT REGISTRY

==================================================

Purpose

Maintain a catalog of all registered agents.

Source

agent-catalog.md

Functions

- Register Agent
- Lookup Agent
- Enable Agent
- Disable Agent
- Validate Agent

==================================================

REGISTERED AGENTS

==================================================

- analyze_organization
- function_analysis
- ai_opportunity
- roadmap
- executive_report

==================================================

AGENT EXECUTION MODEL

==================================================

Current Model

Python Agents

Each agent executes using native Python code.

Current Runtime

Python

Current Hosting

Local Development Runtime

--------------------------------------------------

Future Options

- Python Runtime
- Container Runtime
- AWS AgentCore Runtime

Agent business logic must remain independent from runtime implementation.

==================================================

MCP ACCESS MODEL

==================================================

Current Model

Agent

↓

Tool Interface

↓

Mock MCP Tool

--------------------------------------------------

Target Model

Agent

↓

AWS AgentCore Gateway

↓

MCP Server

↓

Enterprise Tool

==================================================

MCP GOVERNANCE

==================================================

AI Enabler Owns

- Tool Authorization Policy
- Agent Tool Permissions
- Business Approval Rules

AWS Owns

- MCP Connectivity
- Tool Discovery
- Secure Transport
- Runtime Integration

==================================================

AUDIT SERVICE

==================================================

Purpose

Provide full business auditability.

Audit Source

audit-schema.md

Audited Activities

- Authentication
- Authorization
- Agent Execution
- MCP Access
- System Events

==================================================

OBSERVABILITY

==================================================

Metrics

- Agent Executions
- Authorization Decisions
- Failures
- MCP Usage
- Token Usage
- Runtime Latency

Target AWS Services

- CloudWatch
- AgentCore Observability
- OpenSearch

==================================================

COST TRACKING

========================