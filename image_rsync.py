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
        os.system("docker pull %s" % src_image[i])
        os.system("docker tag %s %s" % (src_image[i], dest_image[i]))
        os.system("docker push %s" % dest_image[i])
