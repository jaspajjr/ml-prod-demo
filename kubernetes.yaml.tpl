apiVersion: apps/v1
kind: Deployment
metadata:
  name: ml-prod-demo
  labels:
    app: ml-prod-demo
spec:
  replicas: 1
  selector:
    matchLabels:
      app: ml-prod-demo
  template:
    metadata:
      labels:
        app: ml-prod-demo
    spec:
      containers:
      - name: ml-prod-demo
        image: gcr.io/ml-prod-demo/ml-prod-demo:ed76814
        ports:
        - containerPort: 5000
        volumeMounts:
          - name: myvolume
            mountPath: "/secrets"
            readonly: true
      volumes:
        - name: myvolume
          secret:
            secretName: private-key
---
kind: Service
apiVersion: v1
metadata:
  name: ml-prod-demo
spec:
  selector:
    app: ml-prod-demo
  ports:
  - protocol: TCP
    port: 80
    targetPort: 5000
  type: LoadBalancer