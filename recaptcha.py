class ReCapchaMixin(serializers.Serializer):
    g_recaptcha_response = serializers.CharField()

    def validate_g_recaptcha_response(self, res):
        r = requests.post(settings.GR_CAPTCHA_URL, {
            'secret': settings.GR_CAPTCHA_SECRET_KEY,
            'response': res
        })

        if not r.json()['success']:
            raise serializers.ValidationError('invalid capcha')

        return res
