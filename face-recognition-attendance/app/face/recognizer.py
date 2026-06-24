import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


class FaceRecognizer:
    def __init__(self, threshold=0.7):
        """
        threshold:
        - 0.6 = strict 
        - 0.7 = balanced (recommended)
        - 0.8 = loose 
        """
        self.threshold = threshold
        
    def recognize(self, known_embeddings, encoding):
        """
        Input: 
        - known_embeddings (list of vectors)
        - encoding (single vector)

        Returns:
        - best_match_index (int) or None if no match
        - confidence (%)
        """
        if encoding is None or len(known_embeddings) == 0:
            return None, 0.0

        similarities = cosine_similarity(
            [encoding], 
            known_embeddings
        )[0]
        
        best_idx = np.argmax(similarities)
        best_score = similarities[best_idx]
        
        confidence = best_score * 100
        
        if best_score >= self.threshold:
            return best_idx, confidence
        
        return None, confidence