# Save this as train_model.py and run once
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Dummy training data
df = pd.DataFrame({
    'packet_len': [100, 200, 300, 400],
    'has_TCP': [1, 1, 0, 1],
    'has_UDP': [0, 0, 1, 0],
    'has_ICMP': [0, 0, 0, 1],
    'src_port': [80, 443, 53, 0],
    'dst_port': [8080, 8443, 53, 8],
    'label': [0, 0, 1, 1]
})

X = df.drop('label', axis=1)
y = df['label']

clf = RandomForestClassifier()
clf.fit(X, y)
joblib.dump(clf, 'rf_model.pkl')
