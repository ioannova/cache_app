class Config(object):
    # Flask Security
    SESSION_COOKIE_HTTPONLY  = True
    SESSION_COOKIE_SAMESITE='Lax'
    SESSION_COOKIE_SECURE=True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600
    REMEMBER_COOKIE_SECURE =True

    # SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class Development(Config):
    # Turns on debugging features in Flask
    DEBUG=True
    ENV='development'
    SECRET_KEY = '4t7w!z%C&F)J@NcRfUjXn2r5u8x/A?D(G-KaPdSgV1Yp3s6v9y$B&E)H@MbQeThW'

    # CSRF_Token
    WTF_CSRF_SECRET_KEY='SgVkYp3s6v9y$B?E(H+MbQeThW2Zq4t7w!z%C*F)J@NcRfUjXn2r5u8x/A?D(G+K'
    WTF_CSRF_ENABLE=True

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'


class Production(Config):
    # Turns on debugging features in Flask
    ENV='production'
    SECRET_KEY = 'NcRfTjWnZr4u7x!A%D*G-KaPdSgVkYp2s5v8y/B%E(H+MbQeThWmZq4t6w9z$C&F'

    # CSRF_Token
    WTF_CSRF_SECRET_KEY ="B?E(H+MbQeThVmYq3t6w9z$C&#)J@NcRfUjXnZr4u7x!A%D*G-KaPdSgVkYp3s5v"

    # SQLAlchemy
    # SQLite3
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    # # MariaDB
    # SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}/{}'.format(
    #     'mysql+pymysql',
    #     '<user>',
    #     '<senha>',
    #     '127.0.0.1',
    #     '<database>' )
