# mood_analyzer.py
"""
Rule based mood analyzer for short text snippets.

This class starts with very simple logic:
  - Preprocess the text
  - Look for positive and negative words
  - Compute a numeric score
  - Convert that score into a mood label
"""

from typing import List, Dict, Tuple, Optional

from dataset import POSITIVE_WORDS, NEGATIVE_WORDS, NEUTRAL_WORDS, MIXED_WORDS


class MoodAnalyzer:
    """
    A very simple, rule based mood classifier.
    """

    def __init__(
        self,
        positive_words: Optional[List[str]] = None,
        negative_words: Optional[List[str]] = None,
        neutral_words: Optional[List[str]] = None,
        mixed_words: Optional[List[str]] = None,
    ) -> None:
        # Use the default lists from dataset.py if none are provided.
        positive_words = positive_words if positive_words is not None else POSITIVE_WORDS
        negative_words = negative_words if negative_words is not None else NEGATIVE_WORDS
        neutral_words = neutral_words if neutral_words is not None else NEUTRAL_WORDS
        mixed_words = mixed_words if mixed_words is not None else MIXED_WORDS

        # Store as sets for faster lookup.
        self.positive_words = set(w.lower() for w in positive_words)
        self.negative_words = set(w.lower() for w in negative_words)
        self.neutral_words = set(w.lower() for w in neutral_words)
        self.mixed_words = set(w.lower() for w in mixed_words)

    # ---------------------------------------------------------------------
    # Preprocessing
    # ---------------------------------------------------------------------

    def preprocess(self, text: str) -> List[str]:
        """
        Convert raw text into a list of tokens the model can work with.

        TODO: Improve this method.

        Right now, it does the minimum:
          - Strips leading and trailing whitespace
          - Converts everything to lowercase
          - Splits on spaces

        Ideas to improve:
          - Remove punctuation
          - Handle simple emojis separately (":)", ":-(", "🥲", "😂")
          - Normalize repeated characters ("soooo" -> "soo")
        """
        import re
        cleaned = text.strip().lower()
        cleaned = re.sub(r"[^\w\s:)(💀😭😂🥹🥲]", " ", cleaned)
        tokens = cleaned.split()

        return tokens

    # ---------------------------------------------------------------------
    # Scoring logic
    # ---------------------------------------------------------------------

    def score_text(self, text: str) -> int:
        """
        Compute a numeric "mood score" for the given text.

        Positive words increase the score.
        Negative words decrease the score.

        TODO: You must choose AT LEAST ONE modeling improvement to implement.
        For example:
          - Handle simple negation such as "not happy" or "not bad"
          - Count how many times each word appears instead of just presence
          - Give some words higher weights than others (for example "hate" < "annoyed")
          - Treat emojis or slang (":)", "lol", "💀") as strong signals
        """
        tokens = self.preprocess(text)
        score = 0
        negators = {"not", "never", "no", "cant", "can't", "don't", "dont", "isn't", "isnt"}
        positive_terms = {":)", "😂", "🥹", "lol", "lowkey", "highkey", "no cap", "hyped", "blessed", "vibing"}

        for i, token in enumerate(tokens):
            is_negated = i > 0 and tokens[i - 1] in negators
            if token in self.positive_words or token in positive_terms:
                score += -1 if is_negated else 1
            elif token in self.negative_words:
                score += 1 if is_negated else -1
            elif token in self.neutral_words or token in self.mixed_words:
                score += 0

        return score

    # ---------------------------------------------------------------------
    # Label prediction
    # ---------------------------------------------------------------------

    def predict_label(self, text: str) -> str:
        """
        Turn the numeric score for a piece of text into a mood label.

        The default mapping is:
          - score > 0  -> "positive"
          - score < 0  -> "negative"
          - score == 0 -> "neutral"

        TODO: You can adjust this mapping if it makes sense for your model.
        For example:
          - Use different thresholds (for example score >= 2 to be "positive")
          - Add a "mixed" label for scores close to zero
        Just remember that whatever labels you return should match the labels
        you use in TRUE_LABELS in dataset.py if you care about accuracy.
        """
        tokens = self.preprocess(text)
        positive_terms = {":)", "😂", "🥹", "lol", "lowkey", "highkey", "no cap", "hyped", "blessed", "vibing"}
        negators = {"not", "never", "no", "cant", "can't", "don't", "dont", "isn't", "isnt"}

        pos_count = 0
        neg_count = 0
        neutral_count = 0
        has_mixed_word = False

        for i, token in enumerate(tokens):
            is_negated = i > 0 and tokens[i - 1] in negators
            if token in self.positive_words or token in positive_terms:
                if is_negated:
                    neg_count += 1
                else:
                    pos_count += 1
            elif token in self.negative_words:
                if is_negated:
                    pos_count += 1
                else:
                    neg_count += 1
            elif token in self.neutral_words:
                neutral_count += 1
            elif token in self.mixed_words:
                has_mixed_word = True

        if has_mixed_word and pos_count > 0 and neg_count > 0:
            return "mixed"
        if pos_count > 0 and neg_count > 0 and abs(pos_count - neg_count) <= 1:
            return "mixed"
        if neutral_count > pos_count and neg_count == 0:
            return "neutral"
        elif pos_count > neg_count:
            return "positive"
        elif neg_count > pos_count:
            return "negative"
        else:
            return "neutral"

    # ---------------------------------------------------------------------
    # Explanations (optional but recommended)
    # ---------------------------------------------------------------------

    def explain(self, text: str) -> str:
        """
        Return a short string explaining WHY the model chose its label.

        TODO:
          - Look at the tokens and identify which ones counted as positive
            and which ones counted as negative.
          - Show the final score.
          - Return a short human readable explanation.

        Example explanation (your exact wording can be different):
          'Score = 2 (positive words: ["love", "great"]; negative words: [])'

        The current implementation is a placeholder so the code runs even
        before you implement it.
        """
        tokens = self.preprocess(text)

        positive_hits: List[str] = []
        negative_hits: List[str] = []
        score = 0

        for token in tokens:
            if token in self.positive_words:
                positive_hits.append(token)
                score += 1
            if token in self.negative_words:
                negative_hits.append(token)
                score -= 1

        return (
            f"Score = {score} "
            f"(positive: {positive_hits or '[]'}, "
            f"negative: {negative_hits or '[]'})"
        )
