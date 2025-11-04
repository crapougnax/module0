from fastapi import FastAPI, HTTPException
from nltk.sentiment import SentimentIntensityAnalyzer
from loguru import logger
from pydantic import BaseModel

class Texte(BaseModel):
    texte: str

logger.add("logs/sentiment_api.log", rotation="500 MB", level="INFO")

sia = SentimentIntensityAnalyzer()

app = FastAPI()

@app.post("/analyse_sentiment/")
async def anasent(payload: Texte):
    logger.info(f"Received text: {payload.texte}")
    try:
        sentiment = sia.polarity_scores(payload.texte)
        logger.info(f"Résultats: {sentiment}")
        return {
                "neg": sentiment["neg"],
                "neu": sentiment["neu"],
                "pos": sentiment["pos"],
                "compound": sentiment["compound"],
            }
    except Exception as e:
        logger.error(f"Erreur lors de l'analyse du sentiment: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("sentiment_api:app", host="0.0.0.0", port=9000, reload=True)
