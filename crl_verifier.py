################################
# Start Date: 01/2023
# Last Update: 28/09/2024
# Initial Dev: Marcelo Batista
# Maintained: Marcelo Batista, ...
################################

import requests
import ssl
from cryptography import x509
from datetime import datetime
import sys
import logging

#logging.basicConfig(level=logging.INFO,
#                    filename='crl_verifier_{}.log'.format(datetime.now().strftime('%Y%m%d')),
#                    encoding='utf-8',
#                    filemode='a',
#                    format='%(asctime)s %(levelname)s %(message)s',
#                    datefmt='%Y%m%d-%H:%M:%S'
#                    )

logging.info('Script Inciado')


def CRLvalidate(lcr2,period):
    nextUpdate = datetime.strptime(str(lcr2.next_update), '%Y-%m-%d %H:%M:%S')
    if period == "seconds":
        return (nextUpdate - datetime.now()).seconds
    if period == "days":
        return (nextUpdate - datetime.now()).days
    
def CRTvalidate(cert2,period):
    if period == "after":
        dataExpire = datetime.strptime(str(cert2.not_valid_after), '%Y-%m-%d %H:%M:%S')
        return (dataExpire - datetime.now()).days
    if period == "before":
        lastUpdate = datetime.strptime(str(cert2.not_valid_before), '%Y-%m-%d %H:%M:%S')
        return (datetime.now() - lastUpdate).days

URL = sys.argv[1]

logging.info('\t - Buscando dados para %s em %s',sys.argv[2],sys.argv[1])

match sys.argv[2]:
    case "lcr":
        lcr = requests.get(URL).content
        lcr2 = x509.load_der_x509_crl(lcr)
        data = CRLvalidate(lcr2,"seconds") / 60
    case "lcrdays":
        lcr = requests.get(URL).content
        lcr2 = x509.load_der_x509_crl(lcr)
        data = CRLvalidate(lcr2,"days")
    case "lcrdayspem":
        lcr = requests.get(URL).content
        lcr2 = x509.load_pem_x509_crl(lcr)
        data = CRLvalidate(lcr2,"days")
    case "crt":
        crt = ssl.get_server_certificate((URL,443))
        cert2 = x509.load_pem_x509_certificate(bytes(crt,'utf-8'))
        data = CRTvalidate(cert2,"after")
    case "crtFileVencimento":
        crt = requests.get(URL).content
        cert2 = x509.load_pem_x509_certificate(crt)
        data = CRTvalidate(cert2,"after")
    case "crtFileSerial":
        crt = requests.get(URL).content
        cert2 = x509.load_pem_x509_certificate(crt)
        data = crt2.serial_number
    case "crtFileEmitido":
        crt = requests.get(URL).content
        cert2 = x509.load_pem_x509_certificate(crt)
        data = CRTvalidate(cert2,"before")
    case "crtFileSubject":
        crt = requests.get(URL).content
        cert2 = x509.load_pem_x509_certificate(crt)
        data = crt2.subject

print (data)
logging.info('\t - Resultado dos dados: %s',data)
