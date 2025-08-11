import pickle
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier


def main():
    X, y = load_iris(return_X_y=True)
    clf = RandomForestClassifier()
    clf.fit(X, y)
    with open('src/model/model.pkl', 'wb') as f:
        pickle.dump(clf, f)
    print("Model trained and saved to src/model/model.pkl")


if __name__ == "__main__":
    main()