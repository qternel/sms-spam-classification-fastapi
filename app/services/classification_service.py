from typing import Annotated

from fastapi import Depends, Request
from sklearn.ensemble import VotingClassifier


def get_classifier(request: Request):
    return request.app.state.classifier


class ClassificationService:

    def __init__(
        self, classifier: Annotated[VotingClassifier, Depends(get_classifier)]
    ):
        self._classifier = classifier

    def classify_text(self, text):
        return self._classifier.predict(text)
