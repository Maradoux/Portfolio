import smtplib

try:
    server = smtplib.SMTP('smtp.gmail.com', 587 )
    server.starttls()
    server.login('amarachukwuaguolu@gmail.com', 'juxj avqs fcql newg')
    print("SMTP connection successful!")
    server.quit()
except Exception as e:
    print(f"SMTP connection failed: {e}")