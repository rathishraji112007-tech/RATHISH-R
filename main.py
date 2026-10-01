from fastapi import FastAPI, HTTPException
from gemini_utils import get_recommendations
from models import (
    HomeRequest,
    PartyRequest,
    JewelryRequest
)

app = FastAPI(
    title="PocketSmart AI",
    description="Smart Budget Recommendation Assistant"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to PocketSmart AI"
    }


@app.post("/generate-home")
def generate_home(data: HomeRequest):
    prompt = f"""
    Suggest home interior products.
    Budget: Rs. {data.budget}
    Room: {data.room_type}
    Style: {data.preferences}

    Give product suggestions, estimated prices,
    and shopping links. Stay within the budget.
    """

    try:
        result = get_recommendations(prompt)
        return {"recommendations": result}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="AI recommendation failed"
        )


@app.post("/generate-party")
def generate_party(data: PartyRequest):
    prompt = f"""
    Create a party budget plan.
    Budget: Rs. {data.budget}
    Guests: {data.guests}
    Event: {data.event_type}

    Suggest food, decoration and venue.
    Include estimated costs and a budget breakdown.
    """

    try:
        result = get_recommendations(prompt)
        return {"recommendations": result}
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Party planning failed"
        )


@app.post("/generate-jewelry")
def generate_jewelry(data: JewelryRequest):
    prompt = f"""
    Recommend jewelry within the budget.
    Budget: Rs. {data.budget}
    Occasion: {data.occasion}
    Style: {data.style}

    Suggest suitable jewelry and estimated prices.
    """

    try:
        result = get_recommendations(prompt)
        return {"recommendations": result}
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Jewelry recommendation failed"
        )
