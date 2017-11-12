import os
import shutil
import sys
# import MySQLdb
from . import projectConf
import random, string


def generatePassword():
    import uuid
    thePass = uuid.uuid4().hex[:8].upper()
    thePass+='!'
    return thePass

def createConfFile(name):

    filePath = '/etc/apache2/sites-available'
    file = open("{}/{}.conf".format(filePath,name),'w+')

    redirectHost = "<VirtualHost *:80>\n\tServerName {name}.naysis.com\n\t" \
                   "ServerAlias www.{name}.naysis.com\n\t" \
                   "Redirect permanent / https://{name}.naysis.com\n" \
                   "</VirtualHost>\n\n".format(name=name)


    sshHost = "<IfModule mod_ssl.c>\n" \
              "<VirtualHost 104.236.46.24:443>\n\t" \
              "ServerName {name}.naysis.com\n\t" \
              "Alias /static/ /srv/envs/naysis/src/{name}/Enamra/static/\n\t" \
              "Alias /static/ /srv/envs/naysis/src/{name}/estore/static/\n\t" \
              "Alias /media/ /srv/envs/naysis/src/{name}/media/\n\t" \
              "Alias /static/admin/ /srv/envs/naysis/lib/python3.5/site-packages/django/contrib/admin/static/\n\t" \
              "ServerAlias www.{name}.naysis.com\n\t" \
              "ServerAdmin armanit93@gmail.com\n\t" \
              "DocumentRoot /srv/envs/naysis/src/{name}\n\t" \
              "WSGIDaemonProcess {name}.naysis.com python-path=/srv/envs/naysis/src/{name}:/srv/envs/naysis/lib/python3.5/site-packages\n\t" \
              "WSGIProcessGroup {name}.naysis.com\n\t" \
              "WSGIApplicationGroup %{{GLOBAL}} \n\t" \
              "WSGIScriptAlias / /srv/envs/naysis/src/{name}/Enamra/wsgi.py process-group={name}.naysis.com\n\t" \
              "ErrorLog /srv/envs/naysis/src/logs/{name}/error.log\n\t" \
              "CustomLog /srv/envs/naysis/src/logs/{name}/custom.log combined\n\t" \
              "<Directory /srv/envs/naysis/src/{name}/Enamra/static>\n\t\t" \
              "Require all granted\n\t" \
              "</Directory>\n\t" \
              "<Directory '/srv/envs/naysis/lib/python3.5/site-packages/django/contrib/admin/static/'>\n\t\t" \
              "Order allow,deny\n\t\t" \
              "Options Indexes\n\t\t" \
              "Allow from all\n\t\t" \
              "IndexOptions FancyIndexing\n\t" \
              "</Directory>\n\t" \
              "<Directory /srv/envs/naysis/src/{name}/estore/static>\n\t\t" \
              "Require all granted\n\t" \
              "</Directory>\n\t" \
              "<Directory  /srv/envs/naysis/src/{name}/media>\n\t\t" \
              "Require all granted\n\t" \
              "</Directory>\n\t" \
              "<Directory /srv/envs/naysis/src/{name}>\n\t\t" \
              "<Files wsgi.py>\n\t\t\t" \
              "Require all granted\n\t\t" \
              "</Files>\n\t\t" \
              "AllowOverride None\n\t\t" \
              "Order deny,allow\n\t\t" \
              "Allow from  all\n\t" \
              "</Directory>\n\t" \
              "SSLEngine on\n\t" \
              "SSLCertificateFile    /etc/letsencrypt/live/dev.ararat17.com/fullchain.pem\n\t" \
              "SSLCertificateKeyFile /etc/letsencrypt/live/dev.ararat17.com/privkey.pem\n" \
              "</VirtualHost>\n" \
              "</IfModule>\n".format(name=name)

    # "SSLCertificateFile    /etc/letsencrypt/live/{name}.naysis.com/fullchain.pem\n\t" \
    # "SSLCertificateKeyFile /etc/letsencrypt/live/{name}.naysis.com/privkey.pem\n" \
    file.write(redirectHost+sshHost)

    file.close()

    print("Conf File successfully Created")





def copySampleProject(newName):
    from_path = '/srv/sample/Project'
    to_path = '/srv/envs/naysis/src/{name}'.format(name=newName)

    print(from_path)

    if os.path.exists(to_path):
        shutil.rmtree(to_path)
    shutil.copytree(from_path, to_path)

    print("Project Was Created")



def createLogFiles(name):
    path = "/srv/envs/naysis/src/logs/{name}/".format(name=name)

    if not os.path.exists(path):
        os.makedirs(path)

    error = open('{}/error.log'.format(path), 'w+')
    custom = open('{}/custom.log'.format(path), 'w+')

    error.close()
    custom.close()

    print("Log Files Succesffully Created")


def createSSLCertificate(name):
    cmd = "sudo certbot --apache certonly -d {name}.naysis.com".format(name=name)
    os.system(cmd)
    print("SSL Certificate was successfully created")


def runA2Ensite(name):
    cmd = "sudo a2ensite {name}.conf".format(name=name)
    os.system(cmd)
    print("a2Ensite Executed")

def restartApache():
    cmd = "sudo service apache2 restart"
    os.system(cmd)
    print("APACHE restarted")

def createDatabase(name,password):
    db1 = MySQLdb.connect(host="104.236.46.24", user="naysis", passwd="Zayka2193!", port=2268)
    cursor = db1.cursor()
    #Set Timeouts
    #cursor.execute('SET GLOBAL connect_timeout=28800')
    #cursor.execute('SET GLOBAL wait_timeout=28800')
    #cursor.execute('SET GLOBAL interactive_timeout=28800')



    crateDbSql = 'CREATE DATABASE IF NOT EXISTS naysis_{name}'.format(name=name)
    cursor.execute(crateDbSql)

    crateUserSql = "CREATE USER IF NOT EXISTS '{name}_user'@'%' IDENTIFIED BY '{password}'".format(name=name,password=password)
    cursor.execute(crateUserSql)

    grantPreveligesSql = "GRANT ALL PRIVILEGES ON naysis_{name}.* TO '{name}_user'@'%'".format(name=name)
    cursor.execute(grantPreveligesSql)

    cursor.execute("flush privileges")


    db1.close()

    print("Database Created")

def changeProjectFiles(name,password):
    projectConf.createSettings(name,password)
    projectConf.createWsgi(name)
    print("Settings succesffuly changed")


def executeMigrations(name):
    print("======================================\n\n")
    managePyPath = "/srv/envs/naysis/src/{name}/manage.py".format(name=name)
    mediaPath ="/srv/envs/naysis/src/{name}/media/".format(name=name)
    cmdMake = "/srv/envs/naysis/bin/python {manage} makemigrations".format(manage=managePyPath)
    cmdMigrate = "/srv/envs/naysis/bin/python {} migrate".format(managePyPath)
    cmdCollectStatic = "/srv/envs/naysis/bin/python {} collectstatic".format(managePyPath)
    cmdMediaFilesPermission = "chown www-data:www-data {mediaPath} -R".format(mediaPath=mediaPath)



    print(managePyPath)
    print(cmdMake)

    os.system(cmdMake)
    #os.system(cmdMigrate)
    #os.system(cmdCollectStatic)
    os.system(cmdMediaFilesPermission)

    print("\n\n========================================")


def createSuperUser(name,password):
    print("\n\n=======================Create SuperUser===========================\n\n")
    managePyPath = "/srv/envs/naysis/src/{name}/manage.py".format(name=name)


    cmd = "echo \"from myuser.models import MyUser; MyUser.objects.create_superuser('{name}@naysis.com', '{password}')\" | /srv/envs/naysis/bin/python {managePyPath} shell".format(name=name, managePyPath=managePyPath,password=password)
    os.system(cmd)
    print("Super User was successfully created")
    print("\n========================================================\n")

def setDefaults(name):
    #Set Default Language
    print("\n\n=======================Set Default Language===========================\n\n")
    managePyPath = "/srv/envs/naysis/src/{name}/manage.py".format(name=name)

    cmd = "echo \"from SisianShop.models import Language; Language.objects.create(name='English',shortname='eng',default=True)\" | /srv/envs/naysis/bin/python  {managePyPath} shell".format(managePyPath=managePyPath)
    os.system(cmd)
    print("English -> Default Language")

    print("\n========================================================\n")

def setExamples(name):
    managePyPath = "/srv/envs/naysis/src/{name}/manage.py".format(name=name)
    for i in range(0,2):
        cmd = "echo \"from estore.models import slider\n" \
              "from django.core.files import File\n" \
              "theslider=slider(name='slide_{i}',url='/',sort={i}, status=True)\n" \
              "theslider.image.save('slide_{i}.png',File(open('/srv/envs/naysis/src/{name}/Enamra/static/enirak/store_images/slide.png','rb')))" \
              "\"| /srv/envs/naysis/bin/python  {managePyPath} shell".format(i=i,managePyPath=managePyPath,name=name)
        os.system(cmd)

def sendEmail(message):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Your account was successfully created"
    fromaddr = 'naysis'
    toaddrs = 'armanit93@gmail.com'

    html ="<html xmlns='http://www.w3.org/1999/xhtml'>" \
          "<head>" \
          "<body>" \
          "<h1><b>Your account was successfully created</b></h1>" \
          "<h4>Your username is: {name}@naysis.com</h4>" \
          "<h4>Your password is: {password}</h4>" \
          "<hr>" \
          "<p>Thank's for using naysis.</p>" \
          "</body>" \
          "</html>".format(name=message['name'],password=message['password'])




    BODY = MIMEText(html, 'html')
    msg.attach(BODY)

    username = 'arman.avetisyan93@gmail.com'
    password = 'Zayka2193!'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(username, password)
    server.sendmail(fromaddr, toaddrs, msg.as_string())
    server.quit()

def main(name,password):
    #password=generatePassword()
    createConfFile(name)
    copySampleProject(name)
    createLogFiles(name)
    createSSLCertificate(name)
    createDatabase(name,password)
    changeProjectFiles(name,password)
    executeMigrations(name)
    #createSuperUser(name,password)
    #setDefaults(name)
    #setExamples(name)
    #runA2Ensite(name)
    #restartApache()

    message={'name':name,'password':password}
    sendEmail(message)
"""
if __name__=='__main__':
    name = sys.argv[1]
    password = sys.argv[2]
    main(name,password)
"""