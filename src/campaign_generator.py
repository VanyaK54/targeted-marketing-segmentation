import pandas as pd

def generate_campaign_plan(segmented_data_fp):
    df = pd.read_csv(segmented_data_fp)

    strategy_map = {
        0: "💡 Promote Loyalty Program",
        1: "🎁 Offer Welcome Discounts",
        2: "🔥 Target with Flash Sales",
        3: "🌟 Premium Product Launch"
    }

    df['campaign_strategy'] = df['cluster'].map(strategy_map)

    campaign_plan = df[['customer_id', 'cluster', 'campaign_strategy']]
    campaign_plan.to_csv("outputs/reports/segmentation_campaign_plan.csv", index=False)

    print("✅ Campaign plan generated.")
    return campaign_plan
