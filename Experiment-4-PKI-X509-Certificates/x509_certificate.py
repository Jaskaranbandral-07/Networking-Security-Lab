openssl version

mkdir x509_lab
cd x509_lab

openssl genpkey -algorithm RSA -out private.key -pkeyopt rsa_keygen_bits:2048

openssl pkey -in private.key -check -noout

openssl req -new -x509 -sha256 -key private.key -out certificate.crt -days 365 -subj "/C=IN/ST=Jammu/L=Jammu/O=MIET/OU=CSE/CN=localhost" -addext "subjectAltName=DNS:localhost,IP:127.0.0.1" -addext "basicConstraints=critical,CA:FALSE" -addext "keyUsage=critical,digitalSignature,keyEncipherment" -addext "extendedKeyUsage=serverAuth"

openssl x509 -in certificate.crt -text -noout

openssl verify certificate.crt

openssl verify -CAfile certificate.crt certificate.crt

openssl pkey -in private.key -pubout -outform DER | openssl dgst -sha256

openssl x509 -in certificate.crt -pubkey -noout | openssl pkey -pubin -outform DER | openssl dgst -sha256
