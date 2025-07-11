from prometheus_fastapi_instrumentator import Instrumentator

# We'll Using Counter, Histogram
from prometheus_client import Counter, Histogram

# Define the Instrumentator for Automatic HTTP Metrics
instrumentator = Instrumentator()

# Total Access to Our Model Container ?
logits_requests = Counter("predict_request_total", "Total Prediction Request Sent to Model")

# Average Time (in Second) to Perform Prediciton ?
logits_duration = Histogram("predict_request_duration_seconds", "Duration of Prediction (in Second)")