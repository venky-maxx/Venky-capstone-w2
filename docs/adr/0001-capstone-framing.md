# ADR-0001: Capstone Framing — venky capstone

- **Status:** Draft v1
- **Date:** 2026-09-06
- **Author:** Venkatesh

## Context

This capstone addresses the inefficiency of manual data extraction from unstructured documents for people. This manual process results in high operational costs, slow turnaround times, and frequent human errors. Building this now leverages mature LLM and vector search technologies to automate accurate information retrieval at scale.

## Decision — Solution Framing Canvas

| Box | Your answer |
|-----|-------------|
| **Inputs** | Text queries, file uploads (PDF, CSV, TXT), and API parameters. |
| **Outputs** | Natural language text answers, source citations, and confidence scores. |
| **Tools** | OpenAI API, a vector database, and a document extraction parser. |
| **Memory** | Sliding window memory that retains the last N turns of the conversation. |
| **Autonomy level** | Semi-autonomous; retrieves and synthesizes data but performs no external actions. |
| **Decision boundaries** | Autonomously queries and ranks data; requires human review for final decisions. |

## Consequences

- **Positive:** 
    * Drastically reduces search time via automated grounding.
    * Minimizes hallucinations by restricting answers to provided data.
    * Controls token costs through a fixed memory window.
- **Negative / risks:**
    * Vulnerable to data parsing errors on complex layouts (tables/images).
    * Loses context in long sessions once early turns drop off.
    * Relies entirely on third-party API availability and uptime.
- **Things we'll re-visit:**
    * Upgrading to durable long-term memory systems.
    * Transitioning to fully agentic workflows with live external tools.
