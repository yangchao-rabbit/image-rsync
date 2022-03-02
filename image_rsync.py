# coding = utf-8

import os

src_image = [
    "k8s.gcr.io/ingress-nginx/controller:v1.1.1",
    "k8s.gcr.io/ingress-nginx/kube-webhook-certgen:v1.1.1"
]

dest_image = [
    "yangchao1/ingress-nginx-controller:v1.1.1",
    "yangchao1/ingress-nginx-kube-webhook-certgen:v1.1.1"
]

if __name__ == '__main__':
    for i in range(len(src_image)):
        os.system("sh rsync.sh {} {}".format(src_image[i], "registry.hub.docker.com/" + dest_image[i]))
