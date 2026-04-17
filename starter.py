import os
from openai import OpenAI  # type: ignore
import config

# Load environment variables and initialize OpenAI client

client = OpenAI(
    base_url="https://openai.vocareum.com/v1",
    api_key=config.api_key
)

def call_openai(system_prompt, user_prompt, model="gpt-3.5-turbo"):
    """Simple wrapper for OpenAI API calls"""
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0
    )
    return response.choices[0].message.content



def feedstock_analyst_agent(feedstock_name):
    # Analyze the hydrocarbon feed
    """Feedstock analyst agent that understands and analyzes the hydrocarbon feed"""
    system_prompt = """You are a petrochemical expert analyzing hydrocarbon feedstocks. 
    Provide a concise analysis of the given feedstock, highlighting its key components and general suitability for producing valuable refined products like gasoline, diesel, and kerosene.
    """
    
    user_prompt = f"Analyze the feedstock: {feedstock_name}"
    
    print(f"Feedstock agent analyzing: {feedstock_name}")
    return call_openai(system_prompt, user_prompt)

def distillation_planner_agent(feedstock_analysis):
    # Allocate through distillation tower
    system_prompt = """You are a refinery distillation tower operations planner. 
    Based on the provided feedstock analysis, estimate the potential percentage yields for major products like gasoline, diesel, and kerosene. 
    Be realistic.
    """
    user_prompt = f"""Based on {feedstock_analysis}, suggest allocation through the distillation tower.
    For example: "Based on the analysis, potential yields are: Gasoline: 40%, Diesel: 30%, Kerosene: 20%, Other: 10%"
    """
    print(f"Distillation_planner_agent analyzing....")
    return call_openai(system_prompt, user_prompt)
   

def market_analyst_agent(product_list):
    # Assess current market demand and pricing for products.
 
    # Input: product_list_str (a string containing a comma-separated list of product names extracted from the distillation plan).
   
    system_prompt = """You are an energy market analyst. 
    For the following list of refined products, provide a brief analysis of current market demand (high, medium, low) and general profitability trends.
    """
    user_prompt = f"""Analyze the market for these refined products: {product_list}
    You should return a string with:
    - market analysis
    - demand levels
    - profitability.
    """
    print(f"Market analyst agent analyzing: {product_list}\n")
    return call_openai(system_prompt, user_prompt)

def production_optimizer_agent(distillation_plan, market_data):
    # Recommend an optimal production plan balancing yield and market needs.
    system_prompt = """You are a refinery production optimization expert.
    Your goal is to recommend a production strategy based on potential yields and current market conditions.
    """
    user_prompt = f"""Analyze the market for these refined products: {distillation_plan}
    You should return a string with:
    - market analysis
    - demand levels
    - profitability.
    """
 
    user_prompt = f"""
    Given the following potential distillation plan:
    --- DISTILLATION PLAN ---
    {distillation_plan}
    --- END DISTILLATION PLAN ---
    And the following market analysis:
    --- MARKET ANALYSIS ---
    {market_data}
    --- END MARKET ANALYSIS ---
    Please provide a concise recommendation on which products the refinery should prioritize or focus on to maximize value, considering both the potential yield and market conditions.
    Return a final string recommendation on production focus.
    """
    print(f"Production optimizer agent analyzing: {distillation_plan} and {market_data}")
    return call_openai(system_prompt, user_prompt)



def run_simple_chain(current_feedstock):
    """Run the refinery agentic workflow"""
    print(f"\nStarting refinery optimization workflow for: '{current_feedstock}'")

    # Step 1: Feedstock Analysis
    feedstock_report = feedstock_analyst_agent(current_feedstock)
    print("\nFeedstock analysis complete.")

    # Step 2: Distillation Planning
    distillation_plan = distillation_planner_agent(feedstock_report)
    print("\nDistillation planning complete.")

    # Step 3: Market Analysis
    # We need to extract the list of products from the distillation plan
    system_prompt = "List all products from the distillation plan above."
    product_list = call_openai(system_prompt, distillation_plan)

    # This list of products is then used to perform market analysis
    market_analysis = market_analyst_agent(product_list)
    print("\nMarket analysis complete.")

    # Step 4: Production Optimization
    production_plan = production_optimizer_agent(distillation_plan, market_analysis)
    print("\nProduction optimization complete.")

    # Print results
    print("\n===== FEEDSTOCK REPORT =====")
    print(feedstock_report)

    print("\n===== DISTILLATION PLAN =====")
    print(distillation_plan)

    print("\n===== MARKET ANALYSIS =====")
    print(market_analysis)

    print("\n===== FINAL PRODUCTION PLAN =====")
    print(production_plan)

    return {
        "feedstock": feedstock_report,
        "distillation": distillation_plan,
        "market": market_analysis,
        "plan": production_plan
    }

# Run the example
if __name__ == "__main__":
    current_feedstock = "West Texas Intermediate Crude"
    results = run_simple_chain(current_feedstock)



