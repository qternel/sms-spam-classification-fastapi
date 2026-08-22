from contextlib import asynccontextmanager

import joblib
from fastapi import FastAPI
from mock_objects.mock_classfier import MockClassifier
from routes import classification


@asynccontextmanager
async def lifespan(app: FastAPI):
    # app.state.classifier = joblib.load("../models/voting_classifier.joblib")
    app.state.classifier = MockClassifier()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(classification.router)
