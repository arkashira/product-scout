import json
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List

@dataclass
class Idea:
    name: str
    description: str
    features: List[str]
    marketing_channels: List[str]
    pricing_strategy: str

@dataclass
class LaunchPlan:
    idea: Idea
    mvp_feature_list: List[str]
    target_launch_date: str
    marketing_channels: List[str]
    pricing_strategy: str

def generate_launch_plan(idea: Idea) -> LaunchPlan:
    mvp_feature_list = idea.features[:3]  # Select top 3 features for MVP
    target_launch_date = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
    return LaunchPlan(
        idea=idea,
        mvp_feature_list=mvp_feature_list,
        target_launch_date=target_launch_date,
        marketing_channels=idea.marketing_channels,
        pricing_strategy=idea.pricing_strategy
    )

def launch_plan_to_json(launch_plan: LaunchPlan) -> str:
    return json.dumps({
        "idea": launch_plan.idea.name,
        "mvp_feature_list": launch_plan.mvp_feature_list,
        "target_launch_date": launch_plan.target_launch_date,
        "marketing_channels": launch_plan.marketing_channels,
        "pricing_strategy": launch_plan.pricing_strategy
    }, indent=4)

def launch_plan_to_pdf(launch_plan: LaunchPlan) -> str:
    # Simulate PDF generation
    return f"PDF generated for {launch_plan.idea.name}"

def share_launch_plan(launch_plan: LaunchPlan) -> str:
    # Simulate sharing
    return f"Launch plan shared for {launch_plan.idea.name}"
