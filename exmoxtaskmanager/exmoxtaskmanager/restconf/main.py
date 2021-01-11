REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],

    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

REST_AUTH_SERIALIZERS = {
    'TOKEN_SERIALIZER': 'task.apis.serializers.TokenSerializer',
}