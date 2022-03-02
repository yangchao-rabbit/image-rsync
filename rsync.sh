#!/bin/bash
docker pull k8s.gcr.io/ingress-nginx/kube-webhook-certgen:v1.1.1
sleep 2
docker tag k8s.gcr.io/ingress-nginx/kube-webhook-certgen:v1.1.1 yangchao1/ingress-nginx/kube-webhook-certgen:v1.1.1
sleep 2
docker push yangchao1/ingress-nginx/kube-webhook-certgen:v1.1.1
