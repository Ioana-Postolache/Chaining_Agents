# Refinery Optimization Team

This project demonstrates a prompt chaining workflow in Python by building a refinery optimization team powered by a Large Language Model (LLM).

The workflow is organized as a sequence of specialized agents. Each agent performs one focused task, and its output is passed to the next agent in the chain. Together, the agents analyze a hydrocarbon feedstock, estimate distillation outputs, assess market conditions, and recommend an optimized production strategy.

## Overview

The goal of this project is to show how a complex refinery decision-making process can be broken into smaller, manageable LLM tasks.

Instead of asking one model prompt to solve everything at once, the project uses four specialized agents:

- a feedstock analyst
- a distillation planner
- a market analyst
- a production optimizer

This prompt chaining design makes the workflow easier to understand, debug, and improve.

## Agent Workflow

### 1. Feedstock Analyst Agent

**Function:** `feedstock_analyst_agent(feedstock_name)`

This agent analyzes the type of hydrocarbon feedstock provided as input.

**Input:**
- `feedstock_name` — a string such as `"Light Sweet Crude"` or `"West Texas Intermediate Crude"`

**Output:**
- a concise description of likely feedstock components and its suitability for producing refined products such as gasoline, diesel, and kerosene

### 2. Distillation Planner Agent

**Function:** `distillation_planner_agent(feedstock_analysis)`

This agent uses the feedstock analysis to estimate how the crude might be allocated through the distillation tower.

**Input:**
- `feedstock_analysis` — the output from the feedstock analyst

**Output:**
- an estimated product yield plan, such as percentages for gasoline, diesel, kerosene, and other outputs

### 3. Market Analyst Agent

**Function:** `market_analyst_agent(product_list_str)`

This agent evaluates market demand and profitability trends for the refined products.

**Input:**
- `product_list_str` — a string containing product names or the distillation plan output

**Output:**
- a market analysis describing demand levels and general profitability for the products

### 4. Production Optimizer Agent

**Function:** `production_optimizer_agent(distillation_plan, market_data)`

This agent combines operational yield estimates with market conditions to recommend the best production focus.

**Input:**
- `distillation_plan` — output from the distillation planner
- `market_data` — output from the market analyst

**Output:**
- a final recommendation on which products the refinery should prioritize to maximize value

## How the Prompt Chain Works

The project follows this sequence:

1. The user provides an initial feedstock name.
2. The feedstock analyst examines the crude type.
3. The distillation planner estimates likely product yields.
4. The market analyst evaluates demand and profitability for those products.
5. The production optimizer recommends the best production strategy.

Each step builds on the previous one, creating a clear multi-step reasoning workflow.

## Example Flow

Example starting input:

```python
current_feedstock = "West Texas Intermediate Crude"
