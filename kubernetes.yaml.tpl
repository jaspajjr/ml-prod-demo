apiVersion: apps/v1
kind: Deployment
metadata:
  name: ml-in-production
  labels:
    app: ml-in-production
spec:
  replicas: 1
  selector:
    matchLabels:
      app: ml-in-production
  template:
    metadata:
      labels:
        app: ml-in-production
    spec:
      containers:
      - name: ml-in-production
        image: gcr.io/ml-in-production/ml-in-production:$SHORT_SHA
        ports:
        - containerPort: 5000
---
kind: Service
apiVersion: v1
metadata:
  name: ml-in-production
spec:
  selector:
    app: ml-in-production
  ports:
  - protocol: TCP
    port: 80
    targetPort: 5000
  type: LoadBalancer