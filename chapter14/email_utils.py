# -*- coding: utf_8 -*-
import datetime
import os
import smtplib
import time
import tarfile
import zipfile

from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email import utils


# to：邮件接收者
# cc：邮件抄送者
# subject：主题
# content：正文
# attachments：附件
# delete：是否删除
def send(to, cc, subject, content, attachments, delete):
    user = "ab@banggood.com"
    password = "ab"

    # 准备邮件服务
    server = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)
    smtplib.SMTP
    server.login(user, password)

    start = datetime.datetime.now()

    content_msg = MIMEMultipart()
    content_msg['From'] = user
    content_msg['To'] = ';'.join(to)
    content_msg['Cc'] = ';'.join(cc)
    content_msg['Subject'] = subject
    content_msg['Date'] = utils.formatdate()

    content_msg.attach(MIMEText(content.encode("UTF-8"), _charset='UTF-8'))
    content_type = 'application/octet-stream'
    maintype, subtype = content_type.split('/', 1)

    # Attachment ready
    compress_files = []
    if len(attachments) > 0:
        for path in attachments:
            path = compress_attachment(path)
            if path.__contains__('.csv') is False:
                compress_files.append(path)

            attachment_file = open(path, 'rb')
            file_msg = MIMEBase(maintype, subtype)
            file_msg.set_payload(attachment_file.read())
            attachment_file.close()
            encoders.encode_base64(file_msg)

            basename = os.path.basename(path)
            file_msg.add_header('Content-Disposition', 'attachment', filename=basename)
            content_msg.attach(file_msg)

    try:
        server.sendmail(user, to + cc, content_msg.as_string())
        end = datetime.datetime.now()
        time_str = time.strftime('%Y-%m-%d %H:%M:%S')
        print("{0} Email send successful in {1} seconds. To users: {2}".
              format(time_str, (end - start).seconds, ",".join(to+cc)))
        """
        By the end if delete flag is True, not empty with attachments
        and send email success then will delete all attachments
        """
        try:
            attachments.extend(compress_files)
            if delete and len(attachments) > 0:
                for path in attachments:
                    os.remove(path)
        except IOError as ex:
            print(f'Delete attachments were failed. Case: {ex}')
    except Exception as ex:
        raise RuntimeError(f"Send email[{subject}] failed. Case:{ex}")
    finally:
        server.quit()


# 附件压缩
def compress_attachment(attachment):
    length = os.path.getsize(attachment)
    """
    if the attachment file size greater than 2MB
    then will use zip compress file
    """
    if length > 2097152:
        attachment = zip_compress(attachment)
        print('File\'s [{0}] compress rate is {1}%%'.format(
            os.path.basename(attachment),
            compress_rate(length, os.path.getsize(attachment)) * 100))

    return attachment


# 计算压缩率
def compress_rate(source_size, target_size):
    return round((source_size - target_size) / float(source_size), 4)


# tar格式压缩
def tar_compress(source):
    source = source.decode('UTF-8')
    target = source[0:source.rindex('.')] + '.tar.gz'

    try:
        with tarfile.open(target, "w:gz") as tar_file:
            tar_file.add(source, arcname=source[source.rindex("/"):])
    except IOError as er:
        print(f'Compress file[{source}] with zip model failed.Case: {er}')
        target = source

    return target


# zip格式压缩
def zip_compress(source):
    source = source.decode('UTF-8')
    target = source[0:source.rindex(".")] + '.zip'
    try:
        with zipfile.ZipFile(target, 'w') as zip_file:
            zip_file.write(source, source[source.rindex('/'):], zipfile.ZIP_DEFLATED)
            zip_file.close()
    except IOError as er:
        print(f'Compress file[{source}] with zip model failed.Case: {er}')
        target = source

    return target