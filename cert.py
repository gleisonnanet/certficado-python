import subprocess


def generate_certificate(common_name, key_file, cert_file, days=365, country=None, state=None, city=None,
                         organization=None, organizational_unit=None, email=None, rsa_bits=2048, cert_type='x509'):
    subject = f"/CN={common_name}"
    if country:
        subject += f"/C={country}"
    if state:
        subject += f"/ST={state}"
    if city:
        subject += f"/L={city}"
    if organization:
        subject += f"/O={organization}"
    if organizational_unit:
        subject += f"/OU={organizational_unit}"
    if email:
        subject += f"/emailAddress={email}"
    subprocess.run(f"openssl genrsa -out {key_file} {rsa_bits}", shell=True)
    subprocess.run(f"openssl req -new -{cert_type} -key {key_file} -out {cert_file} -days {days} -subj '{subject}'",
                   shell=True)
    print(f"Certificado gerado com sucesso para o CN: {common_name}")


# example of use
generate_certificate("localhost", "key.pem", "cert.pem", days=365, rsa_bits=4096, cert_type='selfsigned')
