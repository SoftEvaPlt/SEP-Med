from django.core.mail import send_mail
import typing
from datetime import timedelta
from django.core.cache import cache
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _
from hashlib import sha256
from django.contrib.sites.models import Site
from functools import wraps
from django.core.cache import cache

import random
import string

def cache_decorator(expiration=300):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = f'{func.__name__}_{args}_{kwargs}'
            result = cache.get(key)
            if not result:
                result = func(*args, **kwargs)
                cache.set(key, result, expiration)
            return result
        return wrapper
    return decorator

def get_sha256(str):
    m = sha256(str.encode('utf-8'))
    return m.hexdigest()

@cache_decorator()
def get_current_site():
    site = Site.objects.get_current()
    return site

def generate_code() -> str:
    """生成随机数验证码"""
    return ''.join(random.sample(string.digits, 6))

def send_email(emailto, title, content):
    send_mail(
        title,  # 邮件标题
        content,  # 邮件内容
        'your_email@example.com',  # 发件人邮箱
        [emailto],  # 收件人邮箱列表
        fail_silently=False,  # 是否静默处理发送邮件的异常
    )

_code_ttl = timedelta(minutes=5)


def send_verify_email(to_mail: str, code: str, subject: str = _("Verify Email")):
    """发送重设密码验证码
    Args:
        to_mail: 接受邮箱
        subject: 邮件主题
        code: 验证码
    """
    html_content = _(
        "You are resetting the password, the verification code is：%(code)s, valid within 5 minutes, please keep it "
        "properly") % {'code': code}
    send_email([to_mail], subject, html_content)

def verify(email: str, code: str) -> typing.Optional[str]:
    """验证code是否有效
    Args:
        email: 请求邮箱
        code: 验证码
    Return:
        如果有错误就返回错误str
    Node:
        这里的错误处理不太合理，应该采用raise抛出
        否测调用方也需要对error进行处理
    """
    cache_code = get_code(email)
    if cache_code != code:
        return gettext("Verification code error")


def set_code(email: str, code: str):
    """设置code"""
    cache.set(email, code, _code_ttl.seconds)


def get_code(email: str) -> typing.Optional[str]:
    """获取code"""
    return cache.get(email)
