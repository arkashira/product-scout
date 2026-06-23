from launch_plan_generator import Idea, LaunchPlan, generate_launch_plan, launch_plan_to_json, launch_plan_to_pdf, share_launch_plan

def test_generate_launch_plan():
    idea = Idea(
        name="Test Idea",
        description="This is a test idea",
        features=["Feature 1", "Feature 2", "Feature 3", "Feature 4"],
        marketing_channels=["Social Media", "Email Marketing"],
        pricing_strategy="Freemium"
    )
    launch_plan = generate_launch_plan(idea)
    assert launch_plan.mvp_feature_list == ["Feature 1", "Feature 2", "Feature 3"]
    assert launch_plan.target_launch_date == (launch_plan_to_json(launch_plan).split('"target_launch_date": "')[1].split('"')[0])
    assert launch_plan.marketing_channels == ["Social Media", "Email Marketing"]
    assert launch_plan.pricing_strategy == "Freemium"

def test_launch_plan_to_json():
    idea = Idea(
        name="Test Idea",
        description="This is a test idea",
        features=["Feature 1", "Feature 2", "Feature 3", "Feature 4"],
        marketing_channels=["Social Media", "Email Marketing"],
        pricing_strategy="Freemium"
    )
    launch_plan = generate_launch_plan(idea)
    json_string = launch_plan_to_json(launch_plan)
    assert json_string.startswith('{')
    assert json_string.endswith('}')

def test_launch_plan_to_pdf():
    idea = Idea(
        name="Test Idea",
        description="This is a test idea",
        features=["Feature 1", "Feature 2", "Feature 3", "Feature 4"],
        marketing_channels=["Social Media", "Email Marketing"],
        pricing_strategy="Freemium"
    )
    launch_plan = generate_launch_plan(idea)
    pdf_string = launch_plan_to_pdf(launch_plan)
    assert pdf_string.startswith("PDF generated for ")

def test_share_launch_plan():
    idea = Idea(
        name="Test Idea",
        description="This is a test idea",
        features=["Feature 1", "Feature 2", "Feature 3", "Feature 4"],
        marketing_channels=["Social Media", "Email Marketing"],
        pricing_strategy="Freemium"
    )
    launch_plan = generate_launch_plan(idea)
    shared_string = share_launch_plan(launch_plan)
    assert shared_string.startswith("Launch plan shared for ")
