#!/bin/bash

src_image=("k8s.gcr.io/ingress-nginx/controller:v1.1.1", "k8s.gcr.io/ingress-nginx/kube-webhook-certgen:v1.1.1")
dest_image=("yangchao1/ingress-nginx-controller:v1.1.1", "yangchao1/ingress-nginx-kube-webhook-certgen:v1.1.1")

for i in {0..1} ; do
  docker pull ${src_image[i]}
  docker tag ${src_image[i]} ${dest_image[i]}
  docker pull ${dest_image[i]}
done
