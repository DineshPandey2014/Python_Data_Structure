import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Generate a fictional dataset
def test():
    np.random.seed(42)
    texts = ["I love dogs.", "I hate cats.", "Dogs are friendly.", "Cats are cute."]
    labels = [1, 0, 1, 0]  # 1 for positive, 0 for negative

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.25, random_state=42)

    # Step 1: Train a biased model using bag-of-words features
    vectorizer = CountVectorizer()
    X_train_bow = vectorizer.fit_transform(X_train)
    biased_model = LogisticRegression()
    biased_model.fit(X_train_bow, y_train)

    # Evaluate the biased model on the test set
    X_test_bow = vectorizer.transform(X_test)
    y_pred_biased = biased_model.predict(X_test_bow)
    accuracy_biased = accuracy_score(y_test, y_pred_biased)
    print(f"Biased Model Accuracy: {accuracy_biased}")

    # Step 2: Train a debiased model using DRiFt
    # Assume I(x) is the bag-of-words representation
    X_train_debiased = X_train_bow  # For simplicity, in practice, you may need a different representation
    residuals = y_train - biased_model.predict(X_train_bow)

    debiased_model = LogisticRegression()
    debiased_model.fit(X_train_debiased, residuals)

    # Evaluate the debiased model on the test set
    X_test_debiased = X_test_bow  # Again, in practice, you may need a different representation
    y_pred_debiased = biased_model.predict(X_test_bow) + debiased_model.predict(X_test_debiased)
    y_pred_debiased = np.clip(y_pred_debiased, 0, 1)  # Clip predictions to be in [0, 1]
    accuracy_debiased = accuracy_score(y_test, y_pred_debiased)
    print(f"Debiased Model Accuracy: {accuracy_debiased}")

if __name__ == "__main__":
    test()