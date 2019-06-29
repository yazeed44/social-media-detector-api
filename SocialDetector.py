class SocialDetector:
    apps_to_detect = []

    # This method takes an implementation of BaseSocialApp and add it to the list to be detected later
    def add_social_app(self, app):
        self.apps_to_detect.append(app)

    def detect(self):
        for app in self.apps_to_detect:
            app.process()
